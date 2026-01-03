"""History management for cipher operations."""

import json
import os
from datetime import datetime


class HistoryManager:
    """Manages encryption/decryption history."""
    
    def __init__(self, max_items=50):
        self.max_items = max_items
        self.history = []
        self.load_history()
    
    def add_entry(self, cipher, mode, input_text, key, output_text):
        """Add a history entry."""
        entry = {
            'timestamp': datetime.now().isoformat(),
            'cipher': cipher,
            'mode': mode,
            'input': input_text[:100] + '...' if len(input_text) > 100 else input_text,
            'key': key,
            'output': output_text[:100] + '...' if len(output_text) > 100 else output_text
        }
        self.history.insert(0, entry)
        if len(self.history) > self.max_items:
            self.history = self.history[:self.max_items]
        self.save_history()
    
    def get_history(self):
        """Get all history entries."""
        return self.history
    
    def clear_history(self):
        """Clear all history."""
        self.history = []
        self.save_history()
    
    def save_history(self):
        """Save history to file."""
        try:
            with open('.cipher_history.json', 'w') as f:
                json.dump(self.history, f, indent=2)
        except:
            pass
    
    def load_history(self):
        """Load history from file."""
        try:
            if os.path.exists('.cipher_history.json'):
                with open('.cipher_history.json', 'r') as f:
                    self.history = json.load(f)
        except:
            self.history = []
