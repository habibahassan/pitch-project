from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired(), Length(min = 2, max = 45)])
    content = TextAreaField('Pitch', validators = [DataRequired()])
    category = SelectField('Pitch Category', choices=[('pickup lines','pickup lines'),('Interview','Interview'),('Product','Product'),('Promotion','Promotion'),('Academic','Academic'),('Political','Political'),('Technology','Technology'),('Health','Health') ])
    submit = SubmitField('Post')
# class CommentForm(FlaskForm):
#     comment = TextAreaField('Comment', validators=[Required()])
#     submit = SubmitField('Post Comment')