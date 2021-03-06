from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional
from flask_wtf import FlaskForm


class RegisterForm(FlaskForm):
    """Registration form"""

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=5, max=20)]
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=7, max=20)]
    )
    first_name = StringField(
        "First Name",
        validators=[InputRequired(), Length(max=30)]
    )
    last_name = StringField(
        "Last Name",
        validators=[InputRequired(), Length(max=30)]
    )
    email = StringField(
        "Email",
        validators=[InputRequired(), Email(), Length(max=50)]
    )


class LoginForm(FlaskForm):
    """Login form"""

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=5, max=20)]
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=7, max=20)]
    )


class DeleteForm(FlaskForm):
    pass


class FeedbackForm(FlaskForm):
    """Feedback form"""

    title = StringField(
        'Title',
        validators=[InputRequired(), Length(max=100)]
    )
    content = StringField(
        'Content',
        validators=[InputRequired()]
    )
