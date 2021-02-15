# -*- coding:utf-8 -*-
from selenium import webdriver

# 크롬 드라이버 경로 지정
driver = webdriver.Chrome('C:/chromedriver.exe')
driver.implicitly_wait(1)

# 복권 사이트 연결
driver.get("https://www.dhlottery.co.kr/user.do?method=login&returnUrl=")

# 복권 사이트 로그인
driver.find_element_by_xpath('/html/body/div[3]/section/div/div[2]/div/form/div/div[1]/fieldset/div[1]/input[1]').send_keys('')
driver.find_element_by_xpath('/html/body/div[3]/section/div/div[2]/div/form/div/div[1]/fieldset/div[1]/input[2]').send_keys('')
driver.find_element_by_xpath('/html/body/div[3]/section/div/div[2]/div/form/div/div[1]/fieldset/div[1]/a').click()

# 복권 구매 가능한 프레임으로 이동
driver.get("https://el.dhlottery.co.kr/game/TotalGame.jsp?LottoId=LO40")
driver.get("https://ol.dhlottery.co.kr/olotto/game/game645.do")

# 나의 로또 번호 선택
element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[4]/a")
driver.execute_script("selectWayTab(3);", element)

# 1번 항목 선택
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/li/input').click()

# 확인 -> 구매하기 -> 알림창 확인
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[3]/div[2]/input[1]').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[3]/input[1]').click()
alert = driver.switch_to.alert
alert.accept()
driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[4]/input').click()