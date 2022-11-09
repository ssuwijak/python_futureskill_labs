import PyPDF4

def PDFSplit(originalFileName, splitPages):
    start = 0
    end = splitPages[0]
    
    for i in range(len(splitPages) + 1):
        pdfReader = PyPDF4.PdfFileReader(originalFileName)
        pdfWriter = PyPDF4.PdfFileWriter()
        
        for page in range(start,end):
            pdfWriter.addPage(pdfReader.getPage(page))
            
        output = "split_" + str(i + 1) + ".pdf"
    
        newFile = open(output, "wb")   
        pdfWriter.write(newFile)
        newFile.close()
        
        start = end 
        
        try:
            end = splitPages[i + 1]
        except IndexError:
            end = pdfReader.getNumPages()
            
        print("PDF Splitting was done")    
   


originalFile = "merge.pdf"
splitPages = [1,3]
PDFSplit(originalFile, splitPages)