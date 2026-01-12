from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, QLabel, QAbstractItemView

class LeftPanel(QWidget):
    def __init__(self):
        super().__init__()
        
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(10, 10, 10, 10)
        
        self.layout.addWidget(QLabel("<b>Documents</b>"))
        
        self.btn_open = QPushButton("📂 Open PDF")
        self.btn_open.setMinimumHeight(40)
        self.layout.addWidget(self.btn_open)
        
        self.file_list = QListWidget()
        # --- NEW: Enable selecting multiple items (Ctrl+Click or Shift+Click) ---
        self.file_list.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.layout.addWidget(self.file_list)