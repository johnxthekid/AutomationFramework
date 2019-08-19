*** Settings ***
Documentation    Sample suite for notepad test cases
Resource    ${KEYWORDLIBPATH}/keywords.library.resource

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