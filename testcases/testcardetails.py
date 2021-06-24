"""
@Time    :   21/06/2021
@Author  :   Cai Yaling
@Contact :   caiarlene@gmail.com
"""

import requests
import unittest
from framework.browserengine import BrowserEngine
from pageobjects.buycarpage import BuyCarPage
from pageobjects.cardetailspage  import CarDetailsPage
from framework.logger import Logger

logger = Logger(logger='CardDetails').getlog()

class TestCardDetails(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tc02_images_displayed(self):
        carlist = BuyCarPage(self.driver)
        carlist.clickCar()

        cardetails = CarDetailsPage(self.driver)
        example_images = cardetails.find_elements(cardetails.car_images)
        #  image can be displayed while accessing the image url with 200 response
        for image in example_images:
            current_link = image.get_attribute("src")
            res = requests.get(current_link)
            try:
                self.assertEqual(res.status_code, 200)
                logger.info('Image can be displayed')
            except AssertionError as e:
                self.verificationErrors.append(current_link + ' delivered response code of ' + res.status_code)
                logger.error( '%s delivered response code of %s' % (current_link,res.status_code))

if __name__ == "__main__":
    unittest.main()

