"""
@Time    :   20/06/2021
@Author  :   Cai Yaling
@Contact :   caiarlene@gmail.com
"""
from selenium.webdriver.support.ui import WebDriverWait
from framework.basepage import  BasePage
from framework.logger import Logger

logger = Logger(logger='BuyCarPage').getlog()

class BuyCarPage(BasePage):
    car = "xpath=>((//div[contains(@class,'HitCard__StyledCard')])[1]//img)[1]"
    car_brand = "xpath=>//div[contains(text(),'BRANDS')]"
    car_price_range = "xpath=>//div[contains(text(),'PRICE RANGE')]"
    brand_BMW = "xpath=>//div[text()='BMW']"
    filter_BMW = "xpath=>//span[contains( @class ,'ant-tag ant-tag-cyan')]"
    from_price_selector = "xpath=>(//div[contains(@class,'ant-collapse-item-active')]//input[@type='search'])[3]"
    to_price_selector = "xpath=>(//div[contains(@class,'ant-collapse-item-active')]//input[@type='search'])[4]"
    option_prefix = "xpath=>(//div[contains(text(),'"
    option_suffix = "')])[1]"
    next_page_btn_disabled = "xpath=>//li[@title='Next Page']/button"
    car_title = "xpath=>//div[contains(@class,'HitCard__StyledTitle')]/a"
    price_locater = "xpath=>//div[@class='price']"
    from_price = "40000"
    to_price = "100000"
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def clickCar(self):
       self.click(self.car)

    def filterBMW(self):
        self.click(self.car_brand)

        self.click(self.brand_BMW)
    def filterPrice(self):
        self.click(self.car_price_range)
        #from_price = self.get_config("priceRange","from")
        #to_price = self.get_config("priceRange","to")
        self.type(self.from_price_selector, self.from_price)
        from_price_option = list(self.from_price)
        from_price_option.insert(-3,',')
        from_price_k= ''.join(from_price_option)
        from_price_option = self.option_prefix + from_price_k + self.option_suffix
        self.click(from_price_option)
        self.type(self.to_price_selector, self.to_price)
        to_price_option = list(self.to_price)
        to_price_option.insert(-3,',')
        to_price_k = ''.join(to_price_option)
        to_price_option = self.option_prefix + to_price_k + self.option_suffix
        self.click(to_price_option)


