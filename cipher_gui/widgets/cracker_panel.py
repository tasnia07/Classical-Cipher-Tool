"""Cracker panel for Hill Cipher Known Plaintext Attack."""

from PyQt6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout, QLabel, 
                              QPushButton, QTextEdit, QLineEdit, QGroupBox,
                              QScrollArea, QWidget, QSplitter)
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QFont

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from cracker import HillCipherCracker


class CrackerPanel(QFrame):
    """Panel for cracking Hill Cipher using known plaintext attack."""
    
    status_message = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("crackerPanel")
        self.cracker = HillCipherCracker()
        self.cracked_key = None
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(20, 16, 20, 16)
        
        # Title
        title = QLabel("Hill Cipher Cracker")
        title.setStyleSheet("""
            font-size: 18px;
            font-weight: 600;
            color: #cf222e;
            padding: 4px 0;
        """)
        layout.addWidget(title)
        
        # Description
        desc = QLabel("Crack 2×2 Hill Cipher keys using Known Plaintext Attack")
        desc.setStyleSheet("color: #57606a; font-size: 11px; margin-bottom: 4px;")
        layout.addWidget(desc)
        
        # Hill Cipher Information Panel
        info_panel = QGroupBox("ℹ️ About Hill Cipher")
        info_panel.setStyleSheet("""
            QGroupBox {
                font-weight: 600;
                font-size: 12px;
                color: #24292f;
                border: 1px solid #d0d7de;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 6px;
                background-color: #ffffff;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 6px;
            }
        """)
        info_layout = QVBoxLayout(info_panel)
        info_layout.setContentsMargins(12, 16, 12, 12)
        info_layout.setSpacing(8)
        
        # Hill cipher description
        hill_desc = QLabel(
            "<b>Hill Cipher (2×2)</b> is a polygraphic substitution cipher that uses linear algebra. "
            "It encrypts pairs of letters using a 2×2 matrix as the key.<br><br>"
            "<b>How it works:</b><br>"
            "• Plaintext letters are converted to numbers (A=0, B=1, ..., Z=25)<br>"
            "• Pairs of numbers are arranged as vectors and multiplied by the key matrix<br>"
            "• Results are reduced modulo 26 and converted back to letters<br><br>"
            "<b>Known Plaintext Attack:</b><br>"
            "If you know both the plaintext and its corresponding ciphertext (at least 4 letters each), "
            "this tool can recover the encryption key matrix by solving a system of linear equations."
        )
        hill_desc.setWordWrap(True)
        hill_desc.setStyleSheet("""
            color: #24292f;
            font-size: 12px;
            line-height: 1.6;
            padding: 8px;
        """)
        info_layout.addWidget(hill_desc)
        
        layout.addWidget(info_panel)
        
        # Input section
        input_group = QGroupBox("Known Plaintext-Ciphertext Pair")
        input_group.setStyleSheet("""
            QGroupBox {
                font-weight: 600;
                font-size: 12px;
                color: #24292f;
                border: 1px solid #d0d7de;
                border-radius: 6px;
                margin-top: 10px;
                padding-top: 6px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 6px;
            }
        """)
        input_layout = QVBoxLayout(input_group)
        input_layout.setSpacing(8)
        input_layout.setContentsMargins(12, 16, 12, 12)
        
        # Plaintext input
        pt_layout = QHBoxLayout()
        pt_label = QLabel("Plaintext:")
        pt_label.setFixedWidth(70)
        pt_label.setStyleSheet("color: #57606a; font-weight: 500; font-size: 11px;")
        self.plaintext_input = QLineEdit()
        self.plaintext_input.setPlaceholderText("Known plaintext (e.g., hello, attack, secret)")
        self.plaintext_input.textChanged.connect(self._enforce_plaintext_case)
        self.plaintext_input.setStyleSheet("""
            QLineEdit {
                background-color: #f6f8fa;
                border: 1px solid #d0d7de;
                border-radius: 4px;
                padding: 6px 10px;
                color: #24292f;
                font-size: 12px;
            }
            QLineEdit:focus {
                border-color: #cf222e;
            }
        """)
        pt_layout.addWidget(pt_label)
        pt_layout.addWidget(self.plaintext_input)
        input_layout.addLayout(pt_layout)
        
        # Ciphertext input
        ct_layout = QHBoxLayout()
        ct_label = QLabel("Ciphertext:")
        ct_label.setFixedWidth(70)
        ct_label.setStyleSheet("color: #57606a; font-weight: 500; font-size: 11px;")
        self.ciphertext_input = QLineEdit()
        self.ciphertext_input.setPlaceholderText("Corresponding ciphertext")
        self.ciphertext_input.textChanged.connect(self._enforce_ciphertext_case)
        self.ciphertext_input.setStyleSheet("""
            QLineEdit {
                background-color: #f6f8fa;
                border: 1px solid #d0d7de;
                border-radius: 4px;
                padding: 6px 10px;
                color: #24292f;
                font-size: 12px;
            }
            QLineEdit:focus {
                border-color: #cf222e;
            }
        """)
        ct_layout.addWidget(ct_label)
        ct_layout.addWidget(self.ciphertext_input)
        input_layout.addLayout(ct_layout)
        
        layout.addWidget(input_group)
        
        # Action buttons - slimmer
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(8)
        
        self.crack_btn = QPushButton("Crack Key")
        self.crack_btn.setStyleSheet("""
            QPushButton {
                background-color: #cf222e;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 6px 16px;
                font-size: 11px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #ff6b6b;
            }
            QPushButton:pressed {
                background-color: #da3633;
            }
        """)
        self.crack_btn.clicked.connect(self.crack_key)
        btn_layout.addWidget(self.crack_btn)
        
        self.clear_btn = QPushButton("Clear")
        self.clear_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #57606a;
                border: 1px solid #d0d7de;
                border-radius: 4px;
                padding: 6px 16px;
                font-size: 11px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: transparent;
                border-color: #57606a;
            }
        """)
        self.clear_btn.clicked.connect(self.clear_all)
        btn_layout.addWidget(self.clear_btn)
        
        layout.addLayout(btn_layout)
        
        # Results section - takes more space
        result_group = QGroupBox("Results")
        result_group.setStyleSheet("""
            QGroupBox {
                font-weight: 600;
                font-size: 12px;
                color: #24292f;
                border: 1px solid #d0d7de;
                border-radius: 6px;
                margin-top: 10px;
                padding-top: 6px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 6px;
            }
        """)
        result_layout = QVBoxLayout(result_group)
        result_layout.setContentsMargins(12, 16, 12, 12)
        
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setMinimumHeight(200)
        self.result_text.setStyleSheet("""
            QTextEdit {
                background-color: #ffffff;
                border: 1px solid #ffffff;
                border-radius: 4px;
                padding: 10px;
                color: #24292f;
                font-family: 'Consolas', 'Monaco', monospace;
                font-size: 12px;
                line-height: 1.4;
            }
        """)
        result_layout.addWidget(self.result_text)
        
        layout.addWidget(result_group, 1)  # Stretch factor
    
    def _enforce_plaintext_case(self):
        """Enforce lowercase for plaintext input."""
        cursor_pos = self.plaintext_input.cursorPosition()
        current_text = self.plaintext_input.text()
        new_text = current_text.lower()
        
        if new_text != current_text:
            self.plaintext_input.blockSignals(True)
            self.plaintext_input.setText(new_text)
            self.plaintext_input.setCursorPosition(cursor_pos)
            self.plaintext_input.blockSignals(False)
    
    def _enforce_ciphertext_case(self):
        """Enforce uppercase for ciphertext input."""
        cursor_pos = self.ciphertext_input.cursorPosition()
        current_text = self.ciphertext_input.text()
        new_text = current_text.upper()
        
        if new_text != current_text:
            self.ciphertext_input.blockSignals(True)
            self.ciphertext_input.setText(new_text)
            self.ciphertext_input.setCursorPosition(cursor_pos)
            self.ciphertext_input.blockSignals(False)
    
    def crack_key(self):
        """Attempt to crack the Hill cipher key."""
        plaintext = self.plaintext_input.text().strip()
        ciphertext = self.ciphertext_input.text().strip()
        
        if not plaintext or not ciphertext:
            self.result_text.setHtml(
                '<span style="color: #cf222e;">Error: Both plaintext and ciphertext are required</span>'
            )
            self.status_message.emit("Error: Missing input")
            return
        
        # Store original plaintext letter count for padding removal
        self.original_plaintext_length = sum(1 for c in plaintext if c.isalpha())
        
        # Capture output
        import io
        import sys
        old_stdout = sys.stdout
        sys.stdout = captured = io.StringIO()
        
        try:
            self.cracked_key = self.cracker.crack_key(plaintext, ciphertext)
        finally:
            sys.stdout = old_stdout
        
        output = captured.getvalue()
        
        if self.cracked_key is not None:
            # Format result
            key_flat = ','.join(str(int(x)) for x in self.cracked_key.flatten())
            
            result_html = f'''
<div style="font-family: Consolas, Monaco, monospace; line-height: 1.6;">
<span style="color: #1a7f37; font-weight: bold; font-size: 13px;">KEY CRACKED SUCCESSFULLY</span><br><br>
<span style="color: #57606a;">Cracked Key: </span><span style="color: #0969da; font-weight: 500;">[{key_flat}]</span>
</div>
'''
            self.result_text.setHtml(result_html)
            self.status_message.emit(f"Key cracked: [{key_flat}]")
        else:
            self.result_text.setHtml(
                '<span style="color: #cf222e;">Failed to crack key</span><br><br>'
                '<span style="color: #57606a;">Possible issues:</span><br>'
                '<span style="color: #57606a;">• Incorrect plaintext-ciphertext pair<br>'
                '• Texts don\'t correspond to the same encryption<br>'
                '• Use different plaintext-ciphertext pairs</span>'
            )
            self.cracked_key = None
            self.status_message.emit("Failed to crack key")
    
    def clear_all(self):
        """Clear all fields."""
        self.plaintext_input.clear()
        self.ciphertext_input.clear()
        self.result_text.clear()
        self.cracked_key = None
        self.status_message.emit("Cleared")
