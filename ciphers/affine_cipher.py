class AffineCipher:
    """Affine Cipher implementation using formula: E(x) = (ax + b) mod 26"""
    
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
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        return None
    
    def _validate_key(self, a):
        """Validate that key 'a' is coprime with 26"""
        if self._gcd(a, self.m) != 1:
            raise ValueError(f"Key 'a' ({a}) must be coprime with 26. Valid values: 1,3,5,7,9,11,15,17,19,21,23,25")
        return True
    
    def encrypt(self, plaintext, key):
        """
        Encrypt plaintext using Affine cipher
        Args:
            plaintext (str): Text to encrypt
            key (tuple): (a, b) where a is multiplicative key and b is additive key
        Returns:
            str: Encrypted ciphertext (uppercase, spaces/digits omitted)
        """
        if isinstance(key, str):
            key = tuple(map(int, key.split(',')))
        
        a, b = int(key[0]), int(key[1])
        self._validate_key(a)
        
        ciphertext = ''
        for char in plaintext:
            if char == ' ' or char.isdigit():
                # Skip spaces and digits completely
                continue
            elif char.upper() in self.alphabet:
                # Encrypt alphabetic characters (force lowercase processing)
                x = self.alphabet.index(char.upper())
                encrypted_value = (a * x + b) % self.m
                new_char = self.alphabet[encrypted_value]
                # Always return uppercase for encryption
                ciphertext += new_char
        
        return ciphertext
    
    def decrypt(self, ciphertext, key):
        """
        Decrypt ciphertext using Affine cipher
        Args:
            ciphertext (str): Text to decrypt (uppercase)
            key (tuple): (a, b) where a is multiplicative key and b is additive key
        Returns:
            str: Decrypted plaintext (lowercase, spaces/digits omitted)
        """
        if isinstance(key, str):
            key = tuple(map(int, key.split(',')))
        
        a, b = int(key[0]), int(key[1])
        self._validate_key(a)
        
        a_inv = self._mod_inverse(a, self.m)
        if a_inv is None:
            raise ValueError(f"No modular inverse exists for a={a}")
        
        plaintext = ''
        for char in ciphertext:
            if char == ' ' or char.isdigit():
                # Skip spaces and digits completely
                continue
            elif char.upper() in self.alphabet:
                # Decrypt alphabetic characters (force uppercase processing)
                y = self.alphabet.index(char.upper())
                decrypted_value = (a_inv * (y - b)) % self.m
                new_char = self.alphabet[decrypted_value]
                # Always return lowercase for decryption
                plaintext += new_char.lower()
        
        return plaintext
