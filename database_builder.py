import requests
from recipe_scrapers import scrape_me
from ingredient_parser import parse_ingredient

# ingredient class, keeps track of isA list and allergens
class Ingredient:
    isAList = []
    allergens = []

    def __init__(self, name):
        self.name = name

    def isA(self, type):
        self.isAList.append(type)
    
    def allergen(self, item):
        self.allergens.append(item)

ingredient_list = []

# list of all of our recipes, probably no more than five
recipe_urls = ['https://www.allrecipes.com/recipe/235158/worlds-best-honey-garlic-pork-chops/',
               'https://www.allrecipes.com/recipe/229324/ground-beef-and-cabbage/',
               'https://www.allrecipes.com/recipe/280052/bbq-chicken-breasts-in-the-oven/',
               'https://www.allrecipes.com/recipe/245367/pan-roasted-chicken-breasts/',
               'https://www.allrecipes.com/recipe/231939/honey-glazed-chicken/']

# parse recipes from URLs
# gives methods .ingredients(), .instructions(), .instructions_list(), .title(), .total_time()
recipes = []
for i in recipe_urls:
    recipes.append([[], scrape_me(i)])

recipes[0][0] = ['ketchup', 'honey', 'soy sauce', 'garlic', 'pork chop']
recipes[1][0] = ['cabbage', 'tomato', 'onion', 'Italian seasoning', 'salt and ground black pepper']
recipes[2][0] = ['chicken breast', 'barbecue sauce', 'salt and ground black pepper']
recipes[3][0] = ['chicken breast', 'salt and ground black pepper', 'olive oil', 'thyme', 'parsley', 'rosemary', 'apple cider vinegar', 'butter', 'chicken broth']
recipes[4][0] = ['honey', 'soy sauce', 'red pepper flake', 'olive oil', 'chicken breast']

ketchup = Ingredient('ketchup')
ketchup.isA('condiment')
ingredient_list.append(ketchup)

honey = Ingredient('honey')
honey.isA('sauce')
ingredient_list.append(honey)

soy_sauce = Ingredient('soy sauce')
soy_sauce.isA('sauce')
ingredient_list.append(soy_sauce)

garlic = Ingredient('garlic')
garlic.isA('spice')
ingredient_list.append(garlic)

pork_chop = Ingredient('pork chop')
pork_chop.isA('protein')
pork_chop.allergen('vegan')
pork_chop.allergen('vegetarian')
ingredient_list.append(pork_chop)

cabbage = Ingredient('cabbage')
cabbage.isA('leafy green')
ingredient_list.append(cabbage)

tomato = Ingredient('tomato')
tomato.isA('vegetable')
ingredient_list.append(tomato)

onion = Ingredient('onion')
onion.isA('alliaceae')
ingredient_list.append(onion)

