"""UI interaction actions."""

from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import Qt
from cipher_gui.utils.helpers import show_error, show_info


class UIActions:
    """Handles UI interaction operations."""
    
    def __init__(self, parent):
        self.parent = parent
    
    def copy_to_clipboard(self, text):
        """
        Copy text to clipboard.
        
        Args:
            text: Text to copy
            
        Returns:
            bool: True if successful
        """
        if text:
            QApplication.clipboard().setText(text)
            return True
        return False
    
    def swap_texts(self, input_widget, output_widget):
        """
        Swap input and output texts.
        
        Args:
            input_widget: Input widget
            output_widget: Output widget
            
        Returns:
            bool: True if swapped
        """
        output_text = output_widget.get_text()
        if output_text:
            input_text = input_widget.get_text()
            input_widget.set_text(output_text)
            output_widget.set_text(input_text)
            return True
        return False
    
    def clear_all(self, *widgets):
        """
        Clear all provided widgets.
        
        Args:
            *widgets: Widgets to clear
            
        Returns:
            bool: True if user confirmed
        """
        reply = QMessageBox.question(
            self.parent,
            "Clear All",
            "Clear all fields?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            for widget in widgets:
                if hasattr(widget, 'clear'):
                    widget.clear()
            return True
        return False
    
    def validate_key_dialog(self, cipher, cipher_name, key, key_help_details):
        """
        Show key validation dialog.
        
        Args:
            cipher: Cipher instance
            cipher_name: Name of the cipher
            key: Key to validate
            key_help_details: Detailed help text
            
        Returns:
            bool: True if valid
        """
        if not key:
            show_error(self.parent, "Please enter a key to validate", "Missing Key")
            return False
        
        try:
            test_result = cipher.encrypt("TEST", key)
            
            msg = QMessageBox(self.parent)
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle("✓ Key Valid")
            msg.setText(f"Key is valid for {cipher_name} cipher!")
            msg.setInformativeText(f"Test encryption:\n'TEST' → '{test_result}'")
            msg.setDetailedText(key_help_details)
            msg.exec()
            
            return True
        except ValueError as e:
            show_error(self.parent, str(e), "Invalid Key")
            return False
    
    def show_guide(self):
        """Show quick guide dialog."""
        guide_text = """
        <h2>🔐 Quick Guide</h2>
        
        <h3>Getting Started:</h3>
        <ol>
            <li>Select a cipher from the dropdown</li>
            <li>Choose Encrypt or Decrypt mode</li>
            <li>Enter your text</li>
            <li>Enter the key (follow the format shown)</li>
            <li>Click the action button</li>
        </ol>
        
        <h3>Cipher Quick Reference:</h3>
        <p><b>Caesar:</b> Single number (0-25). Example: 3</p>
        <p><b>Affine:</b> Two numbers. Example: 5,8</p>
        <p><b>Playfair:</b> A keyword. Example: MONARCHY</p>
        <p><b>Hill:</b> Four numbers. Example: 3,3,2,5</p>
        
        <h3>Tips:</h3>
        <ul>
            <li>Validate your key before encrypting</li>
            <li>Use keyboard shortcuts for faster workflow</li>
            <li>History saves all your operations</li>
            <li>Import/export for batch processing</li>
        </ul>
        """
        
        msg = QMessageBox(self.parent)
        msg.setWindowTitle("Quick Guide")
        msg.setTextFormat(Qt.TextFormat.RichText)
        msg.setText(guide_text)
        msg.exec()
