ChangeLog
=================
# Changelog

All notable changes to this app will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

New Changes shall remain at the top of this document while older changes shall be recorded below.

Standard for documenting changes to any software.

1. Create a text file and document your changes inside the file. 
   Give a meaningful name to the file.

2. The documentation should contain the following ; 
    a. List of files you editted
    b. The Reason or Aim for the changes.
    c. Explain the exact changes you made so that the steps can be re-traced by another person
    or copy and paste the code you changed 

Note that; If you are not willing to document your changes then don't make any changes.

3. Git Messages:
    You can now copy the block of changes and paste it into message.txt 
    Then run:
        git commit -F changelogs/git_commit_message.txt


=================
Date: 24_JULY_2024 = {


    # ADDED (New Feature): 
    '''
    USE CASE OR FEATURE
    -------------------
        # put your use case here:


    File(s) & Function(s)/Method(s) added:
    ----------------------------------------
    # list your file names and functions here lik so:
        pharmacy_stores.admin.py.
            Pharmacy_Stores_Requisition_and_Issuance2InlineAdmin.get_readonly_fields()

        stores/admin.py
            Requisition_and_Issuance2InlineAdmin.get_readonly_fields()


    REASON / AIM
    -------------


    EXACT CHANGE:
    -------------
    [


    ]

    '''

    # CHANGED (Feature Change):

    '''
    USE CASE
    --------
        Approving Requisitions @ pharmacy stores and general stores


    File(s) & Function(s)/Method(s) editted:
    ----------------------------------------
        pharmacy_stores.admin.py.
            Pharmacy_Stores_Requisition_and_Issuance2InlineAdmin.get_readonly_fields()

        stores/admin.py
            Requisition_and_Issuance2InlineAdmin.get_readonly_fields()


    REASON / AIM
    -------------
    The above code was editted because Ho Royal Hospital wanted the approver to be able to 
    edit the "quantity_required".
    Thereby allowing them to approve lesser quantities than what has been requested.

    EXACT CHANGE:
    -------------
    [
        'item_name_id','unit_of_issue',# 'quantity_required',
        # Ho Royal Hospital wanted the approver to be able to edit the "quantity_required"
        # so that they can approve lesser quantities than what has been requested.

    ]

    '''

    # REMOVED (Feature Removal):
    '''
    USE CASE OR FEATURE
    -------------------

    File(s) & Function(s)/Method(s) added:
    ----------------------------------------

    REASON / AIM
    -------------

    EXACT CHANGE:
    -------------
    [

    ]

    '''

    # FIXED (Bug Fix):

    '''
    USE CASE OR FEATURE
    -------------------

    File(s) & Function(s)/Method(s) added:
    ----------------------------------------

    REASON / AIM
    -------------

    EXACT CHANGE:
    -------------
    [

    ]

    '''

    # SECURITY (Security Fix):

    '''
    USE CASE OR FEATURE
    -------------------

    File(s) & Function(s)/Method(s) added:
    ----------------------------------------

    REASON / AIM
    -------------

    EXACT CHANGE:
    -------------
    [

    ]

    '''
}

xxxxxxxxxxxxxxxxx

