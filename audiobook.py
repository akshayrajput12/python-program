import pyttsx3
import PyPDF2


File= open("pythonBasicsHandbook.pdf",mode="rb")
pdf_reader= PyPDF2.PdfFileReader(File)
pages= pdf_reader.numPages
melo=pyttsx3.init()
page=pdf_reader.getPage(56)
text=page.extract_text()
melo.say(text)
melo.runAndWait()