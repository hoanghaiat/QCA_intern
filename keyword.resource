*** Settings ***
Library    SeleniumLibrary
Variables    locator.py
*** Variables ***
${url}    https://lamthaocosmetics.vn/cart

*** Keywords ***
Open Home Page
    Open Browser    ${url}    chrome
    Maximize Browser Window
Open Product Catalog 
    Click Element    xpath=${product_category}
Choose Beauty Accessories
    Click Element    xpath=${beauty_accessories}
Add to cart
    Click Element    xpath=${add_to_cart}
Select to cart
    Click Element    xpath=${shopping_cart}
Fill in Payment Information
    [Arguments]        ${fullname}    ${address}    ${email}    ${phone}
    Input Text         xpath=${INPUT_FULLNAME}    ${fullname}
    Input Text         xpath=${INPUT_ADDRESS}     ${address}
    Input Text         xpath=${INPUT_EMAIL}       ${email}
    Input Text         xpath=${INPUT_PHONE}       ${phone}
Press the button to continue payment
    Click Button     xpath=${BTN_Pay}
Close Browser Session
    Close Browser