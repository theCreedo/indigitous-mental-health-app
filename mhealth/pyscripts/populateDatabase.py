import pickle
import bisect

from mhealth.app import DB
from models import Dish


# with open('allIngredients.pickle', 'rb') as handle:
#     allIngredients = pickle.load(handle)

# with open('dishToIngredientsDict.pickle', 'rb') as handle:
#     dishToIngredientsDict = pickle.load(handle)
    
with open('allDishes.pickle', 'rb') as handle:
    allDishes = pickle.load(handle)

with open('dishBitMapDict.pickle', 'rb') as handle:
    dishBitMapDict = pickle.load(handle)

with open('dishHTMLDict.pickle', 'rb') as handle:
    dishHTMLDict = pickle.load(handle)

for dish_name in allDishes:
	bitMap = pickle.dumps(dishBitMapDict[dish_name])
	dishData = {
		'dish_name': dish_name,
		'dish_url': dishHTMLDict[dish_name],
		'dish_bitmap': bitMap
	}
	# g.log.info('Creating a Dish')
	# g.log = g.log.bind(dish_name=dishData['dish_name'])
	# g.log.info('Creating a new dish')
	dish = Dish(dishData)
	DB.session.add(dish)
	DB.session.commit()
	# g.log.info('Successfully created dish')


	

##for ingredient in allIngredients:
##    print(ingredient)

##for dish in allDishes:
##    print(dish)

##for dish in dishToIngredientsDict.keys():
##    print(dish + ":")
##    print(dishToIngredientsDict[dish])
##    print("\n\n")

