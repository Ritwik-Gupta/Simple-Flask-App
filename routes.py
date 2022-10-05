from app import app, db
from model import Task
from forms import MyForm
from flask import render_template, redirect, url_for, flash
from datetime import datetime


@app.route("/")
@app.route("/index", methods=["GET", "POST"])
def index():
    tasks = Task.query.all()
    if tasks:
        return render_template("index.html", tasks=tasks)
    flash("No Data Found")
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add():
    form = MyForm()
    if form.validate_on_submit():
        t = Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        return render_template("index.html", tasks=Task.query.all())

    return render_template("add.html", form=form)


@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit(task_id):
    task = Task.query.filter_by(id=task_id).first()
    if task:
        form = MyForm()
        if form.validate_on_submit():
            new_title = form.title.data
            task.title = new_title
            task.date = datetime.utcnow()
            db.session.commit()
            return redirect(url_for("index"))
        else:
            form.title.data = task.title
            return render_template("edit.html", form=form, task_id=task_id)

    flash("No such task found!")


@app.route("/delete/<int:task_id>")
def delete(task_id):
    task = Task.query.filter_by(id=task_id).first()
    if task:
        db.session.delete(task)
        db.session.commit()
        flash("Task deleted successfully!")
        return redirect(url_for("index"))
