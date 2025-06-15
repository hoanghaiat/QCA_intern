*** Settings ***
Library  SeleniumLibrary
Variables    locator.py
Resource    keywords.resource

*** Test Cases ***
CheckOut
    Open Browsers
    Date time
    Wall Area
    Paint Type
    Sketch
   