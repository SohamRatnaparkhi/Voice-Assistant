from speakListen import speak
import textract
import docx

def ms_word():
    file_loc = "D:\College\Air Pollution.docx"
    doc = docx.Document(file_loc)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    #print(fullText)
    doc_file = '\n'.join(fullText)
    print(doc_file)
    speak(doc_file)

ms_word()