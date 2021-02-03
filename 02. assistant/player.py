from time import ctime
import os
from gtts import gTTS
import speech_recognition as sr
import requests


# def speak():
#     audioString = "Finished your command, please call me again"
#     tts = gTTS(text=audioString, lang='en')
#     tts.save("completed_your_command.mp3")
#     os.system("completed_your_command.mp3")

# speak()


# # def recordAudio():
# #     r = sr.Recognizer()
# #     with sr.Microphone() as source:
# #         print("Say Something")
# #         audio = r.listen(source)
    
# #     # Speech recognition using Google Speech Recognition
# #     data = ""
# #     try:
# #         # Uses the default API key
# #         # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
# #         data = r.recognize_google(audio)
# #         print("You said: " + data)
# #     except sr.UnknownValueError:
# #         print("Google Speech Recognition could not understand audio")
# #     except sr.RequestError as e:

# #         print("Could not request results from Google Speech Recognition service; {0}".format(e))

# #     return data
# from selenium import webdriver

# iden = "<USER ID>"
# pw = "<USER PW>"

# driver = webdriver.Chrome('/Users/roytravel/Desktop/chromedriver.exe')
# driver.implicitly_wait(1)
# driver.get('https://www.naver.com')
# driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div[1]/div/a').click()
# driver.execute_script("document.querySelector('#id',{}").format(iden)
# driver.execute_script("document.querySelector('#pw',{}").format(pw)
# driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/form/fieldset/input').click()

from time import ctime
print (ctime()[11:19])
