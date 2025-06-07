import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.login_page import Login
from page_objects.logout import Logout
from utils import excel_utils
from utils.custom_logger import LogGen
from utils.read_props import ReadConfig


class Test_DDT_Login_002:
    baseUrl = ReadConfig.get_app_url()
    data_path = r"C:\Users\varun\OneDrive\Desktop\GE\WEB AUTOMATION\orange_hrm\test_data\login_data.xlsx"
    logger = LogGen.log_gen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):

        self.logger.info("------- Test_002_DDT_Login------")
        self.logger.info("********* Verifying Login DDT test *******")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)

        self.lp = Login(self.driver)
        self.lg = Logout(self.driver)

        self.lst_status = []

        self.confirm_ele = "//p[normalize-space()='My Actions']"

        self.rows = excel_utils.get_row_count(self.data_path, 'Sheet1')
        print("Number of rows:", self.rows)
        list_status = []

        for r in range(2, self.rows + 1):
            self.username = excel_utils.read_data(self.data_path, 'Sheet1', r, 1)
            self.password = excel_utils.read_data(self.data_path, 'Sheet1', r, 2)

            self.expectedResult = excel_utils.read_data(self.data_path, 'Sheet1', r, 3)

            print(
                f"Row {r}: Username: {self.username}, Password: {self.password}, Expected Result: {self.expectedResult}")

            self.lp.set_username(self.username)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(5)
            print(
                f" Successfully Passed: Username: {self.username}, Password: {self.password}, Expected Result: {self.expectedResult}")
            self.logger.info("********* Logged in Successfully *******")

            try:

                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='My Actions']"))
                )
                login_successful = True
            except:
                login_successful = False

            # if login_successful:
            #     if self.expectedResult == "Pass":
            #         self.logger.info(f"Row {r}: Login Passed as expected.")
            #         self.lg.click_logout()
            #         self.lst_status.append("Pass")
            #     else:
            #         self.logger.info(f"Row {r}: Login Failed but was expected to fail.")
            #         self.lg.click_logout()
            #         self.lst_status.append("Fail")
            # else:
            #     if self.expectedResult == "Pass":
            #         self.logger.info(f"Row {r}: Login Failed unexpectedly.")
            #         self.lst_status.append("Fail")
            #     else:
            #         self.logger.info(f"Row {r}: Login Failed as expected.")
            #         self.lst_status.append("Pass")

            if login_successful and self.expectedResult == "Pass":
                self.logger.info(f"Row {r}: Login Passed as expected.")
                self.lg.click_logout()
                self.lst_status.append("Pass")

            elif not login_successful and self.expectedResult == "Fail":
                self.logger.info(f"Row {r}: Login Failed as expected.")
                self.lst_status.append("Pass")

            else:
                self.logger.info(
                    f"Row {r}: Test Failed. Expected: {self.expectedResult}, but got: {'Pass' if login_successful else 'Fail'}")
                self.lst_status.append("Fail")
                if login_successful:
                    self.lg.click_logout()

        print("List Status:", self.lst_status)

        if "Fail" not in self.lst_status:
            self.logger.info("***** Login DDT test passed *****")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** Login DDT test failed ******")
            self.driver.close()
            assert False
        self.logger.info("***** End of Login DDT Test *******")
        self.logger.info("***** Completed TC_LoginDDT_002 ******")
