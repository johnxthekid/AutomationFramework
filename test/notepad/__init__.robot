*** Settings ***
Documentation    Root suite for Notepad
Suite Setup  Open notepad app
Suite Teardown  Close notepad app
Library    pabot.PabotLib
Resource    ${KEYWORDLIBPATH}/keywords.library.resource

*** Keywords ***
Open notepad app
    [Tags]    DEBUG
    ${notepad_id} =     open notepad
    set global variable  ${notepad_id}

close notepad app
    user exit notepad   ${notepad_id}
