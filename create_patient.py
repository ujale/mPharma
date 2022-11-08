from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://localhost:3000/")


if __name__ == '__main__':
    main()