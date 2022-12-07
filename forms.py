from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, NumberRange, Length

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species Name", validators=[InputRequired(), AnyOf(values=["cat", "dog", "porcupine"])])
    photo_url = StringField("Pet Photo", validators=[Optional(), URL()])
    age = IntegerField("Pet Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Pet Notes", validators=[Optional()])
    available = BooleanField("Pet Available?", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing pet data."""

    photo_url = StringField("Photo Photo", validators=[Optional(), URL()],)
    notes = TextAreaField("Pet Comments", validators=[Optional(), Length(min=5)],)
    available = BooleanField("Pet Available?")
