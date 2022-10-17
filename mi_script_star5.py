from codecs import unicode_escape_decode
from http.server import executable
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class ProductList(unittest.TestCase): 
     
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = '/home/thunder/test-Kemok/chromedriver_linux64/chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)

    @classmethod
    def test_hello_world(cls):
        driver = cls.driver
        driver.get('https://webscraper.io/test-sites/e-commerce/static/computers/laptops')



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output = 'reportes', report_name = 'Produc-list-5start'))
    
    
    