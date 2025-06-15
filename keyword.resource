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
Open Product Catalog 
  [Documentation]  Mở danh mục sản phẩm
    Wait Until Element Is Visible    xpath=${product_category}
    Click Element    xpath=${product_category}

Choose Beauty Accessories
     [Documentation]  Chọn mục Phụ Kiện Làm Đẹp
    Wait Until Element Is Visible    xpath=${beauty_accessories}
    Click Element    xpath=${beauty_accessories}
Add to cart
    [Documentation]  Thêm sản phẩm vào giỏ hàng
    Wait Until Element Is Visible    xpath=${add_to_cart}
    Click Element    xpath=${add_to_cart}
Select to cart
    [Documentation]  Chọn giỏ hàng để xem các sản phẩm đã thêm
    Wait Until Element Is Visible    xpath=${shopping_cart}
    Click Element    xpath=${shopping_cart}

Fill in Payment Information
    [Arguments]        ${fullname}    ${address}    ${email}    ${phone}
    [Documentation]    Điền thông tin thanh toán
    Wait Until Element Is Visible    xpath=${INPUT_FULLNAME}
    Input Text         xpath=${INPUT_FULLNAME}    ${fullname}
    Wait Until Element Is Visible    xpath=${INPUT_ADDRESS}
    Input Text         xpath=${INPUT_ADDRESS}     ${address}
    Wait Until Element Is Visible    xpath=${INPUT_EMAIL}
    Input Text         xpath=${INPUT_EMAIL}       ${email}
    Wait Until Element Is Visible    xpath=${INPUT_PHONE}
    Input Text         xpath=${INPUT_PHONE}       ${phone}
Press the button to continue payment
   [Documentation]  Nhấn nút tiếp tục để thanh toán
    Wait Until Element Is Visible    xpath=${BTN_Pay}
    Click Button     xpath=${BTN_Pay}

Close Browser Session
   [Documentation]  Đóng phiên trình duyệt
    Close Browser