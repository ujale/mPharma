import create_patient
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class CreatePatient(unittest.TestCase):

    def test_happy_case(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("http://localhost:3000/")
        patient = create_patient.PatientCreation(driver)
        patient.required_fields_only()
        patient.all_fields()
        print(patient.first_name.text)
        self.assertEqual(patient.second_user_fullname.text, 'Gregory Portu Mubutu')
        self.assertEqual(patient.second_user_dob.text, 'DOB: 21st May 2010')
        self.assertEqual(patient.second_user_address.text, 'ADDRESS: 34, Freedom way, off Kigali street, Nairobi')
        driver.quit()


if __name__ == '__main__':
    unittest.main()
