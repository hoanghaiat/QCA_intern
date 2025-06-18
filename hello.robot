*** Settings ***
Library    SeleniumLibrary
Variables    locator.py
Resource    keyword.resource

Suite Setup    Open Browsers 
Suite Teardown    Close Browser
*** Test Cases ***
Login And Purchase
    #Open Browser
    Menu
    Select Any Product
    Click Buy Now
    Fill In User Information
    Proceed To Payment Method
