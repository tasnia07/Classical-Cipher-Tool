"""Tips card widget - BRIGHT AND READABLE."""

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel


class TipsCard(QFrame):
    """Displays quick tips - bright and readable."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("tipsCard")
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)
        
        header = QLabel("💡 Quick Tips")
        header.setStyleSheet("font-size: 14px; font-weight: 700; color: #24292f; margin-bottom: 6px;")
        layout.addWidget(header)
        
        tips = [
            "✓ Case and spaces are preserved",
            "✓ Validate keys before encrypting",
            "✓ Use Ctrl+W to swap texts",
            "✓ History tracks all operations",
            "✓ Import/export text files"
        ]
        
        for tip in tips:
            tip_label = QLabel(tip)
            tip_label.setStyleSheet("color: #24292f; font-size: 13px; padding: 6px 0; line-height: 1.6;")
            tip_label.setWordWrap(True)
            layout.addWidget(tip_label)
        
        layout.addStretch()

