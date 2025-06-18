*** Settings ***
Library           SeleniumLibrary
Resource          keyword.resource
Variables         locator.py

Suite Setup       Open Website
# Test Setup        Login To Website
# Test Teardown     Logout
Suite Teardown    Close Website

*** Test Cases ***
Complete Checkout Flow
    Select Product
    View Product Detail And Add To Cart
    Open Cart
    Fill Checkout Information
    Submit Order
*** Keywords ***
Open Website
    Open Browser    https://lamthaocosmetics.vn/    Edge
    Maximize Browser Window
    Set Selenium Speed    0.5s
    sleep   3s
    Close Advertisement Popup