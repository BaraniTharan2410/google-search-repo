import unittest
from pages.home.home_page import Homepage
from utils.teststatus import TestStatus
from pages.detailpage.detail_page import Detailpage
import pytest

@pytest.mark.usefixtures("oneTimesetUp","setUp")
class HomeTests(unittest.TestCase):

    @pytest.fixture(autouse= True)
    def classSetup(self,oneTimesetUp):
        self.hp = Homepage(self.driver)
        self.ts = TestStatus(self.driver)
        self.dp = Detailpage(self.driver)

    #verify the clear text functionality by triggering X option in google search text box
    @pytest.mark.run(order= 2)
    def test_googlesearchXfunc(self):
        result1 =self.hp.clickXbuttonInSearchTextBox(keyword="amazon")
        self.ts.mark(result1,"google search X func verification")

    #verify the hyperlink texts are present in the home page
    @pytest.mark.run(order= 1)
    def test_assertionCheckinHomePage(self):
        result4 = self.hp.assertionCheckinHomePage()
        self.ts.mark(result4,"Assertion Check test verification")

    #verify results displayed in google getail page is relevant with the keyword given for search
    @pytest.mark.run(order= 3)
    def test_googlesearch(self):
        self.hp.searchTextingoogle(keyword="amazon")
        result = self.hp.checkAmazonLinkInDetailPage()
        self.ts.mark(result,"google search test verification")

    #test to verify About Results text present in detail page
    @pytest.mark.run(order= 4)
    def test_verifyAboutResults(self):
        result2 =self.dp.verifyAboutResults()
        self.ts.mark(result2,"verifyAboutResults verification")

    #verify paginations are available in google detail page
    @pytest.mark.run(order= 5)
    def test_verifypagination(self):
        self.hp.searchTextingoogle(keyword="amazon")
        result5 =self.dp.verifyPageNo()
        self.ts.mark(result5,"verify pagination test verification")