import time

from selenium.webdriver.common.by import By
from PageObject.PendingTicketsPage import PendingTicketsPage

class AgentLoginPage:
    def __init__(self,driver):
        self.driver=driver

    #Agent Login window Page Elements are defined below
    UserName = (By.ID,"id_username")
    Password = (By.ID,"id_password")
    Login_Button= (By.CSS_SELECTOR,"input[class*='button']")
    remember_checkbox=(By.CSS_SELECTOR,"input[id='id_remember_me']")

    def Set_Username(self,username):
        self.driver.find_element(*AgentLoginPage.UserName).send_keys(username)

    def Set_Password(self,password):
        self.driver.find_element(*AgentLoginPage.Password).send_keys(password)

    def Click_Login_Button(self):
        self.driver.find_element(*AgentLoginPage.remember_checkbox).click()     #deselecting the remember me checkbox
        self.driver.find_element(*AgentLoginPage.Login_Button).click()          #clicking the Login button
        Pending_Tickets = PendingTicketsPage(self.driver)
        time.sleep(9)
        return Pending_Tickets
