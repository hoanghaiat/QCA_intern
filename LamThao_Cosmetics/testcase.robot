*** Settings ***
Library    SeleniumLibrary
Variables    locator.py
Resource    keywords.resource

Suite Setup    Open Browsers
#Test Setup    Menu
Test Teardown   Go Back Home 
Suite Teardown    Close Browser
*** Test Cases ***
CheckOut
    #Open Browsers
    Menu
    Product Information
    Add Product To Cart
    Payment
    Delivery Information
    CheckOut Complete