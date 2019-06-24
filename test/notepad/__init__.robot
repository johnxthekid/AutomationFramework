*** Settings ***
Documentation    suite initialize file
Suite Setup  Open notepad app
Suite Teardown  Close notepad app
Library  ../../lib/frontend/apphelpers/SampleNotepadHelper.py

*** Keywords ***
Open notepad app
    ${notepad_instance} =  open notepad
    set global variable  ${notepad_instance}

close notepad app
    user exit notepad   ${notepad_instance}
