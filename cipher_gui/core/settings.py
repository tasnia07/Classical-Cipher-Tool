"""Settings management."""

from PyQt6.QtCore import QSettings


class SettingsManager:
    """Manages application settings persistence."""
    
    def __init__(self):
        self.settings = QSettings("CipherTool", "ClassicalCiphers")
    
    def save_window_geometry(self, geometry):
        """Save window geometry."""
        self.settings.setValue("geometry", geometry)
    
    def restore_window_geometry(self):
        """Restore window geometry."""
        return self.settings.value("geometry")
    
    def save_cipher_index(self, index):
        """Save selected cipher index."""
        self.settings.setValue("cipher_index", index)
    
    def restore_cipher_index(self):
        """Restore cipher index."""
        return self.settings.value("cipher_index", 0, type=int)
    
    def save_mode(self, mode):
        """Save operation mode."""
        self.settings.setValue("mode", mode)
    
    def restore_mode(self):
        """Restore operation mode."""
        return self.settings.value("mode", "encrypt")
    
    def save_preserve_case(self, value):
        """Save preserve case option."""
        self.settings.setValue("preserve_case", value)
    
    def restore_preserve_case(self):
        """Restore preserve case option."""
        return self.settings.value("preserve_case", True, type=bool)
    
    def save_auto_history(self, value):
        """Save auto history option."""
        self.settings.setValue("auto_history", value)
    
    def restore_auto_history(self):
        """Restore auto history option."""
        return self.settings.value("auto_history", True, type=bool)
