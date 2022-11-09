import PyPDF4

def PDFMerge(pdfs, mergedFileName):
    pdfMerger = PyPDF4.PdfFileMerger()
    
    for pdf in pdfs:
        pdfMerger.append(pdf)
        
    newFile = open(mergedFileName, "wb")
    pdfMerger.write(newFile)
    newFile.close()
    
    print("PDF Merging was done")

pdfs = ["tkinter cheatsheet 2.pdf","rotate.pdf","rotate.pdf","rotate.pdf"]
mergeFile = "merge.pdf"
PDFMerge(pdfs, mergeFile)