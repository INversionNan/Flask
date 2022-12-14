from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import login_required, current_user

from apps.app import db
from apps.model import Task, Kind
from apps.todolist import todolist
from apps.todolist.course import AddToDoList, ChangeToDoList, AddCategory


# User View Task List
@todolist.route('/list/', methods=['GET', 'POST'])
@login_required
def list_1():
    list = AddToDoList()
    page = int(request.args.get('page', 1))
    todolistPage = Task.query.filter_by(user_id=current_user.id).paginate(per_page=current_app.config['PER_PAGE'],
                                                                          error_out=False)

    return render_template('todolist/list.html', todoObj=todolistPage, form=list)


@todolist.route('/add/', methods=['POST', 'GET'])
@login_required
def add_list():
    list = AddToDoList()
    page = int(request.args.get('page', 1))
    todolistPage = Task.query.filter_by(user_id=current_user.id).paginate(per_page=current_app.config['PER_PAGE'],
                                                                          error_out=False)

    if list.validate_on_submit():
        # get users submission
        moduleTitle = list.moduleTitle.data
        assessmentTitle = list.assessmentTitle.data
        content = list.content.data
        kind_id = list.category.data
        urgent = list.urgent.data
        deadline = list.deadline.data
        # add to database
        status = False
        add = Task(task_moduleTitle=moduleTitle, task_assessmentTitle=assessmentTitle, task_content=content,
                   category_id=kind_id,
                   task_urgent=urgent, task_deadline=deadline, user_id=current_user.id, task_status=status)
        db.session.add(add)
        flash('Add task successfully!', category='success')
        return redirect(url_for('todolist.add_list'))
    return render_template('todolist/list.html', todoObj=todolistPage, form=list)


@todolist.route('/change/<int:id>', methods=['GET', 'POST'])
def change(id):
    list = ChangeToDoList()
    page = int(request.args.get('page', 1))
    todolistPage = Task.query.filter_by(user_id=current_user.id).paginate(per_page=current_app.config['PER_PAGE'],
                                                                          error_out=False)
    task = Task.query.filter_by(id=id).first()

    list.content.data = task.task_content
    # list.category.data = task.category_id
    # list.urgent.data = task.task_urgent
    # list.deadline.data = task.task_deadline
    list.moduleTitle.data = task.task_moduleTitle
    list.assessmentTitle.data = task.task_assessmentTitle
    list.urgent.data = task.task_urgent
    list.category.data = task.category_id

    if list.validate_on_submit():
        content = request.form.get('content')
        moduleTitle = request.form.get('moduleTitle')
        category_id = request.form.get('category')
        assessmentTitle = request.form.get('assessmentTitle')
        urgent = request.form.get('urgent')
        task.task_content = content
        task.category_id = category_id
        task.urgent = urgent
        task.task_assessmentTitle = assessmentTitle
        task.task_moduleTitle = moduleTitle

        db.session.add(task)
        flash('Task has been changed', category='success')
        return redirect(url_for('todolist.list_1'))
    return render_template('todolist/change.html', form=list, todoObj=todolistPage)


@todolist.route('/delete/<int:id>/')
@login_required
def delete(id):
    task = Task.query.filter_by(id=id).first()
    # task.task_status = True
    db.session.delete(task)
    flash("Task has been deleted successfully.", category='success')
    return redirect(url_for('todolist.list_1'))


@todolist.route('/hasdone/<int:id>/')
@login_required
def hasdone(id):
    task = Task.query.filter_by(id=id).first()
    task.task_status = True
    db.session.add(task)
    flash("Task status has been changed successfully.", category='success')
    return redirect(url_for('todolist.list_1'))


@todolist.route('/hasnotdone/<int:id>/')
@login_required
def hasnotdone(id):
    task = Task.query.filter_by(id=id).first()
    task.task_status = False
    db.session.add(task)
    flash("Task status has been changed successfully.", category='success')
    return redirect(url_for('todolist.list_1'))


