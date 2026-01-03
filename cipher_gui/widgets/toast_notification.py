"""Modern toast notification widget for user feedback."""

from PyQt6.QtWidgets import QLabel, QGraphicsOpacityEffect
from PyQt6.QtCore import QTimer, Qt, QPropertyAnimation, QEasingCurve, pyqtProperty
from PyQt6.QtGui import QColor


class ToastNotification(QLabel):
    """Modern toast notification with smooth fade-in/out animations."""
    
    # Toast types with colors
    SUCCESS = ("#1a7f37", "✓")  # Green
    ERROR = ("#cf222e", "✗")    # Red
    INFO = ("#0969da", "ℹ")     # Blue
    WARNING = ("#bf8700", "⚠")  # Orange
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedSize(350, 60)
        
        # Opacity effect for animations
        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)
        self.opacity_effect.setOpacity(0.0)
        
        # Timers
        self.show_timer = QTimer(self)
        self.show_timer.timeout.connect(self.fade_out)
        
    def show_toast(self, message, toast_type=INFO, duration=3000):
        """Show toast notification with animation."""
        color, icon = toast_type
        
        # Set styling based on type
        self.setStyleSheet(f"""
            QLabel {{
                background-color: {color};
                color: white;
                border-radius: 8px;
                padding: 15px 20px;
                font-size: 14px;
                font-weight: 500;
            }}
        """)
        
        # Set text with icon
        self.setText(f"{icon}  {message}")
        self.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        # Position at top-right corner
        if self.parent():
            parent_geo = self.parent().geometry()
            x = parent_geo.width() - self.width() - 20
            y = 80  # Below header
            self.move(x, y)
        
        # Show with fade-in animation
        self.show()
        self.fade_in()
        
        # Auto-hide after duration
        self.show_timer.start(duration)
    
    def fade_in(self):
        """Fade in animation."""
        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(300)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.animation.start()
    
    def fade_out(self):
        """Fade out animation."""
        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(300)
        self.animation.setStartValue(1.0)
        self.animation.setEndValue(0.0)
        self.animation.setEasingCurve(QEasingCurve.Type.InCubic)
        self.animation.finished.connect(self.hide)
        self.animation.start()
        
    @staticmethod
    def show_success(parent, message):
        """Show success toast."""
        toast = ToastNotification(parent)
        toast.show_toast(message, ToastNotification.SUCCESS)
        return toast
    
    @staticmethod
    def show_error(parent, message):
        """Show error toast."""
        toast = ToastNotification(parent)
        toast.show_toast(message, ToastNotification.ERROR)
        return toast
    
    @staticmethod
    def show_info(parent, message):
        """Show info toast."""
        toast = ToastNotification(parent)
        toast.show_toast(message, ToastNotification.INFO)
        return toast
    
    @staticmethod
    def show_warning(parent, message):
        """Show warning toast."""
        toast = ToastNotification(parent)
        toast.show_toast(message, ToastNotification.WARNING)
        return toast
