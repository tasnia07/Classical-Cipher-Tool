#!/usr/bin/env python3
"""
Classical Cipher Tool - GUI Application
=======================================
A production-grade graphical interface for classical cryptography.

Features:
- Four classical ciphers (Caesar, Affine, Playfair, Hill)
- Hill Cipher Known Plaintext Attack cracker
- Modern clean interface
- Session history and settings persistence

Usage:
    python run_gui.py              # Normal mode
    python run_gui.py --crack      # Start in crack mode
    python run_gui.py -c           # Start in crack mode (short)

Requirements:
    - Python 3.8+
    - PyQt6
    - NumPy
"""

if __name__ == "__main__":
    from cipher_gui.main import main
    main()
