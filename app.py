from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
 
# SQLite
# DBs
# NoSQL and SQL DB
# SQLAlchemy
 
    #Student('Elvis',19,'male')
    #Student(1,'Elvis',19,'male')
 
 
 
# Configuring the current path of the project
current_path = os.path.abspath(os.path.dirname(__file__))
 
 
app = Flask(__name__)
 
# COnfiguring SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(current_path, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
 
#Model or Entity
class Student(db.Model):
    __tablename__ = 'Student'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    gender = db.Column(db.Text)
 
 
 
    def __init__(self,name:str,age:str,gender:str):
        self.name = name
        self.age = age
        self.gender = gender
 
 
@app.route("/")
def index():
    return "<h1>Getting started with Flask and Databases</h1>"


@app.route("/students")
def get_all_students():
    students = Student.query.all()
    return render_template('students.html',students=students)


@app.route("/students/<string:name>")
def delete_student(name):
    Student.query.filter(Student.name == name).delete(synchronize_session=False)
    remaining_students = Student.query.all()
    db.session.add_all(remaining_students)
    db.session.commit()
    return render_template('students.html',students=remaining_students)