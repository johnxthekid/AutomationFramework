*** Settings ***
Documentation    Browsers Root Suite
Library  ../../lib/browsers/drivermanagers/BrowserManager.py    ${BROWSER}
Suite Setup  launch browser
Suite Teardown  close browser

*** variables ***
${URL}          http://blazedemo.com/
${BROWSER}      chrome

*** keywords ***
launch browser
    [Tags]    DEBUG
    open page   ${URL}
    ${title} =  get page title
    log to console  ${title}
    should match  ${title}  BlazeDemo

    ${driver}   get browser instance
    Set Global Variable     ${BROWSER}
    Set Global Variable     ${driver}
