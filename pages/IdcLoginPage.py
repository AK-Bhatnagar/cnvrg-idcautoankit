from pages.IdcOverviewPage import IdcOverviewPage
import pytest

class IdcLoginPage:

    
    def __init__(self, page):
        self.page = page        
        self._username = self.page.get_by_placeholder("Email Address")
        self._password = self.page.get_by_placeholder("Password")
        self._lgnbtn =  self.page.get_by_text("Continue")
        self._error_message_for_email_address = self.page.locator("div.login-container:nth-child(3) div.form-wrapper form.localAccount div.entry div.entry-item:nth-child(1) div.error.itemLevel:nth-child(2) > p:nth-child(1)")
        self._error_message_for_password = self.page.locator("div.login-container:nth-child(3) div.form-wrapper form.localAccount div.entry div.entry-item:nth-child(2) div.error.itemLevel:nth-child(2) > p:nth-child(1)")
        self._error_messsage_common = self.page.locator('div.login-container:nth-child(3) div.form-wrapper div:nth-child(2) form.localAccount div.error.pageLevel > p:nth-child(1)')
        

    def enter_username(self, u_name):
        self._username.clear()
        self._username.fill(u_name)
    
    
    def enter_password(self, p_word):
        self._password.clear()
        self._password.fill(p_word)
    
    
    def click_login(self):
        self._lgnbtn.click()
   
    
    def do_login(self, credentials):
        self.enter_username(credentials['username'])
        self.enter_password(credentials['password'])
        self.click_login()
        return IdcOverviewPage(self.page)
        
        
    @property
    def get_error_mess_for_email_address(self):
      return self._error_message_for_email_address

    @property
    def get_error_mess_for_password(self):
      return self._error_message_for_password
    
    @property
    def get_error_mess_common(self):
      return self._error_messsage_common



    

