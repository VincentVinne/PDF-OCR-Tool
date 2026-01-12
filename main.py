import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt
from src.ui.main_window import MainWindow

def set_dark_theme(app):
    """
    Applies a professional 'Adobe-style' dark theme to the application.
    """
    app.setStyle("Fusion") 

    palette = QPalette()
    # Dark Grey Backgrounds
    palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    
    # Lighter Grey for Inputs
    palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    
    # White Text
    palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
    
    # Button Colors
    palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
    palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)

    app.setPalette(palette)

def main():
    app = QApplication(sys.argv)
    
    # Apply the paint job
    set_dark_theme(app)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()