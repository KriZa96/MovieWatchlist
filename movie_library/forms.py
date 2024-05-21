from flask_wtf import FlaskForm
from wtforms import (
    IntegerField,
    PasswordField,
    StringField,
    SubmitField,
    TextAreaField,
    URLField,
)

from wtforms.validators import (
    InputRequired,
    Email,
    EqualTo,
    Length,
    NumberRange,
)


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])

    password = PasswordField(
        "Password",
        validators=[
            InputRequired(),
            Length(
                min=4,
                max=20,
                message="Your password must be between 4 and 20 characters long.",
            ),
        ],
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            InputRequired(),
            EqualTo(
                "password",
                message="This password did not match the one in the password field.",
            ),
        ],
    )

    submit = SubmitField("Register")


class MovieForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()], render_kw={"onclick": "findMovies()", "onkeyup": "findMovies()"}, id="movie-search-box")
    director = StringField("Director", validators=[InputRequired()], id="movie-director")

    year = IntegerField(
        "Year",
        validators=[
            InputRequired(),
            NumberRange(min=1878, message="Please enter a year in the format YYYY."),
        ],
        id="movie-year"
    )

    submit = SubmitField("Add Movie")


class StringListField(TextAreaField):
    def _value(self):
        if self.data:
            return "\n".join(self.data)
        else:
            return ""

    def process_formdata(self, valuelist):
        if valuelist and valuelist[0]:
            self.data = [line.strip() for line in valuelist[0].split("\n")]
        else:
            self.data = []


class ExtendedMovieForm(MovieForm):
    cast = StringListField("Cast", id="movie-cast")
    tags = StringListField("Tags", id="movie-tags")
    description = TextAreaField("Description", id="movie-description")
    video_link = URLField("Video link", id="movie-video_link")

    submit = SubmitField("Submit")
