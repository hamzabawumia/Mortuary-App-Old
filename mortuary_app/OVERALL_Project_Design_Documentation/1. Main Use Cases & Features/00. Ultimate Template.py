
--------
USE CASE = "Navigating to the Single Revenue Lines index page "
--------


--------
ARCHITECTURAL PLAN:
--------    
""" 
Since there were different db_tables for each revenue line, I had to have an index page from
where a user can select the revenue line they want to query.

"""

---------
USER FLOW / PROCESS FLOW
---------
"User": [ Administrator ]
    "navigation/nav_links": [ Administration --> Financial Reports --> Revenue Lines ]
    "url": [ single_revenue_line/revenue_line_index/',  name='revenue_line_index' ]
         # Sometimes there may be several links to click but we just focus on the final url that
         # achieves the task at hand
    "view": [ views.revenue_line_index ] 

    --------
    DATA FLOW # In the user flow (process flow) we capture the data flow 
    --------
        model.todo_list------>Table [taskModel]
        
        "db_table": [ Several db_tables depending on what the user selects e.g. Labs_Bridge ] 
                    [ OnlineConsulting (.then =>) Radiology_Bridge] 
        # We show the full db_schemas in the ER Diagrams
    
        #"database signals ?": [Default = Not Applicable]
        #"important dataflows ?": [Default = Not Applicable]    

    "responseTemplate": [ revenue_line/index.html ]
        # this shows the list of consultations ordered by the appointment dates
        # upon clicking on the consultation the patient then sees 
        # the radiology tests that were requested
        # this flows into another Url-->Views-->Template (UVMT)loop 
        # @ [/htmx_crud_for_radiology_bridge/list_my_radiology_tests/{{id}}]


    #"Explain any complex algorithms used here ?": 
        [ 

        '''
        Default = Not Applicable.
        '''

        ]



-------------------
Function Call Pathway ?

'''
Show any complex function call pathways here:
Default = Not Applicable


    |-- Function_1
            |
        Function_2
            |
        Function_3
            |
            |-->Function_4
            |
        Function_3 (this is a recursive call)
            |
            |-- Function_6
            
'''


-------------------




-------------------
Decision Trees ?

'''
Show any complex decision trees e.g. complex if-else algorithms:
Default = Not Applicable


function()
    |-- if condition_2 --->
            |-- do something

    |-- elif condition_3
             |-- do something

    |-- else condition_4
             |-- do something

'''

-------------------

-------------------
DATA-Access Control
-------------------

Using the UserPassesTest Mixin 

or

Filtering Consultations and Labs to restrict to only records belonging to the loggedin user.



-------------------------------
Configuration options for users
-------------------------------

'''
# Config booleans are in the main config file however you may list the key functions that have config options here.
# Also by listing them here; it will allow you to thing through all the possible configurations while developing
#  this use-case
'''

-------------------------------
DIRECT CHANGE DEPENDENCIES (other use-cases that will be affected if this use-case is editted haphazardly)
-------------------------------

'''
# List the function and its location plus, state the kind of issues we are likely to have if changes 
# are made haphazardly.
# i.e. which use-cases will be affected and which functions need to be edited too.
# 
'''
-------------------------------
REVERSE CHANGE DEPENDENCIES (other use-cases that will affect this use-case if they are editted)
-------------------------------

'''
# List the function and its location plus, state the kind of issues we are likely to have if changes are 
# made haphazardly in the other usecase
# i.e. which use-cases will influence the proper functioning of this current user-case.
'''





----------------------------
Schemas for Models involved
----------------------------
# The schemas were copied from the ER Diagrams 
# created with MYSQL WORKBENCH

class OnlineConsulting(models.Model): {

        id, 
        GCS, 
        complaints_and_history, 
        past_medical_history, 
        social_history, 
        provisional_diagnosis, 
        created, 
        updated, 
        created_date, 
        updated_date, 
        consultation_paid, 
        other_notes, 
        attendance_date, 
        client_id_str, 
        client_id_id, 
        updated_by_id, 
        clinician_id_id,
        appointment_id_id, 
        diastolic_bp, 
        height, 
        pulse, 
        rbs, 
        resp, 
        spo2, 
        systolic_bp, 
        temp,
        weight
    
    }
