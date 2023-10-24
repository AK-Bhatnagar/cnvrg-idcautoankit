# from pages import IdcLoginPage
import pytest

class IdcOverviewPage:

    def __init__(self, page):
        self.page = page        
        self._overview_header = self.page.locator("div#app > div > div:nth-of-type(3) > div:nth-of-type(2) > div > span") 
        self._overview_menu_locator = self.page.locator("div#app > div > div:nth-of-type(3) > div > div:nth-of-type(2) > div > span")
        self._catalog_menu_locator = self.page.locator("div#app > div > div:nth-of-type(3) > div > div:nth-of-type(3) > div > span")        
        self._infrastructure_menu_locator = self.page.locator("div#app > div > div:nth-of-type(3) > div > div:nth-of-type(4) > div > span") 
        self._clickadd = self.page.locator('div#app > div > div:nth-of-type(3) > div:nth-of-type(2) > div:nth-of-type(2) > div > button')

   
    ########## Get hold of Overview Header Locator ##########
    @property
    def get_overview_header(self):
        return self._overview_header
    
    ########## Get hold of Overview, Catalog, Infrastructure Menu ##########
    @property
    def get_overview_menu(self):
        return self._overview_menu_locator
    
    @property
    def get_catalog_menu(self):
        return self._catalog_menu_locator
    
    @property
    def get_Infrastructure_menu(self):
        return self._infrastructure_menu_locator
    
    @property
    def get_add_button_locator(self):
        return self._clickadd

    
    ########## Functions to click on Overview, Catalog, Infrastructure Menu ##########

    def click_overview_menu(self):
        return self._overview_menu_locator.click()    
    
    def click_catalog_menu(self):
        return self._catalog_menu_locator.click()    
    
    def click_Infrastructure_menu(self):
        return self._infrastructure_menu_locator.click()
    
    def click_add_button(self):
        return self._clickadd.click()
    
    ########## Functions to click on Overview, Catalog, Infrastructure Menu ##########

 
