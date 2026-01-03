"""Cipher operations (encrypt/decrypt)."""

from cipher_gui.utils.helpers import show_error


class CipherActions:
    """Handles cipher encryption and decryption operations."""
    
    def __init__(self, parent):
        self.parent = parent
    
    def _preserve_digits_in_output(self, original_text, cipher_output):
        """
        Insert digits from original text back into cipher output at their positions.
        Spaces are omitted.
        
        Args:
            original_text: Original text with digits and spaces
            cipher_output: Cipher output (letters only)
        
        Returns:
            str: Output with digits restored at original positions
        """
        # Build position map: track where digits were (excluding spaces)
        digit_positions = []
        pos = 0
        for char in original_text:
            if char == ' ':
                continue  # Skip spaces
            if char.isdigit():
                digit_positions.append((pos, char))
            pos += 1
        
        if not digit_positions:
            return cipher_output  # No digits to insert
        
        # Insert digits back at their positions
        result = []
        cipher_idx = 0
        total_length = pos  # Total length without spaces
        
        for i in range(total_length):
            # Check if there's a digit at this position
            digit_at_pos = next((d for p, d in digit_positions if p == i), None)
            if digit_at_pos:
                result.append(digit_at_pos)
            else:
                # Add character from cipher output
                if cipher_idx < len(cipher_output):
                    result.append(cipher_output[cipher_idx])
                    cipher_idx += 1
        
        return ''.join(result)
    
    def encrypt(self, cipher, text, key):
        """
        Encrypt text with the given cipher and key.
        
        Args:
            cipher: The cipher instance
            text: Text to encrypt
            key: Encryption key
            
        Returns:
            str: Encrypted text with digits preserved, or None if error
        """
        if not text:
            show_error(self.parent, "Please enter text to encrypt", "Empty Input")
            return None
        
        if not key:
            show_error(self.parent, "Please enter an encryption key", "Missing Key")
            return None
        
        try:
            # Encrypt (cipher only processes letters)
            cipher_result = cipher.encrypt(text, key)
            
            # Restore digits at their original positions
            result_with_digits = self._preserve_digits_in_output(text, cipher_result)
            
            return result_with_digits
        except ValueError as e:
            show_error(self.parent, str(e), "Encryption Error")
            return None
        except Exception as e:
            show_error(self.parent, f"Unexpected error: {str(e)}", "Error")
            return None
    
    def decrypt(self, cipher, text, key):
        """
        Decrypt text with the given cipher and key.
        
        Args:
            cipher: The cipher instance
            text: Text to decrypt
            key: Decryption key
            
        Returns:
            str: Decrypted text with digits preserved, or None if error
        """
        if not text:
            show_error(self.parent, "Please enter text to decrypt", "Empty Input")
            return None
        
        if not key:
            show_error(self.parent, "Please enter the decryption key", "Missing Key")
            return None
        
        try:
            # Decrypt (cipher only processes letters)
            cipher_result = cipher.decrypt(text, key)
            
            # Restore digits at their original positions
            result_with_digits = self._preserve_digits_in_output(text, cipher_result)
            
            return result_with_digits
        except ValueError as e:
            show_error(self.parent, str(e), "Decryption Error")
            return None
        except Exception as e:
            show_error(self.parent, f"Unexpected error: {str(e)}", "Error")
            return None
