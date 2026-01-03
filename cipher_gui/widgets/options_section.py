"""Options section widget."""

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel, QCheckBox


class OptionsSection(QFrame):
    """Options and settings section."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("section")
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 8, 12, 8)
        
        header = QLabel("⚙️ Options")
        header.setStyleSheet("font-size: 12px; font-weight: 600; color: #57606a;")
        layout.addWidget(header)
        
        # Preserve case checkbox
        self.preserve_case_check = QCheckBox("Preserve case")
        self.preserve_case_check.setChecked(True)
        self.preserve_case_check.setStyleSheet("color: #24292f; font-size: 12px;")
        layout.addWidget(self.preserve_case_check)
        
        # Auto-save to history
        self.auto_history_check = QCheckBox("Save to history")
        self.auto_history_check.setChecked(True)
        self.auto_history_check.setStyleSheet("color: #24292f; font-size: 12px;")
        layout.addWidget(self.auto_history_check)
    
    def should_preserve_case(self):
        """Check if case should be preserved."""
        return self.preserve_case_check.isChecked()
    
    def should_save_history(self):
        """Check if history should be saved."""
        return self.auto_history_check.isChecked()
    
    def set_preserve_case(self, checked):
        """Set preserve case option."""
        self.preserve_case_check.setChecked(checked)
    
    def set_auto_history(self, checked):
        """Set auto history option."""
        self.auto_history_check.setChecked(checked)
