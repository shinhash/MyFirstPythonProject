from selenium import webdriver as wd 
driver = wd.Chrome(executable_path="chromedriver.exe") 
url = "http://localhost/helloWeb/hello.jsp" 
driver.get(url)

driver.find_element_by_css_selector("td")