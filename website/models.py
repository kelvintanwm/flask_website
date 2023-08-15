from website import db # This is same as from website import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    """
    Represents a note stored in the application's database.

    This class defines the structure of the note entity, including attributes
    like ID, data, creation date, and the associated user.

    Attributes:
        id (int): The unique identifier of the note.
        data (str): The content of the note.
        date (datetime): The creation date and time of the note (default to the current time).
        user_id (int): The ID of the user who created the note.

    Example:
        new_note = Note(data='This is a note content', user_id=1)
        db.session.add(new_note)
        db.session.commit()
    """

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    """
    Represents a user in the application's database.

    This class defines the structure of the user entity, including attributes
    like ID, email, password, first name, and notes associated with the user.

    Attributes:
        id (int): The unique identifier of the user.
        email (str): The email address of the user (unique).
        password (str): The hashed password associated with the user.
        first_name (str): The first name of the user.
        notes (list of Note): A relationship to associated notes.

    Inherits from:
        db.Model: Provides database interaction functionality.
        UserMixin: Adds common user-related attributes and methods.

    Example:
        new_user = User(email='user@example.com', password='hashed_password', first_name='John')
        db.session.add(new_user)
        db.session.commit()
    """

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # Link the relationship of User table with Note table
    notes = db.relationship('Note')