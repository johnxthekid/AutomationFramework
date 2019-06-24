*** Settings ***
Documentation    Sample suite for notepad test cases
Library  ../../lib/frontend/apphelpers/SampleNotepadHelper.py
Library  OperatingSystem

*** Test Cases ***
sample test case scenario
    ${new_dlg} =    open submenu  ${notepad_instance}   Edit  Replace
    ${new_title} =  get dialog title    ${new_dlg}
    log to console  ${new_title}
    close replace menu
    open replace menu   ${notepad_instance}
    close replace menu
    type values  ${notepad_instance}    ${CURDIR}
    ${editor_text} =    get editor value    ${notepad_instance}
    log to console  ${editor_text}

*** Keywords ***
