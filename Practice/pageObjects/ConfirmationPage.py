from selenium.webdriver.common.by import By

class ConfirmationPage:

    def __init__(self, driver):
        self.driver = driver
    

    countryCode = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    countryName = (By.CSS_SELECTOR, "[class*='alert-success']")
    
    def getCountryName(self):
        return self.driver.find_element(*ConfirmationPage.country.click())
    
    def getCheckBox(self):
        return self.driver.find_element(*ConfirmationPage.checkBox.click())
    
    def getCountryText(self):
        return self.driver.find_element(*ConfirmationPage.countryName.tex)
    