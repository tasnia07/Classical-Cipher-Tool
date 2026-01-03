"""Cipher information card - BRIGHT, RICH, READABLE, TALL."""

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QWidget
from PyQt6.QtCore import Qt


class InfoCard(QFrame):
    """Rich cipher information card - tall, clear and bright."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("infoCard")
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)
        
        # Header - BRIGHT
        header = QLabel("📚 Cipher Information")
        header.setStyleSheet("font-size: 14px; font-weight: 700; color: #24292f; margin-bottom: 8px;")
        layout.addWidget(header)
        
        # Cipher name - VERY BRIGHT
        self.info_name = QLabel()
        self.info_name.setStyleSheet("""
            font-size: 20px; 
            font-weight: 700; 
            color: #0969da; 
            margin-bottom: 6px;
        """)
        self.info_name.setWordWrap(True)
        layout.addWidget(self.info_name)
        
        # Origin - BRIGHT
        self.info_origin = QLabel()
        self.info_origin.setStyleSheet("font-size: 12px; color: #57606a; margin-bottom: 14px;")
        layout.addWidget(self.info_origin)
        
        # Description - BRIGHT & SPACED with more room
        self.info_description = QLabel()
        self.info_description.setWordWrap(True)
        self.info_description.setStyleSheet("""
            font-size: 13px; 
            color: #24292f;
            line-height: 1.8;
            margin-bottom: 18px;
        """)
        self.info_description.setMinimumHeight(60)
        layout.addWidget(self.info_description)
        
        # Stats container - ORGANIZED & BRIGHT
        stats_frame = QFrame()
        stats_frame.setStyleSheet("""
            QFrame {
                background-color: transparent;
                border-radius: 10px;
                padding: 16px;
            }
        """)
        stats_layout = QVBoxLayout(stats_frame)
        stats_layout.setContentsMargins(16, 16, 16, 16)
        stats_layout.setSpacing(16)
        
        # Security - BRIGHT
        security_row = QHBoxLayout()
        sec_label = QLabel("Security:")
        sec_label.setStyleSheet("font-size: 13px; color: #24292f; font-weight: 600; min-width: 90px;")
        security_row.addWidget(sec_label)
        
        self.info_strength = QLabel()
        self.info_strength.setStyleSheet("font-size: 15px; color: #bf8700; font-weight: 600;")
        security_row.addWidget(self.info_strength)
        security_row.addStretch()
        stats_layout.addLayout(security_row)
        
        # Key space - BRIGHT
        keys_row = QHBoxLayout()
        keys_label = QLabel("Key Space:")
        keys_label.setStyleSheet("font-size: 13px; color: #24292f; font-weight: 600; min-width: 90px;")
        keys_row.addWidget(keys_label)
        
        self.info_keys = QLabel()
        self.info_keys.setStyleSheet("font-size: 13px; color: #1a7f37; font-weight: 600; line-height: 1.6;")
        self.info_keys.setWordWrap(True)
        keys_row.addWidget(self.info_keys, 1)
        stats_layout.addLayout(keys_row)
        
        # Use case - BRIGHT with more space
        use_container = QVBoxLayout()
        use_container.setSpacing(8)
        
        use_label = QLabel("Best For:")
        use_label.setStyleSheet("font-size: 13px; color: #24292f; font-weight: 600;")
        use_container.addWidget(use_label)
        
        self.info_use_case = QLabel()
        self.info_use_case.setStyleSheet("font-size: 13px; color: #24292f; line-height: 1.7;")
        self.info_use_case.setWordWrap(True)
        self.info_use_case.setMinimumHeight(40)
        use_container.addWidget(self.info_use_case)
        
        stats_layout.addLayout(use_container)
        
        layout.addWidget(stats_frame)
        layout.addStretch()
    
    def update_info(self, cipher_info):
        """Update cipher information display."""
        self.info_name.setText(cipher_info.get('name', ''))
        self.info_origin.setText(cipher_info.get('origin', ''))
        self.info_description.setText(cipher_info.get('description', ''))
        self.info_strength.setText(cipher_info.get('strength', ''))
        self.info_keys.setText(cipher_info.get('keys', ''))
        self.info_use_case.setText(cipher_info.get('use_case', ''))
