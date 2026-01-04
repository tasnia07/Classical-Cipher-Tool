#!/usr/bin/env python3
"""
Hill Cipher Cracker - Known Plaintext Attack
============================================

This cracker finds the 2x2 key matrix used in Hill cipher encryption
when you have a known plaintext-ciphertext pair using matrix mathematics.
"""

import numpy as np


class HillCipherCracker:
    """Hill Cipher Cracker using Known Plaintext Attack for 2x2 matrices."""
    
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    MOD = 26
    
    def _gcd(self, a, b):
        """Calculate Greatest Common Divisor"""
        while b:
            a, b = b, a % b
        return a
    
    def _mod_inverse(self, a, m=26):
        """
        Find modular multiplicative inverse using brute force.
        We try all numbers from 1 to m-1 and check if (a * i) mod m = 1
        """
        a = a % m
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        return None
    
    def _char_to_num(self, char):
        """Convert character to number (A=0, B=1, ..., Z=25)"""
        return ord(char.upper()) - ord('A')
    
    def _num_to_char(self, num):
        """Convert number to character"""
        return chr((num % self.MOD) + ord('A'))
    
    def _clean_text(self, text):
        """Remove spaces and non-alphabetic characters, convert to uppercase"""
        return ''.join(c.upper() for c in text if c.isalpha())
    
    def _pad_text(self, text):
        """Pad text with 'X' to make length even (Hill cipher needs pairs)"""
        if len(text) % 2 != 0:
            text += 'X'
        return text
    
    def _text_to_digraphs(self, text):
        """
        Convert text to digraphs (pairs of numbers)
        Example: "HELLO" -> [(7,4), (11,11), (14,23)] where O=14, X=23 (padding)
        """
        text = self._pad_text(self._clean_text(text))
        digraphs = []
        for i in range(0, len(text), 2):
            num1 = self._char_to_num(text[i])
            num2 = self._char_to_num(text[i+1])
            digraphs.append((num1, num2))
        return digraphs
    
    def _matrix_determinant_2x2(self, matrix):
        """
        Calculate determinant of 2x2 matrix mod 26
        For matrix [[a,b],[c,d]], determinant = (a*d - b*c) mod 26
        """
        a, b = int(matrix[0][0]), int(matrix[0][1])
        c, d = int(matrix[1][0]), int(matrix[1][1])
        det = (a * d - b * c) % self.MOD
        return det
    
    def _matrix_inverse_2x2(self, matrix):
        """
        Calculate modular inverse of 2x2 matrix mod 26
        
        For matrix M = [[a, b], [c, d]]:
        
        Step 1: Calculate determinant
            det = (a*d - b*c) mod 26
        
        Step 2: Check if determinant has inverse (must be coprime with 26)
            Valid determinants: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25
        
        Step 3: Find det_inverse such that (det * det_inverse) mod 26 = 1
        
        Step 4: Calculate inverse matrix
            M⁻¹ = det_inverse × [[d, -b], [-c, a]] (mod 26)
        """
        a, b = int(matrix[0][0]), int(matrix[0][1])
        c, d = int(matrix[1][0]), int(matrix[1][1])
        
        # Step 1: Calculate determinant
        det = (a * d - b * c) % self.MOD
        
        # Step 2: Check if determinant is invertible
        if self._gcd(det, self.MOD) != 1:
            return None
        
        # Step 3: Find modular inverse of determinant
        det_inv = self._mod_inverse(det, self.MOD)
        if det_inv is None:
            return None
        
        # Step 4: Calculate inverse matrix = det_inv * adjugate
        # Adjugate of [[a,b],[c,d]] is [[d,-b],[-c,a]]
        inv_matrix = np.array([
            [(det_inv * d) % self.MOD, (det_inv * (-b)) % self.MOD],
            [(det_inv * (-c)) % self.MOD, (det_inv * a) % self.MOD]
        ], dtype=int)
        
        return inv_matrix
    
    def _encrypt_digraph(self, digraph, key):
        """
        Encrypt a single digraph using key matrix
        Calculation: C = K × P (mod 26)
        """
        p = np.array(digraph)
        c = np.dot(key, p) % self.MOD
        return (int(c[0]), int(c[1]))
    
    def _verify_key(self, pt_digraphs, ct_digraphs, key):
        """Check if key correctly encrypts ALL plaintext digraphs"""
        for pt, ct in zip(pt_digraphs, ct_digraphs):
            if self._encrypt_digraph(pt, key) != ct:
                return False
        return True
    
    def crack_key(self, plaintext, ciphertext):
        """
        Crack the Hill Cipher key using known plaintext attack.
        
        Args:
            plaintext: Known plaintext string
            ciphertext: Corresponding ciphertext string
        
        Returns:
            2x2 numpy array containing the key matrix, or None if not found
        """
        
        print("\n" + "="*70)
        print(" " * 15 + "HILL CIPHER KNOWN PLAINTEXT ATTACK")
        print("="*70)
        
        # Step 1: Convert to digraphs
        print("\nSTEP 1: Converting text to digraphs")
        print("-" * 70)
        pt_clean = self._clean_text(plaintext)
        ct_clean = self._clean_text(ciphertext)
        
        pt_digraphs = self._text_to_digraphs(plaintext)
        ct_digraphs = self._text_to_digraphs(ciphertext)
        
        print(f"Plaintext (cleaned):  {pt_clean}")
        print(f"Plaintext digraphs:   {pt_digraphs}")
        print(f"Ciphertext (cleaned): {ct_clean}")
        print(f"Ciphertext digraphs:  {ct_digraphs}")
        
        # Validation
        if len(pt_digraphs) < 2:
            print("\n❌ ERROR: Need at least 4 characters (2 digraphs) for attack")
            print("   We need two digraph pairs to build 2×2 matrices")
            return None
        
        if len(pt_digraphs) != len(ct_digraphs):
            print(f"\n❌ ERROR: Plaintext and ciphertext length mismatch")
            return None
        
        # Step 2: Build matrices from first two digraphs
        print("\nSTEP 2: Building plaintext and ciphertext matrices")
        print("-" * 70)
        
        p1, p2 = pt_digraphs[0]  # First digraph
        p3, p4 = pt_digraphs[1]  # Second digraph
        
        c1, c2 = ct_digraphs[0]  # First ciphertext digraph
        c3, c4 = ct_digraphs[1]  # Second ciphertext digraph
        
        # Matrices use digraphs as COLUMNS
        P = np.array([[p1, p3], [p2, p4]], dtype=int)
        C = np.array([[c1, c3], [c2, c4]], dtype=int)
        
        print(f"Plaintext matrix P (columns are digraphs):")
        print(f"    P = [[{p1:2d}  {p3:2d}]    <- digraphs: ({self._num_to_char(p1)},{self._num_to_char(p2)}) and ({self._num_to_char(p3)},{self._num_to_char(p4)})")
        print(f"         [{p2:2d}  {p4:2d}]")
        
        print(f"\nCiphertext matrix C (columns are digraphs):")
        print(f"    C = [[{c1:2d}  {c3:2d}]    <- digraphs: ({self._num_to_char(c1)},{self._num_to_char(c2)}) and ({self._num_to_char(c3)},{self._num_to_char(c4)})")
        print(f"         [{c2:2d}  {c4:2d}]")
        
        # Step 3: Find inverse of P
        print("\nSTEP 3: Finding inverse of plaintext matrix P")
        print("-" * 70)
        
        det = self._matrix_determinant_2x2(P)
        print(f"Determinant of P = ({p1}×{p4} - {p3}×{p2}) mod 26")
        print(f"                 = ({p1*p4} - {p3*p2}) mod 26")
        print(f"                 = {p1*p4 - p3*p2} mod 26")
        print(f"                 = {det}")
        
        # Check if invertible
        if self._gcd(det, self.MOD) != 1:
            print(f"\n❌ ERROR: Determinant {det} is NOT coprime with 26!")
            print(f"   gcd({det}, 26) = {self._gcd(det, 26)}")
            print("   Cannot find inverse. Try different plaintext-ciphertext pair.")
            return None
        
        print(f"✓ Determinant {det} is coprime with 26 (invertible)")
        
        # Find modular inverse of determinant
        det_inv = self._mod_inverse(det, self.MOD)
        print(f"\nFinding inverse of {det} mod 26:")
        print(f"   We need x such that ({det} × x) mod 26 = 1")
        print(f"   det_inverse({det}) = {det_inv}")
        print(f"   Verification: ({det} × {det_inv}) mod 26 = {(det * det_inv) % 26} ✓")
        
        # Calculate P inverse
        P_inv = self._matrix_inverse_2x2(P)
        if P_inv is None:
            print("\n❌ ERROR: Cannot find matrix inverse")
            return None
        
        print(f"\nP⁻¹ = {det_inv} × [[{p4:2d}, {-p3:3d}], [{-p2:3d}, {p1:2d}]] mod 26")
        print(f"    = [[{(det_inv * p4) % 26:2d}, {(det_inv * (-p3)) % 26:2d}]")
        print(f"       [{(det_inv * (-p2)) % 26:2d}, {(det_inv * p1) % 26:2d}]]")
        
        # Step 4: Calculate key K = C × P⁻¹
        print("\nSTEP 4: Calculating key matrix K = C × P⁻¹ (mod 26)")
        print("-" * 70)
        
        K = np.dot(C, P_inv) % self.MOD
        K = K.astype(int)
        
        print(f"K = C × P⁻¹ mod 26")
        print(f"K = [[{C[0][0]:2d}, {C[0][1]:2d}]   [[{P_inv[0][0]:2d}, {P_inv[0][1]:2d}]")
        print(f"     [{C[1][0]:2d}, {C[1][1]:2d}] × [{P_inv[1][0]:2d}, {P_inv[1][1]:2d}] mod 26")
        
        # Show calculation
        k11_raw = C[0][0] * P_inv[0][0] + C[0][1] * P_inv[1][0]
        k12_raw = C[0][0] * P_inv[0][1] + C[0][1] * P_inv[1][1]
        k21_raw = C[1][0] * P_inv[0][0] + C[1][1] * P_inv[1][0]
        k22_raw = C[1][0] * P_inv[0][1] + C[1][1] * P_inv[1][1]
        
        print(f"\nK = [[{k11_raw:3d}, {k12_raw:3d}]")
        print(f"     [{k21_raw:3d}, {k22_raw:3d}] mod 26")
        
        print(f"\nK = [[{K[0][0]:2d}, {K[0][1]:2d}]")
        print(f"     [{K[1][0]:2d}, {K[1][1]:2d}]")
        
        # Verify the key
        print("\nSTEP 5: Verifying the key")
        print("-" * 70)
        
        if self._verify_key(pt_digraphs, ct_digraphs, K):
            print("✓ Key verified! It correctly encrypts all digraphs.")
            return K
        else:
            print("❌ Key verification failed!")
            return None
    
    def encrypt(self, plaintext, key):
        """Encrypt plaintext using key matrix"""
        digraphs = self._text_to_digraphs(plaintext)
        result = ''
        for dg in digraphs:
            enc = self._encrypt_digraph(dg, key)
            result += self._num_to_char(enc[0]) + self._num_to_char(enc[1])
        return result
    
    def decrypt(self, ciphertext, key):
        """Decrypt ciphertext using key matrix"""
        key_inv = self._matrix_inverse_2x2(key)
        if key_inv is None:
            print("❌ Error: Key is not invertible")
            return None
        
        digraphs = self._text_to_digraphs(ciphertext)
        result = ''
        for dg in digraphs:
            dec = self._encrypt_digraph(dg, key_inv)
            result += self._num_to_char(dec[0]) + self._num_to_char(dec[1])
        
        # Convert to lowercase and remove trailing padding X if present
        result = result.lower()
        if result.endswith('x'):
            result = result[:-1]
        
        return result


if __name__ == '__main__':
    print("This module is designed to be used through the GUI.")
    print("Run: python run_gui.py")
