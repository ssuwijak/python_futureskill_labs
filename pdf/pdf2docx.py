from pdf2docx import Converter

pdfFile = "tkinter cheatsheet 2.pdf"
docxFile = "tkinter cheatsheet 2.docx"

cv = Converter(pdfFile)
cv.convert(docxFile)