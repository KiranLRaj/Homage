import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Homage_CodeChallenge.PageObjects import OnboardingPageObjects
from Homage_CodeChallenge.test_scripts.conftest import ChromeBrowserSetup

class Test_CodeChallenge:

    def test_codechallenge_TC1(self):
        driver = ChromeBrowserSetup()
        driver.get("https://apply.homage.sg/")
        driver.implicitly_wait(20)
        OnboardingPageObjects.LocationObject(driver).click()
        OnboardingPageObjects.LocationListItem(driver).click()
        OnboardingPageObjects.FirstNameObject(driver).click()
        OnboardingPageObjects.FirstNameObject(driver).clear()
        OnboardingPageObjects.FirstNameObject(driver).send_keys("Peter")
        OnboardingPageObjects.LastNameObject(driver).click()
        OnboardingPageObjects.LastNameObject(driver).send_keys("Parker")
        OnboardingPageObjects.EmailObject(driver).click()
        OnboardingPageObjects.EmailObject(driver).send_keys("petepm@yopmail.com")
        OnboardingPageObjects.PhoneNumObject(driver).click()
        OnboardingPageObjects.PhoneNumObject(driver).send_keys("78798765")
        driver.find_element(By.XPATH, "(// button[text() = 'Yes'])[1]").click()
        driver.find_element(By.XPATH, "(// button[text() = 'Yes'])[2]").click()
        driver.find_element(By.XPATH, "(// button[text() = 'Yes'])[3]").click()
        driver.find_element(By.XPATH, "(// *[text() = '1 to 3'])[1]").click()
        driver.find_element(By.XPATH, "// *[text() = 'Enrolled Nurse (EN)']").click()
        driver.find_element(By.XPATH,"// *[text() = 'Personal care provided in the individual home where the client is living']").click()
        driver.find_element(By.XPATH, "// *[text() = 'Full-Time']").click()
        driver.find_element(By.XPATH, "(// button[text() = 'Yes'])[4]").click()
        driver.find_element(By.XPATH, "// *[text() = 'Select One']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "// *[text() = 'Homage articles'] /.").click()
        driver.find_element(By.XPATH, "// div[@class ='h cpf-checkbox mb-0 '] / i").click()
        driver.find_element(By.XPATH, "// button[text()='Submit Application']").click()

        if len(driver.find_elements(By.XPATH, "//h1[text()='Your application has been submitted!']")) > 0:
            print("Application submitted successfully")
        driver.save_screenshot("TC1.png")
        time.sleep(5)

    def test_codechallenge_TC2(self):
        driver = ChromeBrowserSetup()
        driver.get("https://apply.homage.sg/")
        driver.implicitly_wait(20)
        OnboardingPageObjects.LocationObject(driver).click()
        OnboardingPageObjects.LocationListItem(driver).click()
        OnboardingPageObjects.FirstNameObject(driver).click()
        OnboardingPageObjects.FirstNameObject(driver).clear()
        OnboardingPageObjects.FirstNameObject(driver).send_keys("Peter")
        OnboardingPageObjects.LastNameObject(driver).click()
        OnboardingPageObjects.LastNameObject(driver).send_keys("Parker")
        OnboardingPageObjects.EmailObject(driver).click()
        OnboardingPageObjects.EmailObject(driver).send_keys("pete.p@yopmailc.com")
        OnboardingPageObjects.PhoneNumObject(driver).click()
        OnboardingPageObjects.PhoneNumObject(driver).send_keys("78798765")
        driver.find_element(By.XPATH, "(// button[text() = 'Yes'])[1]").click()
        driver.find_element(By.XPATH, "(// button[text() = 'Yes'])[2]").click()
        driver.find_element(By.XPATH, "(// button[text() = 'Yes'])[3]").click()
        driver.find_element(By.XPATH, "(// *[text() = '1 to 3'])[1]").click()
        driver.find_element(By.XPATH, "// *[text() = 'Enrolled Nurse (EN)']").click()
        driver.find_element(By.XPATH,"// *[text() = 'Personal care provided in the individual home where the client is living']").click()
        driver.find_element(By.XPATH,"//span[text()='Find out more about the different engagement types']/../..").click()
        if len(driver.find_elements(By.XPATH,"//th[text()='Freelance']"))>0:
            print("Freelance Heading validated")
        if len(driver.find_elements(By.XPATH, "//th[text()='Short-Term']")) > 0:
            print("Short Term Heading validated")
        if len(driver.find_elements(By.XPATH,"//th[text()='Full-Time']"))>0:
            print("Full Time Heading validated")
        if len(driver.find_elements(By.XPATH,"//th/b[text()='Employment Period']"))>0:
            print("Employment Period Heading validated")
        if len(driver.find_elements(By.XPATH,"//th/b[text()='Working Hours']"))>0:
            print("Working Hours Heading validated")
        if len(driver.find_elements(By.XPATH,"//th/b[text()='Earnings']"))>0:
            print("Earnings Heading validated")
        if len(driver.find_elements(By.XPATH,"//th/b[text()='Benefits']"))>0:
            print("Benefits Heading validated")
        if len(driver.find_elements(By.XPATH,"//th/b[text()='Income Guarantee']"))>0:
            print("Income Guarantee Heading validated")

    def test_codechallenge_TC3(self):
        driver = ChromeBrowserSetup()
        driver.get("https://apply.homage.sg/")
        driver.implicitly_wait(20)
        OnboardingPageObjects.LocationObject(driver).click()
        OnboardingPageObjects.LocationListItem(driver).click()
        OnboardingPageObjects.FirstNameObject(driver).click()
        OnboardingPageObjects.FirstNameObject(driver).clear()
        OnboardingPageObjects.FirstNameObject(driver).send_keys("Peter")
        OnboardingPageObjects.LastNameObject(driver).click()
        OnboardingPageObjects.LastNameObject(driver).send_keys("Parker")
        OnboardingPageObjects.EmailObject(driver).click()
        OnboardingPageObjects.EmailObject(driver).send_keys("petepm@yopmailc.com")
        OnboardingPageObjects.PhoneNumObject(driver).click()
        OnboardingPageObjects.PhoneNumObject(driver).send_keys("78798765")
        driver.find_element(By.XPATH,"(// button[text() = 'Yes'])[1]").click()
        driver.find_element(By.XPATH, "(// button[text() = 'Yes'])[2]").click()
        driver.find_element(By.XPATH, "(// button[text() = 'Yes'])[3]").click()
        driver.find_element(By.XPATH, "(// *[text() = '1 to 3'])[1]").click()
        driver.find_element(By.XPATH, "// *[text() = 'Enrolled Nurse (EN)']").click()
        driver.find_element(By.XPATH, "// *[text() = 'Personal care provided in the individual home where the client is living']").click()
        driver.find_element(By.XPATH, "// *[text() = 'Full-Time']").click()
        driver.find_element(By.XPATH, "(// button[text() = 'Yes'])[4]").click()
        driver.find_element(By.XPATH, "// *[text() = 'Select One']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "// *[text() = 'Homage articles'] /.").click()
        driver.find_element(By.XPATH, "// div[@class ='h cpf-checkbox mb-0 '] / i").click()
        driver.find_element(By.XPATH, "// button[text()='Submit Application']").click()
        if len(driver.find_elements(By.XPATH,"// *[contains(text(), 'An account with the same email address already exists')]"))>0:
            print("Error message validation successful")
        driver.save_screenshot("TC2.png")











