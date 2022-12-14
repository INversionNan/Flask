from flask import Blueprint, Flask
from apps.model import Task
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired, ValidationError
from wtforms.fields import DateField, DateTimeField, TextAreaField

from apps.model import Kind
from apps.app import create_app


# from flask import current_app
#
# app = Flask(__name__)
# with app.app_context():
#     print(current_app.name())


# course = Blueprint("")

class AddCategory(FlaskForm):
    category = StringField(
        label='Add Category',
        validators=[DataRequired()],
        render_kw={'class': "form-control align-right",
                   'placeholder': 'Add Category',
                   'width': '70%', }
    )
    submit = SubmitField(
        label='Add Category',
        render_kw={'class': "btn btn-default btn-success btn-todolist-add_list"}
    )

    # def validate_category(self, field):
    #     if Kind.query.filter_by(name=field.data ).first():
    #         raise ValidationError("The category  %s has existed." % field.data)


class AddToDoList(FlaskForm):
    moduleTitle = TextAreaField(label='Module Title', validators=[DataRequired()], render_kw={
        'placeholder': 'Module Title',
        'class': 'form-control text-body', 'rows': 2
    })
    assessmentTitle = TextAreaField(label='Assessment Title', validators=[DataRequired()], render_kw={
        'placeholder': 'Assessment Title',
        'class': 'form-control text-body', 'rows': 2
    })
    content = StringField(
        label='Task Content',
        validators=[DataRequired()],
        render_kw={'class': "form-control align-right",
                   'placeholder': 'Task Content',
                   'width': '70%', }
    )
    # The drop - downlist
    # category = SelectField(
    #     label='Task Type',
    #     coerce=int,
    #     # choices=[(item.id, item.name) for item in Kind.query.all()],
    #     choice = [],
    #     render_kw={'class': "btn btn-default dropdown-toggle align-right",
    #                'type': "button",
    #                'placeholder': 'Category',
    #                'data-toggle': "dropdown",
    #                'aria-haspopup': "true",
    #                'aria-expanded': "false"
    #                }
    # )
    category = SelectField(
        label='Task Type',
        coerce=int,
        validators=[DataRequired()],
        choices=[(1, 'Work'), (2, 'Learn'), (3, 'Life')],
        # choices=[(item.id, item.name) for item in Kind.query.all()],
        render_kw={'class': "form-control btn btn-default dropdown-toggle align-center",
                   'type': "button",
                   'placeholder': 'Whether urgent or not',
                   'data-toggle': "dropdown",
                   'aria-haspopup': "true",
                   'aria-expanded': "false"
                   }
    )
    urgent = SelectField(
        label='Task Priority',
        validators=[DataRequired()],
        coerce=int,
        choices=[(1, 'Urgent'), (2, 'Inconsequential')],
        render_kw={'class': "form-control btn btn-default dropdown-toggle align-center",
                   'type': "button",
                   'placeholder': 'Whether urgent or not',
                   'data-toggle': "dropdown",
                   'aria-haspopup': "true",
                   'aria-expanded': "false"
                   }
    )
    # urgent = BooleanField(
    #     label='Task Priority',
    #     validators=[DataRequired()],
    #     render_kw={'class': "form-control btn btn-default dropdown-toggle align-center",
    #                'type': "button",
    #                'placeholder': 'Whether urgent or not'
    #                }
    # )

    # deadline = DateTimeField(
    #     label='Task Deadline', format='%Y-%m-%d %H:%M:%S',
    #     validators=[DataRequired()],
    #     render_kw={'class': "form-control calendar-control align-right",
    #                'placeholder': 'Deadline',
    #                'autocomplete': "off",
    #                'width': '70%', }
    # )
    deadline = DateField(
        label='Task Deadline', format='%Y-%m-%d', default='',
        validators=[DataRequired()],
        # widget=DatePickerWidget(),
        render_kw={'class': "form-control calendar-control pull-right",
                   'placeholder': 'Deadline',
                   'autocomplete': "off",
                   'width': '70%', }
    )

    submit = SubmitField(
        label='Add Task',
        render_kw={'class': "btn btn-default btn-success btn-todolist-add_list"}
    )

    def validate_content(self, field):
        if Task.query.filter_by(task_content=field.data).first():
            raise ValidationError("The task  %s has been registered." % field.data)
    # def __init__(self):
    #     super(AddToDoList, self).__init__()
    #     kinds = Kind.query.all()
    #     if kinds:
    #         self.category.choices = [(item.id, item.name) for item in kinds]
    #     else:
    #         self.category.choices = [(-1, "Please classify first.")]


