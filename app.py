from datetime import datetime
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Specify the parameters of the database
app.config["SECRET_KEY"] = "myapplication123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)


# Create the database by using a database model
class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        date_object = datetime.strptime(date,"%Y-%m-%d")
        occupation = request.form["occupation"]

        # Capture user data in the database
        form = Form(first_name=first_name, last_name=last_name, email=email,
                    date=date_object, occupation=occupation)
        db.session.add(form)
        db.session.commit()
        flash("Your form was submitted successfully!", "success")


    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        # Calls Form class; Database not overwritten once created
        db.create_all()
        app.run(debug=True, port=5001)