"""
@Time    :   21/06/2021
@Author  :   Cai Yaling
@Contact :   caiarlene@gmail.com
"""

import unittest
from framework.browserengine import BrowserEngine
from pageobjects.buycarpage import BuyCarPage
from framework.logger import Logger

logger = Logger(logger='CarFilter').getlog()

class TestCarFilter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tc01_filter_car_by_brand_and_price(self):
        carlist = BuyCarPage(self.driver)
        carlist.filterBMW()
        brand_titile = carlist.find_element(carlist.brand_BMW).text
        filter = carlist.find_element(carlist.filter_BMW)
        try:
            self.assertEqual(brand_titile, filter.text)
            logger.info("Filter BMW exists")
        except AssertionError as e:
            logger.error("Filter BMW doesn\'t exist")

        car_title_list = carlist.find_elements(carlist.car_title)
        for car in car_title_list:
            filter_result = brand_titile in car.text
            try:
                self.assertTrue(str(filter_result) == 'True')
                logger.info("The car matches the brand")
            except AssertionError as e:
                logger.error("The car doesn\'t match the brand")

        carlist.filterPrice()
        price_locator_list = carlist.find_elements(carlist.price_locater)
        for price_locator in price_locator_list:
            price = price_locator.text
            price = price[3:].replace(',', '')

            if int(price) > int(carlist.from_price) and int(price) < int(carlist.to_price):
                logger.info("Car price is in the range")
            else:
                logger.info("Car price is out of the range")


if __name__ == "__main__":
    unittest.main()

