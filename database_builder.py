import requests
from recipe_scrapers import scrape_me
from ingredient_parser import parse_ingredient

# list of all of our recipes, probably no more than five
recipe_urls = ['https://www.allrecipes.com/recipe/235158/worlds-best-honey-garlic-pork-chops/',
               'https://www.allrecipes.com/recipe/229324/ground-beef-and-cabbage/',
               'https://www.allrecipes.com/recipe/280052/bbq-chicken-breasts-in-the-oven/',
               'https://www.allrecipes.com/recipe/245367/pan-roasted-chicken-breasts/',
               'https://www.allrecipes.com/recipe/231939/honey-glazed-chicken/']
parsed_recipes = []
for recipe in recipe_urls: # parse recipes with recipe_scrapers
    parsed_recipes.append(scrape_me(recipe))

class Ingredient:
    isAList = []
    allergens = []

    def __init__(self, name):
        self.name = name

    def isA(self, type):
        self.isAList.append(type)
    
    def allergen(self, item):
        self.allergens.append(item)

# example
beef = Ingredient('beef')
beef.isA('red meat')
print(beef.isAList)

ingredients = []
for i in parsed_recipes:
    for j in i.ingredients():



print(ingredients)

