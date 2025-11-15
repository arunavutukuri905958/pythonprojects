import pyttsx3
engine = pyttsx3.init()

def speak(text):
    print('speaking.....')
    engine.say(text)
    engine.runAndWait()
    
txt='hey friend im your virtual talking friend'    

speak(txt)



while txt !='bye':
    txt = input('What should I say: ')
    txt.lower()
    if txt !='bye':
        speak(txt)
    else:
        speak('see you friend it was nice talking to you ')    





