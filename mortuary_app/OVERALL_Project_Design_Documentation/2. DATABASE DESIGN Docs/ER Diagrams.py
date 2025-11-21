Relationships Between Doctypes in Your Frappe App
Your Mortuary App consists of five main Doctypes:

Motuary_Client = Represents clients (patients).

Mortuary Case = A record of cases related to a client.

List of Items and Services = Defines services or items available.

Mortuary_Orders = A child table linking ordered services/items to a Mortuary Case.

Mortuary_Payments = Tracks payments made for cases.

Relationships:
Motuary_Client → Mortuary Case

Each Mortuary Case is linked to a Motuary_Client.

This means a client can have multiple cases over time.

Mortuary Case → Mortuary_Orders

The Mortuary Case has a table field (table_nrzn), linking it to Mortuary_Orders.

Each case may contain multiple ordered services/items.

Mortuary_Orders → List of Items and Services

Each record in Mortuary_Orders links to an item/service from List of Items and Services.

Mortuary Case → Mortuary_Payments

Each Mortuary_Payments record is linked to a Mortuary Case (invoice_id).

This means a single case can have multiple payments.

// using dbdiagrams.io style
Table Motuary_Client {
  id int [pk, increment]
  first_name varchar [not null]
  last_name varchar [not null]
  opd_no varchar
  ward varchar
  gender varchar
}

Table Mortuary_Case {
  id int [pk, increment]
  patient__cient int [ref: > Motuary_Client.id]
  date date
  time time
  grand_total decimal
  paid boolean
}

Table Mortuary_Orders {
  id int [pk, increment]
  mortuary_case_id int [ref: > Mortuary_Case.id]
  items int [ref: > List_of_Items_and_Services.id]
  quantity varchar
  amount decimal
}

Table List_of_Items_and_Services {
  id int [pk, increment]
  item_name varchar
  selling_price varchar
  description varchar
}

Table Mortuary_Payments {
  id int [pk, increment]
  invoice_id int [ref: > Mortuary_Case.id]
  client_name varchar [not null]
  amount_paid decimal
  received_by int [ref: > User.id]
  payment_method varchar
}

Table User {
  id int [pk, increment]
  full_name varchar
  // Add other fields if needed
}
