from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import TextArea


class DashboardsForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=60)])
    description = StringField("Description", widget=TextArea())
    submit = SubmitField("Save")
    cancel = SubmitField("Cancel")


class NotesForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=60)])
    description = StringField("Description", widget=TextArea())
    submit = SubmitField("Save")
    cancel = SubmitField("Cancel")


class RecipesForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=60)])
    description = StringField("Description", widget=TextArea())
    submit = SubmitField("Save")
    cancel = SubmitField("Cancel")


class SearchesForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=60)])
    description = StringField("Description", widget=TextArea())
    submit = SubmitField("Save")
    cancel = SubmitField("Cancel")


class ScriptsForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=60)])
    description = StringField("Description", widget=TextArea())
    submit = SubmitField("Save")
    cancel = SubmitField("Cancel")
