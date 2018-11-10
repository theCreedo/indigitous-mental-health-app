import os
from bs4 import BeautifulSoup
import pickle

path = '/Users/brianandika/Documents/HACKATHON/ingredients'

allIngredientsSet = set()
allDishes = list()
dishToIngredientsDict = {}
dishHTMLDict = {}
for filename in os.listdir(path):
##     print(filename)
     f = open(path+'/'+filename)
     soup = BeautifulSoup(f, 'html.parser')
     ingredientSoup = soup.find_all("li", class_="recipe-ingredients__list-item")
     dishIngred = list()
     for ingredient in ingredientSoup:
          if not ingredient.span == None:
               i = ingredient.span.string.rstrip().lstrip().lower()
##               print(ingredient.span.string.rstrip().lstrip())
               allIngredientsSet.add(i)
               dishIngred.append(i)
     name = soup.find("h1", class_="content-title__text")
##     print('\nname: ' + name.string.rstrip().lstrip())
     dishName = name.string.rstrip().lstrip()
     dishHTMLDict[dishName] = filename
     allDishes.append(dishName)
     dishToIngredientsDict[dishName] = dishIngred

allIngredients = list(allIngredientsSet)
allIngredients.sort()

#for i in allDishes:
#     print(i+":"+ dishHTMLDict[i])
     
with open('dishHTMLDict.pickle', 'wb') as handle:
    pickle.dump(dishHTMLDict, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('allDishes.pickle', 'wb') as handle:
    pickle.dump(allDishes, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('allIngredients.pickle', 'wb') as handle:
    pickle.dump(allIngredients, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('dishToIngredientsDict.pickle', 'wb') as handle:
    pickle.dump(dishToIngredientsDict, handle, protocol=pickle.HIGHEST_PROTOCOL)
