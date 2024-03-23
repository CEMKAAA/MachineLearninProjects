import pyttsx3

converter = pyttsx3.init()

converter.setProperty('rate', 150)

converter.setProperty('volume', 0.7)

converter.say('Hello i am speaking right now can you believe it')

voices = converter.getProperty('voices')

for voice in voices:
    # to get the info. about various voices in our PC  
    print("Voice:") 
    print("ID: %s" %voice.id) 
    print("Name: %s" %voice.name) 
    print("Age: %s" %voice.age) 
    print("Gender: %s" %voice.gender) 
    print("Languages Known: %s" %voice.languages) 
    
converter.runAndWait()