*** Settings ***
Library           SeleniumLibrary
Variables         locator.py
Library           Collections
Library           BuiltIn

*** Variables ***
${USER_PHONE}       0362631521
${USER_PASSWORD}    Tuyet@1211
${FULL_NAME}        Nguyen Quynh Anh
${EMAIL}            anh32@gmail.com
${ADDRESS}          109 Le Duan
${NOTE_TEXT}        note: abc

*** Keywords ***
Open Website
    Open Browser    https://lamthaocosmetics.vn/    Edge
    Maximize Browser Window
    Set Selenium Speed    0.5s
    sleep   15s
Close Advertisement Popup
    ${result}=    Run Keyword And Ignore Error    Wait Until Element Is Visible    ${AD_POPUP_CLOSE_BTN}    timeout=10s
    Run Keyword If    '${result[0]}' == 'PASS'    Click Element    ${AD_POPUP_CLOSE_BTN}
Select Product
    Click Element    ${PRODUCT_CATEGORY}
    Click Element    ${FIRST_CATEGORY}

View Product Detail And Add To Cart
    Click Element    ${FIRST_PRODUCT}
  
    Input Text       ${QUANTITY_INPUT}    4
    Sleep            1s
    Click Element    ${DECREASE_QUANTITY}
    Sleep            1s
    Click Element    ${INCREASE_QUANTITY}
    Click Element    ${ADD_TO_CART}

Open Cart
    Wait Until Element Is Visible    ${CART_NOTE}    timeout=10s
    Input Text    ${CART_NOTE}    ${NOTE_TEXT}
    Click Element    ${CHECKOUT_NOW}

Fill Checkout Information
    Wait Until Element Is Visible    ${FULL_NAME_INPUT}    timeout=10s
    Input Text    ${FULL_NAME_INPUT}       ${FULL_NAME}
    Input Text    ${EMAIL_CHECKOUT_INPUT}  ${EMAIL}
    Input Text    ${PHONE_INPUT}           ${USER_PHONE}
    Input Text    ${ADDRESS_INPUT}         ${ADDRESS}
    Select From List By Label    ${PROVINCE_SELECT}    Hà Nội
    Wait Until Element Contains    ${DISTRICT_SELECT}   Quận Hoàn Kiếm    timeout=10s
    Select From List By Label      ${DISTRICT_SELECT}   Quận Hoàn Kiếm
    Wait Until Element Contains    ${WARD_SELECT}       Phường Chương Dương    timeout=10s
    Select From List By Label      ${WARD_SELECT}       Phường Chương Dương

Submit Order
    Wait Until Element Is Enabled    ${NEXT_BUTTON}    timeout=10s
    Click Element    ${NEXT_BUTTON}
    Wait Until Page Contains Element    ${FINISH_BUTTON}    timeout=10s
    Click Button    ${FINISH_BUTTON}


Close Website
    Close Browser
