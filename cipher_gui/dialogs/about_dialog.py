"""About dialog."""

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QDialogButtonBox
from PyQt6.QtCore import Qt


class AboutDialog(QDialog):
    """About dialog with app information."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About Classical Cipher Tool")
        self.setFixedSize(500, 400)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Logo
        logo = QLabel("🔐")
        logo.setStyleSheet("font-size: 64px;")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(logo)
        
        # Title
        title = QLabel("Classical Cipher Tool")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #24292f;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # Description
        desc = QLabel(
            "A modern, user-friendly application for classical cryptography.\n\n"
            "Features:\n"
            "• Caesar, Affine, Playfair, and Hill ciphers\n"
            "• Hill Cipher Known Plaintext Attack cracker\n"
            "• Beautiful clean interface\n"
            "• History tracking\n"
            "• Import/Export functionality\n"
            "• Real-time validation\n"
            "• Keyboard shortcuts"
        )
        desc.setStyleSheet("color: #24292f; font-size: 13px; line-height: 1.5;")
        desc.setWordWrap(True)
        layout.addWidget(desc)
        
        layout.addStretch()
        
        # Buttons
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        button_box.accepted.connect(self.accept)
        layout.addWidget(button_box)
        
        self.setStyleSheet("""
            QDialog {
                background-color: #f6f8fa;
            }
            QDialogButtonBox QPushButton {
                background-color: #ffffff;
                color: #24292f;
                border: 1px solid #d0d7de;
                border-radius: 6px;
                padding: 8px 20px;
                min-width: 80px;
                min-height: 32px;
                max-height: 36px;
                font-weight: 500;
                font-size: 13px;
            }
            QDialogButtonBox QPushButton:hover {
                background-color: #0969da;
                border-color: #0969da;
                color: #ffffff;
            }
        """)
