class CaesarCipher:
    """Caesar Cipher implementation with shift-based encryption/decryption"""
    
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    def encrypt(self, plaintext, key):
        """
        Encrypt plaintext using Caesar cipher
        Args:
            plaintext (str): Text to encrypt
            key (int): Shift value (0-25)
        Returns:
            str: Encrypted ciphertext (uppercase, spaces/digits omitted)
        """
        key = int(key) % 26
        ciphertext = ''
        
        for char in plaintext:
            if char == ' ' or char.isdigit():
                # Skip spaces and digits completely
                continue
            elif char.upper() in self.alphabet:
                # Encrypt alphabetic characters (force lowercase processing)
                old_index = self.alphabet.index(char.upper())
                new_index = (old_index + key) % 26
                new_char = self.alphabet[new_index]
                # Always return uppercase for encryption
                ciphertext += new_char
        
        return ciphertext
    
    def decrypt(self, ciphertext, key):
        """
        Decrypt ciphertext using Caesar cipher
        Args:
            ciphertext (str): Text to decrypt (uppercase)
            key (int): Shift value (0-25)
        Returns:
            str: Decrypted plaintext (lowercase, spaces/digits omitted)
        """
        key = int(key) % 26
        plaintext = ''
        
        for char in ciphertext:
            if char == ' ' or char.isdigit():
                # Skip spaces and digits completely
                continue
            elif char.upper() in self.alphabet:
                # Decrypt alphabetic characters (force uppercase processing)
                old_index = self.alphabet.index(char.upper())
                new_index = (old_index - key) % 26
                new_char = self.alphabet[new_index]
                # Always return lowercase for decryption
                plaintext += new_char.lower()
        
        return plaintext
