import time

import pytest

from page_objects.login_page import Login
from page_objects.search_employee_page import SearchEmployee
from utils.custom_logger import LogGen
from utils.read_props import ReadConfig


class TestSearchEmployee_004:
    baseURL = ReadConfig.get_app_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.log_gen()

    @pytest.mark.regression
    def test_search_emp(self, setup):
        self.logger.info("********** Starting Add Employee **********")
        driver = setup
        driver.get(self.baseURL)

        lp = Login(driver)
        se = SearchEmployee(driver)

        try:
            self.logger.info("********** Started Login **********")

            lp.set_username(self.username)
            lp.set_password(self.password)
            lp.click_login()

            self.logger.info("********** Completed Login **********")

            se.click_pim()
            se.redirect_emp_list()

            # se.set_employee_name("Emily Jones")
            se.set_employee_id("0295")
            se.search_button()

            time.sleep(5)

            test = se.search_emp_text("0295")
            print("scdascdsddnvv", test)

            assert test == "0295"


        except Exception as e:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_path = f"C:\\Users\\varun\\OneDrive\\Desktop\\GE\\WEB AUTOMATION\\orange_hrm\\screenshots\\test_homepage_{timestamp}.png"
            time.sleep(3)
            driver.save_screenshot(screenshot_path)
            self.logger.error(f"Test Search Employee failed: {e}")
            # traceback.print_exc()
            assert False

        finally:
            driver.close()
