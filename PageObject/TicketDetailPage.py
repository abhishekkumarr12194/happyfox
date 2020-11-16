import time

from selenium.webdriver.common.by import By


class TicketDetailPage:
    def __init__(self,driver):
        self.driver=driver
        self.driver.implicitly_wait(5)

    #All Elements on ticket detail window are Listed here
    reply_link=(By.CSS_SELECTOR,"a[data-test-id='reply-link']")
    canned_button = (By.CSS_SELECTOR, "div[class*='hf-floating-editor_toolbar-menu-dropdown hf-popover-trigger ember-view']")
    canned_search_box=(By.CSS_SELECTOR,"input[class*='search-input']")
    canned_option=(By.CSS_SELECTOR,"li[class*=power-select-option]")
    apply_button=(By.CSS_SELECTOR,"button[data-test-id='hf-add-canned-action']")
    reply_button=(By.CSS_SELECTOR,"button[data-test-id='add-update-reply-button']")
    current_ticket_status=(By.CSS_SELECTOR,"span[class*='ticket-status_name']")
    current_ticket_priority=(By.CSS_SELECTOR,"div[data-test-id='ticket-box_priority']")
    current_ticket_tag=(By.CSS_SELECTOR,"span[data-test-id='tag']")

    def Click_To_Reply(self):
        self.driver.find_element(*TicketDetailPage.reply_link).click()

    def Reply_Canned_Action(self,canned_message):  #Code to click on message button,selecting the canned action and replying with it
        self.driver.find_element(*TicketDetailPage.canned_button).click()
        self.driver.find_element(*TicketDetailPage.canned_search_box).send_keys(canned_message)
        time.sleep(5)
        self.driver.find_element(*TicketDetailPage.canned_option).click()
        self.driver.find_element(*TicketDetailPage.apply_button).click()
        self.driver.find_element(*TicketDetailPage.reply_button).click()

    def Get_Current_Status(self):       #status after replying
        current_status=self.driver.find_element(*TicketDetailPage.current_ticket_status).text
        return current_status

    def Get_Current_Tag(self):          #tag after replying
        current_tag=self.driver.find_element(*TicketDetailPage.current_ticket_tag).text
        return current_tag

    def Get_Current_Priority(self):       #Priority after replying
        current_priority=self.driver.find_element(*TicketDetailPage.current_ticket_priority).text
        return current_priority







