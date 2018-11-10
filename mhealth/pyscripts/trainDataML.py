import pickle
from sklearn import tree

with open('dishes.pickle', 'rb') as handle:
    dishesList = pickle.load(handle)
with open('ingredients.pickle', 'rb') as handle:
    ingredientList = pickle.load(handle)

with open('dishBitMapDict.pickle', 'rb') as handle:
    dishBitMapDict = pickle.load(handle)

TrainInput = list()

for dish in dishesList[:1000]:
    TrainInput.append(dishBitMapDict[dish])
