import pickle
import bisect


with open('allIngredients.pickle', 'rb') as handle:
    allIngredients = pickle.load(handle)
    
with open('allDishes.pickle', 'rb') as handle:
    allDishes = pickle.load(handle)

with open('dishToIngredientsDict.pickle', 'rb') as handle:
    dishToIngredientsDict = pickle.load(handle)


##for ingredient in allIngredients:
##    print(ingredient)

##for dish in allDishes:
##    print(dish)

##for dish in dishToIngredientsDict.keys():
##    print(dish + ":")
##    print(dishToIngredientsDict[dish])
##    print("\n\n")



dishBitMapDict = {}

for dish in dishToIngredientsDict.keys():
    inIngredients = len(allIngredients) * [0]
    for ingredient in dishToIngredientsDict[dish]:        
        i = bisect.bisect_left(allIngredients, ingredient)
        inIngredients[i] = 1
    dishBitMapDict[dish] = inIngredients

with open('dishBitMapDict.pickle', 'wb') as handle:
    pickle.dump(dishBitMapDict, handle, protocol=pickle.HIGHEST_PROTOCOL)

