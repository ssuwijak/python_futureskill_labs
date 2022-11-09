import PyPDF4

def PDFRotation(originalFile, newFileName, rotateAngle):
    pdfReader = PyPDF4.PdfFileReader(originalFile)
    pdfWriter = PyPDF4.PdfFileWriter()
    
    for page in range(pdfReader.getNumPages()):
        pageObj = pdfReader.getPage(page)
        pageObj.rotateClockwise(rotateAngle)
        
        pdfWriter.addPage(pageObj)
        
    newFile = open(newFileName, "wb")
    pdfWriter.write(newFile)
    newFile.close()
    
    print("PDF Rotation was done")

    
originalFile = "tkinter cheatsheet 2.pdf"
newFile = "rotate.pdf"
rotateAngle = 270

PDFRotation(originalFile, newFile, rotateAngle)