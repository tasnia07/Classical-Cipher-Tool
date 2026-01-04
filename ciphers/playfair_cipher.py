class PlayfairCipher:
    """Playfair Cipher implementation using 5x5 key matrix"""
    
    def __init__(self):
        self.alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # J is omitted, I/J treated as same
    
    def _create_matrix(self, key):
        """Create 5x5 Playfair matrix from key"""
        key = key.upper().replace('J', 'I')
        key_string = ''
        
        # Remove duplicates from key
        for char in key:
            if char in self.alphabet and char not in key_string:
                key_string += char
        
        # Add remaining letters
        for char in self.alphabet:
            if char not in key_string:
                key_string += char
        
        # Create 5x5 matrix
        matrix = []
        for i in range(5):
            matrix.append(list(key_string[i*5:(i+1)*5]))
        
        return matrix
    
    def _find_position(self, matrix, char):
        """Find position of character in matrix"""
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == char:
                    return i, j
        return None, None
    
    def _prepare_text(self, text):
        """Prepare text for Playfair cipher (create digraphs), skipping spaces and digits"""
        # Remove spaces and digits, convert to uppercase, replace J with I
        clean_text = ''
        for c in text:
            if c == ' ' or c.isdigit():
                continue  # Skip spaces and digits
            elif c.isalpha():
                clean_text += c.upper().replace('J', 'I')
        
        prepared = ''
        i = 0
        
        while i < len(clean_text):
            prepared += clean_text[i]
            
            if i + 1 < len(clean_text):
                if clean_text[i] == clean_text[i + 1]:
                    # Same letter repeated, insert X
                    prepared += 'X'
                else:
                    prepared += clean_text[i + 1]
                    i += 1
            else:
                # Odd length, add X at the end
                prepared += 'X'
            
            i += 1
        
        if len(prepared) % 2 != 0:
            prepared += 'X'
        
        return prepared
    
    def encrypt(self, plaintext, key):
        """
        Encrypt plaintext using Playfair cipher
        Args:
            plaintext (str): Text to encrypt
            key (str): Keyword for matrix generation
        Returns:
            str: Encrypted ciphertext (uppercase, spaces/digits omitted)
        """
        matrix = self._create_matrix(key)
        prepared_text = self._prepare_text(plaintext)
        ciphertext = ''
        
        # Encrypt the alphabetic digraphs
        for i in range(0, len(prepared_text), 2):
            char1, char2 = prepared_text[i], prepared_text[i + 1]
            row1, col1 = self._find_position(matrix, char1)
            row2, col2 = self._find_position(matrix, char2)
            
            if row1 == row2:  # Same row
                enc1 = matrix[row1][(col1 + 1) % 5]
                enc2 = matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  # Same column
                enc1 = matrix[(row1 + 1) % 5][col1]
                enc2 = matrix[(row2 + 1) % 5][col2]
            else:  # Rectangle
                enc1 = matrix[row1][col2]
                enc2 = matrix[row2][col1]
            
            # Always return uppercase for encryption
            ciphertext += enc1 + enc2
        
        return ciphertext
    
    def decrypt(self, ciphertext, key):
        """
        Decrypt ciphertext using Playfair cipher
        Args:
            ciphertext (str): Text to decrypt (uppercase)
            key (str): Keyword for matrix generation
        Returns:
            str: Decrypted plaintext (lowercase, spaces/digits omitted)
        """
        matrix = self._create_matrix(key)
        
        # Get only alphabetic characters for decryption (skip spaces and digits)
        cipher_clean = ''.join(c.upper().replace('J', 'I') for c in ciphertext if c.isalpha())
        
        plaintext = ''
        
        for i in range(0, len(cipher_clean) - 1, 2):
            char1, char2 = cipher_clean[i], cipher_clean[i + 1]
            row1, col1 = self._find_position(matrix, char1)
            row2, col2 = self._find_position(matrix, char2)
            
            if row1 is None or row2 is None:
                continue
            
            if row1 == row2:  # Same row
                dec1 = matrix[row1][(col1 - 1) % 5]
                dec2 = matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Same column
                dec1 = matrix[(row1 - 1) % 5][col1]
                dec2 = matrix[(row2 - 1) % 5][col2]
            else:  # Rectangle
                dec1 = matrix[row1][col2]
                dec2 = matrix[row2][col1]
            
            # Always return lowercase for decryption
            plaintext += dec1.lower() + dec2.lower()
        
        # Remove X's that were clearly inserted during encryption
        # The Playfair cipher inserts X in two cases:
        # 1. Between consecutive identical letters (e.g., "hello" has "ll" so becomes "helxlo")
        # 2. As padding at the end if text length is odd
        #
        # Note: This is a heuristic and cannot perfectly handle text that naturally contains X.
        # This is a known limitation of the Playfair cipher.
        
        cleaned = ''
        i = 0
        while i < len(plaintext):
            char = plaintext[i]
            
            if char == 'x':
                # Case 1: X between identical non-X letters (e.g., "lxl" from original "ll")
                # Check if previous and next chars exist and are the same (but not 'x')
                if (i > 0 and i < len(plaintext) - 1 and 
                    plaintext[i-1] == plaintext[i+1] and 
                    plaintext[i-1] != 'x'):
                    # This X was inserted between doubles, remove it
                    i += 1
                    continue
                
                # Case 2: Trailing X at the end (padding for odd length)
                # Only remove if it's the last character
                elif i == len(plaintext) - 1:
                    # Remove trailing X (it was padding)
                    i += 1
                    continue
            
            cleaned += char
            i += 1
        
        return cleaned
