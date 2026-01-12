# PDF-OCR-Tool
PDF-OCR-Tool was built out of frustration with the lack of reliable tools for extracting text and exporting specific images from PDFs. Designed for accuracy and ease of use,it enables OCR-based text extraction and image export in one place. Built with the help of Gemini AI. Disclaimer: OCR results may occasionally differ from the original PDF text.


PDF & OCR Tool (Professional Edition)
Version: 1.0.0
Created by: VincentVinnexGeminiAI
---------------------------------------------------------

DESCRIPTION:
This tool allows you to view PDFs, export pages as high-quality images, 
and convert images into editable text (OCR) using advanced AI.

FEATURES:
- Dark Mode.
- Bulk export to PNG/JPG/TIFF.
- OCR to Text (.txt) or Word (.docx).
- Dual Language Support (English, Hindi, etc.).
- Merge multiple pages into a single document.

INSTALLATION REQUIREMENTS:
1. No installation required for this tool. Just run 'PDF-OCR-Tool.exe'.
2. You can use this command (pip install PyQt6 PyMuPDF pytesseract Pillow python-docx) or You can use the command (pip install -r requirements.txt) 
3. CRITICAL: This tool requires the Tesseract OCR engine to "read" text.
   If OCR does not work, please install Tesseract from here:
   https://github.com/UB-Mannheim/tesseract/wiki
   (Install to default location: C:\Program Files\Tesseract-OCR)

HOW TO ADD FONTS/LANGUAGES:
To read languages other than English:
1. Download the .traineddata file for your language.
2. Place it in: C:\Program Files\Tesseract-OCR\tessdata
3. Restart this app.


Common Issues & Fixes

   Error: "python is not recognized..."
     Cause: You forgot to check "Add Python to PATH".
       Fix: Uninstall Python, restart your computer, and reinstall it (don't forget the checkbox!).

   OCR Button crashes the app or says "Tesseract not found"
     Cause: Tesseract isn't installed in the default folder.
       Fix: Reinstall Tesseract (Step 2) and make sure it goes to C:\Program Files\Tesseract-OCR.
