## parser.py
import requests
import time

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


options = Options()
options.headless = False
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
browser.get("https://map.naver.com/v5/search/%EB%8C%80%EC%A0%84%EB%8C%80%ED%9D%A5%EB%8F%99%20%EB%A7%9B%EC%A7%91/place/11724775?c=14183906.9719249,4345639.7335687,15,0,0,0,dh&placePath=%2Fhome%3Fentry=pll&placeSearchOption=entry=pll%26filterId=r07140105%26from=nx%26fromNxList=true%26sessionid=78s%252FqjVlzuU89y7ABDbWuA%253D%253D")

time.sleep(3)
tag_names = browser.find_elements_by_css_selector("._19NVP")


print(tag_names)


# for tag in tag_names:
#     taged = tag.find_elements_by_tag_name("span")
#     print(taged)

# 
# tag_names = browser.find_elements_by_tag_name("li")
# for tag in tag_names:
#     print()
#     print()
#     print(tag)
