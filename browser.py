from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Browser:
    def __init__(self, driver):
        self.driver = driver
    
    def open(self, url):
        self.driver.get(url)

    def find_element(self, selector):
        if selector.startswith('.'):
            return self.driver.find_element_by_class_name(selector[1:])
        elif selector.startswith('#'):
            return self.driver.find_element_by_id(selector[1:])
        elif selector.contains('/'):
            return self.driver.find_element_by_xpath(selector)
        else:
            return self.driver.find_element_by_tag_name(selector)

    def find_elements(self, selector):
        if selector.startswith('.'):
            return self.driver.find_elements_by_class_name(selector[1:])
        elif selector.startswith('#'):
            return self.driver.find_elements_by_id(selector[1:])
        elif selector.contains('/'):
            return self.driver.find_elements_by_xpath(selector)
        else:
            return self.driver.find_elements_by_tag_name(selector)

    def click(self, selector):
        self.find_element(selector).click()
                
    def type(self, selector, content):
        self.find_element(selector).send_keys(content) 

    def wait_until_presence(self, selector, timeout):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(self.get_locator(selector)))
    
    def screenshot(self, fullname):
        self.driver.save_screenshot(fullname)

    def get_locator(self, selector):
        if selector.startsWith('.'):
            return (By.CLASS_NAME, selector[1:])
        elif selector.startsWith('#'):
            return (By.ID, selector[1:])
        elif selector.contains('/'):
            return (By.XPATH, selector)
        else:
            return (By.TAG_NAME, selector)

    def close(self):
        self.driver.close()
    
class Firefox(Browser):
    def __init__(self, driverPath):
        Browser.__init__(self, webdriver.Firefox(executable_path=driverPath))

class Chrome(Browser):
    def __init__(self, driverPath):
        Browser.__init__(self, webdriver.Chrome(executable_path=driverPath))