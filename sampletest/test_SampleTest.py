from selenium import webdriver
from selenium.webdriver.common import keys


class Testsample:
    def test_Sample1(self):
        driver = webdriver.Chrome("C:\\Users\\admin\\PycharmProjects\\SeleniumTest2\\config\\chromedriver.exe")
        driver.get("https://www.google.com/")
        input=driver.find_element_by_name("q")
        input.send_keys('chennai')
        input.send_keys(keys.ENTER)


    def test_Sample2(self):
        driver = webdriver.Chrome("C:\\Users\\admin\\PycharmProjects\\SeleniumTest2\\config\\chromedriver.exe")
        driver.get("https://www.bing.com/")
        input=driver.find_element_by_name("q")
        input.send_keys('chennai')
        input.send_keys(keys.ENTER)
        input=driver.find_element_by_name("qaaaa")

