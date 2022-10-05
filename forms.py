from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators


# creating the form class

class MyForm(FlaskForm):
    title = StringField(label="Name", validators=[validators.DataRequired()])
    submit = SubmitField(label="Submit")
