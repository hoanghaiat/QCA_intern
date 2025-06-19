*** Settings ***
Library    SeleniumLibrary
Variables  locator.py

*** Variables ***
${Browser}    chrome    
${url}        https://lamthaocosmetics.vn/  

*** Keywords ***

Open Browsers
    Open Browser    ${url}    ${Browser}
    Maximize Browser Window
    Wait Until Page Contains Element    ${menu_danhmucsp}    30s
Handle Advertise
    ${check}=    Run Keyword And Return Status    Wait Until Element Is Visible    //button[@class='close close-popup-contact']    5s
    IF    ${check}
        Click Button    //button[@class='close close-popup-contact']
    END


Menu
    Wait Until Element Is Visible    ${menu_danhmucsp}    30s
    Mouse Over    ${menu_danhmucsp}
    Wait Until Element Is Visible    ${submenu_chamsocdamat}    30s
    Mouse Over    ${submenu_chamsocdamat}
    Wait Until Element Is Visible    ${link_son}    30s
    Scroll Element Into View         ${link_son}
    Wait Until Element Is Enabled    ${link_son}    10s
    Click Element                    ${link_son}

Select Any Product
    Wait Until Element Is Visible    ${product_item}    30s
    Scroll Element Into View         ${product_item}
    Click Element                    ${product_item}

Add Product To Cart
    Wait Until Element Is Visible    ${add_product}    30s
    Scroll Element Into View         ${add_product}
    Wait Until Element Is Enabled    ${add_product}    10s
    Click Element                    ${add_product}

Click Buy Now
    Wait Until Element Is Visible    ${buy_now_button}    20s
    Scroll Element Into View         ${buy_now_button}
    Click Element                    ${buy_now_button}

Fill In User Information 
    Wait Until Element Is Visible    ${full_name_input}    20s
    Input Text    ${full_name_input}    Nguyễn Nho Tường Vi
    Input Text    ${email_input}        nguyennhotuongvi@gmail.com
    Input Text    ${phone_input}        0898224770
    Input Text    ${address_input}      4 Phan Trong Tuệ

  
    Select From List By Label         ${province_select}    Đà Nẵng
    Wait Until Page Contains          Hải Châu              10s

   
    Wait Until Element Is Visible     ${district_select}    10s
    Select From List By Label         ${district_select}    Quận Hải Châu
    Wait Until Page Contains          Hòa Cường Nam         10s

   
    Wait Until Element Is Visible     ${ward_select}        10s
    Select From List By Label         ${ward_select}        Phường Hòa Cường Nam

Proceed To Payment Method
    Wait Until Element Is Visible    ${continue_to_payment_button}    20s
    Scroll Element Into View         ${continue_to_payment_button}
    Wait Until Element Is Enabled    ${continue_to_payment_button}    10s
    Click Element                    ${continue_to_payment_button}
