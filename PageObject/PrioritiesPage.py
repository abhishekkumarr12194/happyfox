import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class PrioritiesPage:
    def __init__(self,driver):
        self.driver=driver

    #All elements on Priority Page management window are Listed here
    priority=(By.CSS_SELECTOR,"a[data-test-id='manage-priorities-left-nav']")
    status=(By.CSS_SELECTOR,"a[data-test-id='manage-statuses-left-nav']")
    Create_Button= (By.CSS_SELECTOR,"button[class*='create']")
    Priority_Name=(By.CSS_SELECTOR,"input[data-test-id='form-field-name']")
    Description=(By.CSS_SELECTOR,"textarea[data-test-id='form-field-description']")
    Add_Priority=(By.CSS_SELECTOR,"button[data-test-id='add-priority']")
    Make_default=(By.XPATH,"//span[@title='Assistance required']/parent::td/parent::tr/td[5]")
    Delete_link = (By.CSS_SELECTOR, "a[data-test-id='priority-delete-trigger']")
    Confirm_delete_button = (By.CSS_SELECTOR, "button[data-test-id='delete-dependants-primary-action']")
    Select_Alternate_DefaultStatus = (By.CSS_SELECTOR, "div[data-test-id='form-field-alternateEntity']")
    Alternate_option = (By.CSS_SELECTOR, "li[data-option-index='0']")
    Display_title = (By.CSS_SELECTOR, "span[title='Assistance required']")
    Agent_user=(By.CSS_SELECTOR,"img[alt='Logged-In Agent']")
    logout_btn=(By.CSS_SELECTOR,"li[class*='mod-logout']")

    def Create_Priority(self):
        self.driver.find_element(*PrioritiesPage.Create_Button).click()

    def Enter_Priority_Name(self,priority):
        self.driver.find_element(*PrioritiesPage.Priority_Name).send_keys(priority)

    def Enter_Priority_Description(self,desc):
        self.driver.find_element(*PrioritiesPage.Description).send_keys(desc)

    def click_AddPriority(self):
        self.driver.find_element(*PrioritiesPage.Add_Priority).click()
        time.sleep(1)

    def click_Make_DefaultPriority(self):
        self.driver.find_element(*PrioritiesPage.Make_default).click()
        time.sleep(2)

    def switch_to_statuses(self):
        time.sleep(1)
        self.driver.find_element(*PrioritiesPage.status).click()

    def delete_priority(self):              #deleting priority handling for both default priority and Non default priority
        self.driver.find_element(*PrioritiesPage.Display_title).click()
        self.driver.find_element(*PrioritiesPage.Delete_link).click()
        try:
            self.driver.find_element(*PrioritiesPage.Select_Alternate_DefaultStatus).click()
            self.driver.find_element(*PrioritiesPage.Alternate_option).click()
            self.driver.find_element(*PrioritiesPage.Confirm_delete_button).click()
            time.sleep(5)
        except:
            self.driver.find_element(*PrioritiesPage.Confirm_delete_button).click()
            time.sleep(2)

    def Logout(self):   #Method to click on Logout
        time.sleep(4)
        self.driver.find_element(*PrioritiesPage.Agent_user).click()
        Action = ActionChains(self.driver)
        Action.move_to_element(self.driver.find_element(*PrioritiesPage.logout_btn)).click().perform()