import time
import traceback

import pytest

from page_objects.add_employee_page import AddCustomer
from page_objects.login_page import Login
from utils.custom_logger import LogGen
from utils.gen_data import GenFakeData
from utils.read_props import ReadConfig


class TestAddEmployee_003:
    baseURL = ReadConfig.get_app_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.log_gen()

    @pytest.mark.sanity
    def test_add_employee(self, setup):
        self.logger.info("********** Starting Add Employee **********")
        driver = setup
        driver.get(self.baseURL)

        lp = Login(driver)
        ac = AddCustomer(driver)

        try:
            self.logger.info("********** Started Login **********")

            lp.set_username(self.username)
            lp.set_password(self.password)
            lp.click_login()

            self.logger.info("********** Completed Login **********")

            ac.click_pin()
            self.logger.info("********** Redirect to PIM **********")

            ac.click_add_employee()

            first_name = GenFakeData.generate_first_name()
            middle_name = GenFakeData.generate_middle_name()
            last_name = GenFakeData.generate_last_name()
            emp_id = GenFakeData.generate_employee_id()

            ac.set_firstname(first_name)
            ac.set_middlename(middle_name)
            ac.set_lastname(last_name)
            ac.set_emp_id(emp_id)
            ac.add_employee()

            time.sleep(10)

            self.logger.info("********** Employee Added Successfully **********")


        except Exception as e:

            self.logger.error(f"Test Add Employee failed: {e}")
            traceback.print_exc()
            assert False

        finally:
            driver.close()
