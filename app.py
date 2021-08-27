from flask import Flask, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, User, Feedback


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = 'postgres:///flask-feedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'incorrect'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def root():
    """Root route, redirects to register.html"""

    return redirect("/register")


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register a user"""
    """Generate form and handle form submission"""

    if 'username' in session:
        return redirect(f"/users/{session['username']}")

    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data

        user = User.register(username, password, first_name, last_name, email)

        db.session.commit()
        session['username'] = user.username

        return redirect(f"/users/{user.username}")

    else:
        return render_template('users/register.html', form=form)
