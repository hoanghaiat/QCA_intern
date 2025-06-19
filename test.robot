*** Settings ***
Library           SeleniumLibrary
Variables         locator.py
Resource          keyword.resource

Suite Setup       open_browsers
Test Teardown     return_to_homepage
Suite Teardown    Close Browser

*** Test Cases ***
full_checkout_flow
    navigate_to_product_category
    select_product
    add_to_cart
    proceed_to_checkout
    fill_delivery_information
    confirm_order
