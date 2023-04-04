from flask_app import app # import app so that routes will run

# import controller
from flask_app.controllers import orders

if __name__ == "__main__": # make sure app is not being run from a module
    app.run(debug = True, port = 5001) # on mac, default port of 5000 is in use