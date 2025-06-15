*** Settings ***
Library   SeleniumLibrary
Variables   locator.py
# Suite Setup  Mở trang web
# Test Setup  Điền thông tin đăng nhập
# Test Teardown Log out tài khoản  quay lại tranhg chủ
# Suite Teardown Đóng trang web   đóng trình duyệt 

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

Chọn danh mục sản phẩm  
    Click Element     //nav[@class="navbar-mainmenu"]/div[@class="danhmucsanpham"]
    Click Element     //div[@class="postionabcat"]/ul[1]/li[1]
Xem chi tiết sản phẩm
    Click Element    //div[@class="templatecolreal"]/div[1]/div/div/div[2]/h3        #click chi tiết sp
    Click Element   //label[text()="22g"]       #chọn kích thước
    Input Text      //input[@class="quantitynum"]    4                #nhap sl
    Sleep           3s
    Click Element    //div[@class="gridoftemplateaction"]/div[1]/div/div[2]/div[1]     #giam sl
    Sleep           3s
    Click Element    //div[@class="gridoftemplateaction"]/div[1]/div/div[2]/div[3]       #tang sl
     #them gio 
    Click Element    //a[text()="Thêm vào giỏ hàng"]        
    # Click Element    //div[@class="gridoftemplateaction3"]            #mua ngay
Xem giỏ hàng
    Wait Until Element Is Visible    //textarea[@id='notecart']    timeout=10s
    Input Text    //textarea[@id='notecart']    note: abc
    Click Element    //div[@class="thantoannga"]/a                    # thanh toán ngay

Tiến hành thanh toán
    Wait Until Element Is Visible    //input[@id="billing_address_full_name"]    timeout=10s
    Input Text     //input[@id="billing_address_full_name"]  Nguyễn Quỳnh Anh
    Input Text     //input[@id="checkout_user_email"]  anh32@gmail.com
    Input Text     //input[@id="billing_address_phone"]   0362631552
    Input Text    //input[@id="billing_address_address1"]    109 Lê Duẩn

    Select From List By Label    //select[@id="customer_shipping_province"]     Hà Nội
    Wait Until Element Contains    //select[@id="customer_shipping_district"]    Quận Hoàn Kiếm    timeout=15s
    Select From List By Label    //select[@id="customer_shipping_district"]    Quận Hoàn Kiếm
    Wait Until Element Contains    //select[@id="customer_shipping_ward"]    Phường Chương Dương    timeout=15s
    Select From List By Label     //select[@id="customer_shipping_ward"]    Phường Chương Dương
  
    Wait Until Element Is Enabled    //div[@id="step-footer-checkout"]//following::button    timeout=10s
    Click Element    //div[@id="step-footer-checkout"]//following::button         #tiếp tục tt
    # Click Element    //div[@class="content-box"]/div[1]/label/div[1]/input   #Chọn phương thức
    Wait Until Page Contains Element    //button[@data-event-added="attached"]    timeout=15s
    Click Button    //button[@data-event-added="attached"]            #Hoàn tất
