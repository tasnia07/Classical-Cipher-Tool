"""Key validation utilities."""


def validate_key(cipher, key_text):
    """
    Validate a key for the given cipher.
    
    Args:
        cipher: The cipher instance to validate against
        key_text: The key text to validate
        
    Returns:
        tuple: (is_valid, message)
    """
    if not key_text:
        return False, "Key is required"
    
    try:
        cipher.encrypt("TEST", key_text)
        return True, "Valid key"
    except ValueError as e:
        return False, str(e)
    except Exception as e:
        return False, f"Invalid key: {str(e)}"
