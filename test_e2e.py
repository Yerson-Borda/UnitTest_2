import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestLargestRectangleAreaE2E(unittest.TestCase):

    def setUp(self):
        chromedriver_path = 'C:\\Users\\kira_\\OneDrive\\Escritorio\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'
        brave_path = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'

        options = Options()
        options.binary_location = brave_path

        self.driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)

    def test_largest_rectangle_area(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")

        input_field = driver.find_element(By.ID, "heights")
        submit_button = driver.find_element(By.XPATH, '//input[@type="submit"]')

        input_field.send_keys("2,1,5,6,2,3")
        submit_button.click()

        result = driver.find_element(By.TAG_NAME, 'h2').text
        self.assertIn("Result: 10", result)

    def test_invalid_input(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")

        input_field = driver.find_element(By.ID, "heights")
        submit_button = driver.find_element(By.XPATH, '//input[@type="submit"]')

        input_field.send_keys("")
        submit_button.click()

        error = driver.find_element(By.TAG_NAME, 'h2').text
        # print(f"Actual error message: {error}")
        self.assertIn("Error", error)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
