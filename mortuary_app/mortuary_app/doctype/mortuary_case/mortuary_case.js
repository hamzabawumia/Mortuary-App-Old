// Copyright (c) 2025, hamza bawumia and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Mortuary Case", {
// 	refresh(frm) {

// 	},
// });


frappe.ui.form.on("Mortuary Case", {
    refresh: function(frm) {
        if (!frm.is_new() && !frm.doc.paid) {
            // Add "Print Receipt" button
            frm.add_custom_button("Receive Payment", function() {

            createMortuaryPayment(frm.doc.name, frm.doc.patient__cient, frm.doc.grand_total)
            // this function is located @
            // "/home/hamza/frappe-bench/apps/mortuary_app/mortuary_app/public/js"

            });


        }


        // 2. Make all fields read-only if paid
        if (frm.doc.paid) {
            frm.fields_dict &&
            Object.keys(frm.fields_dict).forEach(fieldname => {
                frm.set_df_property(fieldname, "read_only", 1);
            });
            frm.refresh_fields();
        }




    }
});
