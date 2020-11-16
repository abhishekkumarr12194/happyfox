import time

from selenium.webdriver.common.by import By
from PageObject.PrioritiesPage import PrioritiesPage


class StatusPage:
    def __init__(self,driver):
        self.driver=driver

    # All elements on Status Page management window are Listed here
    Create_Button= (By.CSS_SELECTOR,"button[class*='create']")
    Status_Name=(By.CSS_SELECTOR,"input[aria-label='Status Name']")
    status = (By.CSS_SELECTOR, "a[data-test-id='manage-statuses-left-nav']")
    priority = (By.CSS_SELECTOR, "a[data-test-id='manage-priorities-left-nav']")
    Color_Code= (By.CSS_SELECTOR,"div[class*='color-code']")
    Behaviour_Input = (By.CSS_SELECTOR,"span[class*=selected]")
    Behaviour_box=(By.CSS_SELECTOR,"div[aria-label='Behavior']")
    Description=(By.CSS_SELECTOR,"textarea[aria-label='Description']")
    Add_Status=(By.CSS_SELECTOR,"button[data-test-id='add-status']")
    Display_title=(By.CSS_SELECTOR,"div[title='Issue created']")
    Make_default=(By.XPATH,"//div[@title='Issue created']/parent::div/parent::td/parent::tr/td[5]")
    Delete_link=(By.CSS_SELECTOR,"a[data-test-id='status-delete-trigger']")
    Confirm_delete_button=(By.CSS_SELECTOR,"button[data-test-id='delete-dependants-primary-action']")
    Select_Alternate_DefaultStatus= (By.CSS_SELECTOR,"div[data-test-id='form-field-alternateEntity']")
    Alternate_option=(By.CSS_SELECTOR,"li[data-option-index='0']")

    def Create_Status(self):
        self.driver.find_element(*StatusPage.Create_Button).click()

    def Enter_Status_Name(self,status):
        self.driver.find_element(*StatusPage.Status_Name).send_keys(status)

    def Select_Behaviour(self,behaviour):
        self.driver.find_element(*StatusPage.Behaviour_Input).click()
        self.driver.find_element(*StatusPage.Behaviour_box).send_keys(behaviour)

    def Enter_Description(self,desc):
        self.driver.find_element(*StatusPage.Description).send_keys(desc)

    def click_AddStatus(self):
        self.driver.find_element(*StatusPage.Add_Status).click()
        time.sleep(1)

    def click_Make_Default(self):
        self.driver.find_element(*StatusPage.Make_default).click()
        time.sleep(2)

    def switch_to_priority(self):       #Switiching to Priority Link
        time.sleep(1)
        self.driver.find_element(*PrioritiesPage.priority).click()
        Priority_Page=PrioritiesPage(self.driver)
        time.sleep(1)
        return Priority_Page

    def delete_status(self):            #deleting status handling for both default priority and Non default priority
        self.driver.find_element(*StatusPage.Display_title).click()
        self.driver.find_element(*StatusPage.Delete_link).click()
        try:
            self.driver.find_element(*StatusPage.Select_Alternate_DefaultStatus).click()
            self.driver.find_element(*StatusPage.Alternate_option).click()
            self.driver.find_element(*StatusPage.Confirm_delete_button).click()
            time.sleep(5)
        except:
            self.driver.find_element(*StatusPage.Confirm_delete_button).click()
            time.sleep(2)

    def switch_to_statuses(self):           #clicking on status link to switich to status window
        time.sleep(1)
        self.driver.find_element(*StatusPage.status).click()
        time.sleep(1)