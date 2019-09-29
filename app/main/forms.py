from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class BlogForm(FlaskForm):
    blog = StringField('blog title', validators=[Required()])
    category = TextAreaField('Description', validators=[Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('comment here', validators=[Required()])
    submit = SubmitField()
class CommentForms(FlaskForm):
    comment = TextAreaField('comment here', validators=[Required()])
    submit = SubmitField()



class BlogUploadForm(FlaskForm):

    category = StringField('blog title', validators=[Required()])
    blog = TextAreaField('comment here', validators=[Required()])
    submit = SubmitField('Add Blog')
