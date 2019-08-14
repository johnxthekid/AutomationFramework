*** Settings ***
Documentation    Root suite for Notepad
Suite Setup  Open notepad app
Suite Teardown  Close notepad app
Library    pabot.PabotLib
Library     OperatingSystem

*** Keywords ***
Open notepad app
    [Tags]    DEBUG
    ${valuesetname}=    Acquire Value Set
    Log    ${valuesetname}
    ${HOST}=    Get Value From Set      HOST
    ${PORT}=    Get Value From Set      PORT
    Conditional Library Import  ${HOST}      ${PORT}

    ${notepad_id} =     open notepad
    Set Global Variable  ${APP_PATH}
    set global variable  ${notepad_id}
    Set Global Variable  ${HOST}
    Set Global Variable  ${PORT}

Conditional Library Import
    [Arguments]     ${HOST}=${EMPTY}     ${PORT}=${EMPTY}
    Run Keyword If  "${HOST}" != "${EMPTY}"
    ...     Import Library      Remote      http://${HOST}:${PORT}
    ...     ELSE
    ...     Import Library      ${APP_PATH}/apphelpers/SampleNotepadHelper.py

close notepad app
    user exit notepad   ${notepad_id}
    Release Value Set
