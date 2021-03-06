*** Settings ***
Documentation    Browsers Root Suite
Resource    ${CURDIR}/../keywords.library.resource
Suite Setup  launch browser
Suite Teardown  close and release values


*** Variables ***
${URL}          http://blazedemo.com/

*** Keywords ***
launch browser
    [Tags]    DEBUG
    ${driver} =   open browser    ${browser}
    open page   ${driver}   ${URL}
    ${title} =  get page title  ${driver}
    log to console  ${title}

    Set Global Variable     ${driver}

close and release values
    close browser   ${driver}
    
