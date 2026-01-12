import pytesseract
from PIL import Image
import os
import glob

# 1. FIND TESSERACT
possible_paths = [
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
    os.path.join(os.getenv("LOCALAPPDATA", ""), r"Tesseract-OCR\tesseract.exe")
]

tesseract_cmd = None
tessdata_dir = None

for path in possible_paths:
    if os.path.exists(path):
        tesseract_cmd = path
        # The data folder is usually in the same folder as the exe, inside 'tessdata'
        tessdata_dir = os.path.join(os.path.dirname(path), "tessdata")
        break

if tesseract_cmd:
    pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
else:
    print("WARNING: Tesseract-OCR not found! OCR will fail.")

class OCREngine:
    def __init__(self):
        pass

    def get_available_languages(self):
        """Scans the Tesseract folder for .traineddata files"""
        if not tessdata_dir or not os.path.exists(tessdata_dir):
            return ["eng"] # Default fallback
        
        # Find all .traineddata files
        files = glob.glob(os.path.join(tessdata_dir, "*.traineddata"))
        
        # Extract just the name (e.g., 'eng', 'hin', 'osd')
        langs = [os.path.basename(f).replace(".traineddata", "") for f in files]
        
        if not langs:
            return ["eng"]
            
        return sorted(langs)

    def extract_text(self, image_path, lang="eng"):
        try:
            img = Image.open(image_path)
            # We pass the selected language here
            text = pytesseract.image_to_string(img, lang=lang)
            return text
        except Exception as e:
            return f"Error during OCR: {str(e)}"