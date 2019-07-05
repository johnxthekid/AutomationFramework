*** Settings ***
Documentation    sample test suite
Library  ../../lib/browsers/drivermanagers/BrowserManager.py    ${BROWSER}
Library  ../../lib/browsers/pageobjectmodels/DemoMainPage.py    ${driver}

*** Test Cases ***
test sample actions on broswer
    [Tags]    DEBUG
    select departure city  Paris
    select destination city  London
    search for flights
    @{results} =    get flight results
    should not be empty  ${results}
    log to console  ${results}
