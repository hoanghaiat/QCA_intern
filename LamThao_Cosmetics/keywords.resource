*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    BuiltIn   
Variables    locator.py


*** Variables ***
${URL}   https://lamthaocosmetics.vn/
${BROWSER}     chrome


*** Keywords ***

Open Browsers
    Open Browser    ${URL}    ${BROWSER}


Handle Advertise
    ${check}=    Run Keyword And Return Status    Wait Until Element Is Visible    //button[@class='close close-popup-contact']    5s
    IF    "${check}" == "True"
        Click Button    //button[@class='close close-popup-contact']
    END
     

Menu
    Handle Advertise

    Wait Until Element Is Visible    ${url_menu_danhmucsp}    30s
    Mouse Over    ${url_menu_danhmucsp}
    Wait Until Element Is Visible    ${url_menu_product}    30s
    Mouse Over    ${url_menu_product}
    Wait Until Element Is Visible    ${url_type_product}    30s
    Click Element    ${url_type_product}

Product Information
    Wait Until Element Is Visible    ${url_product}    30s
    Scroll Element Into View    ${url_product}
    Click Element    ${url_product}

Add Product To Cart
    Wait Until Element Is Visible    ${url_add_product}    30s
    Scroll Element Into View    ${url_add_product}
    Click Element    ${url_add_product}

Payment
    Wait Until Element Is Visible    ${url_payment}    30s
    Scroll Element Into View    ${url_payment}
    Click Element    ${url_payment}

Delivery Information
    Wait Until Element Is Visible    ${fullname_input}    30s
    Input Text    ${fullname_input}    NguyenPhuongLy
    Input Text    ${email_input}    phuongly@gmail.com
    Input Text    ${phone_input}    0708079579
    Input Text    ${address_input}    Tiên Sơn 9
    Select From List By Label   ${province_select}    Đà Nẵng
    Wait Until Element Contains    ${district_select}    Quận Hải Châu    30s
    #Sleep    30s
    Select From List By Label    ${district_select}    Quận Hải Châu
    Wait Until Element Contains    ${ward_select}    Phường Hòa Cường Nam    30s
    #    30s
    Select From List By Label    ${ward_select}    Phường Hòa Cường Nam
    Wait Until Element Contains    ${ward_select}    Phường Hòa Cường Nam    30s

    Scroll Element Into View    //form[@id='form_next_step']
    Wait Until Keyword Succeeds    30s    1s   Click Button    ${submit_btn}

CheckOut Complete
    Wait Until Element Is Visible    ${checkout_complete_btn}    30s
    Scroll Element Into View    ${checkout_complete_btn}

Go Back Home
    Wait Until Element Is Visible    //div[@class='main-header']//following-sibling::h1[@class='logo-text']    30s
    Click Element    //div[@class='main-header']//following-sibling::h1[@class='logo-text']
    
