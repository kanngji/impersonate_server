from pymongo.collection import Collection
from app.models.user import User

def create_user(db: Collection, user: User):
    user_dict = user.dict()
    db.insert_one(user_dict)
