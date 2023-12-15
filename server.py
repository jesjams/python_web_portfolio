# This python templates uses Flask framework
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#variable-rules
# as an alternative, we can also use Django

# to run the flask app, open terminal and run the following:
#   flask --app=server.py run
#  turn on debug mode:
#   flask --app=server.py --debug run
# in debug mode, we can refresh the page and it will auto update

# using flask, we can also run python code in the html file
# by surrounding the code in {{ }}

from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# dynamically accept page name depending on the requested url
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open("database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject},{message}")

def write_to_csv(data):
    with open("database.csv", mode="a", newline='') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


# this function will be called when send button is pressed in the contact page
#  <form action="submit_form" method="post" class="reveal-content">
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":

        # get the form data from the request
        # alternatively, access the parameters by using request.form["email"]
        # this will get this data, base on the field name
        #   <input name="email" type="email" class="form-control" id="email" placeholder="Email">
        data = request.form.to_dict()
        write_to_csv(data)

        # this will redirect the page to http://127.0.0.1:5000/thankyou.html
        # which will open the page through html_page() function
        return redirect("/thankyou.html")
    else:
        return "invalid access"
