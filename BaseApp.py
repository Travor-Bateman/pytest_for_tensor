from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.actual_url = driver.current_url

    def go_to_site(self, new_url):
        return self.driver.get(new_url)

    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def wait_change_url(self, time=30):
        return WebDriverWait(self.driver, time).until(EC.url_changes(self.driver.current_url),
                                                      message="Url not changes")

    def wait_text_in_element(self, locator, text, time=30):
        return WebDriverWait(self.driver, time).until(EC.text_to_be_present_in_element(locator, text),
                                                      message=f"Text not changes by locator {locator}")

    def wait_visible_elements(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                      message=f"Element not visible by locator {locator}")