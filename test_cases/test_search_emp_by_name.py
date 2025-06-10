import time

import pytest
from selenium.common import TimeoutException

from page_objects.login_page import Login
from page_objects.search_employee_page_by_name import SearchEmployeeByName
from utils.custom_logger import LogGen
from utils.csv_report_gen import create_report
from utils.read_props import ReadConfig


@pytest.mark.regression
class TestSearchEmployee_005:
    baseURL = ReadConfig.get_app_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.log_gen()

    search_emp_name = "Charles Carter"

    @pytest.mark.regression
    def test_search_emp(self, setup):
        self.logger.info("********** Starting Search Employee By Name **********")
        driver = setup
        driver.get(self.baseURL)

        lp = Login(driver)
        se = SearchEmployeeByName(driver)
        test_status = "Failed"
        test_result = ""

        try:
            self.logger.info("********** Started Login **********")
            lp.set_username(self.username)
            lp.set_password(self.password)
            lp.click_login()
            self.logger.info("********** Completed Login **********")

            se.click_pim()
            se.redirect_emp_list()
            se.set_employee_name(self.search_emp_name)
            se.search_button()
            time.sleep(5)

            test_result = se.search_emp_text()

            if test_result == self.search_emp_name:
                test_status = "Passed"
                self.logger.info(
                    "********** Completed Search Employee By Name **********"
                )
            else:
                self.logger.error(
                    f"Search Employee By Name failed. Expected: {self.search_emp_name}, Found: {test_result}"
                )

            assert test_result == self.search_emp_name

        except TimeoutException:
            test_result = "Employee not found"
            self.logger.error(
                f"Timeout while searching for employee: {self.search_emp_name}"
            )
        except Exception as e:
            test_result = f"Error: {str(e)}"
            self.logger.error(f"Test Search Employee failed: {e}")
        finally:
            # Take screenshot if test failed
            if test_status == "Failed":
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                screenshot_path = f"C:\\Users\\varun\\OneDrive\\Desktop\\GE\\WEB AUTOMATION\\orange_hrm\\screenshots\\test_search_emp_name_{timestamp}.png"
                driver.save_screenshot(screenshot_path)

            # Always create the report
            create_report(
                self.__class__.__name__,
                f"Search for {self.search_emp_name} - {test_result}",
                test_status,
            )
            driver.close()
