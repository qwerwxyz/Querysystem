from wtforms.validators import DataRequired
from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField,SelectField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    mysubmit = SubmitField('提交')


class QueryForm(FlaskForm):
    keyword = StringField('关键字')
    sno = StringField('学号')
    sname = StringField('姓名')
    sex = StringField('性别')
    dept = StringField('学院')
    classno = StringField('班号')
    mysubmit = SubmitField('提交')
    # sno = StringField('学号', validators=[Length(5),Regexp('\d{5}',0,'sno has exactly 5 number')])
    # sname = StringField('姓名', validators=[Regexp('^[\u4E00-\u9FA5]{2,3}$', 0, 'valid')])
    # sex = SelectField('性别',render_kw={'class': 'form-control'},choices=[('男', '男'), ('女', '女')])
    # dept = SelectField('学院', render_kw={'class': 'form-control'}, choices=[('计算机', '计算机'), ('电信', '电信')])
    # classno = StringField('班号', validators=[Length(5), Regexp('\d{5}', 0, 'classno has exactly 5 number')])
    # submit = SubmitField('Submit')