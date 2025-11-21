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

    # CHANGED (Feature Change):

    '''
    USE CASE
    --------
        Editted booked consultation to be readonly once paid - especially at Records Department


    File(s) & Function(s)/Method(s) editted:
    ----------------------------------------
        smcapp1.read_only_admin_inlines.py
            Consultation_BridgeInline2_ReadOnly_Admin()

        smcapp1/admin.py
            Consultation_BridgeInline2()

        smcapp1/admin.py
            class RecordsConsultationDetailsAdmin(TabbedModelAdmin):

    REASON / AIM
    -------------
    The above code was editted because GAEC Records people keep changing 
    the booked consultation even when paid - this then adjusts the price on the receipt
    with the new consultation, causing inconsistences. 


    EXACT CHANGE:
    -------------
    [
        Added the Consultation_BridgeInline2_ReadOnly_Admin()

        Editted the get_queryset() for Consultation_BridgeInline2() to filter for  ...

                def get_queryset(self, request):
                
                return super(Consultation_BridgeInline2, self).get_queryset(
                request).only(    
                    'item_name_id',
                    'unit_price', 
                    'amount',).filter(
                        Q(paid=False) & Q(nhis_co_payment_paid=False))

        Added the Consultation_BridgeInline2_ReadOnly_Admin to the 
        class RecordsConsultationDetailsAdmin(TabbedModelAdmin):


        Commented out the readonly_fields attribute and add the get_readonly_fields()

                def get_readonly_fields(self, request, obj=None):
                    # Check if obj is None (indicating we are in "Add" mode)
                    if obj is None:
                        # When adding a new patient, no fields are read-only
                        return ["consultation_booked_by",]
                    
                    # If obj is not None, we are in edit mode
                    # Make patient_id read-only
                    return ["consultation_booked_by",'patient_ID']

    ]

    '''


}

xxxxxxxxxxxxxxxxx

