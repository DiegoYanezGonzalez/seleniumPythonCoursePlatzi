import unittest
from selenium import webdriver
from time import sleep

class TestingMercadoLibre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')        
        driver = self.driver
        driver.get('https://www.mercadolibre.com')
        driver.maximize_window()

        def test_search_ps4(self):
            driver = self.driver

            country = driver.find_element_by_id('CL')
            country.click()

            search_field = driver.find_element_by_id('as_word')
            search_field.click()
            search_field.clear()
            search_field.send_keys('playstation 4')
            sleep(3)

            location=driver.find_element_by_partial_link_text('RM (Metropolitana)')
            location.click()
            sleep(3)

            condition = driver.find_element_by_partial_link_text('Nuevo)')
            condition.click()
            sleep(3)

            order_menu = driver.find_element_by_class_name('ui-dropdown_link')
            order_menu.click()
            higher_price = driver.find_element_by_css_selector()



            def tearDown(self):
                self.driver.close()

            if __name__ == '__main__':
                unittest.main(verbosity=2)