*** Settings ***
Documentation    Login to Sofi
Library     Dialogs
Resource    ${CURDIR}/../keywords.library.resource

*** Test Cases ***
Login to Sofi
    [Tags]    DEBUG
    goto sofi login page
    login to sofi   %{sofi_user}     %{sofi_password}
    logout