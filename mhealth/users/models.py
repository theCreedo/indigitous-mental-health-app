from mhealth.app import DB
from flask_user import UserMixin
from mhealth.users.helpers import hash_pwd


class User(DB.Model, UserMixin):
    __tablename__ = 'users'

    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(255))
    email = DB.Column(DB.String(255))
    fname = DB.Column(DB.String(255))
    lname = DB.Column(DB.String(255))
    password = DB.Column(DB.String(255))
    is_auth = DB.Column(DB.Integer)
    is_fitted = DB.Column(DB.Integer)
    num_of_pos_recipes = DB.Column(DB.Integer)
    num_of_neg_recipes = DB.Column(DB.Integer)
    num_of_dishes = DB.Column(DB.Integer)
    num_of_pos_dishes= DB.Column(DB.Integer)
    num_of_neg_dishes = DB.Column(DB.Integer)
    prev_dish = DB.Column(DB.PickleType)
    eval_dish_ids = DB.Column(DB.PickleType)
    X = DB.Column(DB.PickleType)
    y = DB.Column(DB.PickleType)
    clf = DB.Column(DB.PickleType)

    def __init__(self, dictionary):
        self.is_auth = dictionary['is_auth']
        self.is_fitted = dictionary['is_fitted']
        self.username = dictionary['username']
        self.email = dictionary['email']
        self.fname = dictionary['fname']
        self.lname = dictionary['lname']
        self.password = hash_pwd(dictionary['password'])
        self.num_of_dishes = dictionary['num_of_dishes']
        self.num_of_pos_dishes = dictionary['num_of_pos_dishes']
        self.num_of_neg_dishes = dictionary['num_of_neg_dishes']
        self.num_of_pos_recipes = dictionary['num_of_pos_recipes']
        self.num_of_neg_recipes = dictionary['num_of_neg_recipes']

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)
