*** Settings ***
Library    SeleniumLibrary
Variables    locator.py

*** Variables ***
${Browser}    chrome    
${url}        https://lamthaocosmetics.vn/  

*** Keywords ***
Open Browsers
    Open Browser    ${url}    ${Browser}

Menu
    Wait Until Element Is Visible      ${menu_danhmucsp}  20s
    Mouse Over    ${menu_danhmucsp}
    Wait Until Element Is Visible    ${submenu_chamsocdamat}    20s
    Mouse Over    ${submenu_chamsocdamat}
    Wait Until Element Is Visible    ${link_matna89}    20s
    Click Element    ${link_matna89}

Select Any Product
    Click Element    ${product_item}
Add Product To Cart
    Wait Until Element Is Visible    ${add_product}    30s
    Scroll Element Into View    ${add_product}
    Click Element    ${add_product}

Click Buy Now
    Click Element    ${buy_now_button}


Fill In User Information 
    Input Text    ${full_name_input}    Nguyễn Nho Tường Vi
    Input Text    ${email_input}    nguyennhotuongvi@gmail.com
    Input Text    ${phone_input}    0898224770
    Input Text    ${address_input}    4 Phan Trong Tue
    Select From List By Label    ${province_select}    Đà Nẵng
    Select From List By Label    ${district_select}    Hải Châu
    Select From List By Label    ${ward_select}    Hoà Cường Nam 

Proceed To Payment Method
    Click Element    ${continue_to_payment_button}   
