#!/usr/bin/env python3
"""
Classical Cipher Tool
A user-friendly tool for encryption and decryption using classical ciphers:
- Caesar Cipher
- Affine Cipher
- Playfair Cipher
- Hill Cipher (2x2 matrix)
"""

import readline  # Enable arrow keys and command history
from ciphers.caesar_cipher import CaesarCipher
from ciphers.affine_cipher import AffineCipher
from ciphers.playfair_cipher import PlayfairCipher
from ciphers.hill_cipher import HillCipher


def print_banner():
    """Print application banner"""
    print("\n" + "=" * 60)
    print(" " * 15 + "CLASSICAL CIPHER TOOL")
    print("=" * 60)


def print_menu():
    """Print main menu"""
    print("\n[SELECT CIPHER]")
    print("1. Caesar Cipher")
    print("2. Affine Cipher")
    print("3. Playfair Cipher")
    print("4. Hill Cipher (2x2)")
    print("5. Exit")


def print_operation_menu():
    """Print operation menu"""
    print("\n[SELECT OPERATION]")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Back to main menu")


def get_input(prompt, input_type=str):
    """Get validated input from user"""
    while True:
        try:
            user_input = input(prompt)
            if input_type == str:
                return user_input
            else:
                return input_type(user_input)
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")


def caesar_cipher_interface():
    """Interface for Caesar Cipher"""
    cipher = CaesarCipher()
    
    print("\n" + "─" * 60)
    print("CAESAR CIPHER - Simple Shift Cipher")
    print("─" * 60)
    print("📝 Key: A number from 0-25 (shift amount)")
    print("   Example: Key=3 means A→D, B→E, C→F, etc.")
    print("─" * 60)
    
    while True:
        print_operation_menu()
        choice = get_input("Enter your choice (1-3): ")
        
        if choice == '3':
            break
        
        if choice == '1':  # Encrypt
            plaintext = get_input("\nEnter plaintext: ")
            key = get_input("Enter shift value (0-25): ")
            try:
                result = cipher.encrypt(plaintext, key)
                print(f"\n" + "═" * 60)
                print("[ENCRYPTION RESULT]")
                print("═" * 60)
                print(f"Plaintext:  {plaintext}")
                print(f"Key:        {key}")
                print(f"Ciphertext: {result}")
                print("═" * 60)
            except Exception as e:
                print(f"❌ Error: {e}")
        
        elif choice == '2':  # Decrypt
            ciphertext = get_input("\nEnter ciphertext: ")
            key = get_input("Enter shift value (0-25): ")
            try:
                result = cipher.decrypt(ciphertext, key)
                print(f"\n" + "═" * 60)
                print("[DECRYPTION RESULT]")
                print("═" * 60)
                print(f"Ciphertext: {ciphertext}")
                print(f"Key:        {key}")
                print(f"Plaintext:  {result}")
                print("═" * 60)
            except Exception as e:
                print(f"❌ Error: {e}")
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


def affine_cipher_interface():
    """Interface for Affine Cipher"""
    cipher = AffineCipher()
    
    print("\n" + "─" * 60)
    print("AFFINE CIPHER - E(x) = (ax + b) mod 26")
    print("─" * 60)
    print("📝 Key Format: a,b (two numbers separated by comma)")
    print("   • 'a' must be coprime with 26")
    print("   • Valid 'a' values: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25")
    print("   • 'b' can be any number from 0-25")
    print("\n✅ Example Keys:")
    print("   • 5,8   • 7,3   • 9,15   • 11,4")
    print("─" * 60)
    
    while True:
        print_operation_menu()
        choice = get_input("Enter your choice (1-3): ")
        
        if choice == '3':
            break
        
        if choice == '1':  # Encrypt
            plaintext = get_input("\nEnter plaintext: ")
            key = get_input("Enter key (format: a,b): ")
            try:
                result = cipher.encrypt(plaintext, key)
                print(f"\n" + "═" * 60)
                print("[ENCRYPTION RESULT]")
                print("═" * 60)
                print(f"Plaintext:  {plaintext}")
                print(f"Key:        {key}")
                print(f"Ciphertext: {result}")
                print("═" * 60)
            except Exception as e:
                print(f"❌ Error: {e}")
        
        elif choice == '2':  # Decrypt
            ciphertext = get_input("\nEnter ciphertext: ")
            key = get_input("Enter key (format: a,b): ")
            try:
                result = cipher.decrypt(ciphertext, key)
                print(f"\n" + "═" * 60)
                print("[DECRYPTION RESULT]")
                print("═" * 60)
                print(f"Ciphertext: {ciphertext}")
                print(f"Key:        {key}")
                print(f"Plaintext:  {result}")
                print("═" * 60)
            except Exception as e:
                print(f"❌ Error: {e}")
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


