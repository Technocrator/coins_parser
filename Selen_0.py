from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import requests
from selenium import webdriver


def get_source_html(url):
    driver = webdriver.Chrome(executable_path="chromedriver")
    driver.maximize_window()

def main():
    get_source_html()
    
if __name__ == "__main__":
    main()