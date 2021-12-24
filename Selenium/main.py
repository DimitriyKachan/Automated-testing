from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager


class Driver(object):
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def delete_row(self, name):
        href = self.driver.find_element_by_link_text(name).get_attribute("href")
        el_id = href.split("=")[1]
        self.driver.find_element_by_id("ohrmList_chkSelectRecord_" + el_id).click()
        self.driver.find_element_by_id("btnDelete").click()
        self.driver.find_element_by_id("dialogDeleteBtn").click()

    def check_existence(self, name):
        try:
            self.driver.find_element_by_link_text(name)
        except NoSuchElementException:
            print("Element does not exist")
            return False
        print("Element exists")
        return True

    def login(self, link):
        a = self.driver.current_window_handle
        self.driver.get(link)
        g = self.driver.window_handles
        for f in g:
            if f != a:
                self.driver.switch_to.window(f)
        self.driver.find_element_by_id("divUsername").find_element_by_id("txtUsername").send_keys("Admin", Keys.TAB,
                                                                                                  "admin123",
                                                                                                  Keys.ENTER)

    def go_to_PayGrades(self):
        self.driver.find_element_by_id("menu_admin_viewAdminModule").click()
        self.driver.find_element_by_id("menu_admin_Job").click()
        self.driver.find_element_by_id("menu_admin_viewPayGrades").click()

    def add_paygrade(self, name, curr, min_ammount, max_ammount):
        self.driver.find_element_by_id("btnAdd").click()

        self.driver.find_element_by_id("payGrade_name").send_keys(name)
        self.driver.find_element_by_id("btnSave").click()

        self.driver.find_element_by_id("btnAddCurrency").click()

        self.driver.find_element_by_id("payGradeCurrency_currencyName").send_keys(curr, Keys.TAB, min_ammount,
                                                                                  Keys.TAB, max_ammount)
        self.driver.find_element_by_id("btnSaveCurrency").click()

    def execute(self, link, name, curr, min_ammount, max_ammount):
        self.login(link)
        self.go_to_PayGrades()
        self.add_paygrade(name, curr, min_ammount, max_ammount)
        self.go_to_PayGrades()
        self.check_existence(name)
        self.delete_row(name)
        self.check_existence(name)
        self.driver.quit()


#####################################################################################################################

"""
drive = Driver()
drive.execute("https://opensource-demo.orangehrmlive.com/", "Smith", "CAD - Canadian Dollar", "1500", "3000")"""
