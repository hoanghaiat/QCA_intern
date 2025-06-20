*** Settings ***
Resource    keyword.resource
Variables    locator.py
Library    SeleniumLibrary

Suite Setup   Open Home Page
Test Setup     Maximize Browser Window
Test Teardown  Capture Page Screenshot
Suite Teardown  Close Browser
*** Variables ***
${url}    https://lamthaocosmetics.vn/cart
${Browser}        Chrome



*** Test Cases ***
Verify Checkout Functionality
    Handle Advertise
    Menu
    Product Information
    Add Product To Cart         
    Proceed to Payment
    Fill Payment Information    
