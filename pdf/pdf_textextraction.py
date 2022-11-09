import PyPDF4

pdfFile = ""
pdfReader = PyPDF4.PdfFileReader(pdfFile)

"""
pageObj = pdfReader.getPage(0)
txt = pageObj.extractText()
print(txt)
"""
for page in pdfReader.pages:
    print(page.extractText())
