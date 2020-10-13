import urllib.request
from selenium import webdriver as wd 
driver = wd.Chrome(executable_path="chromedriver.exe") 

query = urllib.parse.quote(input("검색: "))
displayLine = "&display=100"
url = "https://naver.com/v1/search/local.xml?query=" + query + displayLine # xml 결과
# url = "http://localhost/helloWeb/hello.jsp" 
# driver.get(url)

html = url.text
print(html)