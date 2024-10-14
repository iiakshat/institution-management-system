from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from .models import *
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('login.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.dashboard'))

        flash('Invalid email or password')
    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

# CRUD
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


@main.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(current_user.id)
    return render_template('dashboard.html', user=user)


@main.route('/analytics')
@login_required
def analytics():
    user = current_user
    attendance = Attendance.query.filter_by(user_id=user.id).all()
    results = Results.query.filter_by(user_id=user.id).all()
    return render_template('analytics.html', user=user, attendance=attendance, results=results)


@main.route('/resources', methods=['GET', 'POST'])
@login_required
def resources():
    if request.method == 'POST':
        date = request.form.get('date')
        subject = request.form.get('subject')
        summary = request.form.get('summary')
        notes_url = request.form.get('notes_url')
        
        resource = Resource(
            user_id=current_user.id,
            date=date,
            subject=subject,
            summary=summary,
            notes_url=notes_url
        )
        db.session.add(resource)
        db.session.commit()
        flash('Resource added successfully!')

    resources = Resource.query.filter_by(user_id=current_user.id).all()
    return render_template('resources.html', resources=resources)


@main.route('/fees', methods=['GET', 'POST'])
@login_required
def fees():
    if request.method == 'POST':
        fee_type = request.form.get('fee_type')
        amount = request.form.get('amount')

        fee = Fee(
            user_id=current_user.id,
            fee_type=fee_type,
            amount=amount
        )
        db.session.add(fee)
        db.session.commit()
        flash('Fee payment recorded successfully!')

    fees = Fee.query.filter_by(user_id=current_user.id).all()
    return render_template('fees.html', fees=fees)


@main.route('/about')
def about():
    # Add any additional information you want to show in the about page
    creators = Faculty.query.all()
    return render_template('about.html', creators=creators)
