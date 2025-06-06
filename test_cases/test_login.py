import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from page_objects.login_page import Login
from utils.custom_logger import LogGen
from utils.read_props import ReadConfig


class TestLogin_001:
    # baseURL = os.getenv("BASE_URL")
    # username = os.getenv("USERNAME")
    # password = os.getenv("PASSWORD")

    baseURL = ReadConfig.get_app_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.log_gen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepage_title(self, setup):
        self.logger.info("********** Starting test_homepage_title **********")
        driver = setup
        driver.get(self.baseURL)

        try:
            act_title = driver.title
            assert act_title == "OrangeHRM", f"Expected 'OrangeHRM' but got '{act_title}'"
            self.logger.info("Homepage title matched.")
        except Exception as e:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_path = f"C:\\Users\\varun\\OneDrive\\Desktop\\GE\\WEB AUTOMATION\\nopcommerce\\screenshots\\test_login_{timestamp}.png"

            time.sleep(3)
            driver.save_screenshot(screenshot_path)
            self.logger.error(f"Homepage title test failed: {e}")
            raise
        finally:
            driver.close()

    def test_login(self, setup):
        self.logger.info("********** Starting Login test **********")
        driver = setup
        driver.get(self.baseURL)
        lp = Login(driver)

        self.confirm_ele = "//p[normalize-space()='My Actions']"

        try:
            lp.set_username(self.username)
            lp.set_password(self.password)
            lp.click_login()

            confirm = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.confirm_ele)))

            assert confirm.text == "My Actions", "Element not detected"
            self.logger.info("Login successful. Element detected")

        except Exception as e:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_path = f"C:\\Users\\varun\\OneDrive\\Desktop\\GE\\WEB AUTOMATION\\nopcommerce\\screenshots\\test_homepage_{timestamp}.png"
            time.sleep(3)
            driver.save_screenshot(screenshot_path)
            self.logger.error(f"Login test failed: {e}")
            assert False
        finally:
            driver.close()
