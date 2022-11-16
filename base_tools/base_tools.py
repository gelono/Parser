from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime


class BaseTools:
    def __init__(self, driver):
        self.driver = driver

    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=1):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=1):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def action_drag_and_drop_by_offset(self, element, x_coords, y_coords):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
        action.perform()

    def action_drag_and_drop_to_element(self, what, where):
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()

    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementsById('close-fixedban').remove();")

    def datetime_format(self, string):
        string = string.split()
        month_dict = {
            'січ': 1,
            'лют': 2,
            'бер': 3,
            'квіт': 4,
            'трав': 5,
            'черв': 6,
            'лип': 7,
            'серп': 8,
            'верес': 9,
            'жовт': 10,
            'лист': 11,
            'груд': 12,
        }
        for month in month_dict:
            if string[1].lower().find(month) != -1:
                string[1] = str(month_dict[month])

        string = string[0] + '.' + string[1] + '.' + string[2]
        date_formatter = '%d.%m.%Y'
        date = datetime.strptime(string, date_formatter)
        date = date.date()
        return date


class Driver:

    def __init__(self, url):
        self.url = url

    def driver_setup(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(self.url)
        #driver.quit()
        return driver

    def loop_driver(self, loop_url):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(loop_url)
        #driver.quit()
        return driver