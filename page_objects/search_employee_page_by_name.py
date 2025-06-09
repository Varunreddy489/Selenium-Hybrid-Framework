from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SearchEmployeeByName:
    pim_xpath = "//span[normalize-space()='PIM']"

    search_button_xpath = "//button[normalize-space()='Search']"

    employee_list_xpath = "//a[normalize-space()='Employee List']"

    employee_name_input = "(//div[@class='oxd-autocomplete-text-input oxd-autocomplete-text-input--active']//input)[1]"

    test_emp_id = "//div[@class='oxd-table-cell oxd-padding-cell' and @role='cell']/div"

    search_emp_firstname_xpath = "//div[@class='oxd-table-cell oxd-padding-cell'][3]"

    search_emp_lastname_xpath = "//div[@class='oxd-table-cell oxd-padding-cell'][4]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_pim(self):
        pim = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_xpath)))
        pim.click()

    def redirect_emp_list(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.employee_list_xpath))).click()

    def set_employee_name(self, name):
        emp_name = self.wait.until(EC.presence_of_element_located((By.XPATH, self.employee_name_input)))
        emp_name.send_keys(name)

    def search_button(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.search_button_xpath))).click()

    def search_emp_text(self):
        firstname = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, self.search_emp_firstname_xpath)))

        lastname = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, self.search_emp_lastname_xpath)))

        name = firstname.text + " " + lastname.text

        return name
