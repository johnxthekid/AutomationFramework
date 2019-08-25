*** Settings ***
Documentation    Root Suite for all test
Library     pabot.PabotLib
Library     ${CURDIR}/../lib/utils/RemoteServerListener.py
# Suite Setup     get arguments
Suite Teardown  reset values

*** Variables ***
${KEYWORDLIBPATH}       ${CURDIR}
${KeywordLibrary}       ${CURDIR}/../lib/utils/AllKeywordsLibrary.py
${RunLocation}          Local Libraries
${HOST}                 ${EMPTY}
${PORT}                 ${EMPTY}

*** Keywords ***
get arguments
    Set Global Variable    ${RunLocation}
    Set Global Variable    ${KeywordLibrary}

    Run Keyword and Ignore Error    get resource values
    Run Keyword If  "${HOST}" != "${EMPTY}"
    ...     Set Remote Library

    Set Global Variable     ${KEYWORDLIBPATH}
    Set Global Variable     ${browser}
    log to console          ${RunLocation}
    log to console          Run Library: ${KeywordLibrary}

    # Import Resource     ${CURDIR}/keywords.library.resource

get resource values
    ${valuesetname}=    Acquire Value Set
    # ${CURRENT_TAG}=     Get Value From Set  tags
    ${browser}=     Get Value From Set   BROWSER
    ${HOST}=    Get Value From Set      HOST
    ${PORT}=    Get Value From Set      PORT


    Set Global Variable     ${BROWSER}
    log to console          Browser: ${BROWSER}
    Set Global Variable     ${HOST}
    log to console          HOST: ${HOST}
    Set Global Variable     ${PORT}
    log to console          PORT: ${PORT}

Set Remote Library
    ${KeywordLibrary}=   Set Variable            Remote
    ${RunLocation}=      Set Variable            http://${HOST}:${PORT}
    Set Global Variable    ${RunLocation}
    Set Global Variable    ${KeywordLibrary}

reset values
    Run Keyword and Ignore Error   Release Value Set