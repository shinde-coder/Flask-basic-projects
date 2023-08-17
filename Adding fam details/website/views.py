from flask import *
from flask_login import login_required, current_user
from .models import Family_members
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':  
        id = request.form.get('id')
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        relation = request.form.get('relation')

        # Perform form validation
        if not name:
            flash('Name is required!', category='error') 
        elif not age:
            flash('Age is required!', category='error') 
        elif not gender:
            flash('Gender is required!', category='error') 
        elif not relation:
            flash('Relation is required!', category='error') 
        else:
            # Creating a new Family_members instance and add it to the database
            new_member = Family_members(
                id=id,
                name=name,
                age=age,
                gender=gender,
                relation=relation,
                user_id=current_user.id
            )
            db.session.add(new_member)
            db.session.commit()
            flash('Family member added!', category='success')
            return redirect(url_for('views.home'))

    return render_template("home.html", user=current_user)

@views.route('/delete/<int:member_id>', methods=['GET','POST'])
@login_required
def delete_member(member_id):
    member = Family_members.query.get(member_id)

    # Check if the member exists and belongs to the current user
    if member and member.user_id == current_user.id:
        db.session.delete(member)
        db.session.commit()
        flash('Family member deleted!', category='success')
    else:
        flash('Family member not found or you do not have permission to delete it.', category='error')

    return redirect(url_for('views.home'))

@views.route('/update/<int:member_id>', methods=['GET', 'POST'])
@login_required
def update_member(member_id):
    member = Family_members.query.get(member_id)

    if not member or member.user_id != current_user.id:
        flash('Family member not found or you do not have permission to update it.', category='error')
        return redirect(url_for('views.home'))

    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        relation = request.form.get('relation')

        # Update the member's details
        member.name = name
        member.age = age
        member.gender = gender
        member.relation = relation

        db.session.commit()
        flash('Family member updated!', category='success')
        return redirect(url_for('views.home'))

    return render_template("update_member.html", member=member, user=current_user)