from app import db, app
from app.user.models import User


def mock_data():
    ...

    db.session.add_all([])
    db.session.commit()
    print("mock data added")


with app.app_context():
    db.create_all()
    print("database created")

    # mock_data()
