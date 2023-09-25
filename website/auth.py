from flask import Blueprint, render_template, request, flash
#import re

auth = Blueprint("auth", __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth.route("/signup", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password')
        repeat_password = request.form.get('repeat_password')

        if len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
        #elif re.search(r"[\w\.-]+@[\w\.-]+\.\w+", email):
        #    flash("Email is not a valid email address.", category="error")
        elif len(first_name) < 2:
            flash("Email must be greater than 2 characters.", category="error")
        elif len(last_name) < 2:
            flash("Email must be greater than 1 characters.", category="error")
        elif len(password) < 8:
            flash("Password must be at least 8 characters.", category="error")
        elif password != repeat_password:
            flash("Passwords do not match.", category="error")
        else:
            flash("Account created.", category="success")
        
        print("Email: " + email)
        print("Last Name: " + last_name)
        print("Password: " + password)
    else:
        pass
    return render_template("signup.html")