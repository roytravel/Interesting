from time import ctime
import os
from gtts import gTTS
import speech_recognition as sr
import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver


def input_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)
    
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: {}".format(data))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data


def speak(audioString):
    
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("result.mp3")
    os.system("result.mp3")


now = time.gmtime(time.time())        # 현재 시각 측정 후 해석
now.tm_year, now.tm_mon, now.tm_mday  # 년, 월, 일

now.tm_hour, now.tm_min, now.tm_sec   # 시, 분, 초


def jarvis(data):
    data = data.lower()
    if "master name" in data:
        speak("Master Name is roytravel")

    if "time" in data:
        speak(ctime()[11:16])

    if "notepad" in data or "Notepad" in data:
        os.system("/Windows/system32/notepad.exe")

    if "calculation" in data:
        os.system("/Windows/system32/calc.exe")

    if "CMD" in data:
        os.system("/Windows/system32/cmd.exe")

    if "turn off the computer" in data:
        os.system("shutdown -s -t 6000")

    if "notion" in data:
        os.system("/Users/Roytravel/Desktop/notion.lnk")

    if "black" in data:
        os.system("/Users/RoyTravel/Desktop/slack.lnk")

    if "love letter" in data:
        os.system("/Users/RoyTravel/Desktop/MUSIC/LuvLetter.mp4")
        time.sleep(280)
    
    if "chinese" in data:
        os.system("/Users/RoyTravel/Desktop/MUSIC/village.mp4")
        time.sleep(260)

    if "ain't me" in data:
        os.system("/Users/RoyTravel/Desktop/MUSIC/It-Aint-Me-COdeko-Remix.mp4")
        time.sleep(260)

    if "morning music" in data:
        os.system("/Users/RoyTravel/Desktop/MUSIC/ghibri.mp4")
        time.sleep(170)

    if "last carnival" in data:
        os.system("/Users/RoyTravel/Desktop/MUSIC/Last-Carnival.mp4")
        time.sleep(240)

    if "la campanella" in data:
        os.system("/Users/RoyTravel/Desktop/MUSIC/La-Campanella.mp4")
        time.sleep(300)

    if "howl's moving castle" in data:
        os.system("/Users/RoyTravel/Desktop/MUSIC/Howls-Moving-Castle.mp4")
        time.sleep(315)
    
    if "reminiscence" in data:
        os.system("/Users/RoyTravel/Desktop/MUSIC/Reminiscence.mp4")
        time.sleep(160)

    if "second waltz" in data:
        os.system("/Users/RoyTravel/Desktop/MUSIC/The-Second-Waltz.mp4")
        time.sleep(230)

    if "romance" in data:
        os.system("/Users/RoyTravel/Desktop/MUSIC/Romance-Yuhki-Kuramoto.mp4")
        time.sleep(270)

    if "top search ranking" in data:
        html = requests.get('https://www.naver.com/').text
        soup = BeautifulSoup(html, 'html.parser')
        title_list = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')
        for idx, title in enumerate(title_list, 1):
            print("{}{} {}".format(idx, '위', title.text))

    if "terminate" in data:
        return False

# data = recordAudio()
# jarvis(data)


def master_authentication():
    os.system("what_is_code.mp3")
    time.sleep(3)
    data = input_voice()
    if ("apple" in data) or ("Apple" in data):
        os.system("confirm_master.mp3")
        return True
    else:
        os.system("fail_message.mp3")
        return False


if __name__ == '__main__':
    # flag = master_authentication()
    # if flag == True:
        while True:
            flag = True
            # time.sleep(3)
            data = input_voice()
            flag = jarvis(data)
            if flag == False:
                speak("Terminate AI service. Please call me again")
                break
            # os.system("completed_your_command.mp3")
