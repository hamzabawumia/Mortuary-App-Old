# Copyright (c) 2025, hamza bawumia and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class MortuaryCase(Document):

    def validate(self):
        """Prevent editing if the case is already paid"""
        if self.paid:
            frappe.throw("This case has already been paid for and cannot be edited.", frappe.PermissionError)


@frappe.whitelist()
def update_totals(doc, event):
    total = 0
    for item in doc.get("table_nrzn", []):
        if item.items:
            item_doc = frappe.get_doc("List of Items and Services", item.items)
            item.amount = float(item_doc.selling_price) * float(item.quantity)
            total += item.amount

    doc.grand_total = total
