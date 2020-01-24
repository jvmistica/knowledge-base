from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import TextArea


class DashboardsForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=70)])
    description = StringField("Description", widget=TextArea())
    submit = SubmitField("Save")
    cancel = SubmitField("Cancel")


class NotesForm(FlaskForm):
    # title = TextAreaField('First Name', widget=TextArea())
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=70)], widget=TextArea())
    description = StringField("Description", widget=TextArea())
    submit = SubmitField("Save")
    cancel = SubmitField("Cancel")


class RecipesForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=70)])
    description = StringField("Description", widget=TextArea())
    submit = SubmitField("Save")
    cancel = SubmitField("Cancel")


class SearchesForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=70)])
    description = StringField("Description", widget=TextArea())
    submit = SubmitField("Save")
    cancel = SubmitField("Cancel")


class ScriptsForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=70)])
    description = StringField("Description", widget=TextArea())
    submit = SubmitField("Save")
    cancel = SubmitField("Cancel")
