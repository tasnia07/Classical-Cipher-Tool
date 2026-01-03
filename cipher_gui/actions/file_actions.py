"""File import/export operations."""

import os
from datetime import datetime
from PyQt6.QtWidgets import QFileDialog
from cipher_gui.utils.helpers import show_error


class FileActions:
    """Handles file import and export operations."""
    
    def __init__(self, parent):
        self.parent = parent
    
    def import_text(self):
        """
        Import text from a file.
        
        Returns:
            str: Imported text, or None if cancelled/error
        """
        filename, _ = QFileDialog.getOpenFileName(
            self.parent,
            "Import Text File",
            "",
            "Text Files (*.txt);;All Files (*)"
        )
        
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    text = f.read()
                return text, filename
            except Exception as e:
                show_error(self.parent, f"Failed to import file: {str(e)}", "Import Error")
                return None, None
        
        return None, None
    
    def export_text(self, text):
        """
        Export text to a file.
        
        Args:
            text: Text to export
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not text:
            show_error(self.parent, "No result to export", "Nothing to Export")
            return False
        
        filename, _ = QFileDialog.getSaveFileName(
            self.parent,
            "Export Result",
            f"cipher_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            "Text Files (*.txt);;All Files (*)"
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(text)
                return True, filename
            except Exception as e:
                show_error(self.parent, f"Failed to export file: {str(e)}", "Export Error")
                return False, None
        
        return False, None
