*** Settings ***
Library    SeleniumLibrary
Variables  locator.py

*** Variables ***
${Browser}    chrome
${url}        https://lamthaocosmetics.vn/

*** Keywords ***
Mở Trang web
    Open Browser    ${url}    ${Browser}
    Maximize Browser Window
    Đóng Popup Nếu Có
    Sleep    2s

Chọn Sản Phẩm Mới
    Wait Until Element Is Visible    ${SAN_PHAM_MOI}    15s
    Click Element    ${SAN_PHAM_MOI}
    Sleep    3s

Chọn Sản Phẩm Và Mua Ngay
    Wait Until Page Contains Element    ${BUTTON_MUA_NGAY}    15s
    Scroll Element Into View            ${BUTTON_MUA_NGAY}
    Sleep                               1s
    Wait Until Element Is Visible       ${BUTTON_MUA_NGAY}    10s
    Click Element                       ${BUTTON_MUA_NGAY}

Điền Thông Tin Mua Hàng
    Wait Until Element Is Visible    ${TEN_KHACH_HANG}    15s
    Input Text    ${TEN_KHACH_HANG}      H Loet eban
    Input Text    ${EMAIL}               na9854@gmail.com
    Input Text    ${SDT}                 0901234567
    Input Text    ${DIA_CHI}             k502/h33/24a

    Wait Until Element Is Visible    ${SELECT_TINH_THANH}    15s
    Select From List By Label        ${SELECT_TINH_THANH}    TP. Đà Nẵng

    Wait Until Element Is Visible    ${SELECT_QUAN_HUYEN}    15s
    Select From List By Label        ${SELECT_QUAN_HUYEN}    Hải Châu

    Wait Until Element Is Visible    ${SELECT_PHUONG_XA}    15s
    Select From List By Label        ${SELECT_PHUONG_XA}     Hòa Cường Nam

    Wait Until Element Is Visible    ${BUTTON_TIEP_TUC_THANH_TOAN}    10s
    Click Element    ${BUTTON_TIEP_TUC_THANH_TOAN}
    Sleep    5s

Đóng Popup Nếu Có
    ${popup_exists}=    Run Keyword And Return Status    Element Should Be Visible    ${POPUP_CLOSE_BUTTON}    5s
    Run Keyword If    ${popup_exists}    Click Element    ${POPUP_CLOSE_BUTTON}
