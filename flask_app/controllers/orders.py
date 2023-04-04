from flask import render_template, redirect, request, session # import module for flask to work
from flask_app import app # import app for routes to work
from flask_app.models.order import Order

@app.route('/') # create a default route to load /cookies during testing
def default():
    return redirect('/cookies')
@app.route('/cookies') # get all orders and return them to index.html
def load_orders():
    session.clear()
    # get all orders from database and pass to index.html
    all_orders = Order.get_all_orders()
    return render_template('index.html', all_orders = all_orders)
@app.route('/cookies/new') # load cookie order form
def load_new_order():
    if 'form' in session: # if form data is present, send it back to the form
        prefilled = session['form']
    else:
        prefilled = { # if not, send blanks to the form
            'name': '',
            'cookie_type': '',
            'number_of_cookies': ''
        }
    return render_template('new_order.html', prefilled = prefilled)
@app.route('/cookies/new/process', methods=['POST']) # validate form and if successful, write new order to database
def log_new_order():
    order_info = request.form
    # if errors:
    # call static method validate_order to validate
    if not Order.validate_order(request.form):
        # set session to load form data for user to fix
        session['form'] = request.form
        return redirect('/cookies/new')
    # else if no errors:
    session.pop('form')
    Order.save(request.form)
    return redirect('/cookies')
@app.route('/cookies/edit/<int:id>')
def edit_order(id):
    # get record from database
    this_order = Order.get_order_by_id(id)
    if 'edit' in session:
        prefilled = session['edit']
    else:
        prefilled = {
            'id': this_order.id,
            'name': this_order.name,
            'cookie_type': this_order.cookie_type,
            'number_of_boxes': this_order.num_boxes
        }
    # send instance to html for editing
    return render_template('change_order.html', prefilled = prefilled)
@app.route('/cookies/edit/process', methods=['POST'])
def process_edits():
    order_info = request.form
    # if errors:
    # call static method validate_order to validate
    if not Order.validate_order(request.form):
        # set session to load form data for user to fix
        session['edit'] = request.form
        return redirect(f"/cookies/edit/{request.form['id']}")
    # else if no errors:
    if 'edit' in session: # clear the session so it doesn't keep coming back
        session.pop('edit')
    Order.update(request.form)
    return redirect('/cookies')
