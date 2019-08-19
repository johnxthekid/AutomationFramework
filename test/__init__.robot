*** Settings ***
Documentation    Root Suite for all test
Library    pabot.PabotLib
Suite Setup     get arguments
Suite Teardown  Run Keyword and Ignore Error   Release Value Set

*** Variables ***
${KEYWORDLIBPATH}       ${CURDIR}
${KeywordLibrary}       ${CURDIR}/../lib/utils/AllKeywordsLibrary.py
${RunLocation}          Local Libraries
${HOST}                 ${EMPTY}
${PORT}                 ${EMPTY}

*** Keywords ***
get arguments
    Run Keyword and Ignore Error    get resource values
    Run Keyword If  "${HOST}" != "${EMPTY}"
    ...     Set Remote Library

    Set Global Variable    ${KEYWORDLIBPATH}
    Set Global Variable    ${RunLocation}
    Set Global Variable    ${KeywordLibrary}
    Set Global Variable    ${browser}

    Import Resource     ${CURDIR}/keywords.library.resource

get resource values
    ${valuesetname}=    Acquire Value Set
    Log    ${valuesetname}
    ${browser}=     Get Value From Set   BROWSER
    ${HOST}=    Get Value From Set      HOST
    ${PORT}=    Get Value From Set      PORT

    Set Global Variable     ${BROWSER}
    Set Global Variable     ${HOST}
    Set Global Variable     ${PORT}

Set Remote Library
    Set Variable      ${KeywordLibrary}      Remote
    Set Variable      ${RunLocation}         http://${HOST}:${PORT}