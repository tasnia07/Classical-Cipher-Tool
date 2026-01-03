"""Clean, minimal header with title."""

from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt


class HeaderWidget(QFrame):
    """Minimal, beautiful header."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("header")
        self.setMinimumHeight(50)
        self.setMaximumHeight(50)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(24, 0, 24, 0)
        
        # Logo and title
        logo = QLabel("🔐")
        logo.setStyleSheet("font-size: 28px;")
        layout.addWidget(logo)
        
        title_text = QLabel("Classical Cipher Tool")
        title_text.setStyleSheet("""
            font-size: 18px;
            font-weight: 600;
            color: #24292f;
            margin-left: 12px;
        """)
        layout.addWidget(title_text)
        
        layout.addStretch()
