import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


hp = ""

options = Options()
options.headless = False
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
browser.get("http://localhost/helloWeb/hello.jsp")

time.sleep(3)
tag_names = browser.find_element_by_css_selector(".rank_top1000_list").find_elements_by_tag_name("li")
for tag in tag_names:
    print(tag.text.split("\n"))

tds = browser.find_element_by_css_selector("table").find_elements_by_tag_name("td")
i = 0;
for td in tds:
     
    if i%2 == 1:
        hp = td.text
        print(hp)
    i += 1
# 
# print(hp)