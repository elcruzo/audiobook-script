import pyttsx3
import PyPDF3

with open('book.pdf', 'rb') as book:

    full_text = ""

    reader = PyPDF3.PdfFileReader(book)
    
    audio_reader = pyttsx3.init()
    audio_reader.setProperty("rate", 100)
    
    for page in range(reader.numPages):
        next_page = reader.getPage(page)
        content = next_page.extractText()
        full_text += content
        
    audio_reader.save_to_file(content, "myaudiobook.mp3")
    audio_reader.runAndWait()
