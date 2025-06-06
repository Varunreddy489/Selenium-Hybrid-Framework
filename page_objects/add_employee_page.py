from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AddCustomer:
    pim_xpath = "//span[normalize-space()='PIM']"

    add_emp_xpath = "//a[normalize-space()='Add Employee']"

    first_name_xpath = "//input[@placeholder='First Name']"
    middle_name_xpath = "//input[@placeholder='Middle Name']"
    last_name_xpath = "//input[@placeholder='Last Name']"
    employee_id_xpath = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"

    save_button_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_pin(self):
        pim = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_xpath)))
        pim.click()

    def click_add_employee(self):
        emp = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.add_emp_xpath)))
        emp.click()

    def set_firstname(self, firstname):
        first_name = self.wait.until(EC.presence_of_element_located((By.XPATH, self.first_name_xpath)))
        first_name.send_keys(firstname)

    def set_middlename(self, middlename):
        middle_name = self.wait.until(EC.presence_of_element_located((By.XPATH, self.middle_name_xpath)))
        middle_name.send_keys(middlename)

    def set_lastname(self, lastname):
        last_name = self.wait.until(EC.presence_of_element_located((By.XPATH, self.last_name_xpath)))
        last_name.send_keys(lastname)

    def set_emp_id(self, empId):
        emp_id = self.wait.until(EC.presence_of_element_located((By.XPATH, self.employee_id_xpath)))
        emp_id.clear()
        emp_id.send_keys(empId)

    def add_employee(self):
        save = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.save_button_xpath)))
        save.click()
 