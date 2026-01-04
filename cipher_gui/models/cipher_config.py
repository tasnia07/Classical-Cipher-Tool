"""Cipher configuration and metadata."""


class CipherConfig:
    """Configuration data for all ciphers."""
    
    CIPHER_ICONS = {
        "Caesar": "🔄",
        "Affine": "🔢",
        "Playfair": "🔲",
        "Hill (2×2)": "📊"
    }
    
    KEY_HELP = {
        "Caesar": {
            "title": "Caesar Cipher Key",
            "format": "Single number (0-25)",
            "example": "3",
            "tip": "Larger shifts create more scrambling",
            "details": "The key represents how many positions each letter shifts in the alphabet."
        },
        "Affine": {
            "title": "Affine Cipher Key",
            "format": "Two numbers: a,b",
            "example": "5,8",
            "tip": "Valid 'a' values: 1,3,5,7,9,11,15,17,19,21,23,25",
            "details": "The 'a' value must be coprime with 26. Common values are 5, 7, 11, 15, 17, 21, 23."
        },
        "Playfair": {
            "title": "Playfair Cipher Key",
            "format": "Keyword or phrase",
            "example": "MONARCHY",
            "tip": "J is treated as I in the matrix",
            "details": "Use a memorable word or phrase. Longer keys provide better security."
        },
        "Hill (2×2)": {
            "title": "Hill Cipher Key",
            "format": "Four numbers: a,b,c,d",
            "example": "3,3,2,5",
            "tip": "Matrix determinant must be coprime with 26",
            "details": "Forms a 2×2 matrix [[a,b],[c,d]]. The determinant (ad-bc) must be coprime with 26."
        }
    }
    
    CIPHER_INFO = {
        "Caesar": {
            "name": "Caesar Cipher",
            "origin": "Julius Caesar, ~50 BC",
            "description": "Named after Julius Caesar, this is one of the simplest encryption techniques. Each letter is shifted by a fixed number of positions in the alphabet.",
            "strength": "⭐☆☆☆☆",
            "keys": "26 possible keys",
            "security": "Very weak - easily broken with brute force",
            "use_case": "Historical interest, basic learning"
        },
        "Affine": {
            "name": "Affine Cipher",
            "origin": "Mathematical cipher",
            "description": "A type of monoalphabetic substitution cipher using mathematical formula E(x) = (ax + b) mod 26. Combines multiplicative and additive operations.",
            "strength": "⭐⭐☆☆☆",
            "keys": "312 possible keys",
            "security": "Weak - vulnerable to frequency analysis",
            "use_case": "Educational purposes, simple obfuscation"
        },
        "Playfair": {
            "name": "Playfair Cipher",
            "origin": "Charles Wheatstone, 1854",
            "description": "A digraph substitution cipher that encrypts pairs of letters using a 5×5 key matrix. Used in WWI and WWII for tactical purposes.",
            "strength": "⭐⭐⭐☆☆",
            "keys": "Keyword-based (vast)",
            "security": "Moderate - resists simple frequency analysis",
            "use_case": "Historical military communications"
        },
        "Hill (2×2)": {
            "name": "Hill Cipher",
            "origin": "Lester S. Hill, 1929",
            "description": "A polygraphic substitution cipher using linear algebra. Encrypts blocks of letters using matrix multiplication. First cipher designed to be resistant to frequency analysis.",
            "strength": "⭐⭐⭐⭐☆",
            "keys": "Matrix-based (many)",
            "security": "Strong against frequency analysis",
            "use_case": "Secure classical encryption"
        }
    }
    
    @classmethod
    def get_icon(cls, cipher_name):
        """Get icon for cipher."""
        return cls.CIPHER_ICONS.get(cipher_name, "🔐")
    
    @classmethod
    def get_key_help(cls, cipher_name):
        """Get key help for cipher."""
        return cls.KEY_HELP.get(cipher_name, {})
    
    @classmethod
    def get_cipher_info(cls, cipher_name):
        """Get cipher information."""
        return cls.CIPHER_INFO.get(cipher_name, {})
    
    @classmethod
    def get_all_cipher_names(cls):
        """Get list of all cipher names."""
        return list(cls.CIPHER_ICONS.keys())
