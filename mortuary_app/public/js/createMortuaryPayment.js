// function createMortuaryPayment(mortuary_case, patient, grand_total) {

//     console.log("Mortuary Case:", mortuary_case);
//     console.log("Patient:", patient);
//     console.log("Grand Total:", grand_total);

//     frappe.new_doc('Mortuary_Payments', {
//         invoice_id: mortuary_case,
//         client_name: patient,
//         amount_paid: grand_total
//     });
// }

// function createMortuaryPayment(mortuary_case, patient, grand_total) {
//     console.log("Mortuary Case:", mortuary_case);
//     console.log("Patient:", patient);
//     console.log("Grand Total (before conversion):", grand_total); 

//     // Ensure grand_total is correctly converted to a number
//     let amountPaid = parseFloat(grand_total.replace(/,/g, '')) || 0; 

//     console.log("Grand Total (after conversion):", amountPaid); 

//     frappe.new_doc('Mortuary_Payments', {
//         invoice_id: mortuary_case,
//         client_name: patient,
//         amount_paid: amountPaid // Store as a number
//     });
// }

// function createMortuaryPayment(mortuary_case, patient, grand_total) {
//     console.log("Mortuary Case:", mortuary_case);
//     console.log("Patient:", patient);
//     console.log("Grand Total (before conversion):", grand_total);

//     let amountPaid = parseFloat(grand_total.replace(/,/g, '')) || 0;
//     console.log("Grand Total (after conversion):", amountPaid);

//     frappe.new_doc('Mortuary_Payments', {
//         invoice_id: mortuary_case,
//         client_name: patient
//     });

//     setTimeout(() => {
//         frappe.ui.form.on("Mortuary_Payments", "onload", function(frm) {
//             frm.set_value("amount_paid", amountPaid);
//         });
//     }, 500); // Delay to ensure the form is fully loaded
// }


// function createMortuaryPayment(mortuary_case, patient, grand_total) {
//     console.log("Mortuary Case:", mortuary_case);
//     console.log("Patient:", patient);
//     console.log("Grand Total (before conversion):", grand_total);

//     let amountPaid = parseFloat(grand_total.replace(/,/g, '')) || 0;
//     console.log("Grand Total (after conversion):", amountPaid);

//     frappe.new_doc('Mortuary_Payments', {});

//     setTimeout(() => {
//         frappe.ui.form.on("Mortuary_Payments", "onload", function(frm) {
//             console.log("Form Loaded. Setting values...");

//             frm.set_value("invoice_id", mortuary_case);
//             frm.set_value("client_name", patient);
//             frm.set_value("amount_paid", amountPaid);

//             console.log("Values Set:");
//             console.log("Invoice ID:", mortuary_case);
//             console.log("Client Name:", patient);
//             console.log("Amount Paid:", amountPaid);
//         });
//     }, 500); // Delay to ensure form is fully loaded
// }


function createMortuaryPayment(mortuary_case, patient, grand_total) {
    // console.log("Mortuary Case:", mortuary_case);
    // console.log("Patient:", patient);
    // console.log("Grand Total (before conversion):", grand_total);

    let amountPaid = 0;
    if (typeof grand_total === "string") {
        amountPaid = parseFloat(grand_total.replace(/,/g, '')) || 0;
    } else if (typeof grand_total === "number") {
        amountPaid = grand_total;
    }

    // console.log("Grand Total (after conversion):", amountPaid);

    frappe.new_doc('Mortuary_Payments');

    frappe.ui.form.on("Mortuary_Payments", "onload", function(frm) {
        // console.log("Form Loaded. Setting values...");

        // Set field values
        frm.set_value("invoice_id", mortuary_case);
        frm.set_value("client_name", patient);
        frm.set_value("amount_paid", amountPaid);
        frm.set_value("received_by", frappe.session.user);

        // Make fields read-only
        frm.set_df_property("invoice_id", "read_only", 1);
        frm.set_df_property("client_name", "read_only", 1);
        frm.set_df_property("amount_paid", "read_only", 1);
        frm.set_df_property("received_by", "read_only", 1);

        // Ensure UI updates
        frm.refresh_field("invoice_id");
        frm.refresh_field("client_name");
        frm.refresh_field("amount_paid");
        frm.refresh_field("received_by");

        // console.log("Fields set to read-only.");
    });

        // Open receipt after saving
        frappe.ui.form.on("Mortuary_Payments", "after_save", function(frm) {
            let receipt_url = `/printview?doctype=Mortuary_Payments&name=${frm.doc.name}&format=Your Custom Print Format&no_letterhead=0`;
            window.open(receipt_url, "_blank");
        });


}

