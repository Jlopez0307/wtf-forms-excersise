from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, validators, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional


class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators= [InputRequired()])
    species = SelectField("Species",choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo", validators= [Optional() , URL()])
    age = FloatField("Pet age", validators=[Optional(), NumberRange(message="Age must be between 0-30",min=0, max=30)])
    notes = TextAreaField("Notes", [validators.Optional()])
    

class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField("Photo URL",validators=[Optional(), URL()],)

    notes = TextAreaField("Comments",validators=[Optional(), Length(min=10)],)

    available = BooleanField("Available?")