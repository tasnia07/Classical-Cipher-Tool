import numpy as np

class HillCipher:
    """Hill Cipher implementation using 2x2 key matrix"""
    
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.m = 26
    
    def _gcd(self, a, b):
        """Calculate Greatest Common Divisor"""
        while b:
            a, b = b, a % b
        return a
    
    def _mod_inverse(self, a, m):
        """Find modular multiplicative inverse of a under modulo m"""
        a = a % m
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        return None
    
    def _matrix_determinant_2x2(self, matrix):
        """Calculate determinant of 2x2 matrix"""
        return int(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])
    
    def _matrix_inverse_2x2(self, matrix):
        """Calculate modular inverse of 2x2 matrix"""
        det = self._matrix_determinant_2x2(matrix)
        det_mod = det % self.m
        
        if self._gcd(det_mod, self.m) != 1:
            raise ValueError(f"Matrix determinant ({det_mod}) is not coprime with 26. Cannot find inverse.")
        
        det_inv = self._mod_inverse(det_mod, self.m)
        if det_inv is None:
            raise ValueError("Cannot find modular inverse of determinant")
        
        # Adjugate matrix for 2x2: swap diagonal, negate off-diagonal
        adj_matrix = np.array([
            [matrix[1][1], -matrix[0][1]],
            [-matrix[1][0], matrix[0][0]]
        ])
        
        # Multiply by determinant inverse and take modulo
        inv_matrix = (det_inv * adj_matrix) % self.m
        return inv_matrix.astype(int)
    
    def _validate_key_matrix(self, matrix):
        """Validate that matrix determinant is coprime with 26"""
        det = self._matrix_determinant_2x2(matrix)
        det_mod = det % self.m
        
        if self._gcd(abs(det_mod), self.m) != 1:
            return False, det_mod
        return True, det_mod
    
    def _parse_key(self, key):
        """Parse key string into 2x2 matrix and validate"""
        if isinstance(key, str):
            # Expected format: "a,b,c,d" for [[a,b],[c,d]]
            values = [int(x.strip()) for x in key.split(',')]
            if len(values) != 4:
                raise ValueError("Key must contain 4 values for 2x2 matrix")
            matrix = np.array([[values[0], values[1]], [values[2], values[3]]])
        elif isinstance(key, (list, np.ndarray)):
            matrix = np.array(key)
        else:
            raise ValueError("Invalid key format")
        
        # Validate the matrix
        is_valid, det_mod = self._validate_key_matrix(matrix)
        if not is_valid:
            raise ValueError(
                f"Invalid key matrix! Determinant mod 26 = {det_mod}, which is not coprime with 26.\n"
                f"The determinant must be coprime with 26 (gcd(det, 26) = 1).\n"
                f"Valid determinant values: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25"
            )
        
        return matrix
    
    def _prepare_text(self, text):
        """Prepare text by skipping spaces and digits"""
        # Remove spaces and digits, convert to uppercase
        clean_text = ''.join(c.upper() for c in text if c.isalpha())
        
        # Pad with 'X' if odd length
        if len(clean_text) % 2 != 0:
            clean_text += 'X'
        
        return clean_text
    
    def encrypt(self, plaintext, key):
        """
        Encrypt plaintext using Hill cipher (2x2 matrix)
        Args:
            plaintext (str): Text to encrypt
            key: 2x2 matrix as string "a,b,c,d" or array [[a,b],[c,d]]
        Returns:
            str: Encrypted ciphertext (uppercase, spaces/digits omitted)
        """
        key_matrix = self._parse_key(key)
        prepared_text = self._prepare_text(plaintext)
        ciphertext = ''
        
        for i in range(0, len(prepared_text), 2):
            # Convert digraph to vector
            char1, char2 = prepared_text[i], prepared_text[i + 1]
            vector = np.array([
                self.alphabet.index(char1),
                self.alphabet.index(char2)
            ])
            
            # Multiply by key matrix and mod 26
            encrypted_vector = np.dot(key_matrix, vector) % self.m
            
            # Convert back to characters, always uppercase
            enc1 = self.alphabet[encrypted_vector[0]]
            enc2 = self.alphabet[encrypted_vector[1]]
            
            ciphertext += enc1 + enc2
        
        return ciphertext
    
    def decrypt(self, ciphertext, key):
        """
        Decrypt ciphertext using Hill cipher (2x2 matrix)
        Args:
            ciphertext (str): Text to decrypt (uppercase)
            key: 2x2 matrix as string "a,b,c,d" or array [[a,b],[c,d]]
        Returns:
            str: Decrypted plaintext (lowercase, spaces/digits omitted)
        """
        key_matrix = self._parse_key(key)
        inv_key_matrix = self._matrix_inverse_2x2(key_matrix)
        prepared_text = self._prepare_text(ciphertext)
        plaintext = ''
        
        for i in range(0, len(prepared_text), 2):
            # Convert digraph to vector
            char1, char2 = prepared_text[i], prepared_text[i + 1]
            vector = np.array([
                self.alphabet.index(char1),
                self.alphabet.index(char2)
            ])
            
            # Multiply by inverse key matrix and mod 26
            decrypted_vector = np.dot(inv_key_matrix, vector) % self.m
            
            # Convert back to characters, always lowercase
            dec1 = self.alphabet[int(decrypted_vector[0])]
            dec2 = self.alphabet[int(decrypted_vector[1])]
            
            plaintext += dec1.lower() + dec2.lower()
        
        # Remove padding X at the end if it exists
        if len(plaintext) > 0 and plaintext[-1] == 'x':
            plaintext = plaintext[:-1]
        
        return plaintext
