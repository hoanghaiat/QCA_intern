*** Settings ***
Library    SeleniumLibrary
Variables    locator.py

*** Variables ***
${Browser}    chrome    
${url}      https://lamthaocosmetics.vn/  


*** Keywords ***
Mở Trang web
    Open Browser    ${url}    ${Browser}
chọn vào một sản phẩm bất kì
    Click Element    $(product_item)
kích vào mua ngay
    Click Element   $(buy_now_button)
điền thông tin 
    Input Text       $(full_name_input)    Nguyễn Nho Tường Vi
    Input Text       $(email_input)    nguyennhotuongvi@gmail.com
    Input Text       $(phone_input)    0898224770
    Input Text      $(address_input)    4 Phan Trong Tue
    Select From List By Label   $(province_select)     Đà Nẵng
    Select From List By Label    $(district_select)   Hải Châu
    Select From List By Label     $(ward_select) Hoà Cường Nam 
kích vào tiếp tục đến phương thức thanh toán 
    Click Element       $(continue_to_payment_button)   
 




    




