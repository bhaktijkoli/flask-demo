import os
from app.models import User
from app import db
import __main__


def boot():
    if os.path.basename(__main__.__file__).strip(".py") == "run":
        # CREATE DEFAULT USER
        if User.query.count() == 0:
            user = User(os.getenv("DEFAULT_USER_NAME", "admin"), os.getenv("DEFAULT_USER_EMAIL", "admin"), os.getenv("DEFAULT_USER_EMAIL", "admin"))
            db.session.add(user)
            db.session.commit()
            print(" * Created Default User")
