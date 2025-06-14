*** Settings ***
Library    SeleniumLibrary
Variables    locator.py
Resource    keywords.resource

*** Test Cases ***
CheckOut
    Open Browsers
    Menu
    Product Information
    Add Product To Cart
    Payment
    Delivery Information
    CheckOut Complete