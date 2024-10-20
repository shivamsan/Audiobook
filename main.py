import pyttsx3
import PyPDF2 

book = open('book2.pdf','rb')

pdfReader = PyPDF2.PdfReader(book) #var
pages = len(pdfReader.pages)


1
print(pages)

speaker = pyttsx3.init()

for num in range(4,pages):
    page = pdfReader.pages[num]#indexing starts from 0 
    text =page.extract_text()

    speaker.say("Wassup! I am you Bot Barney. I am you AI reader")
    speaker.say(text)
    speaker.runAndWait()


