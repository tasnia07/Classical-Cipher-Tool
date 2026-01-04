"""Right panel with cipher selector and rich information cards - SCROLLABLE."""

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QScrollArea, QWidget
from PyQt6.QtCore import Qt, pyqtSignal
from cipher_gui.widgets.cipher_selector import CipherSelector
from cipher_gui.widgets.info_card import InfoCard


class RightPanel(QFrame):
    """Right panel with cipher selector and scrollable info/tips cards."""
    
    collapsed_changed = pyqtSignal(bool)
    cipher_changed = pyqtSignal(str)
    
    def __init__(self, cipher_names, cipher_icons, parent=None):
        super().__init__(parent)
        self.setObjectName("panel")
        self.is_collapsed = False
        self.cipher_names = cipher_names
        self.cipher_icons = cipher_icons
        self.setup_ui()
    
    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Cipher selector - fixed at top
        self.cipher_selector = CipherSelector(self.cipher_names, self.cipher_icons)
        self.cipher_selector.cipher_changed.connect(self.cipher_changed.emit)
        main_layout.addWidget(self.cipher_selector)
        
        # Scrollable content area with smooth scrolling
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setStyleSheet("""
            QScrollArea {
                border: none;
                background: transparent;
            }
            QScrollBar:vertical {
                background: transparent;
                width: 10px;
                border-radius: 5px;
                margin: 0px;
            }
            QScrollBar::handle:vertical {
                background: transparent;
                border-radius: 5px;
                min-height: 30px;
            }
            QScrollBar::handle:vertical:hover {
                background: transparent;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)
        
        # Content widget
        content = QWidget()
        content.setStyleSheet("background: transparent;")
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(0, 12, 0, 12)
        content_layout.setSpacing(12)
        
        # Rich info card - taller
        self.info_card = InfoCard()
        self.info_card.setMinimumHeight(400)
        content_layout.addWidget(self.info_card)
        
        content_layout.addStretch()
        
        scroll.setWidget(content)
        main_layout.addWidget(scroll)
