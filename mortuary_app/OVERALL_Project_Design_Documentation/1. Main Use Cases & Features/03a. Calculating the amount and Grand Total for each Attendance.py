
--------
USE CASE = 
"""
Calculating the amount and Grand Total for each Attendance
saved """
--------


--------
ARCHITECTURAL PLAN:
--------    
""" 
On Click of save the javascript functions 
(update_row_total, calculate_grand_total)
are called from the public/js/mortuary_orders.js file
and these are used to update the row totals = amount for each row
and then the final grandtotal is also calculated and saved in the Mortuary Case its self.

What it means is that we need to tell the users not to edit any paid invoice
or we need to make any paid invoice uneditable after payment.
If there are any new changes then a new invoice should be created.
"""

how order-line pricing & encounter totals are calculated/displayed.
--------------------------------------------------------------------

Your actual architecture is:

Parent Doctype.JS owns behavior

Child JS only reacts (no js code is in the childtable.JS)

Pricing is queried and inserted via client-side

Totals are derived , also client side


