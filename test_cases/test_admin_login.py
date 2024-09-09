import pytest
import os,shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker


class Test_01_Admin_Login:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger = Log_Maker.log_gen()
    # def test_clear_screenshot_folder(self):
    #     filepath = '.\\screenshots\\'
    #     # try:
    #     #     #os.chmod(filepath, 0o777)
    #     #     os.chmod('.\\screenshots', stat.S_IWRITE)
    #     #     os.remove(filepath)
    #     #     print(f"{filepath} deleted succssfully")
    #     # except OSError as e:
    #     #     print(f"error deleting {filepath}: {e}")
    #     screenshot_folder = '.\\screenshots\\'
    #     try:
    #         shutil.rmtree(screenshot_folder)
    #     except Exception as e:
    #         print(f"Error deleting {screenshot_folder}: {e}")


    def test_title_verification(self,setup):
        self.logger.info("****************************Test_01_Admin_Login********************************")
        self.logger.info("**************************Verification of admin login page title********************************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        actual_title = self.driver.title
        exp_title = "OrangeHRM"
        if actual_title == exp_title:
            assert True
            self.logger.info("****************************Test_Title_Match********************************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.driver.close()
            assert False

    def test_valid_admin_login(self,setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_user_name(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        exp_dashboard_text = "Dashboard"
        act_dashboard_text = self.driver.find_element(By.XPATH,"//h6").text
        self.driver.implicitly_wait(20)
        # act_dashboard_text = WebDriverWait(webdriver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='content-header']/h1"))).text
        if act_dashboard_text == exp_dashboard_text:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.driver.close()
            assert False

    def test_invalid_admin_login(self,setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_user_name(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        exp_error_text = "Invalid credentials"
        act_error_text = self.driver.find_element(By.XPATH,"//p").text
        if act_error_text == exp_error_text:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.driver.close()
            assert False