class ChangeToDoList(FlaskForm):
    moduleTitle = StringField(label='Module Title', validators=[DataRequired()])
    assessmentTitle = StringField(label='Assessment Title', validators=[DataRequired()])
    content = StringField(
        label='Task Content',
        validators=[DataRequired()]
    )
    # The drop - downlist
    category = SelectField(
        label='Task Type',
        coerce=int,
        choices=[(1, 'Urgent'), (2, 'Un')],
        # choices=[(item.id, item.name) for item in Kind.query.all()],
        render_kw={'class': "form-control btn btn-default dropdown-toggle align-center",
                   'type': "button",
                   'data-toggle': "dropdown",
                   'aria-haspopup': "true",
                   'aria-expanded': "false"
                   }
    )
    urgent = SelectField(
        label='Task Priority',
        coerce=int,
        choices=[(1, 'Urgent'), (2, 'Inconsequential')],
        render_kw={'class': "form-control btn btn-default dropdown-toggle align-center",
                   'type': "button",
                   'data-toggle': "dropdown",
                   'aria-haspopup': "true",
                   'aria-expanded': "false"
                   }
    )
    submit = SubmitField(
        label='Change Task',
        render_kw={'class': "btn btn-default btn-success btn-todolist-add_list"}
    )

# class ChangeToDoList(FlaskForm):
#     moduleTitle = TextAreaField(label='Module Title', validators=[DataRequired()], render_kw={
#         'placeholder': 'Module Title',
#         'class': 'form-control text-body', 'rows': 2
#     })
#     assessmentTitle = TextAreaField(label='Assessment Title', validators=[DataRequired()], render_kw={
#         'placeholder': 'Assessment Title',
#         'class': 'form-control text-body', 'rows': 2
#     })
#     content = StringField(
#         label='Task Content',
#         validators=[DataRequired()],
#         render_kw={'class': "form-control align-right",
#                    'placeholder': 'Task Content',
#                    'width': '70%', }
#     )
#     # The drop - downlist
#     # category = SelectField(
#     #     label='Task Type',
#     #     coerce=int,
#     #     # choices=[(item.id, item.name) for item in Kind.query.all()],
#     #     choice = [],
#     #     render_kw={'class': "btn btn-default dropdown-toggle align-right",
#     #                'type': "button",
#     #                'placeholder': 'Category',
#     #                'data-toggle': "dropdown",
#     #                'aria-haspopup': "true",
#     #                'aria-expanded': "false"
#     #                }
#     # )
#     category = SelectField(
#         label='Task Type',
#         coerce=int,
#         validators=[DataRequired()],
#         # choices=[(1, 'Work'), (2, 'Learn'), (3, 'Life')],
#         choices=[(item.id, item.name) for item in Kind.query.all()],
#         render_kw={'class': "form-control btn btn-default dropdown-toggle align-center",
#                    'type': "button",
#                    'placeholder': 'Whether urgent or not',
#                    'data-toggle': "dropdown",
#                    'aria-haspopup': "true",
#                    'aria-expanded': "false"
#                    }
#     )
#     urgent = SelectField(
#         label='Task Priority',
#         validators=[DataRequired()],
#         coerce=int,
#         choices=[(1, 'Urgent'), (2, 'Inconsequential')],
#         render_kw={'class': "form-control btn btn-default dropdown-toggle align-center",
#                    'type': "button",
#                    'placeholder': 'Whether urgent or not',
#                    'data-toggle': "dropdown",
#                    'aria-haspopup': "true",
#                    'aria-expanded': "false"
#                    }
#     )
#     # urgent = BooleanField(
#     #     label='Task Priority',
#     #     validators=[DataRequired()],
#     #     render_kw={'class': "form-control btn btn-default dropdown-toggle align-center",
#     #                'type': "button",
#     #                'placeholder': 'Whether urgent or not'
#     #                }
#     # )
#
#     # deadline = DateTimeField(
#     #     label='Task Deadline', format='%Y-%m-%d %H:%M:%S',
#     #     validators=[DataRequired()],
#     #     render_kw={'class': "form-control calendar-control align-right",
#     #                'placeholder': 'Deadline',
#     #                'autocomplete': "off",
#     #                'width': '70%', }
#     # )
#     deadline = DateField(
#         label='Task Deadline', format='%Y-%m-%d', default='',
#         validators=[DataRequired()],
#         # widget=DatePickerWidget(),
#         render_kw={'class': "form-control calendar-control pull-right",
#                    'placeholder': 'Deadline',
#                    'autocomplete': "off",
#                    'width': '70%', }
#     )
#
#     submit = SubmitField(
#         label='Add Task',
#         render_kw={'class': "btn btn-default btn-success btn-todolist-add_list"}
#     )
#
#     def validate_content(self, field):
#         if Task.query.filter_by(task_content=field.data).first():
#             raise ValidationError("The task  %s has been registered." % field.data)
# def __init__(self):
#     super(AddToDoList, self).__init__()
#     kinds = Kind.query.all()
#     if kinds:
#         self.category.choices = [(item.id, item.name) for item in kinds]
#     else:
#         self.category.choices = [(-1, "Please classify first.")]
