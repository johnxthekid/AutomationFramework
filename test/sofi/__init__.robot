*** Settings ***
Documentation    Browsers Root Suite
Resource    ${CURDIR}/../keywords.library.resource
Suite Setup  launch browser
Suite Teardown  close and release values


*** Variables ***
${URL}          http://sofi.com/

*** Keywords ***
launch browser
    [Tags]    DEBUG
    open browser    ${browser}
    open page   ${URL}
    verify sofi page loaded

close and release values
    close browser