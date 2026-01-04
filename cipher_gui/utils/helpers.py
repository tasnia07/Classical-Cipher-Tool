"""Helper utility functions."""

from PyQt6.QtWidgets import QMessageBox


def show_error(parent, message, title="Error"):
    """Show error message dialog."""
    msg = QMessageBox(parent)
    msg.setIcon(QMessageBox.Icon.Warning)
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.exec()


def show_info(parent, message, title="Information"):
    """Show information message dialog."""
    msg = QMessageBox(parent)
    msg.setIcon(QMessageBox.Icon.Information)
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.exec()


def show_question(parent, message, title="Question"):
    """Show question dialog."""
    reply = QMessageBox.question(
        parent,
        title,
        message,
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
    )
    return reply == QMessageBox.StandardButton.Yes
