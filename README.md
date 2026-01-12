# PDF-OCR-Tool
PDF-OCR-Tool was built out of frustration with the lack of reliable tools for extracting text and exporting specific images from PDFs. Designed for accuracy and ease of use,it enables OCR-based text extraction and image export in one place. Built with the help of Gemini AI. Disclaimer: OCR results may occasionally differ from the original PDF text.


<h1 align="center">📄 PDF & OCR Tool (Professional Edition)</h1>

<p align="center">
  <strong>Version:</strong> 1.0.0<br>
  <strong>Created by:</strong> VincentVinnex × Gemini AI
</p>

<hr>

<h2>🧾 Description</h2>
<p>
PDF & OCR Tool is a powerful desktop application designed to simplify working with PDF files.
It allows users to view PDFs, export pages as high-quality images, and convert images or scanned PDFs
into editable text using advanced OCR technology.
</p>

<p><strong>Disclaimer:</strong> Due to OCR limitations, some extracted words may not exactly match the original PDF content.</p>

<hr>

<h2>✨ Features</h2>
<ul>
  <li>🌙 Dark Mode interface</li>
  <li>📦 Bulk export to PNG / JPG / TIFF</li>
  <li>🧠 OCR to Text (.txt) or Word (.docx)</li>
  <li>🌐 Dual language support (English, Hindi, and more)</li>
  <li>📑 Merge multiple pages into a single document</li>
</ul>

<hr>

<h2>⚙️ Installation Requirements</h2>
<ul>
  <li>No installation required — simply run <code>PDF-OCR-Tool.exe</code></li>
  <li>For source usage, install dependencies:</li>
</ul>

<pre>
pip install PyQt6 PyMuPDF pytesseract Pillow python-docx
</pre>

<p>or</p>

<pre>
pip install -r requirements.txt
</pre>

<p><strong>CRITICAL:</strong> This tool requires the Tesseract OCR engine.</p>

<p>
If OCR does not work, install Tesseract from:<br>
<a href="https://github.com/UB-Mannheim/tesseract/wiki" target="_blank">
https://github.com/UB-Mannheim/tesseract/wiki
</a>
</p>

<p>
Install to the default location:<br>
<code>C:\Program Files\Tesseract-OCR</code>
</p>

<hr>

<h2>🌍 Adding Languages / Fonts</h2>
<ol>
  <li>Download the <code>.traineddata</code> file for your language</li>
  <li>Place it in:<br>
    <code>C:\Program Files\Tesseract-OCR\tessdata</code>
  </li>
  <li>Restart the application</li>
</ol>

<hr>

<h2>🛠 Common Issues & Fixes</h2>

<h3>❌ Error: "python is not recognized"</h3>
<p><strong>Cause:</strong> Python was not added to PATH.</p>
<p><strong>Fix:</strong> Uninstall Python, restart your PC, and reinstall it while checking <em>"Add Python to PATH"</em>.</p>

<h3>❌ OCR crashes or says "Tesseract not found"</h3>
<p><strong>Cause:</strong> Tesseract is not installed in the default directory.</p>
<p><strong>Fix:</strong> Reinstall Tesseract and ensure it is installed at:</p>
<pre>
C:\Program Files\Tesseract-OCR
</pre>

<hr>

<p align="center">
  🚀 Built for speed, accuracy, and productivity
</p>
