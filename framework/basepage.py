"""
@Time    :   1i/06/2021
@Author  :   Cai Yaling
@Contact :   caiarlene@gmail.com
"""
import configparser
import time
import os.path

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from framework.logger import Logger
from selenium.common.exceptions import NoSuchElementException

from framework.readconfig import ReadConfig

logger = Logger(logger='BasePage').getlog()


class BasePage(object):
    waittime = 0
    # init driver
    def __init__(self, driver):
        self.driver = driver
        getconfig = ReadConfig()
        self.waittime = int(getconfig.getConfigValue("waitTime","elewaitTime"))

    # Get config and return values
    def get_config(self,section,key):
        config_get = self.config.get(section, key)
        return  config_get

    # set implicitly wait time
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("Set implicitly wait time as：%d s." % seconds)

    def get_window_img(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '/Carro_Pytho/images/'  # set screenshot saving path
        timeset = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))  # format time
        pic_name = file_path + timeset + '.png'  # define screenshot name
        try:
            self.driver.get_screenshot_as_file(pic_name)
            logger.info('Take screenshot successfully, saving to path：/Carro_Pytho/images.')
        except Exception as e:
            logger.error('', format(e))
            self.get_window_img()

    # locate element
    def find_element(self, selector):

        element = ''
        if '=>' not in selector:

            return WebDriverWait(self.driver,self.waittime).until(EC.presence_of_element_located((By.ID, selector)))
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == 'i' or selector_by == 'id':
            try:
                element = WebDriverWait(self.driver,self.waittime).until(EC.presence_of_element_located((By.ID, selector_value)))
                logger.info("Located the element as：%s is：%s" % (selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("No element found, throw exception：%s" % e)
                self.get_window_img()
        elif selector_by == 'n' or selector_by == 'name':
            element = WebDriverWait(self.driver,self.waittime).until(EC.presence_of_element_located((By.NAME, selector_value)))
        elif selector_by == 'c' or selector_by == 'class_name':
            element = WebDriverWait(self.driver,self.waittime).until(EC.presence_of_element_located((By.CLASS_NAME, selector_value)))
        elif selector_by == 'l' or selector_by == 'link_text':
            element = WebDriverWait(self.driver,self.waittime).until(EC.presence_of_element_located((By.LINK_TEXT, selector_value)))
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            element = WebDriverWait(self.driver,self.waittime).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, selector_value)))
        elif selector_by == 't' or selector_by == 'tag_name':
            element = WebDriverWait(self.driver,self.waittime).until(EC.presence_of_element_located((By.TAG_NAME, selector_value)))
        elif selector_by == 'x' or selector_by == 'xpath':
            try:
                element = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, selector_value)))
                logger.info("Located the element as：%s is：%s" % (selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("No element found, throw exception：%s" % e)
                self.get_window_img()
        elif selector_by == 'c' or selector_by == 'css_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please in put correct type of element.")
        return element  # return element

    # locate elements
    def find_elements(self, selector):

        elements = ''
        if '=>' not in selector:
            return self.driver.find_elements_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == 'i' or selector_by == 'id':
            try:
                elements = WebDriverWait(self.driver,self.waittime).until(EC.presence_of_all_elements_located((By.ID, selector_value)))
                logger.info("Located the element as：%s is：%s" % (selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("No element found, throw exception：%s" % e)
                self.get_window_img()
        elif selector_by == 'n' or selector_by == 'name':
            elements = WebDriverWait(self.driver,self.waittime).until(EC.presence_of_all_elements_located((By.NAME, selector_value)))
        elif selector_by == 'c' or selector_by == 'class_name':
            elements = WebDriverWait(self.driver,self.waittime).until(EC.presence_of_all_elements_located((By.CLASS_NAME, selector_value)))
        elif selector_by == 'l' or selector_by == 'link_text':
            elements = WebDriverWait(self.driver,self.waittime).until(EC.presence_of_all_elements_located((By.LINK_TEXT, selector_value)))
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            elements = WebDriverWait(self.driver,self.waittime).until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, selector_value)))
        elif selector_by == 't' or selector_by == 'tag_name':
            elements = WebDriverWait(self.driver,self.waittime).until(EC.presence_of_all_elements_located((By.TAG_NAME, selector_value)))
        elif selector_by == 'x' or selector_by == 'xpath':
            try:
                elements = WebDriverWait(self.driver,self.waittime).until(EC.presence_of_all_elements_located((By.XPATH, selector_value)))
                logger.info("Located the element as：%s is：%s" % (selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("No element found, throw exception：%s" % e)
                self.get_window_img()
        elif selector_by == 'c' or selector_by == 'css_selector':
            elements = WebDriverWait(self.driver,self.waittime).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector_value)))
        else:
            raise NameError("Please in put correct type of element.")
        return elements  # return element

    # Click on element
    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("Done with click element ")
        except NameError as e:
            logger.error("Click action failed, throw exception：%s" % e)

    #input value
    def type(self, selector, text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Input value is：%s" % text)
        except NameError as e:
            logger.error("Input value gets error and throw exception ：%s" % e)

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep time is：%s s" % seconds)

