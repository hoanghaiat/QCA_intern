*** Settings ***
Library    SeleniumLibrary
Resource    keyword.resource
Variables    locator.py

*** Variables ***   
${test}    A
*** Test Cases ***
Đăng nhập tài khoản 
    Mở Trang web    
    chọn vào một sản phẩm bất kì
    kích vào mua ngay
    điền thông tin
    kích vào tiếp tục đến phương thức thanh toán