#!/usr/bin/env python3
"""
Hill Cipher Known Plaintext Attack Cracker
==========================================
Robust implementation for cracking 2x2 Hill Cipher keys 
using known plaintext-ciphertext pairs.

Mathematical Background:
    - Hill cipher encryption: C = K × P (mod 26)
    - To find key K: K = C × P⁻¹ (mod 26)
    - P⁻¹ exists only when gcd(det(P), 26) = 1
    - Valid determinants mod 26: {1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25}

Attack Strategy:
    1. Algebraic Attack: Find invertible plaintext matrix, compute K = C × P⁻¹
    2. Brute Force Fallback: Search all valid 2x2 keys (~157,248 candidates)

Usage:
    Command Line:
        python cracker.py -p "hello" -c "hiozhn"
        python cracker.py -p "hello" -c "hiozhn" -d "moretext"
        python cracker.py -a "hello"  # Analyze plaintext
        python cracker.py -i          # Interactive mode
    
    As Module:
        from cracker import HillCipherCracker
        cracker = HillCipherCracker()
        key = cracker.crack_key("hello", "hiozhn")
"""

import numpy as np
import argparse
from math import gcd


class HillCipherCracker:
    """
    Robust 2x2 Hill Cipher Cracker using Known Plaintext Attack.
    
    Works with ANY valid plaintext-ciphertext pair by combining:
    1. Fast algebraic approach (when plaintext matrix is invertible)
    2. Optimized brute force (when algebraic approach fails)
    """
    
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    MOD = 26
    # Determinants coprime with 26 (have modular inverse)
    VALID_DETS = frozenset({1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25})
    
    def __init__(self):
        # Precompute modular inverses for efficiency
        self._mod_inverses = {d: self._compute_mod_inverse(d) for d in self.VALID_DETS}
    
    @staticmethod
    def _compute_mod_inverse(a, m=26):
        """Compute modular multiplicative inverse using extended Euclidean algorithm"""
        if gcd(a, m) != 1:
            return None
        # Extended Euclidean Algorithm
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 % m0
    
    def _char_to_num(self, char):
        """Convert character to number (A=0, B=1, ..., Z=25)"""
        return ord(char.upper()) - ord('A')
    
    def _num_to_char(self, num):
        """Convert number to character"""
        return chr((num % self.MOD) + ord('A'))
    
    def _clean_text(self, text):
        """Remove non-alphabetic characters, remove spaces, and convert to uppercase"""
        return ''.join(c.upper() for c in text if c.isalpha())
    
    def _pad_text(self, text):
        """Pad text with 'X' to make length even (for 2x2 block size)"""
        if len(text) % 2 != 0:
            text += 'X'
        return text
    
    def _text_to_digraphs(self, text):
        """Convert text to list of digraph tuples [(a,b), (c,d), ...]"""
        text = self._pad_text(self._clean_text(text))
        return [(self._char_to_num(text[i]), self._char_to_num(text[i+1])) 
                for i in range(0, len(text), 2)]
    
    def _det_2x2(self, a, b, c, d):
        """Calculate determinant of 2x2 matrix [[a,b],[c,d]] mod 26"""
        return (a * d - b * c) % self.MOD
    
    def _matrix_mod_inverse_2x2(self, matrix):
        """
        Calculate modular inverse of 2x2 matrix mod 26.
        
        For matrix [[a,b],[c,d]]:
        - det = ad - bc
        - inverse = det⁻¹ × [[d, -b], [-c, a]] (mod 26)
        
        Returns None if matrix is not invertible.
        """
        a, b = int(matrix[0][0]), int(matrix[0][1])
        c, d = int(matrix[1][0]), int(matrix[1][1])
        
        det = self._det_2x2(a, b, c, d)
        
        if det not in self.VALID_DETS:
            return None
        
        det_inv = self._mod_inverses[det]
        
        # Adjugate matrix: [[d, -b], [-c, a]]
        inv = np.array([
            [(det_inv * d) % self.MOD, (det_inv * (-b)) % self.MOD],
            [(det_inv * (-c)) % self.MOD, (det_inv * a) % self.MOD]
        ], dtype=int)
        
        return inv
    
    def _encrypt_digraph(self, digraph, key):
        """Encrypt a single digraph (p1, p2) with key matrix"""
        p = np.array(digraph)
        c = np.dot(key, p) % self.MOD
        return (int(c[0]), int(c[1]))
    
    def _verify_key(self, pt_digraphs, ct_digraphs, key):
        """Verify that key encrypts all plaintext digraphs to ciphertext digraphs"""
        for pt, ct in zip(pt_digraphs, ct_digraphs):
            if self._encrypt_digraph(pt, key) != ct:
                return False
        return True
    
    def _crack_algebraic(self, pt_digraphs, ct_digraphs):
        """
        Algebraic attack: Find key using K = C × P⁻¹ (mod 26)
        
        We need to find 2 plaintext digraphs that form an invertible 2x2 matrix.
        The matrix P has digraphs as columns: P = [[p1, p3], [p2, p4]]
        """
        from itertools import combinations
        
        n = len(pt_digraphs)
        
        # Try all pairs of digraphs to form invertible matrix
        for i, j in combinations(range(n), 2):
            # Build plaintext matrix P (columns are digraphs)
            p1, p2 = pt_digraphs[i]
            p3, p4 = pt_digraphs[j]
            P = np.array([[p1, p3], [p2, p4]], dtype=int)
            
            # Check if P is invertible
            det = self._det_2x2(p1, p3, p2, p4)
            if det not in self.VALID_DETS:
                continue
            
            # P is invertible, compute P⁻¹
            P_inv = self._matrix_mod_inverse_2x2(P)
            if P_inv is None:
                continue
            
            # Build ciphertext matrix C (columns are digraphs)
            c1, c2 = ct_digraphs[i]
            c3, c4 = ct_digraphs[j]
            C = np.array([[c1, c3], [c2, c4]], dtype=int)
            
            # Compute K = C × P⁻¹ (mod 26)
            K = np.dot(C, P_inv) % self.MOD
            K = K.astype(int)
            
            # Verify key works on ALL digraphs
            if self._verify_key(pt_digraphs, ct_digraphs, K):
                return K
        
        return None
    
    def _crack_bruteforce(self, pt_digraphs, ct_digraphs):
        """
        Brute force attack: Search all valid 2x2 key matrices.
        
        Optimization: Only test keys with valid determinants (coprime with 26).
        This reduces search from 26⁴ = 456,976 to ~157,248 candidates.
        
        Further optimization: Test against first digraph pair to eliminate
        candidates early before verifying against all pairs.
        """
        pt_first = pt_digraphs[0]
        ct_first = ct_digraphs[0]
        
        for a in range(self.MOD):
            for b in range(self.MOD):
                # Early check: first row of K must produce correct first ciphertext char
                c1_expected = ct_first[0]
                c1_computed = (a * pt_first[0] + b * pt_first[1]) % self.MOD
                if c1_computed != c1_expected:
                    continue
                
                for c in range(self.MOD):
                    for d in range(self.MOD):
                        # Check determinant validity
                        det = (a * d - b * c) % self.MOD
                        if det not in self.VALID_DETS:
                            continue
                        
                        # Early check: second row must produce correct second ciphertext char
                        c2_expected = ct_first[1]
                        c2_computed = (c * pt_first[0] + d * pt_first[1]) % self.MOD
                        if c2_computed != c2_expected:
                            continue
                        
                        # Full verification
                        K = np.array([[a, b], [c, d]], dtype=int)
                        if self._verify_key(pt_digraphs, ct_digraphs, K):
                            return K
        
        return None
    
    def crack_key(self, plaintext, ciphertext):
        """
        Crack 2x2 Hill Cipher key using known plaintext attack.
        
        Args:
            plaintext: Known plaintext string
            ciphertext: Corresponding ciphertext string
        
        Returns:
            2x2 numpy array containing the key matrix, or None if not found
        
        Strategy:
            1. Try algebraic approach first (fast, O(n²) where n = number of digraphs)
            2. Fall back to optimized brute force if algebraic fails
        
        Note: With only 1 digraph (2 chars), multiple keys may produce the same
        ciphertext. Use at least 4 characters (2 digraphs) for unique key recovery.
        """
        # Prepare digraphs
        pt_digraphs = self._text_to_digraphs(plaintext)
        ct_digraphs = self._text_to_digraphs(ciphertext)
        
        # Validate input
        if len(pt_digraphs) < 1:
            print("Error: Need at least 2 characters (1 digraph)")
            return None
        
        if len(pt_digraphs) != len(ct_digraphs):
            print(f"Error: Plaintext ({len(pt_digraphs)} digraphs) and ciphertext ({len(ct_digraphs)} digraphs) must have same length")
            return None
        
        # Warn about uniqueness with insufficient data
        if len(pt_digraphs) < 2:
            print("Warning: Only 1 digraph provided. Multiple keys may match.")
            print("         Use 4+ characters for guaranteed unique key recovery.")
        
        # Method 1: Algebraic attack (requires invertible plaintext matrix)
        key = self._crack_algebraic(pt_digraphs, ct_digraphs)
        if key is not None:
            return key
        
        # Method 2: Optimized brute force
        print("Algebraic approach failed (no invertible plaintext matrix). Using brute force...")
        return self._crack_bruteforce(pt_digraphs, ct_digraphs)
    
    def encrypt(self, plaintext, key):
        """Encrypt plaintext using key matrix"""
        digraphs = self._text_to_digraphs(plaintext)
        result = ''
        for dg in digraphs:
            enc = self._encrypt_digraph(dg, key)
            result += self._num_to_char(enc[0]) + self._num_to_char(enc[1])
        return result
    
    def decrypt(self, ciphertext, key, original_plaintext_length=None):
        """Decrypt ciphertext using key matrix, returning lowercase without spaces.
        
        Args:
            ciphertext: The ciphertext to decrypt
            key: The key matrix
            original_plaintext_length: If provided, strips padding 'X' if it was added
        """
        key_inv = self._matrix_mod_inverse_2x2(key)
        if key_inv is None:
            print("Error: Key is not invertible")
            return None
        
        digraphs = self._text_to_digraphs(ciphertext)
        decrypted_letters = ''
        for dg in digraphs:
            dec = self._encrypt_digraph(dg, key_inv)
            decrypted_letters += self._num_to_char(dec[0]) + self._num_to_char(dec[1])
        
        # Convert to lowercase and remove spaces
        result = decrypted_letters.lower()
        
        # Strip padding X if it exists at the end
        if len(result) > 0 and result[-1] == 'x':
            # Only remove if it's likely padding (odd original length or specified)
            if original_plaintext_length is not None:
                if len(result) > original_plaintext_length:
                    result = result[:-1]
            else:
                # Be cautious - don't remove trailing X unless we're sure it's padding
                pass
        
        return result
    
    def format_key(self, key):
        """Format key matrix for display"""
        if key is None:
            return "No key found"
        
        det = self._det_2x2(key[0][0], key[0][1], key[1][0], key[1][1])
        
        result = f"\n{'='*50}\n"
        result += "CRACKED KEY MATRIX (2x2):\n"
        result += f"{'='*50}\n"
        result += f"┌{'─'*15}┐\n"
        result += f"│ {int(key[0][0]):5d}  {int(key[0][1]):5d} │\n"
        result += f"│ {int(key[1][0]):5d}  {int(key[1][1]):5d} │\n"
        result += f"└{'─'*15}┘\n"
        result += f"Determinant (mod 26): {det}\n"
        result += f"Key as flat array: [{','.join(str(int(x)) for x in key.flatten())}]\n"
        result += f"{'='*50}\n"
        
        return result
    
    def analyze_plaintext(self, plaintext):
        """Analyze plaintext to check if algebraic attack is possible"""
        digraphs = self._text_to_digraphs(plaintext)
        n = len(digraphs)
        
        print(f"\nPlaintext Analysis: '{plaintext}'")
        print(f"Cleaned & padded: '{self._pad_text(self._clean_text(plaintext))}'")
        print(f"Digraphs: {digraphs}")
        print(f"\nPossible matrix pairs and their determinants:")
        
        from itertools import combinations
        invertible_count = 0
        
        for i, j in combinations(range(n), 2):
            p1, p2 = digraphs[i]
            p3, p4 = digraphs[j]
            det = self._det_2x2(p1, p3, p2, p4)
            invertible = det in self.VALID_DETS
            if invertible:
                invertible_count += 1
            status = "✓ INVERTIBLE" if invertible else "✗ not invertible"
            print(f"  Digraphs ({i},{j}): det = {det:2d} -> {status}")
        
        print(f"\nResult: {invertible_count} invertible pairs found")
        if invertible_count > 0:
            print("Algebraic attack WILL work.")
        else:
            print("Algebraic attack will fail. Brute force required.")


