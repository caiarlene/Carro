import os
import time
import unittest
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
from testcases.testcardetails import TestCardDetails
from testcases.testcarfilter import TestCarFilter

if __name__ == "__main__":
    testlist = unittest.TestSuite()
    testlist.addTest(TestCarFilter("tc01_filter_car_by_brand_and_price"))
    testlist.addTest(TestCardDetails("tc02_images_displayed"))
    now = time.strftime("%Y%m%d_%H%M%S")
    fp = open("./testreports/"+now+" test result.html", 'w')
    runner = HTMLTestRunner(stream=fp, title='Automation test report', description='case execution status')
    runner.run(testlist)
    fp.close()