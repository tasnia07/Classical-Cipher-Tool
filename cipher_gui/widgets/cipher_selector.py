"""Beautiful cipher selector with button grid - No scrolling needed."""

from PyQt6.QtWidgets import (QFrame, QVBoxLayout, QGridLayout, QPushButton, QLabel)
from PyQt6.QtCore import pyqtSignal


class CipherButton(QPushButton):
    """Beautiful cipher selection button."""
    
    def __init__(self, icon, name, parent=None):
        super().__init__(parent)
        self.cipher_name = name
        self.setCheckable(True)
        self.setText(f"{icon}\n{name}")
        self.setMinimumSize(140, 90)
        self.setMaximumSize(140, 90)
        self.setup_style()
    
    def setup_style(self):
        """Setup beautiful button style."""
        self.setStyleSheet("""
            QPushButton {
                background-color: #ffffff;
                color: #24292f;
                border: 1px solid #d0d7de;
                border-radius: 12px;
                padding: 10px;
                font-size: 12px;
                font-weight: 500;
                text-align: center;
            }
            QPushButton:hover {
                background-color: #f6f8fa;
                border-color: #24292f;
                color: #24292f;
            }
            QPushButton:checked {
                background-color: #ffffff;
                border: 2px solid #24292f;
                color: #24292f;
                font-weight: 600;
            }
        """)


class CipherSelector(QFrame):
    """Modern cipher selector with button grid - all visible, no scroll."""
    
    cipher_changed = pyqtSignal(str)  # Emits cipher name
    
    def __init__(self, cipher_names, cipher_icons, parent=None):
        super().__init__(parent)
        self.cipher_names = cipher_names
        self.cipher_icons = cipher_icons
        self.buttons = []
        self.current_cipher = None
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the beautiful cipher selector."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)
        
        # Header
        header = QLabel("📚 Select Cipher")
        header.setStyleSheet("""
            font-size: 14px;
            font-weight: 600;
            color: #24292f;
            padding-bottom: 8px;
        """)
        layout.addWidget(header)
        
        # Grid for buttons - 2 columns for better fit
        grid = QGridLayout()
        grid.setSpacing(12)
        grid.setContentsMargins(0, 0, 0, 0)
        
        # Create buttons in grid (2 columns for 4 ciphers = 2 rows)
        row, col = 0, 0
        for name in self.cipher_names:
            icon = self.cipher_icons.get(name, "🔐")
            btn = CipherButton(icon, name)
            btn.clicked.connect(lambda checked, n=name: self.select_cipher(n))
            self.buttons.append(btn)
            grid.addWidget(btn, row, col)
            
            col += 1
            if col >= 2:
                col = 0
                row += 1
        
        layout.addLayout(grid)
        
        # Select first cipher
        if self.buttons:
            self.buttons[0].setChecked(True)
            self.current_cipher = self.cipher_names[0]
    
    def select_cipher(self, cipher_name):
        """Select a cipher."""
        # Uncheck all buttons
        for btn in self.buttons:
            if btn.cipher_name != cipher_name:
                btn.setChecked(False)
            else:
                btn.setChecked(True)
        
        self.current_cipher = cipher_name
        self.cipher_changed.emit(cipher_name)
    
    def get_current_cipher(self):
        """Get currently selected cipher."""
        return self.current_cipher
    
    def set_current_cipher(self, cipher_name):
        """Set current cipher by name."""
        for btn in self.buttons:
            if btn.cipher_name == cipher_name:
                btn.setChecked(True)
                self.current_cipher = cipher_name
            else:
                btn.setChecked(False)