def interactive_mode():
    """Run cracker in interactive mode"""
    cracker = HillCipherCracker()
    
    print("\n" + "="*60)
    print("  HILL CIPHER KNOWN PLAINTEXT ATTACK (2x2)")
    print("  Interactive Mode")
    print("="*60)
    
    while True:
        print("\nOptions:")
        print("  1. Crack key from plaintext-ciphertext pair")
        print("  2. Decrypt with known key")
        print("  3. Encrypt with known key")
        print("  4. Analyze plaintext (check invertibility)")
        print("  5. Exit")
        
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == '1':
            plaintext = input("Enter known plaintext: ").strip()
            ciphertext = input("Enter corresponding ciphertext: ").strip()
            
            if not plaintext or not ciphertext:
                print("Error: Both plaintext and ciphertext are required")
                continue
            
            key = cracker.crack_key(plaintext, ciphertext)
            
            if key is not None:
                print(cracker.format_key(key))
                
                decrypted = cracker.decrypt(ciphertext, key)
                print(f"Verification - Decrypted: {decrypted}")
                
                decrypt_more = input("\nDecrypt more ciphertext with this key? (y/n): ").strip().lower()
                if decrypt_more == 'y':
                    more_cipher = input("Enter ciphertext to decrypt: ").strip()
                    result = cracker.decrypt(more_cipher, key)
                    print(f"Decrypted: {result}")
            else:
                print("\nFailed to crack key. Check your plaintext-ciphertext pair.")
        
        elif choice == '2':
            key_str = input("Enter key as comma-separated values (e.g., 3,3,2,5): ").strip()
            try:
                values = [int(x.strip()) for x in key_str.split(',')]
                if len(values) != 4:
                    print("Error: Need exactly 4 values for 2x2 key matrix")
                    continue
                key = np.array(values).reshape(2, 2)
                
                ciphertext = input("Enter ciphertext to decrypt: ").strip()
                result = cracker.decrypt(ciphertext, key)
                if result:
                    print(f"\nDecrypted: {result}")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == '3':
            key_str = input("Enter key as comma-separated values (e.g., 3,3,2,5): ").strip()
            try:
                values = [int(x.strip()) for x in key_str.split(',')]
                if len(values) != 4:
                    print("Error: Need exactly 4 values for 2x2 key matrix")
                    continue
                key = np.array(values).reshape(2, 2)
                
                plaintext = input("Enter plaintext to encrypt: ").strip()
                result = cracker.encrypt(plaintext, key)
                print(f"\nEncrypted: {result}")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == '4':
            plaintext = input("Enter plaintext to analyze: ").strip()
            if plaintext:
                cracker.analyze_plaintext(plaintext)
        
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


