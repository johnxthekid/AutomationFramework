*** Settings ***
Documentation    Browsers Root Suite
Library    pabot.PabotLib
Library  ../../lib/browsers/drivermanagers/BrowserManager.py    #${BROWSER}
Suite Setup  launch browser
Suite Teardown  close browser

*** Variables ***
${URL}          http://blazedemo.com/
${BROWSER}      chrome

*** Keywords ***
launch browser
    [Tags]    DEBUG
    ${valuesetname}=    Acquire Value Set
    Log    ${valuesetname}
    ${browser}=     Get Value From Set   browser
    Log    ${browser}
    
    set_browser_instance    ${browser}
    open page   ${URL}
    ${title} =  get page title
    log to console  ${title}
    should match  ${title}  BlazeDemo

    ${driver}   get browser instance
    Set Global Variable     ${browser}
    Set Global Variable     ${driver}
