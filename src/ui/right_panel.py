from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QGroupBox, 
                             QFormLayout, QComboBox, QPushButton, QHBoxLayout, QCheckBox, QLabel)
from src.core.ocr_engine import OCREngine

class RightPanel(QWidget):
    def __init__(self):
        super().__init__()
        
        # Get languages once
        self.engine_helper = OCREngine()
        self.available_langs = self.engine_helper.get_available_languages()
        
        self.layout = QVBoxLayout(self)
        
        # --- SECTION 1: VIEW CONTROLS ---
        self.view_group = QGroupBox("View Settings")
        self.view_layout = QVBoxLayout()
        self.zoom_layout = QHBoxLayout()
        self.btn_zoom_out = QPushButton("➖ Zoom Out")
        self.btn_zoom_in = QPushButton("➕ Zoom In")
        self.zoom_layout.addWidget(self.btn_zoom_out)
        self.zoom_layout.addWidget(self.btn_zoom_in)
        self.view_layout.addLayout(self.zoom_layout)
        self.view_group.setLayout(self.view_layout)
        self.layout.addWidget(self.view_group)

        # --- SECTION 2: IMAGE EXPORT ---
        self.export_group = QGroupBox("Image Export Settings")
        self.export_layout = QFormLayout()
        self.format_combo = QComboBox()
        self.format_combo.addItems(["PNG", "JPG", "TIFF"])
        self.export_layout.addRow("Format:", self.format_combo)
        self.dpi_combo = QComboBox()
        self.dpi_combo.addItems(["72", "150", "300", "600"])
        self.dpi_combo.setCurrentText("150")
        self.export_layout.addRow("DPI:", self.dpi_combo)
        self.export_group.setLayout(self.export_layout)
        self.layout.addWidget(self.export_group)

        # --- SECTION 3: OCR SETTINGS (DUAL LANGUAGE SUPPORT) ---
        self.ocr_group = QGroupBox("OCR Text Settings")
        self.ocr_layout = QFormLayout()
        
        # 1. Primary Language
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(self.available_langs)
        if "eng" in self.available_langs:
            self.lang_combo.setCurrentText("eng")
        self.ocr_layout.addRow("Primary Lang:", self.lang_combo)

        # 2. Secondary Language (Optional) <--- NEW
        self.lang_combo_2 = QComboBox()
        self.lang_combo_2.addItem("None") # Default option
        self.lang_combo_2.addItems(self.available_langs)
        self.ocr_layout.addRow("Second Lang:", self.lang_combo_2)

        # 3. Merge Checkbox
        self.check_merge = QCheckBox("Merge into one file")
        self.check_merge.setChecked(True) 
        self.ocr_layout.addRow(self.check_merge)
        
        # 4. Output Format
        self.ocr_format_combo = QComboBox()
        self.ocr_format_combo.addItems(["TXT (.txt)", "Word (.docx)"])
        self.ocr_layout.addRow("Output:", self.ocr_format_combo)
        
        self.ocr_group.setLayout(self.ocr_layout)
        self.layout.addWidget(self.ocr_group)
        
        # --- SECTION 4: ACTIONS ---
        self.btn_export = QPushButton("Images Export")
        self.btn_export.setMinimumHeight(40)
        self.layout.addWidget(self.btn_export)

        self.btn_ocr = QPushButton("Start OCR")
        self.btn_ocr.setMinimumHeight(40)
        self.layout.addWidget(self.btn_ocr)
        
        self.layout.addStretch()