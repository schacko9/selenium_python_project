import pytest
import allure
from Framework.testData.HomePageData import HomePageData
from Framework.pageObjects.HomePage import HomePage
from Framework.utilities.BaseTest import BaseTest


class TestHomePage(BaseTest):

    @pytest.mark.regression
    def test_form_submission(self, get_data):
        self.home = HomePage(self.driver)
        self.home.get_home()
        self.home.expects()
        self.home.get_name(get_data["Name"])
        self.home.get_email(get_data["Email"])
        self.home.get_password(get_data["Password"])
        self.home.get_checkbox()
        self.home.get_gender(get_data["Gender"])
        self.home.get_employment(get_data["Employment"])
        self.home.get_dob(get_data["DOB"])
        self.home.get_submit()

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.sample_data)
    def get_data(self, request):
        return request.param

