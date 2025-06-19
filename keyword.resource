*** Settings ***
Library           SeleniumLibrary
Library           Collections
Library           BuiltIn
Variables         locator.py

*** Keywords ***

open_browsers
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    close_advertise_popup

close_advertise_popup
    ${popup_visible}=    Run Keyword And Return Status    Wait Until Element Is Visible    ${advertise_close_button}    5s
    IF    '${popup_visible}' == 'True'
        Click Element    ${advertise_close_button}
    END

navigate_to_product_category
    close_advertise_popup
    Wait Until Element Is Visible    ${menu_category}        20s
    Mouse Over                       ${menu_category}
    Wait Until Element Is Visible    ${menu_skincare}        10s
    Click Element                    ${menu_skincare}

select_product
    Wait Until Element Is Visible    ${product_link}         20s
    Scroll Element Into View         ${product_link}
    Click Element                    ${product_link}

add_to_cart
    Wait Until Element Is Visible    ${add_to_cart_button}   20s
    Scroll Element Into View         ${add_to_cart_button}
    Click Element                    ${add_to_cart_button}

proceed_to_checkout
    Wait Until Element Is Visible    ${proceed_to_checkout_button}    20s
    Scroll Element Into View         ${proceed_to_checkout_button}
    Click Element                    ${proceed_to_checkout_button}

fill_delivery_information
    Wait Until Element Is Visible    ${input_fullname}    20s
    Input Text                       ${input_fullname}    hloeteban
    Input Text                       ${input_email}       eban@gmail.com
    Input Text                       ${input_phone}       0962457584
    Input Text                       ${input_address}     k502/h33/24a đường 2/9

    Select From List By Label        ${select_province}    Đà Nẵng
    Wait Until Element Contains      ${select_district}    Quận Hải Châu    20s
    Select From List By Label        ${select_district}    Quận Hải Châu
    Wait Until Element Contains      ${select_ward}        Phường Hòa Cường Nam    20s
    Select From List By Label        ${select_ward}        Phường Hòa Cường Nam

    Scroll Element Into View         ${submit_button}
    Wait Until Keyword Succeeds      30s    1s    Click Element    ${submit_button}

confirm_order
    Wait Until Element Is Visible    ${confirm_order_button}    20s
    Scroll Element Into View         ${confirm_order_button}
    Click Element                    ${confirm_order_button}

return_to_homepage
    Wait Until Element Is Visible    ${home_logo}    20s
    Click Element                    ${home_logo}
