from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
class BlogForm(FlaskForm):
   blog = StringField('blog title',validators=[Required()])
   category= TextAreaField('Description', validators=[Required()])
   submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
   bio = TextAreaField('Tell us about you.',validators = [Required()])
   submit = SubmitField('Submit')

# class ReviewForm(FlaskForm):

#      title = StringField('Review title',validators=[Required()])

#      review = TextAreaField('Movie review')

#      submit = SubmitField('Submit')
