import requests
from recipe_scrapers import scrape_me
from ingredient_parser import parse_ingredient

# list of all of our recipes, probably no more than five
recipe_urls = ['https://www.allrecipes.com/recipe/235158/worlds-best-honey-garlic-pork-chops/']
parsed_recipes = []
for recipe in recipe_urls: # parse recipes with recipe_scrapers
    parsed_recipes.append(scrape_me(recipe))
