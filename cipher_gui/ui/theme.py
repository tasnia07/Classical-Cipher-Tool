"""Perfect, professional white theme - Figma quality."""

from PyQt6.QtGui import QColor


class Theme:
    """Figma-quality white theme with perfect spacing and aesthetics."""
    
    # Colors - Professional palette
    BG_DARK = "#ffffff"
    BG_MEDIUM = "#f6f8fa"
    BG_ELEVATED = "#ffffff"
    
    BORDER = "#d0d7de"
    
    TEXT_PRIMARY = "#24292f"
    TEXT_SECONDARY = "#57606a"
    TEXT_DISABLED = "#8c959f"
    
    ACCENT_BLUE = "#0969da"
    SUCCESS = "#1a7f37"
    WARNING = "#bf8700"
    ERROR = "#cf222e"
    
    @staticmethod
    def get_stylesheet():
        """Perfect stylesheet with no cut-offs and great spacing."""
        return """
            /* ==================== GLOBAL ==================== */
            * {
                font-family: -apple-system, 'Segoe UI', 'SF Pro Display', 'Roboto', 'Ubuntu', 'Arial', sans-serif;
                outline: none;
            }
            
            QMainWindow {
                background-color: #ffffff;
            }
            
            /* ==================== MENU & TOOLBAR ==================== */
            QMenuBar {
                background-color: #ffffff;
                color: #24292f;
                border: none;
                border-bottom: 1px solid #d0d7de;
                padding: 6px 10px;
            }
            
            QMenuBar::item {
                background-color: transparent;
                padding: 8px 14px;
                border-radius: 6px;
                margin: 0px 2px;
                color: #24292f;
            }
            
            QMenuBar::item:selected {
                background-color: #f6f8fa;
                color: #24292f;
            }
            
            QMenu {
                background-color: #ffffff;
                border: 1px solid #d0d7de;
                border-radius: 10px;
                padding: 6px;
                color: #24292f;
            }
            
            QMenu::item {
                padding: 10px 28px 10px 14px;
                border-radius: 6px;
                margin: 2px 4px;
                color: #24292f;
            }
            
            QMenu::item:selected {
                background-color: #f6f8fa;
                color: #24292f;
            }
            
            QToolBar {
                background-color: #ffffff;
                border: none;
                border-bottom: 1px solid #d0d7de;
                spacing: 8px;
                padding: 8px;
            }
            
            QToolBar QToolButton {
                background-color: #ffffff;
                color: #24292f;
                border: 1px solid #d0d7de;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 12px;
                font-weight: 500;
            }
            
            QToolBar QToolButton:hover {
                background-color: #f6f8fa;
                color: #24292f;
                border-color: #24292f;
            }
            
            /* ==================== FRAMES - Perfect Cards ==================== */
            QFrame#header {
                background-color: #ffffff;
                border-bottom: 1px solid #d0d7de;
            }
            
            QFrame#panel {
                background-color: transparent;
                border: none;
            }
            
            QFrame#section {
                background-color: #ffffff;
                border: 1px solid #d0d7de;
                border-radius: 12px;
            }
            
            QFrame#modeContainer {
                background-color: transparent;
                border: none;
            }
            
            QFrame#infoCard, QFrame#tipsCard, QFrame#shortcutsCard {
                background-color: #ffffff;
                border: 1px solid #d0d7de;
                border-radius: 12px;
            }
            
            /* ==================== LABELS ==================== */
            QLabel {
                color: #24292f;
                background-color: transparent;
            }
            
            /* ==================== TEXT INPUTS - PERFECT ROUNDED ==================== */
            QTextEdit {
                background-color: #ffffff;
                color: #24292f;
                border: 1px solid #d0d7de;
                border-radius: 12px;
                padding: 16px;
                font-size: 14px;
                font-family: 'SF Mono', 'Monaco', 'Consolas', 'Courier New', monospace;
                selection-background-color: #0969da;
                selection-color: #ffffff;
                line-height: 1.6;
                min-height: 120px;
            }
            
            QTextEdit:hover {
                border-color: #24292f;
            }
            
            QTextEdit:focus {
                border-color: #24292f;
                border-width: 2px;
                padding: 15px;
            }
            
            QTextEdit:read-only {
                background-color: #ffffff;
                color: #24292f;
                selection-background-color: #0969da;
                selection-color: #ffffff;
            }
            
            QLineEdit {
                background-color: #ffffff;
                color: #24292f;
                border: 1px solid #d0d7de;
                border-radius: 10px;
                padding: 10px 14px;
                font-size: 14px;
                font-family: -apple-system, 'Segoe UI', 'SF Pro Display', 'Roboto', 'Ubuntu', sans-serif;
                selection-background-color: #0969da;
                selection-color: #ffffff;
                min-height: 38px;
                max-height: 38px;
            }
            
            QLineEdit:hover {
                border-color: #24292f;
            }
            
            QLineEdit:focus {
                border-color: #24292f;
                border-width: 2px;
                padding: 9px 13px;
            }
            
            /* ==================== CHECKBOXES ==================== */
            QCheckBox {
                color: #24292f;
                spacing: 10px;
                padding: 4px;
            }
            
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #d0d7de;
                border-radius: 6px;
                background-color: #ffffff;
            }
            
            QCheckBox::indicator:hover {
                border-color: #24292f;
                background-color: #f6f8fa;
            }
            
            QCheckBox::indicator:checked {
                background-color: #24292f;
                border-color: #24292f;
            }
            
            /* ==================== SCROLLBARS - Minimal ==================== */
            QScrollBar:vertical {
                background-color: transparent;
                width: 12px;
                margin: 0px;
            }
            
            QScrollBar::handle:vertical {
                background-color: #d0d7de;
                border-radius: 6px;
                min-height: 30px;
            }
            
            QScrollBar::handle:vertical:hover {
                background-color: #8c959f;
            }
            
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                height: 0px;
                background: none;
            }
            
            QScrollBar:horizontal {
                background-color: transparent;
                height: 12px;
                margin: 0px;
            }
            
            QScrollBar::handle:horizontal {
                background-color: #d0d7de;
                border-radius: 6px;
                min-width: 30px;
            }
            
            QScrollBar::handle:horizontal:hover {
                background-color: #8c959f;
            }
            
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal,
            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                width: 0px;
                background: none;
            }
            
            /* ==================== STATUS BAR ==================== */
            QStatusBar {
                background-color: #ffffff;
                color: #24292f;
                border-top: 1px solid #d0d7de;
                font-size: 12px;
                padding: 6px 12px;
            }
            
            /* ==================== DIALOGS ==================== */
            QDialog {
                background-color: #ffffff;
            }
            
            QMessageBox {
                background-color: #ffffff;
            }
            
            QMessageBox QLabel {
                color: #24292f;
                min-width: 350px;
                padding: 10px;
            }
            
            /* ==================== FILE DIALOGS ==================== */
            QFileDialog {
                background-color: #ffffff;
                color: #24292f;
            }
            
            QFileDialog QLabel {
                color: #24292f;
            }
            
            QFileDialog QLineEdit {
                background-color: #ffffff;
                color: #24292f;
            }
            
            QFileDialog QListView {
                background-color: #ffffff;
                color: #24292f;
            }
            
            QFileDialog QTreeView {
                background-color: #ffffff;
                color: #24292f;
            }
            
            QFileDialog QPushButton {
                background-color: #ffffff;
                color: #24292f;
                border: 1px solid #d0d7de;
            }
            
            /* ==================== TOOLTIPS ==================== */
            QToolTip {
                background-color: #24292f;
                color: #ffffff;
                border: 1px solid #d0d7de;
                border-radius: 8px;
                padding: 8px 12px;
                font-size: 12px;
            }
        """
    
    @staticmethod
    def adjust_brightness(hex_color, factor):
        """Adjust color brightness."""
        color = QColor(hex_color)
        h, s, l, a = color.getHslF()
        l = min(1.0, max(0.0, l * factor))
        color.setHslF(h, s, l, a)
        return color.name()
