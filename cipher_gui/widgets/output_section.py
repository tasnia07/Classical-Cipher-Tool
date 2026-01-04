"""Output section widget."""

from PyQt6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout, 
                              QLabel, QTextEdit)
from PyQt6.QtCore import QTimer


class OutputSection(QFrame):
    """Output section for displaying results."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("section")
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        
        # Header
        header = QHBoxLayout()
        icon = QLabel("📤")
        icon.setStyleSheet("font-size: 16px;")
        header.addWidget(icon)
        
        self.label = QLabel("Result")
        self.label.setStyleSheet("font-size: 13px; font-weight: 600; color: #24292f;")
        header.addWidget(self.label)
        
        header.addStretch()
        
        layout.addLayout(header)
        
        # Text edit
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setPlaceholderText("Results will appear here...")
        self.text_edit.setMinimumHeight(60)
        self.text_edit.setMaximumHeight(100)
        self.text_edit.setStyleSheet("""
            QTextEdit {
                background-color: #ffffff;
                color: #24292f;
                selection-background-color: #0969da;
                selection-color: #ffffff;
            }
        """)
        layout.addWidget(self.text_edit)
    
    def set_label(self, text):
        """Set the section label."""
        self.label.setText(text)
    
    def get_text(self):
        """Get the output text."""
        return self.text_edit.toPlainText()
    
    def set_text(self, text, force_case=None):
        """
        Set the output text with optional case enforcement.
        
        Args:
            text: Text to display
            force_case: 'upper' for UPPERCASE, 'lower' for lowercase, None for no change
        """
        if force_case == 'upper':
            text = text.upper()
        elif force_case == 'lower':
            text = text.lower()
        
        self.text_edit.setPlainText(text)
    
    def clear(self):
        """Clear the output text."""
        self.text_edit.clear()
    
    def flash_success(self):
        """Flash success indicator."""
        self.text_edit.setStyleSheet("""
            QTextEdit {
                background-color: #ffffff;
                color: #24292f;
                border: 2px solid #1a7f37;
                border-radius: 8px;
                padding: 12px;
                font-size: 13px;
                font-family: 'Consolas', 'Monaco', monospace;
                selection-background-color: #0969da;
                selection-color: #ffffff;
            }
        """)
        
        QTimer.singleShot(500, lambda: self.text_edit.setStyleSheet("""
            QTextEdit {
                background-color: #ffffff;
                color: #24292f;
                border: 1px solid #d0d7de;
                border-radius: 8px;
                padding: 12px;
                font-size: 13px;
                font-family: 'Consolas', 'Monaco', monospace;
                selection-background-color: #0969da;
                selection-color: #ffffff;
            }
        """))
