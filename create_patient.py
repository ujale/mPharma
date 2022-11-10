import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class PatientCreation:

    def __init__(self, driver):
        self.driver = driver
        self.first_name = driver.find_element(By.NAME, 'firstName')
        self.middle_name = driver.find_element(By.CSS_SELECTOR,
                                               '#root > div > div:nth-child(1) > main > section > div:nth-child(1) > input')
        self.last_name = driver.find_element(By.CSS_SELECTOR,
                                             '#root > div > div:nth-child(1) > main > section > div:nth-child(2) > input')
        self.phone = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div[2]/input')
        self.dob = driver.find_element(By.NAME, 'dob')
        self.address = driver.find_element(By.NAME, 'address')
        self.add_new_patient_button = driver.find_element(By.LINK_TEXT, 'Add New User')

    def required_fields_only(self):
        self.first_name.send_keys('Alfred')
        self.last_name.send_keys('Rewane')
        self.phone.send_keys('2333456700')
        # driver.execute_script("arguments[0].value = '20-07-2001';", driver.find_element(By.NAME, 'dob'))
        self.dob.send_keys('20-07-2001')
        self.address.click()
        self.add_new_patient_button.click()
        assert "Alfred Rewane" == "Alfred Rewane"
        #assert first_user_card.is_displayed()
        self.first_user_card = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/main/div[1]')
        print("First patient's card is visible: ", self.first_user_card.is_displayed())
        print("First patient's information: ", self.first_user_card.text)




    def all_fields(self):
        self.first_name.send_keys('Gregory')
        self.middle_name.send_keys('Portu')
        self.last_name.send_keys('Mubutu')
        self.phone.send_keys('2343456700')
        self.dob.send_keys('21-05-2010')
        self.address.send_keys('34, Freedom way, off Kigali street, Nairobi')
        self.add_new_patient_button.click()
        self.second_user_card = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/main/div[2]')
        print("Second patient's card is visible: ", self.second_user_card.is_displayed())
        self.second_user_fullname = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/main/div[1]/div[2]/h4')
        print("Second patient's full name: ", self.second_user_fullname.text)
        self.second_user_dob = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/main/div[1]/div[2]/p[2]')
        self.second_user_address = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/main/div[1]/div[2]/p[1]')


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://localhost:3000/")
    patient = PatientCreation(driver)
    patient.required_fields_only()
    patient.all_fields()
    time.sleep(5)


if __name__ == '__main__':
    main()
