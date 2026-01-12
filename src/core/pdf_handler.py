import fitz  # PyMuPDF
from PIL import Image
import io

class PDFHandler:
    def __init__(self):
        self.doc = None
        self.file_path = None

    def load_pdf(self, file_path):
        """Open a PDF and return number of pages."""
        try:
            self.doc = fitz.open(file_path)
            self.file_path = file_path
            return self.doc.page_count
        except Exception as e:
            print(f"Error opening PDF: {e}")
            return None

    def get_page_image(self, page_index, scale_factor=1.5):
        """
        Render a page for UI preview.
        scale_factor:
            1.0 = normal quality
            1.5 = better quality (default)
            2.0+ = very high quality
        Returns: (samples, width, height, stride)
        """
        if not self.doc:
            return None

        try:
            page = self.doc.load_page(page_index)
            matrix = fitz.Matrix(scale_factor, scale_factor)
            pix = page.get_pixmap(matrix=matrix)

            return pix.samples, pix.width, pix.height, pix.stride
        except Exception as e:
            print(f"Error getting page image: {e}")
            return None

    def save_page(self, page_index, output_path, dpi=150, fmt="png"):
        """
        Save a single PDF page as an image.
        dpi controls quality (150–300 recommended).
        """
        if not self.doc:
            return False

        try:
            page = self.doc.load_page(page_index)

            zoom = dpi / 72  # DPI → scale
            matrix = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=matrix)

            pix.save(output_path)
            return True
        except Exception as e:
            print(f"Error saving page {page_index}: {e}")
            return False
