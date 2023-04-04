# Dojo Assignment: Cookies Order Validation
Create a new schema and table for cookie orders and forward engineer

Schema design:
- Tables
    - orders
        - id
        - customer_name
        - cookie_type
        - quantity
        - created_at
        - updated_at

Set up a new modularized project, with crud functionality as shown above, be sure to test every feature before moving on to the next.

Routes to build (Visible):
- /cookies - DONE
- /cookies/new -DONE
- /cookies/edit/int:id - DONE

Hidden routes:
- cookies/new/process -DONE 
- cookies/edit/process -DONE

Add validation to the create method: All fields are required, name and cookie_type must be at least 2 characters, number must be a positive number. -DONE

Redirect and display any validation errors on the create page. -DONE

Add validation to the edit page, same validations as for create. -DONE

Redirect back to the edit page for that same order to show any errors. -DONE

Pre-populate the edit fields with the existing record's values. -DONE