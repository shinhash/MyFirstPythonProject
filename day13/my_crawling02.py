## parser.py
import requests
from bs4 import BeautifulSoup

## HTTP GET Request
req = requests.get('http://localhost/helloWeb/hello.jsp')

## HTML 소스 가져오기
html = req.text
## HTTP Header 가져오기
header = req.headers
## HTTP Status 가져오기 (200: 정상)
status = req.status_code
## HTTP가 정상적으로 되었는지 (True/False)
is_ok = req.ok



soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
    'table td'
    )
## my_titles는 list 객체
for title in my_titles:
    ## Tag안의 텍스트
    print(title.text)
    ## Tag의 속성을 가져오기(ex: href속성)
#     print(title.get('href'))