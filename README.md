# MIS511
UofA MIS511-Privacy

alexa-obsure.py 
---------------
Obfuscates alexa dot/echo/auto/etc. smart devices by announcing random Alexa Smart Commands to any Alexa device. Source Code can be modified for other privacy intrusive technologies such as Google, Bixby, Siri, and more. This program attempts to obfuscate the following: 

1) Voice (via pyttsx voices)
2) Speech analytics and Cadence  (via speed/rates)
3) Command behavior (via seudo random commands and times)
4) Non-Repudiation (via seudo random voices/dialects/speech that can be used to repudiate a claim) 
5) Number of People (via voice genders, rates, dialects) 
6) Age of Commander (via voice genders, rates, dialects)



Install Pre-req's: 
------------------
pip install pyttsx
pip install pyttsx3
pip install gTTS
conda install


Usage: 
-----------------
python alexa-obscure.py
