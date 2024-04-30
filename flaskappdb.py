# ----------------------------------------------------------------------
# Name:        flaskappdb
# Purpose:     Demonstrate web development with Flask and Alchemy
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Module containing a starter web application with database access.

Download and save into your PyCharm project.
Run the program.
Point your browser to http://localhost:5000/
"""
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cs122.db'
db = SQLAlchemy(app)


class Review(db.Model): # what field has been created to db object

    """
    Class to represent and access the review table.
    Attributes:
    id (integer)
    comment (string)
    grade (string)
    """

    __tablename__ = "review" # table is review
    id = db.Column(db.Integer, primary_key=True) # table has different column
    comment = db.Column(db.String) # also we have comment column here
    grade = db.Column(db.String) # also we have grade column here


@app.route('/')
@app.route('/home')
def welcome():
    return render_template('home.html')

@app.route('/about')
def about():
    results = Review.query.all() # Get the all entries in our db
    results.reverse()
    # Render them
    return render_template('about.html', results=results)



@app.route('/review', methods=["POST", "GET"]) # in addition to route get
# the methods
def review():
    if request.method == "POST": # if request method is post method
        comment_input= request.form.get('comment')# getting the comment
        # from the request form
        grade_input = request.form.get('grade')#grade here is also a input
        # and getting from the request form
        # instantiation review:
        new_review = Review(comment=comment_input, grade=grade_input)
        db.session.add(new_review)
        db.session.commit()

    # this function render review template
    return render_template('review.html')

@app.route('/more', methods=["POST" , "GET"])
def more():
    results = []
    grade = ''
    if request.method == "POST":
        grade = request.form.get('grade')
        query = Review.query # start with all the reviews
        if grade:
            query = query.filter(Review.grade == grade) #filter
        results = query.all()
    return render_template('more.html', results = results, grade=grade)

def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
