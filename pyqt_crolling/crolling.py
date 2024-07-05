#관련 패키지 import
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결 코드
UI_class = uic.loadUiType("MyGui.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, UI_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # GUI의 버튼을 눌렀을 때 아래 정의한 ReviewCrawlingFunction이 실행됨
        self.pushButton.clicked.connect(self.ReviewCrawlingFunction)

    #이하 지난 프로젝트 조금 개선해서 메소드 안에 넣어줌
    def ReviewCrawlingFunction(self) :

        # 크롬 드라이버 실행 및 잡플래닛 로그인 페이지 접속
        driver = webdriver.Chrome("크롬드라이버가 위치하는 경로 ex)/Users/codingkindergarten/Desktop/chromedriver")
        driver.get("https://www.jobplanet.co.kr/users/sign_in?_nav=gb")
        driver.implicitly_wait(10)

        #입력 받은 정보로 로그인
        login_id = driver.find_element_by_css_selector("input#user_email")
        login_id.send_keys(self.lineEdit_ID.text())

        login_pw = driver.find_element_by_css_selector("input#user_password")
        login_pw.send_keys(self.lineEdit_PW.text())

        login_id.send_keys(Keys.RETURN)
        driver.implicitly_wait(10)
        time.sleep(1) #implicityly_wait로 잘 작동하지 않아서 추가함
        
        #원하는 회사의 리뷰 페이지까지 이동
        company = driver.find_element_by_css_selector("input#search_bar_search_query")
        company.send_keys(self.lineEdit_CN.text())
        company.send_keys(Keys.RETURN)
        driver.implicitly_wait(15)

        driver.find_element_by_css_selector("a.tit").click()
        driver.implicitly_wait(15)

        driver.find_element_by_css_selector("button.btn_close_x_ty1 ").click()
        driver.implicitly_wait(15)

        review_cnt_raw = driver.find_elements_by_css_selector("span.num.notranslate")[1]
        review_cnt = int(review_cnt_raw.text)
        review_page = int(review_cnt/5) + 1
        

        #크롤링한 정보를 담을 리스트명 정의
        list_div = []
        list_cur = []
        list_date =[]
        list_stars = []
        list_summery = []
        list_merit = []
        list_disadvantages = []
        list_managers =[]


        #원하는 회사의 직무/근속여부/일시/요약/평점/장점/단점/경영진에게 바라는 점 크롤링 (for문으로 반복)
        for i in range(review_page): 

            #직무, 근속여부, 지역 ,일시
            user_info = driver.find_elements_by_css_selector("span.txt1")

            #한 페이지 안의 리뷰 갯수
            #한 페이지에 정보 5set씩 나옴. 마지막 페이지는 5개 미만일 수 있으므로 count 변수를 반복횟수로 넣어줌.
            count = int(len(user_info)/4)

            list_user_info = []

            for j in user_info:
                list_user_info.append(j.text)

            for j in range(count):            
                a = list_user_info[4*j]
                list_div.append(a)
                
                b = list_user_info[4*j+1]
                list_cur.append(b)

                c = list_user_info[4*j+3]
                list_date.append(c)

            #별점
            stars = driver.find_elements_by_css_selector("div.star_score")
            for j in stars:
                a = j.get_attribute('style')
                if a[7:9] == '20':
                    list_stars.append("1점")
                elif a[7:9] == '40':
                    list_stars.append("2점")
                elif a[7:9] == '60':
                    list_stars.append("3점")
                elif a[7:9] == '80':
                    list_stars.append("4점")
                else:
                    list_stars.append("5점")
                
            #요약 정보
            summery = driver.find_elements_by_css_selector("h2.us_label")

            for j in summery:
                list_summery.append(j.text)
            
            #장점, 단점, 경영진에게 바라는 점
            list_review = []

            review = driver.find_elements_by_css_selector("dd.df1")

            for j in review:
                list_review.append(j.text)

            for j in range(count):            #한 페이지에 정보 5set씩 나옴. 마지막 페이지는 5개 미만일 수 있으므로 count 변수를 반복횟수로 넣어줌.
                a = list_review[3*j]
                list_merit.append(a)
                
                b = list_review[3*j+1]
                list_disadvantages.append(b)

                c = list_review[3*j+2]
                list_managers.append(c)

            # 다음 페이지 클릭 후 for문 진행, 끝 페이지에서 다음 페이지 클릭 안되는 것 대비해서 예외처리 구문 추가
            try:
                driver.find_element_by_css_selector("a.btn_pgnext").click()
                driver.implicitly_wait(15)
                time.sleep(2) #implicityly_wait로 잘 작동하지 않아서 추가함
            except:
                pass


        # step8.pandas 라이브러리로 표 만들기
        total_data = pd.DataFrame()
        total_data['날짜'] = pd.Series(list_date)
        total_data['직무'] = pd.Series(list_div)
        total_data['재직여부'] = pd.Series(list_cur)
        total_data['별점'] = pd.Series(list_stars)
        total_data['요약'] = pd.Series(list_summery)
        total_data['장점'] = pd.Series(list_merit)
        total_data['단점'] = pd.Series(list_disadvantages)
        total_data['경영진에게 바라는 점'] = pd.Series(list_managers)

        # step9.엑셀 형태로 저장하기
        total_data.to_excel(self.lineEdit_CN.text() + "_잡플래닛 리뷰.xls" ,index=True)

        # step10.크롬 드라이버 종료
        driver.quit()

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()

    