*** Settings ***
Library   SeleniumLibrary
Variables   locator.py

*** Variables ***
${test}  A

*** Keywords ***
Mở trang web
    Open Browser  https://lamthaocosmetics.vn/  Edge
Điền thông tin đăng nhập
    Click Element    ${account_icon}
    Wait Until Element Is Visible    //input[@id="login-customer[email]"]    timeout=10s
    Input Text    //input[@id="login-customer[email]"]    0362631552
    Input Text    //input[@id="login-customer[password]"]    Tuyet2003
    Press Key    //input[@id="login-customer[password]"]    ENTER
Ấn nút Đăng nhập
    Click Button    //button[@id="form_submit-login"]   
    Wait Until Page Contains Element    //div[@class="header-wrap-logo"]   timeout=10s
    Go To    https://lamthaocosmetics.vn/    # ve trang chu

Chọn danh mục sản phẩm   #ok  Choose product category 
    Wait Until Page Contains Element    //nav    timeout=10s
    Sleep    2s
    Click Element     //div[contains(@class, 'danhmucsanpham')]
    Wait Until Page Contains Element    //div[contains(@class, 'danhmucsanpham')]/div[2]/ul[1]    timeout=5s
    Click Element    //div[contains(@class, 'danhmucsanpham')]/div[2]/ul[1]/li[1]/a
Xem chi tiết sản phẩm
    Click Element    //div[contains(@class, 'product-loop')]        #click sp
    Click Element    //label[normalize-space(text())='1 Hộp (10 Miếng)']        #chọn kích thước
    Input Text    //input[@class="quantitynum"]    2                #nhap sl
    Click Element    //div[contains(@class, 'cuccongtrusoboxgrid1 controplus ')]     #giam sl
    Click Element    //div[contains(@class, 'cuccongtrusoboxgrid3 controplus ')]       #tang sl
     #them gio 
    Click Element    //div[@class='gridoftemplateaction2']         
    # Click Element    //div[@class="gridoftemplateaction3"]            #mua ngay
Xem giỏ hàng
    Click Element    //a[@id="site-cart-handle"]
    Input Text    //input[@class="quantitynum"]    2                #nhap sl
    Click Button    //div[contains(@class, 'cuccongtrusoboxgrid1 controplus ')]       #giam sl
    Click Button    //div[contains(@class, 'cuccongtrusoboxgrid3 controplus ')]     #tang sl
    Input Text    //textarea[@id="notecart"]    note: abc
    Click Element    //div[@class="thantoannga"]                     # thanh toán ngay

Tiến hành thanh toán
    Input Text     //input[@id="billing_address_full_name"]  Nguyễn Quỳnh Anh
    Input Text     //input[@id="checkout_user_email"]  anh32@gmail.com
    Input Text     //input[@id="billing_address_phone"]  09872221121
    Input Text    //input[@id="billing_address_address1"]    109 Lê Duẩn
    Click Element    //select[@id="customer_shipping_province"]/option[3]  
    Click Element    //select[@id="customer_shipping_district"]/option[1]
    Click Element     //select[@id="customer_shipping_ward"]/option[2]
    Input Text     //input[@class="field-input"]    GIAM20
    Click Element    //div[@class="content-box"]/div[1]/label/div[1]/input   #Chọn phương thức
    Click Button    //button[@class="step-footer-continue-btn btn"]            #Hoàn tất