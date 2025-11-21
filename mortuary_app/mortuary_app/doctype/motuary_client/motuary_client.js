// Copyright (c) 2025, hamza bawumia and contributors
// For license information, please see license.txt

frappe.ui.form.on("Motuary_Client", {
	refresh(frm) {

        // Show "Print Receipt" button if the record is saved
        if (!frm.is_new()) {  
            frm.add_custom_button("Make Mortuary Request(s)", function() {
                let new_form_url = `/app/mortuary-case/new`;
                window.open(new_form_url, "_blank");
                
            });
        }

	},
});
