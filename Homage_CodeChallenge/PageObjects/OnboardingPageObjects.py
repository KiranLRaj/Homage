from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Homage_CodeChallenge.test_scripts.conftest import ChromeBrowserSetup

# Create all the objects and return them to calling function

def LocationObject(driver):
    LocationElement = driver.find_element(By.XPATH, "//div[@id='location']")
    return LocationElement

def LocationListItem(driver):
    LocationListItem = driver.find_element(By.XPATH, "//li[@role='option']")
    return LocationListItem

def FirstNameObject(driver):
    FirstName=driver.find_element(By.XPATH, "//input[@id='firstName']")
    return FirstName

def LastNameObject(driver):
    LastName=driver.find_element(By.XPATH, "//input[@id='lastName']")
    return LastName

def EmailObject(driver):
    Email=driver.find_element(By.XPATH, "// input[ @ id = 'email']")
    return Email

def PhoneNumObject(driver):
    PhoneNum=driver.find_element(By.XPATH, "// input[ @ id = 'phone']")
    return PhoneNum






