import random 
import pyttsx
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
print count

while True: 
    inty = random.randint(1,count)
    print inty +1

    lines = f.readlines()
    cmd = content_list[inty]
    print content_list[inty]
    #readline(inty)
    
    engine = pyttsx.init()
    if "'" or "(" or ")" or "[" or "]" or '"' in cmd:
        pass
        engine.say(cmd)
        engine.runAndWait()
    
        sleep(randint(1,5))
    
    
    
