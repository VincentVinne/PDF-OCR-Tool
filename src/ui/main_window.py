from PyQt6.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QLabel, 
                             QFileDialog, QMessageBox, QProgressBar, QScrollArea)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage, QPixmap 
import os
import sys

from src.ui.left_panel import LeftPanel
from src.ui.right_panel import RightPanel
from src.core.pdf_handler import PDFHandler
from src.utils.workers import ExportWorker, OCRWorker

# Helper to find images when compiled as EXE
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PDF & OCR Tool")
        self.setGeometry(100, 100, 1200, 800)

        # Logic
        self.pdf_handler = PDFHandler()
        self.current_zoom = 1.0
        self.current_page_index = -1

        # Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QHBoxLayout(central_widget)
        
        # 1. Left Panel
        self.left_panel = LeftPanel()
        self.main_layout.addWidget(self.left_panel, 20)
        
        # 2. Main View (Middle)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("border: none;") 
        
        self.main_view = QLabel()
        self.main_view.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # --- NEW: CUSTOM BACKGROUND IMAGE ---
        # We try to load 'background.jpg'. If it exists, we show it.
        bg_path = resource_path("background.jpg")
        # Note: We use forward slashes for CSS to work on Windows
        bg_path = bg_path.replace("\\", "/") 
        
        if os.path.exists("background.jpg"):
            self.main_view.setStyleSheet(f"""
                QLabel {{
                    background-image: url({bg_path});
                    background-position: center;
                    background-repeat: no-repeat;
                    background-color: #2b2b2b; /* Fallback color */
                }}
            """)
        else:
            self.main_view.setText("Open a PDF to start")
            self.main_view.setStyleSheet("background-color: transparent; color: #888; font-size: 16px;") 
        
        self.scroll_area.setWidget(self.main_view)
        self.main_layout.addWidget(self.scroll_area, 60)
        
        # 3. Right Panel
        self.right_panel = RightPanel()
        self.main_layout.addWidget(self.right_panel, 20)

        # --- NEW: TRADEMARK & PROGRESS BAR ---
        self.setStatusBar(self.statusBar())
        
        # Progress Bar (Hidden by default)
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setMaximumWidth(200) # Keep it small
        self.statusBar().addWidget(self.progress_bar)
        
        # Trademark Label (Bottom Right)
        self.trademark_label = QLabel("Made by VincentVinnexGeminiAI")
        self.trademark_label.setStyleSheet("color: #666; font-weight: bold; margin-right: 10px;")
        self.statusBar().addPermanentWidget(self.trademark_label)

        # Connections
        self.left_panel.btn_open.clicked.connect(self.open_file_dialog)
        self.left_panel.file_list.currentRowChanged.connect(self.display_page)
        self.right_panel.btn_export.clicked.connect(self.start_export)
        self.right_panel.btn_ocr.clicked.connect(self.start_ocr)
        self.right_panel.btn_zoom_in.clicked.connect(self.zoom_in)
        self.right_panel.btn_zoom_out.clicked.connect(self.zoom_out)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open PDF File", "", "PDF Files (*.pdf)")

        if file_path:
            page_count = self.pdf_handler.load_pdf(file_path)
            if page_count is not None:
                self.left_panel.file_list.clear()
                for i in range(page_count):
                    self.left_panel.file_list.addItem(f"Page {i + 1}")
                self.left_panel.file_list.setCurrentRow(0)
                # Remove background image style when PDF is loaded
                self.main_view.setStyleSheet("background-color: transparent;")
            else:
                QMessageBox.critical(self, "Error", "Could not open the PDF file.")

    def display_page(self, list_index):
        if list_index < 0: return 
        self.current_page_index = list_index 
        image_data = self.pdf_handler.get_page_image(list_index, scale_factor=self.current_zoom)
        if image_data:
            samples, width, height, stride = image_data
            qt_image = QImage(samples, width, height, stride, QImage.Format.Format_RGB888)
            pixmap = QPixmap.fromImage(qt_image)
            self.main_view.setPixmap(pixmap)
            self.main_view.resize(pixmap.width(), pixmap.height())

    def zoom_in(self):
        if self.current_page_index == -1: return 
        self.current_zoom += 0.25
        self.display_page(self.current_page_index)

    def zoom_out(self):
        if self.current_page_index == -1: return 
        if self.current_zoom > 0.5:
            self.current_zoom -= 0.25
            self.display_page(self.current_page_index)

    def start_export(self):
        selected_items = self.left_panel.file_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Warning", "Select pages to export.")
            return
        indices = [self.left_panel.file_list.row(item) for item in selected_items]
        output_dir = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if not output_dir: return
        fmt = self.right_panel.format_combo.currentText()
        dpi = self.right_panel.dpi_combo.currentText()
        self.right_panel.btn_export.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.worker = ExportWorker(self.pdf_handler, indices, output_dir, fmt, dpi)
        self.worker.progress.connect(self.progress_bar.setValue)
        self.worker.finished.connect(self.on_task_finished)
        self.worker.start()

    def start_ocr(self):
        selected_items = self.left_panel.file_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Warning", "Select pages to OCR.")
            return

        indices = [self.left_panel.file_list.row(item) for item in selected_items]
        
        is_merge = self.right_panel.check_merge.isChecked()
        combo_text = self.right_panel.ocr_format_combo.currentText()
        file_type = "docx" if "docx" in combo_text else "txt"
        
        lang1 = self.right_panel.lang_combo.currentText()
        lang2 = self.right_panel.lang_combo_2.currentText()
        final_lang_code = lang1
        if lang2 != "None" and lang2 != lang1:
            final_lang_code = f"{lang1}+{lang2}"

        output_path = ""
        if is_merge:
            filter_str = "Word Document (*.docx)" if file_type == "docx" else "Text File (*.txt)"
            output_path, _ = QFileDialog.getSaveFileName(self, "Save Merged File", "", filter_str)
        else:
            output_path = QFileDialog.getExistingDirectory(self, "Select Output Folder")

        if not output_path: return
        
        self.right_panel.btn_ocr.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)

        self.ocr_worker = OCRWorker(self.pdf_handler, indices, output_path, is_merge, file_type, lang=final_lang_code)
        self.ocr_worker.progress.connect(self.progress_bar.setValue)
        self.ocr_worker.finished.connect(self.on_task_finished)
        self.ocr_worker.start()

    def on_task_finished(self, message):
        self.progress_bar.setVisible(False)
        self.right_panel.btn_export.setEnabled(True)
        self.right_panel.btn_ocr.setEnabled(True)
        QMessageBox.information(self, "Success", message)