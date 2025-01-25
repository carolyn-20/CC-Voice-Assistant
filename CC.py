import speech_recognition as aa
import pyttsx3 #Text-to-speech
import pywhatkit  #type:ignore
import datetime
import wikipedia


listener = aa.Recognizer()      #Handles all the speech rocognition tasks

machine = pyttsx3.init()

def talk(text):
    machine.say(text)

    machine.runAndWait()
#talk("Hello,Carolyn")

def input_instruction():
    global instruction 
    try:
        with aa.Microphone() as origin:   #Accessing computer's microphone as origin
            print('Listening...')
            speech = listener.listen(origin)   #Listens the audio from origin
            instruction = listener.recognize_google(speech)   #Converts speech to text
            instruction = instruction.lower()
            if 'CC' in instruction:
                instruction = instruction.replace('CC', '')
                print(instruction)
        
        
        
        print(instruction)
    
    except:
        pass
    return instruction
    
def play_cc():

    instruction = input_instruction()
    print(instruction)
    if 'play' in instruction:
        song = instruction.replace('play', '')
        talk('Playing'+song)
        pywhatkit.playonyt(song)
        
    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk('Current time is '+ time)
        
    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d / %m / %Y')
        talk("Today's date is"+ date)
        
    elif 'how are you' in instruction:
        talk("I'm fine. What about you ?")
        
    elif "what's your name" in instruction:
        talk("I'm CC, your assisstant. You may approach me for all your doubts.")
        
    elif 'who is' in instruction:
        human = instruction.replace('who is', '')
        info =wikipedia.summary(human, 1)
        print(info)
        talk(info)
        
    else:
        talk("Sorry! I can't hear you")
        
play_cc()


    
        
        