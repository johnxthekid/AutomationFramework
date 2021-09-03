*** Settings ***
Documentation    Login to Sofi
Library     Dialogs
Resource    ${CURDIR}/../keywords.library.resource

*** Test Cases ***
Login to Sofi
    [Tags]    DEBUG
    goto sofi login page
    ${username} =	Get Value From User	    Input user name
    ${password} =	Get Value From User	    Input password	    hidden=yes
    login to sofi   ${username}     ${password}