# Copyright (c) 2025, hamza bawumia and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Mortuary_Payments(Document):

    # def on_submit(self):
    #     """Update MortuaryCase status to PAID when a payment is made"""
    #     if self.invoice_id:
    #         frappe.db.set_value("MortuaryCase", self.invoice_id, "paid", 1)
    # on_submit didn't work at all

    # def after_insert((self):
    #     """Update MortuaryCasestatus to PAID when a payment is made"""
    #     if self.invoice_id:
    #         mortuary_case = frappe.get_doc("MortuaryCase", self.invoice_id)
    #         mortuary_case.paid = 1
    #         frappe.db.commit()

    def after_insert(self):
        """Update MortuaryCase status to PAID when a payment is made"""
        if self.invoice_id:
            frappe.db.set_value("Mortuary Case", self.invoice_id, "paid", 1)
            frappe.db.commit()