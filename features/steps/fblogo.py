from behave import *
from behave.__main__ import main as behave_main
from behave.configuration import ConfigError
import time
import os


from selenium import webdriver


@given('user launches chromebowser')
def launchChrome(context):
    print()
    context.driver=webdriver.Chrome(executable_path=f"{os.getcwd()}/resources/chromedriver")
    


@when('launches facebook')
def launchFacebook(context):
    context.driver.get('https://facebook.com')
    context.driver.implicitly_wait(5000)
    
    
    


@then('facebook logo is visible')
def assertLogo(context):
    status=context.driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[1]/div/img').is_displayed()
    assert status is True
    
    


@then('close the browser')
def closeBrowser(context):
    time.sleep(5)
    context.driver.close()