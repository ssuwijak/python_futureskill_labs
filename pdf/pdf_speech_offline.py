import PyPDF4
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")
print(len(voices))

#for v in range(voices):
#    print(v.id)


engine.setProperty("rate", 220)
engine.setProperty("volume", 1.0)
engine.setProperty("voice", voices[1].id)

readFile = "article.pdf"
pdfReader = PyPDF4.PdfFileReader(readFile)

for page in range(pdfReader.getNumPages()):
    text = pdfReader.getPage(page).extractText()
    print(text)
    engine.say(text)
    engine.runAndWait()
    
engine.stop()

engine.save_to_file(text, "article.mp3")
engine.runAndWait()
print("done")
