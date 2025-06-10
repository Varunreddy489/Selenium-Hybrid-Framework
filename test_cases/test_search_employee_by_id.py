import time

import pytest
from selenium.common.exceptions import TimeoutException

from page_objects.login_page import Login
from page_objects.search_employee_page_by_id import SearchEmployeeById
from utils.custom_logger import LogGen
from utils.csv_report_gen import create_report
from utils.read_props import ReadConfig


class TestSearchEmployee_004:
    baseURL = ReadConfig.get_app_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.log_gen()

    emp_id = "0377"

    @pytest.mark.regression
    def test_search_emp(self, setup):
        self.logger.info("********** Starting Search Employee By ID **********")
        driver = setup
        driver.get(self.baseURL)

        lp = Login(driver)
        se = SearchEmployeeById(driver)

        test_status = "Failed"
        test_result = "Not executed"
        test_details = f"Search for employee ID: {self.emp_id}"

        try:
            self.logger.info("********** Started Login **********")
            lp.set_username(self.username)
            lp.set_password(self.password)
            lp.click_login()
            self.logger.info("********** Completed Login **********")

            se.click_pim()
            se.redirect_emp_list()

            se.set_employee_id(self.emp_id)
            se.search_button()

            time.sleep(2)

            test_result = se.search_emp_text(self.emp_id)

            if test_result == self.emp_id:
                test_status = "Passed"
                test_details = f"Successfully found employee ID: {self.emp_id}"
                self.logger.info(f"Employee found: {test_result}")
            else:
                test_details = f"Expected ID: {self.emp_id}, Found: {test_result}"
                self.logger.error(test_details)

            assert test_result == self.emp_id

        except TimeoutException as te:
            test_result = f"Timeout waiting for element: {str(te)}"
            self.logger.error(test_result)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_path = f"C:\\Users\\varun\\OneDrive\\Desktop\\GE\\WEB AUTOMATION\\orange_hrm\\screenshots\\test_by_id_{timestamp}.png"
            driver.save_screenshot(screenshot_path)

        except Exception as e:
            test_result = f"Error occurred: {str(e)}"
            self.logger.error(test_result)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_path = f"C:\\Users\\varun\\OneDrive\\Desktop\\GE\\WEB AUTOMATION\\orange_hrm\\screenshots\\test_by_id_{timestamp}.png"
            driver.save_screenshot(screenshot_path)

        finally:
            create_report(
                self.__class__.__name__,
                test_details,
                test_status
            )
            self.logger.info(f"Test status: {test_status}, Result: {test_result}")
            driver.close()
