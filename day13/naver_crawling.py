#제목: 네이버 검색 API 활용하기
 
#import
import sqlite3
import urllib.request
# import requests
from bs4 import BeautifulSoup



#애플리케이션 클라이언트 id 및 secret
client_id = "vSrhWEauWM31KSkRgmnJ" 
client_secret = "zeSv_5apNi"

# query = urllib.parse.quote("인천")
query = urllib.parse.quote(input("검색: "))
displayLine = "&display=5"
# url = "https://openapi.naver.com/v1/search/blog?query=" + query # json 결과
url = "https://openapi.naver.com/v1/search/local.xml?query=" + query + displayLine # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

# sqlite3 설정
conn = sqlite3.connect("./naverTest.db", isolation_level=None)
# conn = sqlite3.connect("./naverTest.db")
cursor = conn.cursor()


if(rescode==200):
    response_body = response.read()
    resp_dec = response_body.decode('utf-8')
    print(resp_dec)
    
    
    items = BeautifulSoup(resp_dec, 'xml')
    my_titles = items.select(
        'item'
    )
    
    
    print(items)
    for item in my_titles:
        
        print()
        print()
        print()
        print("title : ", item.find("title").text.replace("<b>", "").replace("</b>", ""))
        print("link : ", item.find("link").text)
        print("category : ", item.find("category").text)
        print("description : ", item.find("description").text)
        print("telephone : ", item.find("telephone").text)
        print("address : ", item.find("address").text)
        print("roadAddress : ", item.find("roadAddress").text)
        print("mapx : ", item.find("mapx").text)
        print("mapy : ", item.find("mapy").text)
        
        title       = item.find("title").text.replace("<b>", "").replace("</b>", "")
        link        = item.find("link").text
        category    = item.find("category").text
        description = item.find("description").text
        telephone   = item.find("telephone").text
        address     = item.find("address").text
        roadAddress = item.find("roadAddress").text
        mapx        = item.find("mapx").text
        mapy        = item.find("mapy").text
        
#         sql = "insert into naverTestDB(title, link, category, description, telephone, address, roadAddress, mapx, mapy) values( ? , ? , ? , ? , ? , ? , ? , ? , ?)"
#         data = (title, link, category, description, telephone, address, roadAddress, mapx, mapy)
#         cursor.execute(sql, data)
    
else:
    print("Error Code:" + rescode)