def main():
    parser = argparse.ArgumentParser(
        description='Hill Cipher Known Plaintext Attack Cracker (2x2 Matrix)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -i                            # Interactive mode

Mathematical Background:
  Hill cipher: C = K × P (mod 26)
  Attack: K = C × P⁻¹ (mod 26)
  P⁻¹ exists when gcd(det(P), 26) = 1
        """
    )
    
    parser.add_argument('-p', '--plaintext',
                        help='Known plaintext')
    parser.add_argument('-c', '--ciphertext',
                        help='Corresponding ciphertext')
    parser.add_argument('-d', '--decrypt', type=str,
                        help='Additional ciphertext to decrypt with cracked key')
    parser.add_argument('-a', '--analyze', type=str,
                        help='Analyze plaintext for invertibility')
    parser.add_argument('-i', '--interactive', action='store_true',
                        help='Run in interactive mode')
    
    args = parser.parse_args()
    
    cracker = HillCipherCracker()
    
    # Analyze mode
    if args.analyze:
        cracker.analyze_plaintext(args.analyze)
        return
    
    # Interactive mode
    if args.interactive or (not args.plaintext and not args.ciphertext):
        interactive_mode()
        return
    
    if not args.plaintext or not args.ciphertext:
        parser.error("Both --plaintext and --ciphertext are required (or use -i for interactive mode)")
    
    print("\n" + "="*60)
    print("  HILL CIPHER KNOWN PLAINTEXT ATTACK (2x2)")
    print("="*60)
    print(f"\nPlaintext:  {args.plaintext}")
    print(f"Ciphertext: {args.ciphertext}")
    
    # Crack the key
    key = cracker.crack_key(args.plaintext, args.ciphertext)
    
    if key is not None:
        print(cracker.format_key(key))
        
        # Verify by decrypting
        decrypted = cracker.decrypt(args.ciphertext, key)
        print(f"Verification - Decrypted: {decrypted}")
        
        # Decrypt additional ciphertext if provided
        if args.decrypt:
            print(f"\n{'='*50}")
            print("DECRYPTING ADDITIONAL CIPHERTEXT:")
            print(f"{'='*50}")
            print(f"Ciphertext: {args.decrypt}")
            decrypted_extra = cracker.decrypt(args.decrypt, key)
            print(f"Decrypted:  {decrypted_extra}")
    else:
        print("\nFailed to crack the key.")
        print("Tips:")
        print("  - Ensure plaintext-ciphertext pair is correct")
        print("  - Verify they correspond to the same encryption")
        print("  - Use -a to analyze plaintext invertibility")


if __name__ == '__main__':
    main()
