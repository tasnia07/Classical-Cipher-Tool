"""Left panel with input/output sections."""

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import pyqtSignal
from cipher_gui.widgets.modern_button import ModernButton
from cipher_gui.widgets.input_section import InputSection
from cipher_gui.widgets.key_section import KeySection
from cipher_gui.widgets.output_section import OutputSection


class LeftPanel(QFrame):
    """Left panel containing mode selector and I/O sections."""
    
    mode_changed = pyqtSignal(str)
    action_requested = pyqtSignal()
    validate_requested = pyqtSignal()
    clear_requested = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("panel")
        self.current_mode = "encrypt"
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(16, 16, 16, 16)
        
        # Mode selector - CHIP STYLE
        mode_container = QFrame()
        mode_container.setObjectName("modeContainer")
        mode_layout = QHBoxLayout(mode_container)
        mode_layout.setContentsMargins(6, 6, 6, 6)
        mode_layout.setSpacing(6)
        
        mode_label = QLabel("Mode:")
        mode_label.setStyleSheet("font-size: 11px; font-weight: 500; color: #57606a;")
        mode_layout.addWidget(mode_label)
        
        self.encrypt_mode_btn = ModernButton("Encrypt", "#1a7f37")
        self.encrypt_mode_btn.clicked.connect(lambda: self._set_mode("encrypt"))
        self.encrypt_mode_btn.setCheckable(True)
        mode_layout.addWidget(self.encrypt_mode_btn, 1)
        
        self.decrypt_mode_btn = ModernButton("Decrypt", "#bf8700")
        self.decrypt_mode_btn.clicked.connect(lambda: self._set_mode("decrypt"))
        self.decrypt_mode_btn.setCheckable(True)
        mode_layout.addWidget(self.decrypt_mode_btn, 1)
        
        layout.addWidget(mode_container)
        
        # Input section (flexible height)
        self.input_section = InputSection()
        layout.addWidget(self.input_section, 2)  # Reduced from 3
        
        # Key section (more space for validation messages)
        self.key_section = KeySection()
        layout.addWidget(self.key_section, 4)  # Increased - options removed
        
        # Action button - slimmer
        self.action_btn = ModernButton("Encrypt Now", "#1a7f37")
        self.action_btn.setMinimumHeight(32)
        self.action_btn.setMaximumHeight(32)
        self.action_btn.clicked.connect(self.action_requested.emit)
        self.action_btn.setStyleSheet("""
            QPushButton {
                background-color: #1a7f37;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 0px 20px;
                font-size: 12px;
                font-weight: 600;
                min-height: 32px;
                max-height: 32px;
            }
            QPushButton:hover {
                background-color: #56d364;
            }
            QPushButton:pressed {
                background-color: #2ea043;
            }
        """)
        layout.addWidget(self.action_btn)
        
        # Quick actions - slimmer chips
        quick_actions = QHBoxLayout()
        quick_actions.setSpacing(6)
        
        validate_btn = QPushButton("Validate")
        validate_btn.setMaximumHeight(26)
        validate_btn.clicked.connect(self.validate_requested.emit)
        validate_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #0969da;
                border: 1px solid transparent;
                border-radius: 4px;
                padding: 4px 12px;
                font-size: 11px;
                font-weight: 500;
                max-height: 26px;
            }
            QPushButton:hover {
                background-color: transparent;
                border-color: #0969da;
            }
        """)
        quick_actions.addWidget(validate_btn)
        
        clear_btn = QPushButton("Clear")
        clear_btn.setMaximumHeight(26)
        clear_btn.clicked.connect(self.clear_requested.emit)
        clear_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #57606a;
                border: 1px solid transparent;
                border-radius: 4px;
                padding: 4px 12px;
                font-size: 11px;
                font-weight: 500;
                max-height: 26px;
            }
            QPushButton:hover {
                background-color: transparent;
                border-color: #57606a;
            }
        """)
        quick_actions.addWidget(clear_btn)
        
        layout.addLayout(quick_actions)
        
        # Output section (reduced height for small texts)
        self.output_section = OutputSection()
        layout.addWidget(self.output_section, 1)  # Reduced from 2
        
        # Set initial mode
        self._set_mode("encrypt")
    
    def _set_mode(self, mode):
        """Set the operation mode."""
        self.current_mode = mode
        
        if mode == "encrypt":
            # Update button states - selected button should be highlighted
            self.encrypt_mode_btn.setChecked(True)
            self.decrypt_mode_btn.setChecked(False)
            
            # Style the SELECTED button with bright green
            self.encrypt_mode_btn.setStyleSheet("""
                QPushButton {
                    background-color: #1a7f37;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    padding: 5px 14px;
                    font-size: 11px;
                    font-weight: 600;
                    min-height: 26px;
                    max-height: 26px;
                }
                QPushButton:hover {
                    background-color: #56d364;
                }
            """)
            
            # Style the UNSELECTED button as subtle chip
            self.decrypt_mode_btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: #57606a;
                    border: 1px solid transparent;
                    border-radius: 4px;
                    padding: 5px 14px;
                    font-size: 11px;
                    font-weight: 500;
                    min-height: 26px;
                    max-height: 26px;
                }
                QPushButton:hover {
                    background-color: transparent;
                    color: #bf8700;
                    border-color: #bf8700;
                }
            """)
            
            self.input_section.set_label("Text to Encrypt")
            self.output_section.set_label("Encrypted Result")
            self.action_btn.setText("Encrypt Now")
            self.action_btn.setStyleSheet("""
                QPushButton {
                    background-color: #1a7f37;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    padding: 0px 20px;
                    font-size: 12px;
                    font-weight: 600;
                    min-height: 32px;
                    max-height: 32px;
                }
                QPushButton:hover {
                    background-color: #56d364;
                }
                QPushButton:pressed {
                    background-color: #2ea043;
                }
            """)
        else:
            # Update button states
            self.encrypt_mode_btn.setChecked(False)
            self.decrypt_mode_btn.setChecked(True)
            
            # Style the UNSELECTED button as subtle chip
            self.encrypt_mode_btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: #57606a;
                    border: 1px solid transparent;
                    border-radius: 4px;
                    padding: 5px 14px;
                    font-size: 11px;
                    font-weight: 500;
                    min-height: 26px;
                    max-height: 26px;
                }
                QPushButton:hover {
                    background-color: transparent;
                    color: #1a7f37;
                    border-color: #1a7f37;
                }
            """)
            
            # Style the SELECTED button with bright orange
            self.decrypt_mode_btn.setStyleSheet("""
                QPushButton {
                    background-color: #bf8700;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    padding: 5px 14px;
                    font-size: 11px;
                    font-weight: 600;
                    min-height: 26px;
                    max-height: 26px;
                }
                QPushButton:hover {
                    background-color: #ff9f66;
                }
            """)
            
            self.input_section.set_label("Text to Decrypt")
            self.output_section.set_label("Decrypted Result")
            self.action_btn.setText("Decrypt Now")
            self.action_btn.setStyleSheet("""
                QPushButton {
                    background-color: #bf8700;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    padding: 0px 20px;
                    font-size: 12px;
                    font-weight: 600;
                    min-height: 32px;
                    max-height: 32px;
                }
                QPushButton:hover {
                    background-color: #ff9f66;
                }
                QPushButton:pressed {
                    background-color: #d77735;
                }
            """)
        
        self.mode_changed.emit(mode)
    
    def get_mode(self):
        """Get current mode."""
        return self.current_mode
