import pytest
import time
from PageObject.AgentLoginPage import AgentLoginPage
from utilities.BaseClass import BaseClass
from PageObject.PendingTicketsPage import PendingTicketsPage
from PageObject.StatusPage import StatusPage
from PageObject.NewTicket import NewTicket
from PageObject.TicketDetailPage import TicketDetailPage

class Test_two(BaseClass):

    '''***********Test case for first scenario: To perform AgentLogin and create Status & Priority*************'''
    @pytest.mark.testcase1
    @pytest.mark.testcase2
    def test_scenario_one(self):
        self.driver.implicitly_wait(10)
        log = self.Get_log()                                   #created log object of Get_Log function of parent BaseClass

        LoginPage = AgentLoginPage(self.driver)                # Creation of an Object 'LoginPage' to Access AgentLogin Page
        LoginPage.Set_Username("interview_agent")              #Entering Username in AgentLogin window
        log.info("Username is Entered")
        LoginPage.Set_Password("Interview@123")                #Entering Password in AgentLogin window
        log.info("Password is Entered")
        Pending_Tickets = LoginPage.Click_Login_Button()        # Clicking on Login and Transfering control to Pending Tickets window
        log.info("Login button is clicked")


        Currnt_url = str(self.driver.current_url)               #Getting current_url of page after Login on AgentLogin window
        #Verifying if HomePage after Login is Pending Tickets window
        assert "https://interview2.supporthive.com/staff/tickets/?status=_pending" in Currnt_url, log.error("Login is Not Successful")
        log.info("Login is successful and control in on Pending Tickets window")

        Status_Page=Pending_Tickets.Click_On_Statuses()         #Clicking on Status Link and Transfering control to Status Management window
        log.info("Control is now on Status management window")

        Status_Page.Create_Status()                             #Clicking on '+' icon to create a new status
        Status_Page.Enter_Status_Name("Issue created")          #Entering New Status Name
        Status_Page.Select_Behaviour("Pending")                          #Entering Behaviour while creating new status
        Status_Page.Enter_Description("Status when a new issue ticket is created in HappyFox")  #Entering Description while creating new status
        Status_Page.click_AddStatus()                           #Clicking on AddStatus to create status
        log.info("New Status is Created")

        Priority_Page=Status_Page.switch_to_priority()         #Clicking on Priority Link and Transfering control to Priority Management window
        log.info("Control is now on Priority management window")

        Priority_Page.Create_Priority()                         #Clicking on '+' icon to create a new priority
        Priority_Page.Enter_Priority_Name("Assistance required")#Entering New Status Name
        Priority_Page.Enter_Priority_Description("Priority of the newly created tickets")#Entering Description
        Priority_Page.click_AddPriority()                       #Clicking on AddPriority to create priority
        log.info("New Status is Created")



    #********** Test case for second scenario:To set created Status/Priority as default, create New ticket,reply to ticket.**********
    @pytest.mark.testcase2(after='test_scenario_one')
    def test_scenario_two(self):
        self.driver.implicitly_wait(10)
        log = self.Get_log()        #created log object of Get_Log function of parent BaseClass

        Status_Page=StatusPage(self.driver)                 #Created an object of Status Window Page
        Status_Page.switch_to_statuses()                    #Clicking on Status Link on Status window Page
        Status_Page.click_Make_Default()                    #Making the specific Status as default
        log.info("created status is made default status")

        Priority_Page = Status_Page.switch_to_priority()    #Clicking on Priority Link on status winow page
        Priority_Page.click_Make_DefaultPriority()          #Making the specific priority as default
        log.info("created priority is made default priority")

        self.driver.get("https://interview2.supporthive.com/new")       #Transffering the control to Create new ticket window
        Ticket_Page=NewTicket(self.driver)                              #Creation of New Ticket window Page Object
        log.info("Control is Transffered to New Ticket Creation window")

        Ticket_Page.Enter_Subject('Ticket by Abhishek')                     #Entering a subject in Ticket creation
        Ticket_Page.Enter_Message("This is a test message")                     #Entering a Message in Ticket creation
        Ticket_Page.Attatch_Image()                     #Inserting a Image while ticket creation
        Ticket_Page.Enter_Name("Abhishek Kumar")                        #Entering a Full Name
        Ticket_Page.Enter_Email("abhishekkumar.r12194@gmail.com")                       #Entering an Email ID while Ticket creation
        Message = str(Ticket_Page.Create_Ticket())      #Retreiving the message after Ticket Page creation button is clicked
        assert  Message.find("Your ticket has been created"),log.error("New Ticket creation Failed")
        log.info("Successfuly created New Ticket")      #Verifying if the New Ticket Creation is succesfuly completed

        self.driver.get("https://interview2.supporthive.com/staff/login")   #Transfering the control to HomePage of Pending Tickets
        time.sleep(5)
        Pending_Tickets=PendingTicketsPage(self.driver)                     #created an object of Pending Tickets Page
        log.info("Transfered the Control to Pending Tickets Page detail")

        ticket=Pending_Tickets.Check_Ticket_Present()                       #Getting the newly created ticket from all Pending Tickets
        Status=Pending_Tickets.Check_Ticket_Status(ticket)                  #Getting the status from the selected ticket
        assert "ISSUE CREATED"==str(Status).upper(),log.error("Default Status not selected")
        log.info("Default status is selected successfuly in New Ticket")                  #Verifying if the status is same as default status created earlier

        Priority=Pending_Tickets.Check_Ticket_Priority(ticket)              #Getting the priority from the selected ticket
        assert "ASSISTANCE REQUIRED" == str(Priority).upper(),log.error("Default Priority not selected")
        log.info("Default priority is selected successfuly in New Ticket")                #Verifying if the priority is same as default priority created earlier

        ticket.click()                                     #clicking on the selected ticket to go into ticket detail
        log.info("Transfered control to Ticket Detail Page")

        Ticket_Detail=TicketDetailPage(self.driver)        #Creating a Ticket Detail object transffering control to Ticket Detail Page
        Ticket_Detail.Click_To_Reply()                     #clicking on reply button
        Ticket_Detail.Reply_Canned_Action("Reply to Customer Query")                #Replying with the canned action message
        log.info("Replied to Ticket with canned action success")

        current_status=Ticket_Detail.Get_Current_Status()  #Getting updated status of ticket after replying with canned action
        assert "CLOSED"==str(current_status).upper(),log.error("Incorrect Current Status for Ticket")#Verifying the updated status is CLOSED
        log.info("Ticket status updated as CLOSED after canned action reply")

        current_tag=Ticket_Detail.Get_Current_Tag()        #Getting updated tag of ticket after replying with canned action
        assert "customer_query"==str(current_tag).lower(),log.error("Incorrect Tag for Ticket")#verifying the updated tag
        log.info("Ticket tag updated with customer_query tag after canned action reply")

        current_priority=Ticket_Detail.Get_Current_Priority()#Getting updated priority of ticket after replying with canned action
        assert "medium"==str(current_priority).lower(),log.error("Incorrect Current Priority for Ticket")#verifying the updated priority
        log.info("Ticket priority updated as medium after canned action reply")

        self.driver.get("https://interview2.supporthive.com/staff/login")  # Transffering the control to pending Tickets window
        log.info("Transferring control to Pending Tickets window")

        Status_Page = Pending_Tickets.Click_On_Statuses()  # Transferring the control to status Window
        log.info("clicking and Transferring control to the Status window")


    '''Test case for third scenario: deleting the created status/priority , Logout from the account'''
    @pytest.mark.testcase1(after='test_scenario_one')
    @pytest.mark.testcase2(after='test_scenario_two')
    def test_scenario_three(self):
        self.driver.implicitly_wait(3)
        log=self.Get_log()

        Status_Page = StatusPage(self.driver)    #Creating an object of status window
        log.info("Status Object Created ")

        Status_Page.switch_to_statuses()         #Switicing to status window if control is present on priority window
        log.info("clicked on statuses link to switch to status window")
        Status_Page.delete_status()              #deleting the default status that was created
        log.info("deleted the status")

        Priority_Page=Status_Page.switch_to_priority() #Switching to the priority window
        log.info("clicked on priorities link to switch to priority window")
        Priority_Page.delete_priority()          #deleting the default priority that was created
        log.info("deleted the priority")

        Priority_Page.Logout()                   #Logging out from the Agent Login window
        log.info("Logout Completed")