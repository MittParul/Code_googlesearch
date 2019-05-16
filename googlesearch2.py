import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait


class MyTestCase(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/aarviaditya/Desktop/Testing/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_1(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Automation")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name('btnK').click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Automation - Google Search")

    def test_search_2(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Canadian All Care College")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name('btnK').click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Canadian All Care College - Google Search")
    @ classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/aarviaditya/Desktop/Testing/HTML_Python"),verbosity=2)
