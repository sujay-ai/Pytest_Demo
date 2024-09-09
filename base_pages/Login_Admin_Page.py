from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Login_Admin_Page:
    textbox_username_xpath = "//input[@name='username']"
    textbox_password_xpath = "//input[@name='password']"
    btn_login_xpath = "//button[@type='submit']"
    dropdown_for_logout_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/p'
    logout_btn_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a'

    def __init__(self, driver):
        self.driver = driver

    def enter_user_name(self, username):
        # self.driver.find_element(By.ID, self.textbox_username_xpath).clear()
        # self.driver.find_element(By.ID, self.textbox_username_xpath).send_keys(username)
        self.driver.implicitly_wait(2)
        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.textbox_username_xpath)))
        element.send_keys(username)

    def enter_password(self, password):
        # self.driver.find_element(By.ID, self.textbox_password_xpath).clear()
        # self.driver.find_element(By.ID, self.textbox_password_xpath).send_keys(password)
        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.textbox_password_xpath)))
        element.send_keys(password)

    def click_login(self):
        # self.driver.find_element(By.XPATH, self.btn_login_xpath).click()
        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.btn_login_xpath)))
        element.click()

    def click_logout(self):
        # # dropdown = WebDriverWait(self.driver, 30).until(
        # #     EC.presence_of_element_located((By.XPATH, self.dropdown_for_logout_xpath)))
        # # dropdown.click()
        # element = WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.XPATH, self.dropdown_for_logout_xpath)))
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).click().perform()
        # logout_button = WebDriverWait(self.driver, 30).until(
        #     EC.presence_of_element_located((By.XPATH, self.logout_btn_xpath)))
        # logout_button.click()
        try:
            # Wait until the close button is visible and clickable
            close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/p'))
            )

            # Click the close button
            close_button.click()

            # Wait until the dropdown logout item is visible and clickable
            logout_item = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a'))
            )

            # Click the logout item
            logout_item.click()

        except Exception as e:
            print(f"An error occurred during logout: {e}")
