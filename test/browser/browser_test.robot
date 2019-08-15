*** Settings ***
Documentation    sample test suite
Library    pabot.PabotLib
Suite Setup     Conditional Library Import    ${HOST}  ${PORT}

*** Test Cases ***
test sample actions on broswer
    [Tags]    DEBUG
    select departure city  ${driver}   Paris
    select destination city  ${driver}   London
    search for flights      ${driver}   
    @{results} =    get flight results      ${driver}   

    should not be empty  ${results}
    log to console  ${results}



*** Keywords ***
Conditional Library Import
    [Arguments]     ${HOST}=${EMPTY}     ${PORT}=${EMPTY}
    Run Keyword If  "${HOST}" != "${EMPTY}"
    ...     Import Library      Remote      http://${HOST}:${PORT}
    ...     ELSE
    ...     Import Library  ${BROWSER_PATH}/pageobjectmodels/DemoMainPage.py    