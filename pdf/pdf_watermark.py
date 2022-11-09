import PyPDF4

def PDFWaterMark(originalFile, waterMarkFile, outputFile):
    originPDF = PyPDF4.PdfFileReader(originalFile)
    waterPDF = PyPDF4.PdfFileReader(waterMarkFile)
    outputPDF = PyPDF4.PdfFileWriter()

    watermark = waterPDF.getPage(0)
    
    for page in range(originPDF.getNumPages()):
        pageObj = originPDF.getPage(page)
        pageObj.mergePage(watermark)
        
        outputPDF.addPage(pageObj)
        
    newFile  = open(outputFile, "wb")
    outputPDF.write(newFile)

    print("PDF Watermark was done")

originalFile = "merge.pdf"
waterMarkFile = "doraemon_watermark.pdf"
outputFile = "watermark_output.pdf"

PDFWaterMark(originalFile, waterMarkFile, outputFile)