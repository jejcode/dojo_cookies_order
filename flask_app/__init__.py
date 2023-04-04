from flask import Flask # import Flask to create instance
app = Flask(__name__) # create instance of Flask called app
app.secret_key = "I finally get to use secret key!" # session needs secret key to run