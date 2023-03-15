import unittest
import warnings
from appium import webdriver
from Funciones.Funciones import Funciones2

tg = 3


class base_test(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore', DeprecationWarning)
        d = {
            "platformName": "Android",
            "appium:platformVersion": "11",
            "appium:deviceName": "generic_x86",
            "appium:automationName": "UiAutomator2"
        }
        self.driver = webdriver.Remote('C:\Users\2554184\Downloads\chromedriver.exe', d)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
