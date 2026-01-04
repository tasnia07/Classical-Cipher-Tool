"""Key input section widget."""

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit
from PyQt6.QtCore import pyqtSignal, Qt


class KeySection(QFrame):
    """Key input section with validation indicator."""
    
    key_changed = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("section")
        self.setMinimumHeight(220)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 12, 16, 12)
        layout.setSpacing(6)
        
        # Header
        header = QHBoxLayout()
        icon = QLabel("🔑")
        icon.setStyleSheet("font-size: 16px;")
        header.addWidget(icon)
        
        title = QLabel("Encryption Key")
        title.setStyleSheet("font-size: 13px; font-weight: 600; color: #24292f; margin-left: 6px;")
        header.addWidget(title)
        header.addStretch()
        
        layout.addLayout(header)
        
        # Key input
        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("Enter key...")
        self.key_input.textChanged.connect(self._on_key_changed)
        layout.addWidget(self.key_input)
        
        # Key help - compact single line
        self.key_help_text = QLabel()
        self.key_help_text.setWordWrap(False)
        self.key_help_text.setStyleSheet("color: #0969da; font-size: 10px; padding: 2px 0;")
        layout.addWidget(self.key_help_text)
        
        # Validation area - QTextEdit with always-visible scrollbar
        self.key_validation = QTextEdit()
        self.key_validation.setReadOnly(True)
        self.key_validation.setMinimumHeight(80)
        self.key_validation.setMaximumHeight(100)
        self.key_validation.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.key_validation.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.key_validation.setStyleSheet("""
            QTextEdit {
                background-color: #f6f8fa;
                border: 1px solid #d0d7de;
                border-radius: 4px;
                color: #57606a;
                font-size: 11px;
                padding: 4px;
            }
            QScrollBar:vertical {
                background: #ffffff;
                width: 10px;
                border-radius: 5px;
                margin: 2px;
            }
            QScrollBar::handle:vertical {
                background: #8c959f;
                border-radius: 5px;
                min-height: 20px;
            }
            QScrollBar::handle:vertical:hover {
                background: #57606a;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }
        """)
        layout.addWidget(self.key_validation, 1)
    
    def set_key_help(self, help_data):
        """Set key help information - compact single line."""
        if isinstance(help_data, dict):
            example_text = help_data.get('example', '')
            format_text = help_data.get('format', '')
            
            # Compact format: just show example in placeholder and format hint
            if example_text:
                self.key_input.setPlaceholderText(f"e.g., {example_text}")
            if format_text:
                self.key_help_text.setText(f"Format: {format_text}")
                self.key_help_text.setToolTip(help_data.get('tip', help_data.get('details', '')))
            else:
                self.key_help_text.setText("")
        else:
            self.key_help_text.setText(str(help_data))
            self.key_input.setPlaceholderText("Enter key...")
    
    def _on_key_changed(self):
        """Handle key text changes with uppercase enforcement."""
        cursor_pos = self.key_input.cursorPosition()
        current_text = self.key_input.text()
        new_text = current_text.upper()
        
        if new_text != current_text:
            self.key_input.blockSignals(True)
            self.key_input.setText(new_text)
            self.key_input.setCursorPosition(cursor_pos)
            self.key_input.blockSignals(False)
        
        self.key_changed.emit()
    
    def get_key(self):
        """Get the key text."""
        return self.key_input.text().strip()
    
    def set_validation(self, is_valid, message=""):
        """Set validation status."""
        if not message:
            self.key_validation.setText("")
        elif is_valid:
            self.key_validation.setText(f"✓ {message}")
            self.key_validation.setStyleSheet("""
                QTextEdit { background-color: #f6f8fa; border: 1px solid #d0d7de; border-radius: 4px; color: #1a7f37; font-size: 11px; padding: 4px; }
                QScrollBar:vertical { background: #ffffff; width: 10px; border-radius: 5px; margin: 2px; }
                QScrollBar::handle:vertical { background: #8c959f; border-radius: 5px; min-height: 20px; }
                QScrollBar::handle:vertical:hover { background: #57606a; }
                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }
            """)
        else:
            self.key_validation.setText(f"✗ {message}")
            self.key_validation.setStyleSheet("""
                QTextEdit { background-color: #f6f8fa; border: 1px solid #d0d7de; border-radius: 4px; color: #cf222e; font-size: 11px; padding: 4px; }
                QScrollBar:vertical { background: #ffffff; width: 10px; border-radius: 5px; margin: 2px; }
                QScrollBar::handle:vertical { background: #8c959f; border-radius: 5px; min-height: 20px; }
                QScrollBar::handle:vertical:hover { background: #57606a; }
                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }
            """)
    
    def clear(self):
        """Clear the key input."""
        self.key_input.clear()
        self.key_validation.setText("")
