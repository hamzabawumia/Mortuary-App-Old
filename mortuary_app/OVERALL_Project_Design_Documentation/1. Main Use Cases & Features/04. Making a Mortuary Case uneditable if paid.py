
--------
USE CASE = 
"""
Making a Mortuary Case uneditable if paid """
--------


--------
ARCHITECTURAL PLAN:
--------    
""" 
To achieve this functionality in Frappe, you can follow these steps:

1. Add the "PAID" Field to the Mortuary Case Doctype


2. Set "PAID" Status When a Payment is Made
Modify the Mortuary_Payments Doctype's controller (Python file) 
to update the paid field in Mortuary Case when a payment is recorded.

Update mortuary_payments.py (Controller for Mortuary Payments)

import frappe
from frappe.model.document import Document


class Mortuary_Payments(Document):

    def after_insert(self):
        """Update MortuaryCase status to PAID when a payment is made"""
        if self.invoice_id:
            frappe.db.set_value("Mortuary Case", self.invoice_id, "paid", 1)
            frappe.db.commit()


    def validate(self):
        """THE ACTUAL VALIDATION IS BE DONE IN THE Mortuary Case doctype"""
        this prevents any editing or saving if paid is True
"""
