import unittest

from selenium.webdriver.chrome.service import Service
from selenium import webdriver


class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\2554184\Downloads\chromedriver.exe')

    def test1(self):
        driver = self.driver
        driver.get("https://www.google.com.mx/")
    

    def tearDown(self):
        driver = self.driver
        driver.close()


if __name__ == '__main__':
    unittest.main()
