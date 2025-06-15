*** Settings ***
Library  SeleniumLibrary
Library    Collections
Library    BuiltIn

Variables   locator.py

*** Variables ***
${URL}            http://127.0.0.1:5500/Booking.html
${BROWSER}        chrome
${url_booking}    //span[text()='PLAN YOUR VISIT']
${ROOM_SINGLE_LIST}=    Create Room List
${ROOM_COUPLE_LIST}=    Create Room List
${ROOM_WALL_LIST}=    Create Room List Wall
${IMG_LIST}=    Create Image List
@{NEXT_PAGE}=    Create Next Page List
@{COLOR_NAMES}    White    Red    Green    Pink    Gray    Blue    Orange    Yellow    Purple    Black    Pastel    Brown

*** Keywords ***
Open Browsers
    Open Browser    ${URL}    ${BROWSER}
      
Date time
    Wait Until Element Is Visible    ${date_input}    30s
    Scroll Element Into View    ${date_input}
    Input Text    ${date_input}    08-06-2025
    Input Text    ${time_input}    09:30
    Click Button    ${next_btn}

Wall Area
    Wait Until Element Is Visible    ${single_room_btn}    30s
    Random Rooms Single
    Random Rooms Couple
    Random Rooms Wall
    Click Button    ${next_btn}

Paint Type
    Wait Until Element Is Visible    ${water_color}    30s
    Scroll Element Into View    ${water_color}
    Click Element    ${water_color}
    Scroll Element Into View    ${white_color}
    Click Random Paint Colors
    Scroll Element Into View    ${next_btn}
    Click Button    ${next_btn}

Sketch
    Random Page Image
    Random Image
    Scroll Element Into View    ${next_btn}
    Click Button    ${next_btn}
 
Create Room List
    ${room_list}=    Create List
    FOR    ${i}    IN RANGE    1    17
        ${room}=    Evaluate    "ROOM {:02}".format(${i})
        Append To List    ${room_list}    ${room}
    END
    RETURN   ${room_list}
Create Room List Wall
    ${room_list}=    Create List
    FOR    ${i}    IN RANGE    1    17
        ${room}=    Evaluate    "WALL {:02}".format(${i})
        Append To List    ${room_list}    ${room}
    END
    RETURN   ${room_list}

Create Image List
    ${img_list}=    Create List
    FOR    ${i}    IN RANGE    1    9
        ${img}=    Evaluate    "image_{}".format(${i})
        Append To List    ${img_list}    ${img}
    END
    RETURN    ${img_list}

Create Next Page List
    ${page_list}=    Create List
    FOR    ${i}    IN RANGE    1    5
        ${page}=    Set Variable    ${i}
        Append To List    ${page_list}    ${page}
    END
    RETURN    ${page_list}

Random Rooms Single
    ${ROOM_SINGLE_LIST}=    Create Room List
    ${room_id}=       Evaluate    random.choice(${ROOM_SINGLE_LIST})    modules=random
    ${room_xpath}=    Set Variable     //div[@id='single-rooms-container']//button[normalize-space(text())='${room_id}']
    Wait Until Element Is Visible    ${room_xpath}    30s
    Click Button    ${room_xpath}

Random Rooms Couple
    ${ROOM_COUPLE_LIST}=    Create Room List
    ${rooms_id}=            Evaluate    random.choice(${ROOM_COUPLE_LIST})    modules=random
    ${rooms_xpath}=         Set Variable    //div[@id='couple-rooms-container']//button[normalize-space(text())='${rooms_id}']
    Wait Until Element Is Visible    ${rooms_xpath}    30s
    Click Button            ${rooms_xpath}

Random Rooms Wall
    ${ROOM_WALL_LIST}=     Create Room List Wall
    ${room_wall_id}=       Evaluate    random.choice(${ROOM_WALL_LIST})    modules=random
    ${room_wall_xpath}=    Set Variable    //div[@id='walls-container']//button[normalize-space(text())='${room_wall_id}']
    Wait Until Element Is Visible    ${room_wall_xpath}    30s
    Scroll Element Into View    ${room_wall_xpath}
    Click Button    ${room_wall_xpath}
Click Random Paint Colors
    ${color_count}=     Get Length    ${COLOR_NAMES}
    ${pick_count}=      Evaluate    min(6, ${color_count})
    @{random_colors}=   Evaluate    random.sample(${COLOR_NAMES}, ${pick_count})    modules=random
    FOR    ${color}     IN    @{random_colors}
        ${color_xpath}=    Set Variable    //div[contains(text(),'${color}')]
        Scroll Element Into View    ${color_xpath}
        Click Element               ${color_xpath}
    END
Random Image
    @{IMG_LIST}=        Create Image List
    ${img_id}=          Evaluate    random.choice(${IMG_LIST})    modules=random
    ${img_xpath}=       Set Variable    //img[@class='${img_id}']
    Wait Until Element Is Visible    ${img_xpath}    30s
    Scroll Element Into View    ${img_xpath}
    Click Element        ${img_xpath}
    
Random Page Image
   @{NEXT_PAGE}=    Create Next Page List
    ${page_id}=      Evaluate    random.choice(${NEXT_PAGE})    modules=random
    ${page_xpath}=   Set Variable    //button[text()='${page_id}']
    Wait Until Element Is Enabled    ${page_xpath}    30s
    Scroll Element Into View         ${page_xpath}
    Click Button                     ${page_xpath}
  
   
 
    




    


