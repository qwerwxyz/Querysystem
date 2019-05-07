from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import NameForm,QueryForm
from .. import db
from ..models import User, Student
from sqlalchemy import or_
from flask import request


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    # form = NameForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(username=form.name.data).first()
    #     if user is None:
    #         user = User(username=form.name.data)
    #         db.session.add(user)
    #         session['known'] = False
    #     else:
    #         session['known'] = True
    #         session['name'] = form.name.data
    #         form.name.data = ''
    #         return redirect(url_for('main.index'))
    # return render_template('index.html', form=form, name=session.get('name'),
    #                        known=session.get('known', False))


# @main.route('/query', methods=['GET', 'POST'])
@main.route('/query/<int:page>',methods=['GET', 'POST'])
def query(page):
    form = QueryForm()
    data = None
    if not page:
        page = 1
    if request.method == 'POST':
        page = 1
        session['keyword'] = form.keyword.data
        print(session.get('keyword'))
        session['sname'] = form.sname.data
        session['sno'] = form.sno.data
        session['sex'] = form.sex.data
        print(session.get('sex'))
        session['dept'] = form.dept.data
        session['classno'] = form.classno.data
    if form.validate_on_submit() or page >= 2:
        if session.get('keyword') != '':
            print("keyword")
            print(session.get('keyword'))
            data = Student.query.filter(or_(Student.sname.like("%" + session.get('keyword') + "%") if session.get('keyword') is not None else "",
                                        Student.sno.like("%" + session.get('keyword') + "%") if session.get('keyword') is not None else "",
                                        Student.sex.like("%" + session.get('keyword') + "%") if session.get('keyword') is not None else "",
                                        Student.dept.like("%" + session.get('keyword') + "%") if session.get('keyword') is not None else "",
                                        Student.classno.like("%" + session.get('keyword') + "%") if session.get('keyword') is not None else ""
                                            )).paginate(page=page, per_page=3)
        else:
            print("else")
            data = Student.query.filter(
                Student.sname.like("%" + session.get('sname') + "%") ,
                Student.sno.like("%" + session.get('sno') + "%") ,
                Student.sex.like("%" + session.get('sex') + "%") ,
                Student.dept.like("%" + session.get('dept') + "%"),
                Student.classno.like("%" + session.get('classno') + "%")
                ).order_by(Student.sno).paginate(page=page, per_page=3)
            print(data)



    if data is None:
        print("can not find it")
        return render_template('query.html', form=form, data=data, pagination=data)
    print('find it')
    print(data.items)
    pagination = data
    print(type(pagination))
    print(pagination)
    return render_template('query.html', form=form, data=data.items, pagination=data)