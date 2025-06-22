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
    Handle Advertise

    Wait Until Element Is Visible    ${product_category}    30s
    Mouse Over    ${product_category}
    Wait Until Element Is Visible    ${beauty_accessories}    30s
    Mouse Over    ${beauty_accessories}
    Wait Until Element Is Visible    ${type_product}    30s
    Click Element    ${type_product}
Product Information
    
    Wait Until Element Is Visible    ${product_1}    timeout=30
    Scroll Element Into View         ${product_1}
    Click Element                    ${product_1}

Add Product To Cart
    
    Wait Until Element Is Visible    ${add_to_cart}    timeout=30
    Scroll Element Into View         ${add_to_cart}
    Click Element                    ${add_to_cart}


Proceed to Payment
    Wait Until Element Is Visible    ${pay_ment}    timeout=30
    Scroll Element Into View         ${pay_ment}
    Click Element                    ${pay_ment}

Fill Payment Information
    Wait Until Element Is Visible    ${INPUT_FULLNAME}    30s
    Input Text    ${INPUT_FULLNAME}   Trandathuy
    Input Text    ${INPUT_EMAIL}    dathuyne@gmail.com
    Input Text    ${INPUT_PHONE}    0942192764
    Input Text    ${INPUT_ADDRESS}    Hoi Kieng 32
Close Browser Session
    [Documentation]  Đóng phiên trình duyệt
    Close Browser


