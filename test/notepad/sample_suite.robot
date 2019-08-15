*** Settings ***
Documentation    Sample suite for notepad test cases
Library  OperatingSystem

Suite Setup     Conditional Library Import  ${HOST}      ${PORT}


*** Keywords ***
Conditional Library Import
    [Arguments]     ${HOST}=${EMPTY}     ${PORT}=${EMPTY}
    Run Keyword If  "${HOST}" != "${EMPTY}"
    ...     Import Library      Remote      http://${HOST}:${PORT}
    ...     ELSE
    ...     Import Library  ${APP_PATH}/apphelpers/SampleNotepadHelper.py


*** Test Cases ***
sample test case scenario
    open submenu  ${notepad_id}   Edit  Replace
    ${new_title} =  get dialog title    ${notepad_id}
    log to console  ${new_title}
    close submenu
    open replace menu   ${notepad_id}
    close submenu
    type values  ${notepad_id}    ${CURDIR}
    ${editor_text} =    get editor value    ${notepad_id}
    log to console  ${editor_text}