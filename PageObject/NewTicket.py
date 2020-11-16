import os

from selenium.webdriver.common.by import By

class NewTicket:
    def __init__(self,driver):
        self.driver=driver

    # New Ticket creation window Page Elements are defined below
    ticket_subject = (By.CSS_SELECTOR,"input[id='id_subject']")
    ticket_message = (By.XPATH,"//div[@id='cke_1_contents']/div/p")
    full_name = (By.ID,"id_name")
    email = (By.ID,"id_email")
    create_ticket_button = (By.ID,"submit")
    after_ticket_creation=(By.CSS_SELECTOR,"div[class*='message-after-ticket-creation']")


    def Enter_Subject(self,subject):
        self.driver.find_element(*NewTicket.ticket_subject).send_keys(subject)

    def Enter_Message(self,message):
        self.driver.find_element(*NewTicket.ticket_message).send_keys(message)

    def Attatch_Image(self):
        attatch_image = self.driver.execute_script("return document.getElementById('attach-file-input');")
        attatch_image.send_keys(os.path.abspath('Image.jpg'))           #attatching image from tests folder of project directory

    def Enter_Name(self,name):
        self.driver.find_element(*NewTicket.full_name).send_keys(name)

    def Enter_Email(self,email):
        self.driver.find_element(*NewTicket.email).send_keys(email)

    def Create_Ticket(self):
        self.driver.find_element(*NewTicket.create_ticket_button).click()
        return self.driver.find_element(*NewTicket.after_ticket_creation).text   #Returning the successful ticket created text