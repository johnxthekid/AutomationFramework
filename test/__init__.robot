*** Settings ***
Documentation    Root Suite for all test
Library     pabot.PabotLib
Library     ${CURDIR}/../lib/utils/RemoteServerListener.py
Suite Teardown  reset values

*** Variables ***
${KeywordLibrary}       ${CURDIR}/../lib/utils/AllKeywordsLibrary.py
${Server_URI}           Local Libraries
${HOST}                 ${EMPTY}
${PORT}                 ${EMPTY}

*** Keywords ***
get arguments
    Set Global Variable    ${Server_URI}
    Set Global Variable    ${KeywordLibrary}

    Run Keyword If  "${RUN_LOCATION}" == "remote"
    ...     Set Remote Library

    Set Global Variable     ${BROWSER}
    log to console          Sever URI: ${Server_URI}
    log to console          Run Library: ${KeywordLibrary}

Set Remote Library
    ${valuesetname}=    Acquire Value Set
    ${browser}=     Get Value From Set   BROWSER
    ${HOST}=    Get Value From Set      HOST
    ${PORT}=    Get Value From Set      PORT


    Set Global Variable     ${BROWSER}
    log to console          Browser: ${BROWSER}
    Set Global Variable     ${HOST}
    log to console          HOST: ${HOST}
    Set Global Variable     ${PORT}
    log to console          PORT: ${PORT}

    ${KeywordLibrary}=   Set Variable            Remote
    ${Server_URI}=      Set Variable            http://${HOST}:${PORT}
    Set Global Variable    ${Server_URI}
    Set Global Variable    ${KeywordLibrary}

reset values
    Run Keyword and Ignore Error   Release Value Set