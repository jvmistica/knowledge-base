from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import TextArea


class DashboardsForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=50)])
    description = StringField("Description", widget=TextArea())
    submit = SubmitField("Save")


class NotesForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=50)])
    description = StringField("Description", widget=TextArea())
    submit = SubmitField("Save")


class RecipesForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=50)])
    description = StringField("Description", widget=TextArea())
    submit = SubmitField("Save")


class SearchesForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=50)])
    description = StringField("Description", widget=TextArea())
    submit = SubmitField("Save")


class ScriptsForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=50)])
    description = StringField("Description", widget=TextArea())
    submit = SubmitField("Save")


