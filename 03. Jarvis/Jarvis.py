import os
import pyttsx3
import datetime
import speech_recognition as sr
import wolframalpha
import wikipedia
import webbrowser
from selenium import webdriver
from gtts import gTTS
import socket
import json
import requests
import youtube_dl


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

    # 지식 검색
    def wiki(self,keyword):
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
    
    def google(self, keyword):
        ''' need to add'''
        pass

    def papago(self, word):
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Naver-Client-Id': '<ID>',
        'X-Naver-Client-Secret': '<Secret>',
        }

        data = {
        'source': 'en',
        'target': 'ko',
        'text': word
        }
        response = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
        translated_word = response.text
        json_result = json.loads(translated_word)
        result = json_result['message']['result']['translatedText']
        return result

    
    def geometry(self, data):
        # 위도 경도 반환 (카카오 API 사용)
        url = "https://dapi.kakao.com/v2/local/search/address.json?query={}".format(data)
        api = os.environ.get('KakaoAK')
        api = "KakaoAK " + api
        headers = {"Authorization": api}
        result = json.loads(str(requests.get(url ,headers=headers).text))
        match_first = result['documents'][0]['address']
        return float(match_first['y']),float(match_first['x'])


    def wether(self, longitude, latitude):
        appid = os.environ.get('OpenWetherAPI')
        url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(longitude, latitude, appid)
        response = requests.get(url)
        return response.text


class Listen(object):

    def __init__(self):
        pass

    # 사용자 음성 인식
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
    
    # 사용자 음성에 따른 유튜브 비디오 검색
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


    def download_video_and_subtitle(self, youtube_video_list):
        download_path = ''  # 다운로드 경로
        download_path = os.path.join(download_path, '%(id)s-%(title)s.%(ext)s')
        
        for video_url in youtube_video_list:
            # youtube_dl options
            ydl_opts = {
                'format': 'best/best',  # 가장 좋은 화질로 선택(화질을 선택하여 다운로드 가능)
                'outtmpl': download_path, # 다운로드 경로 설정
                'writesubtitles': 'best', # 자막 다운로드(자막이 없는 경우 다운로드 X)
                'writethumbnail': 'best',  # 영상 thumbnail 다운로드
                'writeautomaticsub': True, # 자동 생성된 자막 다운로드
                'subtitleslangs': 'kr'  # 자막 언어가 영어인 경우(다른 언어로 변경 가능)
                }

            try:
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_url])
            
            except Exception as e:
                print('[!] Error : {}'.format(e))
                pass
        print('[+] Completed download!')


class Data(object):

    def __init__(self):
        pass

    # 사용자의 음성 데이터 수집
    def save(self, data):
        print(data)
        tts = gTTS(text=data, lang='en')
        tts.save("<PATH>")
        os.system("<PATH>")

    # 사용자의 IP 정보 수집
    def address(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(('gmail.com', 80))
        res = sock.getsockname()[0]
        sock.close()
        return res

    # 사용자의 MAC 정보 수집
    def mac(self):
        pass

    # 음성인식 시간 정보 수집
    def time(self):
        pass

    # 데이터베이스로 사용자 정보 송신
    def send(self):
        '''Send to database '''
        pass


if __name__ == '__main__':
    S = Speech()
    R = Search()
    L = Listen()
    A = Action()

    # data = ""
    # S.speak(data)
    # longtidue, latitude = R.geometry(data)
    # result = R.wether(longtidue, latitude)
    # print (result)

    data = L.say()

    youtube_url_list = list()
    url = "https://www.youtube.com/results?search_query={}".format(data)
    youtube_url_list.append(url)
    A.download_video_and_subtitle(youtube_url_list)