from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Student
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('login.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('main.dashboard')) 
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html')

@main.route('/dashboard')
@login_required
def dashboard():
    students = Student.query.all()
    return render_template('dashboard.html', students=students)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))  

@main.route('/student/new', methods=['GET', 'POST'])
@login_required
def new_student():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        major = request.form['major']
        new_student = Student(name=name, email=email, age=age, major=major)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('main.dashboard')) 
    return render_template('new_student.html')

@main.route('/student/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_student(id):
    student = Student.query.get_or_404(id)
    if request.method == 'POST':
        student.name = request.form['name']
        student.email = request.form['email']
        student.age = request.form['age']
        student.major = request.form['major']
        db.session.commit()
        return redirect(url_for('main.dashboard'))  
    return render_template('edit_student.html', student=student)

@main.route('/student/<int:id>/delete', methods=['POST'])
@login_required
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('main.dashboard'))  
