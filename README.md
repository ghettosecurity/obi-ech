# Privacy, Obfuscation, Social and Ethical Issues of the Internet

Obi-Ech
Built to Obfuscate alexa dot/echo/auto/etc. smart devices by announcing random Alexa Smart Commands to any Alexa device. Source Code can be modified for other privacy intrusive technologies such as Google, Bixby, Siri, and more. This program attempts to obfuscate the following: 

1) Voice (via pyttsx voices)
2) Speech analytics and Cadence  (via speed/rates)
3) Command behavior (via seudo random commands and times)
4) Non-Repudiation (via seudo random voices/dialects/speech that can be used to repudiate a claim) 
5) Number of People (via voice genders, rates, dialects) 
6) Age of Commander (via voice genders, rates, dialects)


## alexa-obscure-with-pyttsx3.py ##
Implements a better version of alexa-obscure code with version 3 of pyttsx (pyttsx3). Pyttsx3 Works with python 2 and 3. 

### Install Pre-req's: ###
Run with administrator rights and install Anaconda with python 2.7
~~~~
pip install pyttsx3
pip install gTTS
pip install pyaudio
~~~~

### Usage: ###
~~~~
python alexa-obscure-with-pyttsx3.py
~~~~


## alexa-obsure.py ##
Implements a simple version of alexa-obscure code with version 1 of pyttsx. Does not implement Speech Cadence or other obfuscation techniques besides randomized commands.

### Install Pre-req's: ### 
Run with administrator rights and install Anaconda with python 2.7
~~~~
pip install pyttsx
pip install gTTS
pip install pyaudio
~~~~

### Usage: ### 
~~~~
python alexa-obscure.py
~~~~    

## acommands.txt ##
This is a list of alexa commands via text file that is used for input into the core alexa-obscure* code. List was sourced from http://www.simplyinformed.uk/PDF/Alexa_Commands_2019.pdf. The program will reference this list when choosing randomized lines of commands to use for obfuscation. 
