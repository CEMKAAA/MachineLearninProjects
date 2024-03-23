from tiktokvoice import *

text = "i just pooped at my pants isn`t that too funny i can`t believe that i do this shit man yeahhh that was good i really do not know why i do that shit hahahaahahh" 
voice = "en_us_001" # all possible voices can be found here

# arguments:
#   - input text
#   - vocie which is used for the audio
#   - output file name
#   - play sound after generating the audio
tts(text, voice, "output1.mp3", play_sound=True)
