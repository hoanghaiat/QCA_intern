*** Settings ***
Library   SeleniumLibrary
Resource    keyword.resource
Variables   locator.py

*** Test Cases ***
Đăng nhập tài khoản
    Mở trang web
    # Điền thông tin đăng nhập
    # Ấn nút đăng nhập
    # Chọn danh mục sản phẩm 
    # Xem chi tiết sản phẩm
    Xem giỏ hàng
    # Tiến hành thanh toán
*** Keywords ***