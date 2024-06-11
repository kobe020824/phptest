#필요한 라이브러리 불러오기
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip
import time
from datetime import datetime

#크롬 실행
def exec_chrom():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver

url = 'http://www.naver.com'

#브라우저실행(검색)
def exe_browser():    
    while True:
        print('잠시만 기다려 주세요')        
        keyword = input("검색할 단어를 입력하세요(종료를 원할시 살짝 엔터만) : ")
        if keyword == '':           #아무것도 입력하지 않고 엔터를 눌렀을때 즉 null 혹은 None시 종료
            break
        else:
            print('정상적으로 처리중입니다. 조금만 기다려 주세요.')
        
        driver.get(url)                                                                     #지정된 url로 이동
        driver.find_element(By.XPATH, '//*[@id="query"]').click()                           #검색바를 클릭
        pyperclip.copy(keyword)                                                             #input 복사
        driver.find_element(By.XPATH, '//*[@id="query"]').send_keys(Keys.CONTROL, 'v')      #복사한거 붙혀넣기
        time.sleep(1)                                                                       #잠시대기
        driver.find_element(By.XPATH, '//*[@id="sform"]/fieldset/button').click()           #클릭(엔터)
        time.sleep(5)                                                                       #잠시대기
    return driver



start_time = datetime.now() # get the time when the program starts

def chrom_exit(driver):
    end_time = datetime.now() #get the time when the program ends
    elapsed_time = end_time - start_time # calculate the elapsed time
    print('실행한시간:', start_time.strftime('%Y-%m-%d %H:%M:%S'))
    print('끝난시간:', end_time.strftime('%Y-%m-%d %H:%M:%S'))
    print('총작업시간:', str(elapsed_time))
    print('총작업시간:', str(elapsed_time).split('.')[0])       #소수점 생략
    print('Total working time (2 decimal places): {:.2f}'.format(elapsed_time.total_seconds())) #two decimal places
    print('Operation is complete')
    time.sleep(2)
    driver.quit()


#메인
if __name__ == '__main__':
    driver = exec_chrom()
    driver = exe_browser()
    chrom_exit(driver)
