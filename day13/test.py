# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
import time
import requests
from bs4 import BeautifulSoup



class CrawlingVo():
    title=""
    link=""
    category=""
    description=""
    telephone=""
    address=""
    roadAddress=""
    map_x=""
    map_y=""
    
    def __init__(self):
        pass
        
class api_naver():
    def __init__(self):
        self.client_id = "c2B6tQ6F7XTAKp6g8sny"
        self.client_secret = "uBROrFUpwH"
        self.encText = urllib.parse.quote("대전 대흥동 맛집")
        self.url = "https://openapi.naver.com/v1/search/local.xml?query=" + self.encText + "&display=5" # json 결과
    def naver(self):
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
        request = urllib.request.Request(self.url)
        request.add_header("X-Naver-Client-Id", self.client_id)
        request.add_header("X-Naver-Client-Secret", self.client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        
        if(rescode==200):
            response_body = response.read()
            
            response_decode = response_body.decode('utf-8')
            return response_decode
            
        #     print(response_decode)
        else:
            return "Error Code:" + rescode
    

## HTTP GET Request

## HTML 소스 가져오기
voList = []
naver = api_naver()
html = naver.naver()
## BeautifulSoup으로 html소스를 python객체로 변환하기
## 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
## 이 글에서는 Python 내장 html.parser를 이용했다.
soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select(
    'item'
    )
## my_titles는 list 객체
for item in my_titles:
    ## Tag안의 텍스트
    
    
    print(item.link.text)
    

    
    ## Tag의 속성을 가져오기(ex: href속성)
#     print(title.get('href'))







    