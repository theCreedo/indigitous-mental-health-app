from mhealth.app import DB

class Dish(DB.Model):
    __tablename__ = 'dishes'

    id = DB.Column(DB.Integer, primary_key=True)
    dish_name = DB.Column(DB.String(255))
    dish_url = DB.Column(DB.String(255))
    dish_bitmap = DB.Column(DB.PickleType)
    
    def __init__(self, dict):
        self.dish_name = dict['dish_name']
        self.dish_url = dict['dish_url']
        self.dish_bitmap = dict['dish_bitmap']
