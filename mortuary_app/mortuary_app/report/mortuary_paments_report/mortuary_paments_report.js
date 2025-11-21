// Copyright (c) 2025, hamza bawumia and contributors
// For license information, please see license.txt

// frappe.query_reports["Mortuary Paments Report"] = {
// 	"filters": [

// 	]
// };

frappe.query_reports["Mortuary Paments Report"] = {
    "filters": [
        {
            "fieldname": "from_date",
            "label": "From Date",
            "fieldtype": "Date",
            "default": frappe.datetime.add_days(frappe.datetime.get_today(), -30)
        },
        {
            "fieldname": "to_date",
            "label": "To Date",
            "fieldtype": "Date",
            "default": frappe.datetime.get_today()
        },
        {
            fieldname: "client_name",
            label: __("Client Name"),
            fieldtype: "Data",
            reqd: 0
        },
        {
            "fieldname": "received_by",
            "label": "Received By",
            "fieldtype": "Link",
            "options": "User",
            "reqd": 0
        },
        {
            fieldname: "payment_method",
            label: __("Payment Method"),
            fieldtype: "Select",
            options: "\nCash\nMobile Money\nCheque\nCredit Card\nWallet Account\nOther",
            reqd: 0
        }
    ]
}
