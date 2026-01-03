"""Input text section widget."""

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton
from PyQt6.QtCore import Qt, pyqtSignal


class InputSection(QFrame):
    """Input text section with character counter."""
    
    text_changed = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("section")
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        
        # Header
        header = QHBoxLayout()
        icon = QLabel("📝")
        icon.setStyleSheet("font-size: 16px;")
        header.addWidget(icon)
        
        self.label = QLabel("Text to Encrypt")
        self.label.setStyleSheet("font-size: 13px; font-weight: 600; color: #24292f;")
        header.addWidget(self.label)
        
        header.addStretch()
        
        self.char_count_label = QLabel("0 chars")
        self.char_count_label.setStyleSheet("font-size: 11px; color: #57606a;")
        header.addWidget(self.char_count_label)
        
        layout.addLayout(header)
        
        # Text edit
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Enter your message here...")
        self.text_edit.textChanged.connect(self._on_text_changed)
        self.text_edit.setMinimumHeight(120)
        layout.addWidget(self.text_edit)
    
    def _on_text_changed(self):
        count = len(self.text_edit.toPlainText())
        self.char_count_label.setText(f"{count} chars")
        self.text_changed.emit()
    
    def set_mode(self, mode):
        """Set input mode to enforce case: 'encrypt' for lowercase, 'decrypt' for uppercase."""
        self.mode = mode
        if hasattr(self, 'text_edit'):
            # Disconnect the signal if it exists
            try:
                self.text_edit.textChanged.disconnect(self._on_text_changed)
            except TypeError:
                # Signal was not connected, ignore
                pass
            
            try:
                self.text_edit.textChanged.disconnect(self._on_text_changed_with_case_enforcement)
            except TypeError:
                # Signal was not connected, ignore
                pass
            
            # Force case conversion on existing text
            cursor_pos = self.text_edit.textCursor().position()
            current_text = self.text_edit.toPlainText()
            
            if mode == 'encrypt':
                # Force lowercase for encryption input
                new_text = current_text.lower()
            elif mode == 'decrypt':
                # Force uppercase for decryption input
                new_text = current_text.upper()
            else:
                new_text = current_text
            
            if new_text != current_text:
                self.text_edit.setPlainText(new_text)
                # Restore cursor position
                cursor = self.text_edit.textCursor()
                cursor.setPosition(min(cursor_pos, len(new_text)))
                self.text_edit.setTextCursor(cursor)
            
            # Connect the signal with case enforcement
            self.text_edit.textChanged.connect(self._on_text_changed_with_case_enforcement)
            self._on_text_changed_with_case_enforcement()  # Update char count
    
    def _on_text_changed_with_case_enforcement(self):
        """Handle text changes with automatic case enforcement."""
        if not hasattr(self, 'mode'):
            self._on_text_changed()
            return
        
        # Disconnect signal to avoid recursion
        try:
            self.text_edit.textChanged.disconnect(self._on_text_changed_with_case_enforcement)
        except TypeError:
            pass
        
        # Get current text and cursor position
        cursor_pos = self.text_edit.textCursor().position()
        current_text = self.text_edit.toPlainText()
        
        # Apply case conversion based on mode
        if self.mode == 'encrypt':
            new_text = current_text.lower()
        elif self.mode == 'decrypt':
            new_text = current_text.upper()
        else:
            new_text = current_text
        
        # Only update if text actually changed
        if new_text != current_text:
            self.text_edit.setPlainText(new_text)
            # Restore cursor position
            cursor = self.text_edit.textCursor()
            cursor.setPosition(min(cursor_pos, len(new_text)))
            self.text_edit.setTextCursor(cursor)
        
        # Reconnect signal
        self.text_edit.textChanged.connect(self._on_text_changed_with_case_enforcement)
        
        # Update character count
        count = len(new_text)
        self.char_count_label.setText(f"{count} chars")
        self.text_changed.emit()
    
    def set_label(self, text):
        """Set the section label."""
        self.label.setText(text)
    
    def get_text(self):
        """Get the input text."""
        return self.text_edit.toPlainText().strip()
    
    def set_text(self, text):
        """Set the input text."""
        self.text_edit.setPlainText(text)
    
    def clear(self):
        """Clear the input text."""
        self.text_edit.clear()
