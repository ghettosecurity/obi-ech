import random 
import pyttsx3
from random import randint
from time import sleep

filename = r'acommands.txt'

f= open(filename,"r")
contents =f.read()

content_clean1 = contents.strip('"')
content_clean2 = content_clean1.strip("[")
content_clean3 = content_clean2.strip("]")

#print type(contents)
#print contents

content_list = content_clean3.split("\n")
#print content_list

count = len(open(filename).readlines())
print "Number of Cmds: " + str(count)        


class _TTS:
    engine = None
    rate = None
    def __init__(self):
#       self.engine = pyttsx3.init(driverName='sapi5')
        self.engine = pyttsx3.init()

    def start(self,text):
        #Speech Cadence/rate 
        rate = self.engine.getProperty('rate')
        cadence = random.randint(90,220)
        print("cadence:" + str(cadence))
        self.engine.setProperty('rate', cadence) # 100-220  (150 is best)

        #Speech Volume 
        volume = self.engine.getProperty('volume')
        self.engine.setProperty('volume', volume-0.25)

        self.engine.say(text)
        self.engine.runAndWait()

        ###engine = pyttsx3.init(driverName='sapi5')
        ###engine.say(cmd)
        ###engine.runAndWait()
                
                
while True: 
    inty = random.randint(1,count)
    print "CMD ID: " + str(inty +1)

    lines = f.readlines()
    cmd = content_list[inty]
    print  "CMD Text: " + content_list[inty]
    #readline(inty)
    
    ###engine = pyttsx3.init(driverName='sapi5')
    """
    #Speech Cadence/rate 
    rate = engine.getProperty('rate')
    cadence = random.randint(90,220)
    print("cadence:" + str(cadence))
    engine.setProperty('rate', cadence) # 100-220  (150 is best)
    
    #Speech Volume 
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume-0.25)
    """
    
    
    if "'" or "(" or ")" or "[" or "]" or '"' or "#" in cmd:
        pass
        tts = _TTS()
        tts.start(cmd)
        del(tts)      
    
        sleep(randint(1,5))
    
