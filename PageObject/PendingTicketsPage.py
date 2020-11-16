import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select
from PageObject.StatusPage import StatusPage



class PendingTicketsPage:
    def __init__(self,driver):
        self.driver=driver

    # Pending Tickets window Page Elements are defined below
    ticket = (By.CSS_SELECTOR,"span[title='Tickets']")
    ticket_subject_list=(By.CSS_SELECTOR,"a[data-test-id*='link-to-ticket-details-']")

    def Click_On_Statuses(self):  #Method to click on status Link and transffer the control to status management Page
        try:
            Action=ActionChains(self.driver)
            Action.move_to_element(self.driver.find_element(*PendingTicketsPage.ticket)).click().perform()
            self.driver.execute_script('document.getElementsByTagName("a")[7].click();')
            Status_Page = StatusPage(self.driver)
            return Status_Page
        except Exception as e:
            print("Error Observed:" + str(e.args))


    def Check_Ticket_Present(self):    #Checking if a particular Ticket with title is present in pending tickets page
        time.sleep(3)
        try:
            ticket_lists=self.driver.find_elements(*PendingTicketsPage.ticket_subject_list)
            print(ticket_lists)
            for ticket in ticket_lists:
                if ticket.get_attribute("title")=="Ticket by Abhishek":
                    return ticket
                else:
                    pass
        except Exception as e:
            print("Error Observed:"+str(e.args))


    def Check_Ticket_Status(self,ticket):
        status=ticket.find_element_by_xpath("parent::div/parent::div/parent::div/parent::div/div[1]/div[2]/div[1]/div[1]/div/span").text
        return status

    def Check_Ticket_Priority(self,ticket):
        priority=ticket.find_element_by_xpath("parent::div/parent::div/parent::div/parent::div/parent::article/div[2]/div[4]/div[3]/div/div/div[2]").text
        return priority
