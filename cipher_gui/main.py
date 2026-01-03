#!/usr/bin/env python3
"""
Classical Cipher Tool - GUI Application
=======================================
Modern PyQt6 interface for classical cryptography.

Main entry point for the modularized GUI application.
"""

import sys
import os
import argparse
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont

# Add parent directory to path if running from cipher_gui folder
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)

from cipher_gui import CipherGUI


def main():
    """Run the application."""
    parser = argparse.ArgumentParser(
        description='Classical Cipher Tool - GUI Application',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py              # Start in normal cipher mode
  python main.py --crack      # Start in crack mode (Hill cipher cracker)
        """
    )
    parser.add_argument('--crack', '-c', action='store_true',
                        help='Start in crack mode (Hill cipher known plaintext attack)')
    
    args = parser.parse_args()
    
    app = QApplication(sys.argv)
    app.setApplicationName("Classical Cipher Tool")
    app.setOrganizationName("CipherTool")
    app.setOrganizationDomain("ciphertool.app")
    
    # Set application-wide font
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    
    # Create and show window
    window = CipherGUI(crack_mode=args.crack)
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
