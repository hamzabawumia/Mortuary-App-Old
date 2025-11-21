frappe.ui.form.on("Mortuary_Orders", {
    items: function(frm, cdt, cdn) {
        update_row_total(frm, cdt, cdn);
    },
    quantity: function(frm, cdt, cdn) {
        update_row_total(frm, cdt, cdn);
    }
});

function update_row_total(frm, cdt, cdn) {
    let row = frappe.get_doc(cdt, cdn);

    if (row.items) {
        frappe.db.get_value("List of Items and Services", row.items, "selling_price").then(response => {
            if (response && response.message) {
                let selling_price = parseFloat(response.message.selling_price) || 0;
                let quantity = parseFloat(row.quantity) || 0;
                frappe.model.set_value(cdt, cdn, "amount", selling_price * quantity);
                calculate_grand_total(frm);
            }
        });
    }
}

function calculate_grand_total(frm) {
    let total = 0;
    (frm.doc.table_nrzn || []).forEach(row => {
        total += row.amount || 0;
    });
    frm.set_value("grand_total", total);
}
