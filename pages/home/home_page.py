import logging
from base.basepage import BasePage
import utils.customlogger as cl

class Homepage(BasePage):

    log = cl.consoleLogger(logging.DEBUG)

    def __init__(self, driver):
        super(Homepage,self).__init__(driver)
        self.driver = driver

    ##############
    ###Locators###
    ##############

    __googlesearchtextbox__ = "//*[@class='gLFyf gsfi']"
    __googleSearchButton__ = "//*[@value='Google Search'][1]"
    __amazontext__ = "//*[contains(text(),'Amazon.in')]"
    __xbuttton__="//*[@class='lBbtTb z1asCe rzyADb']"
    __India__  = "//*[contains(text(),'India')]"
    __About__  = "//*[contains(text(),'About')]"
    __Advertising__ = "//*[contains(text(),'Advertising')]"
    __Business__ = "//*[contains(text(),'Business')]"
    __HowSearchworks__  = "//*[contains(text(),'How Search works')]"
    __Privacy__ = "//*[contains(text(),'Privacy')]"
    __Terms__ = "//*[contains(text(),'Terms')]"
    __Settings__ = "//*[contains(text(),'Settings')]"

    def enterTextInGoogleSearch(self, keyword):
        self.enterTextByXpath(self.__googlesearchtextbox__,keyword)

    def pressEnterKeyInGoogleSearch(self):
        self.enterOperationByXpath(self.__googleSearchButton__)

    def searchTextingoogle(self,keyword):
        self.enterTextInGoogleSearch(keyword)
        self.pressEnterKeyInGoogleSearch()

    def checkAmazonLinkInDetailPage(self):
        actualtext = self.getTextByXpath(self.__amazontext__)
        if actualtext == "Amazon.in":
            return True
        else:
            return False
    def clickXbuttonInSearchTextBox(self,keyword):
        self.enterTextInGoogleSearch(keyword)
        self.doubleClickByXpath(self.__xbuttton__)
        actual_text = self.getTextByXpath(self.__googlesearchtextbox__)
        if actual_text == "":
            return True
        else:
            return False
    def assertionCheckinHomePage(self):
        flag = 0
        if "India" == self.__India__:
            flag =1
        if 'About' == self.__About__:
            flag = 1
        if 'Advertising' == self.__Advertising__:
            flag = 1
        if 'Business' == self.__Business__:
            flag = 1
        if 'HowSearchworks' == self.__HowSearchworks__:
            flag = 1
        if 'Privacy' == self.__Privacy__:
            flag = 1
        if 'Terms' == self.__Terms__:
            flag = 1
        if "Settings" == self.__Settings__:
            flag = 1
        if flag == 1:
            return True
        else:
            return False
