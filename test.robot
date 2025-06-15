*** Settings ***
Library    SeleniumLibrary
Resource   keyword.resource
Variables  locator.py

*** Test Cases ***
Đặt Hàng Một Sản Phẩm Thành Công
    Mở Trang Web
    Chọn Sản Phẩm Mới
    Chọn Sản Phẩm Và Mua Ngay
    Điền Thông Tin Mua Hàng
