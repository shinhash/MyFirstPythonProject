

# qt5
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


# oracle
import cx_Oracle
import os


# selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


form_class = uic.loadUiType("menuFrame.ui")[0]

class WindowClass(QMainWindow, form_class) :
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        options = Options()
        options.headless = False
        self.browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
        self.browser.get("https://place.map.kakao.com/8801978")
#         self.browser.get("https://map.naver.com/v5/search/%EB%8C%80%EC%A0%84%EB%8C%80%ED%9D%A5%EB%8F%99%20%EB%A7%9B%EC%A7%91/place/11724775?c=14183906.9719249,4345639.7335687,15,0,0,0,dh&placePath=%2Fhome%3Fentry=pll&placeSearchOption=entry=pll%26filterId=r07140105%26from=nx%26fromNxList=true%26sessionid=78s%252FqjVlzuU89y7ABDbWuA%253D%253D")
        
        os.putenv('NLS_LANG', '.UTF8')
        self.conn = cx_Oracle.connect('SHS/java@localhost:1521/xe')
        self.cursor = self.conn.cursor()
        
        self.pushButton.clicked.connect(self.insertOracleToMenuInfo)
        
        
        
        
    def insertOracleToMenuInfo(self):
        
        try:
            url = self.browser.current_url
            self.browser.switch_to.window(self.browser.window_handles[-1])
            
            # 메뉴
            menus = self.browser.find_element_by_css_selector(".list_menu").find_elements_by_tag_name("li")
            # 가게이름
            name = self.browser.find_element_by_css_selector(".inner_place").find_elements_by_tag_name("h2")
            for foodHome in name:
                foodHomeName = foodHome
                
            shopName = foodHome.text
#             print(shopName)
            # 더보기 클릭 액션
            more = self.browser.find_element_by_css_selector(".link_more").find_element_by_tag_name("span")
            while True:
                if more.text == "메뉴 더보기":
                    more.click()
                else:
                    break
             
            sql = "insert into FOODSTORE(STORENAME, FOODNAME, FOODPRICE) values(:1, :2, :3)"
             
            for menu in menus:
                menuText = menu.text.split("\n")
                foodName = menuText[0]
                price = menuText[1]
                print("가게이름 : ", shopName, "메뉴이름 : ", foodName, " 가격 : ", price)
                
                data = (shopName, foodName, price)
                self.cursor.execute(sql, data)
                
                # 데이터 저장
                self.conn.commit()
                
        except:
            print("error!!!")
        
        
        
    def __del__(self):
        # 자원 반납
        self.cursor.close()
        
        # 연결 종료
        self.conn.close()
    
    
        

if __name__ == "__main__" :
    app = QApplication(sys.argv) 

    myWindow = WindowClass() 

    myWindow.show()

    app.exec_()
    
    
    
    
    
    
    
    
    
    
    
    