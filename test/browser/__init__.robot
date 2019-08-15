*** Settings ***
Documentation    Browsers Root Suite
Library    pabot.PabotLib
Library     OperatingSystem
Suite Setup  launch browser
Suite Teardown  close and release values


*** Variables ***
${URL}          http://blazedemo.com/

*** Keywords ***
launch browser
    [Tags]    DEBUG
    ${valuesetname}=    Acquire Value Set
    Log    ${valuesetname}
    ${browser}=     Get Value From Set   BROWSER
    ${HOST}=    Get Value From Set      HOST
    ${PORT}=    Get Value From Set      PORT
    Log    ${browser}

    Conditional Library Import  ${HOST}  ${PORT}
    ${driver} =   open browser    ${browser}
    open page   ${driver}   ${URL}
    ${title} =  get page title  ${driver}
    log to console  ${title}

    Set Global Variable     ${driver}
    Set Global Variable     ${HOST}
    Set Global Variable     ${PORT}
    Set Global Variable     ${BROWSER_PATH}

Conditional Library Import
    [Arguments]     ${HOST}=${EMPTY}     ${PORT}=${EMPTY}
    Run Keyword If  "${HOST}" != "${EMPTY}"
    ...     Import Library      Remote      http://${HOST}:${PORT}
    ...     ELSE
    ...     Import Library  ${BROWSER_PATH}/pageobjectmodels/DemoMainPage.py

close and release values
    close browser   ${driver}
    Release Value Set
    
