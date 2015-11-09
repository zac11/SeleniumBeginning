__author__ = 'rahul'
 
import unittest
from selenium import webdriver
 
 
class MyRadiobtn(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Firefox()
 
    def test_Radiobtn(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('http://openwritings.net/sites/default/files/radio_checkbox.html')
 
 
        eleapple= driver.find_element_by_name('apple')
        elebanana= driver.find_element_by_name('orange')
        if eleapple.is_selected():
            eleapple.click()
            elebanana.click()
 
 
        driver.save_screenshot('location_where_screenshot_is_to_be_saved')
 
    def tearDown(self):
        self.driver.quit()
 
 
 
if __name__ == '__main__':
    unittest.main()
