import time

from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities import excel_utils
from utilities.custom_logger import Log_Maker
from utilities.read_properties import Read_Config


class Test_02_Admin_Login_Data_Driven:
    admin_page_url = Read_Config.get_admin_page_url()
    logger = Log_Maker.log_gen()
    path = './/test_data//admin_login_data.xlsx'
    status_list = []

    def test_valid_admin_login_data_driven(self, setup):
        self.logger.info("********************test valid admin login data driven started ************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)

        self.rows = excel_utils.get_row_count(self.path, "Sheet1")
        print("number of rows", self.rows)

        for r in range(2, self.rows+1):
            self.username = excel_utils.read_data(self.path, "Sheet1", r, 1)
            self.password = excel_utils.read_data(self.path, "Sheet1", r, 2)
            self.exp_login_status = excel_utils.read_data(self.path, "Sheet1", r, 3)
            self.admin_lp.enter_user_name(self.username)
            self.admin_lp.enter_password(self.password)
            self.admin_lp.click_login()
            time.sleep(5)
            exp_dashboard_text = "OrangeHRM"
            act_dashboard_text = self.driver.title
            self.driver.implicitly_wait(20)

            if act_dashboard_text == exp_dashboard_text:
                if self.exp_login_status == "Yes":
                    self.logger.info("test data is passed")
                    self.status_list.append("Pass")
                    self.admin_lp.click_logout()

                elif self.exp_login_status == "No":
                    self.logger.info("test data has passed,it should not have logged in ")
                    self.status_list.append("Fail")
                    self.admin_lp.click_logout()

            elif act_dashboard_text != exp_dashboard_text:
                if self.exp_login_status == "Yes":
                    self.logger.info("the data is fail")
                    self.status_list.append("Fail")

                elif self.exp_login_status == "No":
                    self.status_list.append("Pass")
        print("Status list is", self.status_list)

        if "Fail" in self.status_list:
            self.logger.info("the test case has failed for one or more data sets")
            assert False
        else:
            self.logger.info("the test case has passed fro all the data")
            assert True