@todolist.route('/urgent/<int:id>/')
@login_required
def urgent(id):
    task = Task.query.filter_by(id=id).first()
    task.task_urgent = 1
    db.session.add(task)
    flash("Task priority has been changed successfully.", category='success')
    return redirect(url_for('todolist.list_1'))


@todolist.route('/noturgent/<int:id>/')
@login_required
def noturgent(id):
    task = Task.query.filter_by(id=id).first()
    task.task_urgent = 2
    db.session.add(task)
    flash("Task priority has been changed successfully.", category='success')
    return redirect(url_for('todolist.list_1'))


@todolist.route('/search/<int:id>/', methods=['POST', 'GET'])
@login_required
def search(id):
    task = Task.query.filter_by(id=id).all()
    return render_template('todolist/search.html', todoObj=task)


@todolist.route('/searchModuleTitle/<int:id>/', methods=['POST', 'GET'])
@login_required
def search_ModuleTitle(id):
    moduleTitle = request.form.get('moduleTitle')
    task = Task.query.filter_by(user_id=id, task_moduleTitle=moduleTitle).paginate(per_page=current_app.config['C_PAGE'],
                                                                          error_out=False)
    return render_template('todolist/search.html', todoObj=task)


@todolist.route('/searchAssessmentTitle/<int:id>/', methods=['POST', 'GET'])
@login_required
def search_AssessmentTitle(id):
    assessmentTitle = request.form.get('assessmentTitle')
    task = Task.query.filter_by(user_id=id, task_assessmentTitle=assessmentTitle).paginate(per_page=current_app.config['C_PAGE'],
                                                                          error_out=False)
    return render_template('todolist/search.html', todoObj=task)


@todolist.route('/searchContent/<int:id>/', methods=['POST', 'GET'])
@login_required
def search_Content(id):
    content = request.form.get('content')
    task = Task.query.filter_by(user_id=id, task_content=content).paginate(per_page=current_app.config['C_PAGE'],
                                                                          error_out=False)
    return render_template('todolist/search.html', todoObj=task)


@todolist.route('/searchPriority/<int:id>/', methods=['POST', 'GET'])
@login_required
def search_Urgent(id):
    priority = request.form.get('priority')
    task = Task.query.filter_by(user_id=id, task_urgent=priority).paginate(per_page=current_app.config['C_PAGE'],
                                                                          error_out=False)

    return render_template('todolist/search.html', todoObj=task)


@todolist.route('/category/', methods=['POST', 'GET'])
@login_required
def category():
    category_list = AddCategory()
    KindPage = Kind.query.filter_by(user_id=current_user.id).paginate(per_page=current_app.config['PER_PAGE'],
                                                                      error_out=False)
    return render_template('todolist/category.html', kindObj=KindPage, form=category_list)


@todolist.route('/addcategory/', methods=['POST', 'GET'])
@login_required
def add_category():
    list = AddCategory()
    KindPage = Kind.query.filter_by(user_id=current_user.id).paginate(per_page=current_app.config['PER_PAGE'],
                                                                      error_out=False)
    if list.validate_on_submit():
        # get category submission
        name = list.category.data
        user_id = current_user.id
        # add to database
        add = Kind(name=name, user_id=user_id)
        db.session.add(add)
        flash('Add category successfully!', category='success')
        return redirect(url_for('todolist.category'))
    return render_template('todolist/category.html', kindObj=KindPage, form=list)


@todolist.route('/complete/<int:id>/', methods=['POST', 'GET'])
@login_required
def complete(id):
    todolistPage = Task.query.filter_by(user_id=current_user.id).paginate(per_page=current_app.config['C_PAGE'],
                                                                          error_out=False)

    return render_template('todolist/complete.html', todoObj=todolistPage)


@todolist.route('/uncomplete/<int:id>/', methods=['POST', 'GET'])
@login_required
def uncomplete(id):
    todolistPage = Task.query.filter_by(user_id=current_user.id).paginate(per_page=current_app.config['C_PAGE'],
                                                                          error_out=False)

    return render_template('todolist/uncomplete.html', todoObj=todolistPage)
