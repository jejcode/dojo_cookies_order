import re # import reg ex for validation
from flask_app.config.mysqlconnection import connectToMySQL # import db connection function
from flask import flash # import flash to save validation messages

class Order:
    DB = 'cookies_order_schema'
    def __init__(self, data) -> None: # instance models the columns in DB
        self.id = data['id']
        self.name = data['name']
        self.cookie_type = data['cookie_type']
        self.num_boxes = data['num_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_orders(cls): # get all rows from table
        query = "SELECT * FROM orders"
        results = connectToMySQL(cls.DB).query_db(query)
        all_orders = [] # create empty list to store each instance of a DB row
        for order in results:
            all_orders.append(cls(order)) # convert DB row in class instance and store in list
        return all_orders # send list to controller
    @classmethod
    def get_order_by_id(cls, id): # send query based on order id
        query = "SELECT * FROM orders WHERE id=%(id)s"
        results = connectToMySQL(cls.DB).query_db(query, {'id': id}) # connect to DB returns single item list
        return cls(results[0]) # return instance of lone db row
    @classmethod
    def save(cls, data): # save form data to database
        query = """INSERT INTO orders (name, cookie_type, num_boxes)
                VALUES (%(name)s, %(cookie_type)s, %(number_of_boxes)s)"""
        return connectToMySQL(cls.DB).query_db(query, data)
    @classmethod
    def update(cls,data): # update current record at id
        query = """UPDATE orders
                SET name=%(name)s, cookie_type=%(cookie_type)s, num_boxes=%(number_of_boxes)s
                WHERE id=%(id)s"""
        return connectToMySQL(cls.DB).query_db(query, data)
    @staticmethod
    def validate_order(order): # form validation
        is_valid = True # if validation passes, will return true 
        if len(order['name']) < 2:
            flash('Name must be at least 2 characters long.')
            is_valid = False
        if len(order['cookie_type']) < 2:
            flash('Cookie type must be at least 2 characters long.')
        for field in order:
            if len(order[field]) <= 0:
                is_valid = False
                message = f"{field} is required.".capitalize() # create message string using field name, and capitalize the first word to make a proper sentence.
                make_pretty = message.maketrans("_", " ") # make a translate map to replace all _ with a space
                flash(message.translate(make_pretty)) # store translated message in flash
        if len(order['number_of_boxes']) > 0 and (int(order['number_of_boxes']) < 1 or int(order['number_of_boxes']) > 200): 
            # don't let one person buy the whole inventory.
            is_valid = False
            flash('Please order between 1 and 200 boxes.')
        return is_valid
