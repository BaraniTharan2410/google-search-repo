import logging
from base.basepage import BasePage
import utils.customlogger as cl

class Detailpage(BasePage):

    log = cl.consoleLogger(logging.DEBUG)

    def __init__(self, driver):
        super(Detailpage,self).__init__(driver)
        self.driver = driver

    ##############
    ###Locators###
    ##############

    __aboutresults__ = "//*[@id='result-stats']  "
    __pagination__ = "//*[contains(text(),'Page navigation')]//following::td"
    def verifyAboutResults(self):
        txt = self.getTextByXpath(self.__aboutresults__)
        import re
        arr = re.split('About',txt)
        print(arr)
        if "results" and "seconds" in arr[1]:
            return True
        else:
            return False

    def verifyPageNo(self):
        self.scrollToElementByXpath(self.__pagination__)
        pages= self.isElementPresentByXpath(self.__pagination__)
        if pages:
            return True
        else:
            return False
