from pages.IdcLoginPage import IdcLoginPage
from pages.IdcOverviewPage import IdcOverviewPage
from playwright.sync_api import Page, expect
import pytest
import time
import conftest


############### Function to verify login without entering the username and password ########################
def test01_login_without_username_and_password(setbrowserconfig) -> None:
   page = setbrowserconfig
   blank_credentials = {'username': '', 'password': ''}
   login_object = IdcLoginPage(page)
   login_object.do_login(blank_credentials)
   expected_error_mess_for_email_address = "Please enter your Email Address"
   expect(login_object.get_error_mess_for_email_address).to_contain_text(expected_error_mess_for_email_address)


############### Function to verify login without entering the username ########################################
def test02_login_without_username(setbrowserconfig) -> None:
   page=setbrowserconfig
   credentials_without_username = {'username': '', 'password': 'Cnvrg@123#'}    
   login_object=IdcLoginPage(page)
   login_object.do_login(credentials_without_username)
   expected_error_mess_for_missing_username="Please enter your Email Address"
   expect(login_object.get_error_mess_for_email_address).to_contain_text(expected_error_mess_for_missing_username)


############### Function to verify login without entering the password ########################################
def test03_login_without_password(setbrowserconfig) -> None:
   page=setbrowserconfig
   credentials_without_password = {'username': 'idcuser6687@mailinator.com', 'password': ''}    
   login_object=IdcLoginPage(page)
   login_object.do_login(credentials_without_password)
   expected_error_mess_for_missing_password="Please enter your password"
   expect(login_object.get_error_mess_for_password).to_contain_text(expected_error_mess_for_missing_password)


############### Function to verify login with entering the wrong password ########################################
def test04_login_with_incorrect_password(setbrowserconfig) -> None:
   page=setbrowserconfig
   credentials_with_incorrect_password = {'username': 'idcuser6687@mailinator.com', 'password': '/Cnvrg@123#'}    
   login_object=IdcLoginPage(page)
   login_object.do_login(credentials_with_incorrect_password)
   expected_error_mess_for_incorrect_password="Your password is incorrect."
   expect(login_object.get_error_mess_common).to_contain_text(expected_error_mess_for_incorrect_password)


############### Function to verify login with entering the wrong username ########################################
def test05_login_with_incorrect_username(setbrowserconfig) -> None:
   page=setbrowserconfig
   credentials_with_incorrect_password = {'username': 'idcuser66870@mailinator.com', 'password': 'Cnvrg@123#'}    
   login_object=IdcLoginPage(page)
   login_object.do_login(credentials_with_incorrect_password)
   expected_error_mess_for_incorrect_password="We can't seem to find your account."
   expect(login_object.get_error_mess_common).to_contain_text(expected_error_mess_for_incorrect_password)



############### Function to verify login with entering the correct username and password ########################
def test06_successful_login(setbrowserconfig) -> None:
    page=setbrowserconfig
    credentials01 = {'username': 'idcuser6687@mailinator.com', 'password': 'Cnvrg@123#'}    
    login_p=IdcLoginPage(page)
    overview_p=login_p.do_login(credentials01)
    time.sleep(10)
    expect(overview_p.get_overview_header).to_contain_text("Overview")
   
   













    
    

    

    
    
   



   




    
  
    





   
    