def playfair_cipher_interface():
    """Interface for Playfair Cipher"""
    cipher = PlayfairCipher()
    
    print("\n" + "─" * 60)
    print("PLAYFAIR CIPHER - 5x5 Key Matrix Cipher")
    print("─" * 60)
    print("📝 Key: Any keyword or phrase")
    print("   Example: MONARCHY, SECRET, HELLO WORLD")
    print("\n⚠️  Note: J is treated as I in Playfair cipher")
    print("   (The 26-letter alphabet is reduced to 25 letters)")
    print("─" * 60)
    
    while True:
        print_operation_menu()
        choice = get_input("Enter your choice (1-3): ")
        
        if choice == '3':
            break
        
        if choice == '1':  # Encrypt
            plaintext = get_input("\nEnter plaintext: ")
            key = get_input("Enter key (keyword): ")
            try:
                result = cipher.encrypt(plaintext, key)
                print(f"\n" + "═" * 60)
                print("[ENCRYPTION RESULT]")
                print("═" * 60)
                print(f"Plaintext:  {plaintext}")
                print(f"Key:        {key}")
                print(f"Ciphertext: {result}")
                print("═" * 60)
            except Exception as e:
                print(f"❌ Error: {e}")
        
        elif choice == '2':  # Decrypt
            ciphertext = get_input("\nEnter ciphertext: ")
            key = get_input("Enter key (keyword): ")
            try:
                result = cipher.decrypt(ciphertext, key)
                print(f"\n" + "═" * 60)
                print("[DECRYPTION RESULT]")
                print("═" * 60)
                print(f"Ciphertext: {ciphertext}")
                print(f"Key:        {key}")
                print(f"Plaintext:  {result}")
                print("═" * 60)
            except Exception as e:
                print(f"❌ Error: {e}")
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


def display_hill_help():
    """Display helpful information for Hill Cipher"""
    print("\n" + "─" * 60)
    print("HILL CIPHER - Key Matrix Guide")
    print("─" * 60)
    print("\n📝 Key Format: Enter 4 numbers separated by commas")
    print("   Format: a,b,c,d")
    print("   This creates matrix: [[a, b],")
    print("                         [c, d]]")
    print("\n✅ Valid Example Keys:")
    print("   • 3,3,2,5   → [[3,3],[2,5]]   (det mod 26 = 9)")
    print("   • 5,8,17,3  → [[5,8],[17,3]]  (det mod 26 = 7)")
    print("   • 7,8,11,11 → [[7,8],[11,11]] (det mod 26 = 1)")
    print("\n⚠️  Important: Matrix determinant (mod 26) must be coprime with 26")
    print("   Valid determinant values: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25")
    print("─" * 60)


def validate_and_display_matrix(key_str):
    """Validate and display the matrix for user confirmation"""
    try:
        values = [int(x.strip()) for x in key_str.split(',')]
        if len(values) != 4:
            print("❌ Error: Need exactly 4 values for 2x2 matrix")
            return False
        
        print(f"\nYour matrix:")
        print(f"  ┌         ┐")
        print(f"  │ {values[0]:2d}  {values[1]:2d} │")
        print(f"  │ {values[2]:2d}  {values[3]:2d} │")
        print(f"  └         ┘")
        
        # Calculate determinant
        det = values[0] * values[3] - values[1] * values[2]
        det_mod = det % 26
        print(f"  Determinant = {det}")
        print(f"  Determinant (mod 26) = {det_mod}")
        
        # Check if coprime with 26
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        if gcd(abs(det_mod), 26) != 1:
            print(f"\n❌ Invalid! Determinant {det_mod} is NOT coprime with 26")
            print(f"   GCD({abs(det_mod)}, 26) = {gcd(abs(det_mod), 26)}")
            print("   Please try a different matrix.")
            return False
        else:
            print(f"✅ Valid! Determinant {det_mod} is coprime with 26")
            return True
            
    except ValueError:
        print("❌ Error: Please enter valid numbers")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def hill_cipher_interface():
    """Interface for Hill Cipher (2x2 matrix)"""
    cipher = HillCipher()
    
    display_hill_help()
    
    while True:
        print_operation_menu()
        choice = get_input("Enter your choice (1-3): ")
        
        if choice == '3':
            break
        
        if choice == '1':  # Encrypt
            plaintext = get_input("\nEnter plaintext: ")
            
            # Key input with validation loop
            while True:
                print("\nEnter key matrix (type 'help' for examples)")
                key = get_input("Key (format a,b,c,d): ")
                
                if key.lower() == 'help':
                    display_hill_help()
                    continue
                
                if validate_and_display_matrix(key):
                    break
                print("Please enter a valid key matrix.\n")
            
            try:
                result = cipher.encrypt(plaintext, key)
                print(f"\n" + "═" * 60)
                print("[ENCRYPTION RESULT]")
                print("═" * 60)
                print(f"Plaintext:  {plaintext}")
                print(f"Key Matrix: {key}")
                print(f"Ciphertext: {result}")
                print("═" * 60)
            except Exception as e:
                print(f"❌ Error: {e}")
        
        elif choice == '2':  # Decrypt
            ciphertext = get_input("\nEnter ciphertext: ")
            
            # Key input with validation loop
            while True:
                print("\nEnter key matrix (type 'help' for examples)")
                key = get_input("Key (format a,b,c,d): ")
                
                if key.lower() == 'help':
                    display_hill_help()
                    continue
                
                if validate_and_display_matrix(key):
                    break
                print("Please enter a valid key matrix.\n")
            
            try:
                result = cipher.decrypt(ciphertext, key)
                print(f"\n" + "═" * 60)
                print("[DECRYPTION RESULT]")
                print("═" * 60)
                print(f"Ciphertext: {ciphertext}")
                print(f"Key Matrix: {key}")
                print(f"Plaintext:  {result}")
                print("═" * 60)
            except Exception as e:
                print(f"❌ Error: {e}")
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


def main():
    """Main application loop"""
    print_banner()
    
    while True:
        print_menu()
        choice = get_input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            caesar_cipher_interface()
        elif choice == '2':
            affine_cipher_interface()
        elif choice == '3':
            playfair_cipher_interface()
        elif choice == '4':
            hill_cipher_interface()
        elif choice == '5':
            print("\nThank you for using Classical Cipher Tool!")
            print("=" * 60 + "\n")
            break
        else:
            print("\nInvalid choice. Please select a number between 1 and 5.")


if __name__ == "__main__":
    main()
