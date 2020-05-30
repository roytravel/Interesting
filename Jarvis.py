import os
import pyttsx3
import datetime
import speech_recognition as sr
import wolframalpha
import wikipedia
import webbrowser
from selenium import webdriver

class Speech(object):

    def __init__(self):

        # TTS 엔진 초기화
        self.engine = pyttsx3.init()

        # 말 속도 (Default : 180)
        self.engine.setProperty('rate', 180)
        self.rate = self.engine.getProperty('rate')

        # 말 소리 크기
        self.engine.setProperty('volume', 0.5)
        self.volume = self.engine.getProperty('volume')


    def init_hello(self):
        self.engine.say("뭐 도와줄까?")
        self.engine.runAndWait()
        self.engine.stop()


    def speak(self,audio):
        print('[+] Jarvis : ' + audio)
        self.engine.say(audio)
        self.engine.runAndWait()
        self.engine.stop()


    def greet(self):
        currentH = int(datetime.datetime.now().hour)
        if currentH >= 0 and currentH < 12:
            self.speak('좋은 아침이야')

        if currentH >= 12 and currentH < 21:
            self.speak('오늘 되게 좋은일 일어나지 않을까?')

        if currentH >= 21 and currentH !=0:
            self.speak('오늘 하루 어땠어?')


class Search(object):

    def __init__(self):
        self.app_id = os.environ.get('WOLFRAMALPHA_APP_ID')
        self.client = wolframalpha.Client(self.app_id)

    
    def find(self,keyword):
        try:
            try:
                result = wikipedia.summary(keyword, sentences=2)
                S.speak(result)

            except:
                response = self.client.query(keyword)
                result = next(response.results).text
                S.speak(result)
                
        except Exception as error:
            print (error)
            pass


class Listen(object):

    def __init__(self):
        pass

    def say(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            data = ""
            try:
                data = r.recognize_google(audio)
                print ("[+] You said : {}".format(data))
            except sr.UnknownValueError:
                print ("[!] Google Speech Recognition colud not understand audio")
                return False
            except sr.RequestError as e:
                print ("[!] Colud not request results from Google Speech Recognition service; {}".format(e))
                return False
        return data


class Action(object):
    def __init__(self):
        self.chrome_driver = os.environ.get('CHROME')
        
    def youtube(self):
        S.speak("무슨 노래 듣고 싶어?")
        data = L.say()
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        options.add_experimental_option("detach", True) #Keep chrome window
        driver = webdriver.Chrome(self.chrome_driver, options=options)
        url = "https://www.youtube.com/results?search_query={}".format(data)
        driver.get(url)
        driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a').click()
        


if __name__ == '__main__':
    S = Speech()
    R = Search()
    L = Listen()
    A = Action()

    data = L.say()

    if 'youtube' in data.lower():
        A.youtube()
