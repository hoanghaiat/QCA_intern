*** Settings ***
Library    SeleniumLibrary
Variables    locator.py
*** Variables ***
${url}    https://lamthaocosmetics.vn/cart

*** Keywords ***
Open Home Page
    [Documentation]  Mở trình duyệt và truy cập trang chủ
    Open Browser    ${url}    chrome
    Maximize Browser Window

Handle Advertise
    [Documentation]  Xử lý popup quảng cáo nếu có
    ${popup_visible}=    Run Keyword And Return Status    Wait Until Element Is Visible    xpath=//button[@class='close close-popup-contact']    timeout=5
    IF    ${popup_visible}
        Click Element    xpath=//button[@class='close close-popup-contact']
    END

Menu
    Wait Until Element Is Visible    xpath=${product_category}    timeout=30
    Mouse Over                      xpath=${product_category}
    Wait Until Element Is Visible    xpath=${beauty_accessories}    timeout=30
    Mouse Over                      xpath=${beauty_accessories}
    Wait Until Element Is Visible    xpath=${type_product}    timeout=30
    Click Element                   xpath=${type_product}

Product Information
    
    Wait Until Element Is Visible    xpath=${product_1}    timeout=30
    Scroll Element Into View         xpath=${product_1}
    Click Element                    xpath=${product_1}

Add Product To Cart
    
    Wait Until Element Is Visible    xpath=${add_to_cart}    timeout=30
    Scroll Element Into View         xpath=${add_to_cart}
    Click Element                    xpath=${add_to_cart}

Go to Shopping Cart
    
    Wait Until Element Is Visible    xpath=${shopping_cart}    timeout=30
    Click Element                    xpath=${shopping_cart}

Proceed to Payment
    Wait Until Element Is Visible    xpath=${pay_ment}    timeout=30
    Scroll Element Into View         xpath=${pay_ment}
    Click Element                    xpath=${pay_ment}

Fill Payment Information
    [Arguments]        ${fullname}    ${address}    ${email}    ${phone}
    Wait Until Element Is Visible    xpath=${INPUT_FULLNAME}    timeout=30
    Input Text         xpath=${INPUT_FULLNAME}    ${fullname}
    Wait Until Element Is Visible    xpath=${INPUT_ADDRESS}    timeout=30
    Input Text         xpath=${INPUT_ADDRESS}     ${address}
    Wait Until Element Is Visible    xpath=${INPUT_EMAIL}    timeout=30
    Input Text         xpath=${INPUT_EMAIL}       ${email}
    Wait Until Element Is Visible    xpath=${INPUT_PHONE}    timeout=30
    Input Text         xpath=${INPUT_PHONE}       ${phone}
Close Browser Session
    [Documentation]  Đóng phiên trình duyệt
    Close Browser


