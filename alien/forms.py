from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired, Length


class regform(FlaskForm):
    name=StringField('Name',validators=[DataRequired(),Length(min=2,max=20)])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Register')



class logform(FlaskForm):
    name=StringField('Name',
                            validators=[DataRequired(),Length(min=2,max=20)])
    password=PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit=SubmitField('Log in',)

class postform(FlaskForm):
    title=StringField('Title',validators=[DataRequired(),Length(min=2,max=20)])
    content=StringField('Content',validators=[DataRequired(),Length(min=2,max=20)])
    submit=SubmitField('post',)
    
