## parser.py
import requests
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


options = Options()
options.headless = False
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
browser.get("http://www.goobne.co.kr/menu/menu_list.jsp?class=")

time.sleep(3)
tag_names = browser.find_element_by_css_selector(".menu_list_wrap")
print(tag_names.text)
# for tag in tag_names:
#     print(tag.text)
