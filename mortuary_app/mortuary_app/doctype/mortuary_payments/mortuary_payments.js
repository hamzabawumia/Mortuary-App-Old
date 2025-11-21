// frappe.ui.form.on("Mortuary_Payments", {
//     refresh: function(frm) {
//         if (!frm.is_new()) {  
//             frm.add_custom_button("Print Receipt", function() {
//                 let receipt_url = `/printview?doctype=Mortuary_Payments&name=${frm.doc.name}&format=Your Custom Print Format&no_letterhead=0`;
//                 window.open(receipt_url, "_blank");
//             });
//         }
//     }
// });


// frappe.ui.form.on("Mortuary_Payments", {
//     refresh: function(frm) {
//         if (!frm.is_new()) {  
//             // Add "Print Receipt" button
//             frm.add_custom_button("Print Receipt", function() {
//                 let receipt_url = `/printview?doctype=Mortuary_Payments&name=${frm.doc.name}&format=Your Custom Print Format&no_letterhead=0`;
//                 window.open(receipt_url, "_blank");
//             });

//             // Make specific fields read-only
//             let fields = ["invoice_id", "client_name", "amount_paid", "received_by"];
//             fields.forEach(field => frm.set_df_property(field, "read_only", 1));
//         }
//     }
// });

frappe.ui.form.on("Mortuary_Payments", {
    refresh: function(frm) {
        if (!frm.is_new()) {  
            // Add "Print Receipt" button
            frm.add_custom_button("Print Receipt", function() {
                let receipt_url = `/printview?doctype=Mortuary_Payments&name=${frm.doc.name}&format=Mortuary Payments Receipt&no_letterhead=0`;
                window.open(receipt_url, "_blank");
            });

            // Make specific fields read-only
            let fields = ["invoice_id", "client_name", "amount_paid", "received_by"];
            fields.forEach(field => frm.set_df_property(field, "read_only", 1));

            // Disable link behavior for "invoice_id"
            if (frm.fields_dict.invoice_id) {
                frm.fields_dict.invoice_id.$wrapper.find("a").removeAttr("href").css("pointer-events", "none");
            }
        }
    }
});
