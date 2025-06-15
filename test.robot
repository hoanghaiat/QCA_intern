*** Settings ***
Resource    keyword.resource
Variables    locator.py
Library    SeleniumLibrary

Suite Setup    Open Browser    ${url}    ${Browser}
Test Setup     Maximize Browser Window
Test Teardown  Capture Page Screenshot
Suite Teardown  Close Browser
*** Variables ***
${url}    https://lamthaocosmetics.vn/cart
${Browser}        Chrome

${fullname}      Trần Đạt Huy 
${email}          dathuy@gmail.com 
${phone}  0123456789
${address}        32 Đường hoikieng, Phường HoaQuy



*** Test Cases ***
Verify Checkout Functionality
    Open Home Page
    Open Product Catalog 
    Choose Beauty Accessories
    Add to cart
    Select to cart
    Fill in Payment Information  ${fullname}    ${address}    ${email}    ${phone}
    Press the button to continue payment