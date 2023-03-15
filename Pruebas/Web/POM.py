import unittest

from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from Funciones.Funciones import Funciones2
from Funciones.Funciones2 import Global2


class base_test(unittest.TestCase):

    def setUp(self):
        c = Service(r'C:\Users\2554184\Downloads\chromedriver.exe')
        self.driver = webdriver.Chrome(service=c)

    def test1(self):
        driver = self.driver
        f = Funciones2(driver)
        f.saludos()
        t = 2

    def test2(self):
        driver = self.driver
        f = Global2(driver)
        f.Navegar()
        t = 2

    def tearDown(self):
        driver = self.driver
        driver.close()


if __name__ == '__main__':
    unittest.main()
