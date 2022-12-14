from apps.user import user
from apps.model import User
from apps.app import db

from flask import Flask, render_template, flash, redirect, abort, url_for
from flask_login import login_required, current_user

from apps.user.operate import ChangeUserList


@user.route('/user/<id>')
@login_required
def get_user(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        abort(404)  # throw a 404 exception
    else:
        return render_template('user/user.html', user=user)


@user.route('/changedpassword/<id>')
def change_password(id):

    return 'change password'


@user.route('/changeuser', methods=['GET', 'POST'])
def change_user():
    user_list = ChangeUserList()
    if user_list.validate_on_submit():
        current_user.name = user_list.name.data
        current_user.location = user_list.location.data
        current_user.information = user_list.information.data
        db.session.add(current_user)
        flash('User information has been changed successfully!', category='success')
        return redirect(url_for('user.get_user', id=current_user))
    user_list.name.data = current_user.name
    user_list.location.data = current_user.location
    user_list.information.data = current_user.information
    return render_template('user/change.html', form=user_list)
