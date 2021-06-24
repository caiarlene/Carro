"""
@Time    :   20/06/2021
@Author  :   Cai Yaling
@Contact :   caiarlene@gmail.com
"""
import requests
from selenium.webdriver.remote.webelement import WebElement
from urllib3.contrib._securetransport.bindings import Boolean

from framework.basepage import  BasePage

class CarDetailsPage(BasePage):
    car_images = "xpath=>//div[contains(@class,'thumbnails-container')]//img"

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def test_images_for_200_response(self):
        example_images = self.find_elements(self.car_images)

        for image in example_images:
            current_link = image.get_attribute("src")
            res = requests.get(current_link)
            try:
                self.assertEqual(res.status_code, 200)
            except AssertionError as e:
                self.verificationErrors.append(current_link + ' delivered response code of ' + res.status_code)

