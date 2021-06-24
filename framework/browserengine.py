"""
@Time    :   19/06/2021
@Author  :   Cai Yaling
@Contact :   caiarlene@gmail.com
"""
import configparser, time, os
from selenium import webdriver
from framework.logger import Logger
from framework.readconfig import ReadConfig

logger = Logger(logger='BrowserEngine').getlog()


class BrowserEngine(object):
    # dir = os.path.dirname(os.path.abspath(''))
    browserwaittime = 0
    url = ''
    browser = ""
    def __init__(self, driver):
        self.driver = driver
        getconfig = ReadConfig()
        self.browserwaittime = int(getconfig.getConfigValue("waitTime","browserwaitTime"))
        self.browser = getconfig.getConfigValue("browserType","browserName")
        self.url = getconfig.getConfigValue('testServer', 'URL')

    def open_browser(self, driver):

        logger.info('You have select %s browser' % self.browser)
        logger.info('Test URL is: %s' % self.url)

        if self.browser == 'Firefox':
            driver = webdriver.Firefox()
            logger.info('Launching Firefox')
        elif self.browser == 'Chrome':
            driver = webdriver.Chrome()
            logger.info('Launching Chrome')
        elif self.browser == 'Edge':
            driver = webdriver.Ie()
            logger.info('Launching Edge')

        driver.get(self.url)
        logger.info('Open %s' % self.url)
        driver.maximize_window()
        logger.info('Maximize browser')
        driver.implicitly_wait(self.browserwaittime)
        return driver

    def quit_browser(self):
        self.driver.quit()
        logger.info('Close browser')

