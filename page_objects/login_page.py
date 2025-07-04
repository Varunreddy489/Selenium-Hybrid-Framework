from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login:
    textbox_username_xpath = "//input[@name='username']"
    textbox_password_xpath = "//input[@name='password']"
    button_login_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_username(self, username):
        user_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.textbox_username_xpath)))
        user_field.clear()
        user_field.send_keys(username)

    def set_password(self, password):
        pass_field = (self.driver.find_element(By.XPATH, self.textbox_password_xpath))
        pass_field.clear()
        pass_field.send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
