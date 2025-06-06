from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Logout:
    dropdown_xpath = "//p[@class='oxd-userdropdown-name']"
    logout_href = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_dropdown(self):
        profile = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.dropdown_xpath)))
        profile.click()

    def click_logout(self):
        self.click_dropdown()
        logout_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.logout_href)))
        logout_option.click()
