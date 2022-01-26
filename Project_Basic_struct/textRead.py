from speakListen import speak
import textract
import docx

def ms_word():
    filename = ""
    doc = docx.Document("D:\College\Air Pollution.docx")
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    content = '\n'.join(fullText)
    print(content)
    speak(content)

ms_word()