# 셀레늄 모듈 임포트
from selenium import webdriver
import time

# 크롬 물리드라이버 가동 명령
driver = webdriver.Chrome("C:\chrome/chromedriver.exe")

# 물리 드라이버로 사이트 이동 명령
# 유튜브 조회수 올리기
while True:
    time.sleep(1)
    driver.get("https://www.youtube.com/watch?v=TsNldS4kwKM")

