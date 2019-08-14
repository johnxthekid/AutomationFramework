*** Settings ***
Documentation    Root Suite for all test
Suite Setup     get arguments

*** Variables ***
${BROWSER_PATH}     ${CURDIR}/../lib/browsers
${APP_PATH}     ${CURDIR}/../lib/frontend

*** keywords ***
get arguments
    Set Global Variable    ${BROWSER_PATH}
    Set Global Variable    ${APP_PATH}
