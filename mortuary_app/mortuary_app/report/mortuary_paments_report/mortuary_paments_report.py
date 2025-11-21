import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {"label": "Client Name", "fieldname": "client_name", "fieldtype": "Data", "width": 200},
        {"label": "Received By", "fieldname": "received_by", "fieldtype": "Link", "options": "User", "width": 150},
        {"label": "Payment Method", "fieldname": "payment_method", "fieldtype": "Select", "width": 150},
        {"label": "Amount Paid", "fieldname": "amount_paid", "fieldtype": "Currency", "width": 150},
        {"label": "Creation Date", "fieldname": "creation", "fieldtype": "Datetime", "width": 180},
    ]

def get_data(filters):
    conditions = []
    values = {}

    if filters.get("from_date"):
        conditions.append("creation >= %(from_date)s")
        values["from_date"] = filters["from_date"]

    if filters.get("to_date"):
        conditions.append("creation <= %(to_date)s")
        values["to_date"] = filters["to_date"]

    if filters.get("client_name"):
        conditions.append("client_name LIKE %(client_name)s")
        values["client_name"] = f"%{filters['client_name']}%"

    if filters.get("received_by"):
        conditions.append("received_by = %(received_by)s")
        values["received_by"] = filters["received_by"]

    if filters.get("payment_method"):
        conditions.append("payment_method = %(payment_method)s")
        values["payment_method"] = filters["payment_method"]

    condition_str = " AND ".join(conditions) if conditions else "1=1"

    return frappe.db.sql(f"""
        SELECT
            client_name,
            received_by,
            payment_method,
            amount_paid,
            creation
        FROM `tabMortuary_Payments`
        WHERE {condition_str}
        ORDER BY creation DESC
    """, values, as_dict=True)







# import frappe


# def execute(filters=None):
#     if filters is None:
#         filters = {}

#     conditions = []
#     if filters.get("from_date"):
#         conditions.append("DATE(mp.creation) >= %(from_date)s")
#     if filters.get("to_date"):
#         conditions.append("DATE(mp.creation) <= %(to_date)s")
#     if filters.get("received_by"):
#         conditions.append("mp.received_by = %(received_by)s")

#     where_clause = " AND ".join(conditions)
#     if where_clause:
#         where_clause = "WHERE " + where_clause

#     query = f"""
#         SELECT
#             mp.name AS payment_id,
#             mp.client_name,
#             mp.amount_paid,
#             mp.received_by,
#             mp.creation AS payment_date
#         FROM
#             `tabMortuary_Payments` mp
#         {where_clause}
#         ORDER BY
#             mp.modified DESC
#     """

#     data = frappe.db.sql(query, filters, as_dict=True)

#     columns = [
#         {"label": "Payment ID", "fieldname": "payment_id", "fieldtype": "Link", "options": "Mortuary_Payments", "width": 120},
#         {"label": "Client Name", "fieldname": "client_name", "fieldtype": "Data", "width": 150},
#         {"label": "Amount Paid", "fieldname": "amount_paid", "fieldtype": "Currency", "width": 120},
#         {"label": "Received By", "fieldname": "received_by", "fieldtype": "Data", "width": 120},
#         {"label": "Payment Date", "fieldname": "payment_date", "fieldtype": "Datetime", "width": 150},
#     ]

#     return columns, data
