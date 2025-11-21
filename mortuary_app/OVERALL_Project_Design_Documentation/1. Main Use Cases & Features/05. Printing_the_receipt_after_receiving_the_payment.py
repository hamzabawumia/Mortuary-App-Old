
USE CASE:
"""
Print the receipt after receiving the Payment
"""

AIM:
"""
As above
"""

ARCHITECTURAL PLAN:
"""
When the use clicks on receive payment the receipt should be automatically generated.

Code Details:
-------------------
Redirect to PrintOut upon saving a Record.

Add the script below to the doctype.js file
e.g. frappe-bench/apps/mortuary_app/mortuary_app/mortuary_app/doctype/mortuary_payments/mortuary_payments.js

frappe.ui.form.on("Mortuary_Payments", {
    after_save: function(frm) {
        // Automatically open receipt after saving
        let receipt_url = `/printview?doctype=Mortuary_Payments&name=${frm.doc.name}&format=Your Custom Print Format&no_letterhead=0`;
        window.open(receipt_url, "_blank");
    },

    refresh: function(frm) {
        // Show "Print Receipt" button only if the record is saved
        if (!frm.is_new()) {  
            frm.add_custom_button("Print Receipt", function() {
                let receipt_url = `/printview?doctype=Mortuary_Payments&name=${frm.doc.name}&format=Your Custom Print Format&no_letterhead=0`;
                window.open(receipt_url, "_blank");
            });
        }
    }
});

// How It Works
// After Saving (after_save)

// The receipt automatically opens after saving.

// On Form Load (refresh)

// If the record is already saved, show the "Print Receipt" button.

// If the record is new (not yet saved), the button does not appear.
"""

User Navigation / nav_links:
"""
View Mortuary Requests --> Select the Patient's Name & Open the Invoice --> Click Receive Payments
"""

URL:
"""

"""

View:
"""

"""

Template:
"""

"""

Models Involved:
"""
The details are passed from the "Mortuary Request" to the "Mortuary Payments" Model
"""

# Start implementing the use case logic here
