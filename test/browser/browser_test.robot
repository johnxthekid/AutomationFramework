*** Settings ***
Documentation    sample test suite
Resource    ${KEYWORDLIBPATH}/keywords.library.resource

*** Test Cases ***
test sample actions on broswer
    [Tags]    DEBUG
    select departure city  ${driver}   Paris
    select destination city  ${driver}   London
    search for flights      ${driver}   
    @{results} =    get flight results      ${driver}   

    should not be empty  ${results}
    log to console  ${results}

