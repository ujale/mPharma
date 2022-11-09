import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def required_fields_only(driver):
    driver.find_element(By.CSS_SELECTOR, '#root > div > div:nth-child(1) > main > div:nth-child(1) > input').send_keys('Alfred')
    driver.find_element(By.CSS_SELECTOR, '#root > div > div:nth-child(1) > main > section > div:nth-child(2) > input').send_keys('Rewane')
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div[2]/input').send_keys('2333456700')
    driver.find_element(By.XPATH, r'//*[@id="root"]/div/div[1]/main/div[3]/input').click()
    driver.find_element(By.LINK_TEXT, 'Add New User').click()
    assert ("Alfred Rewane", "Alfred Rewane", "Full name is displayed correctly")
    first_user_card = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/main/div[1]')
    assert first_user_card.is_displayed()
    print("First patient's card is visible: ", first_user_card.is_displayed())
    print("First patient's information: ", first_user_card.text)


def all_fields(driver):
    driver.find_element(By.CSS_SELECTOR, '#root > div > div:nth-child(1) > main > div:nth-child(1) > input').send_keys(
        'Gregory')
    driver.find_element(By.CSS_SELECTOR, '#root > div > div:nth-child(1) > main > section > div:nth-child(1) > input').send_keys('Portu')
    driver.find_element(By.NAME, 'lastName').send_keys('Mubutu')
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div[2]/input').send_keys('2343456700')
    driver.find_element(By.NAME, 'address').send_keys('34, Freedom way, off Kigali street, Nairobi')
    driver.find_element(By.XPATH, r'//*[@id="root"]/div/div[1]/main/div[3]/input').click()
    driver.find_element(By.LINK_TEXT, 'Add New User').click()
    second_user_card = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/main/div[1]')
    print("Second patient's card is visible: ", second_user_card.is_displayed())
    print("Second patient's information: ", second_user_card.text)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://localhost:3000/")
    required_fields_only(driver)
    time.sleep(3)
    all_fields(driver)
    time.sleep(10)


if __name__ == '__main__':
    main()
