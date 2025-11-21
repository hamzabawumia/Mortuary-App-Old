
--------
USE CASE = 
"""
Redirecting from the link in a query report and passing
then parameters  to create a new record in another doctype
"""
--------


--------
ARCHITECTURAL PLAN:
--------    
""" 
On Click of a the link a JS function (createMortuaryPayment.js)
is called this function is saved in the public js folder.

this function takes the parameters that are passed to it via the link and 
uses frappe's new_doc() function to open a new document with a prefilled form 
containing the passed parameter.

Recall that every doctype also has its own .js file right.
so we use that .js file to ensure that the passed fields are read only.

"""
