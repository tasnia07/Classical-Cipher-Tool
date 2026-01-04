"""
Classical Cipher Tool - GUI Package
===================================
Production-grade GUI for classical cryptography.

This package provides a modern PyQt6-based graphical interface
for encrypting/decrypting text using classical ciphers and
cracking Hill cipher keys using known plaintext attacks.

Modules:
    core/       - Main application logic and settings
    ui/         - User interface components (panels, headers)
    widgets/    - Reusable UI widgets
    dialogs/    - Dialog windows (about, history)
    actions/    - Action handlers (cipher ops, file ops)
    models/     - Data models (history, cipher config)
    utils/      - Utility functions (validators, helpers)

Usage:
    from cipher_gui import CipherGUI
    
    window = CipherGUI()
    window.show()
"""

from cipher_gui.core.application import CipherGUI

__all__ = ['CipherGUI']
