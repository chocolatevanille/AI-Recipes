import requests
from recipe_scrapers import scrape_me
from ingredient_parser import parse_ingredient

# ingredient class, keeps track of various important details
class Ingredient:
    isAList = []
    genLList = []
    allergens = []

    def __init__(self, name):
        self.name = name

    def isA(self, type):
        self.isAList.append(type)

    def genL(self, type):
        self.genLList.append(type)
        type.instance(self)

    def allergen(self, item):
        self.allergens.append(item)

    # for some reason, this is necessary on initialization
    # otherwise, these lists start out with random shit in them
    # wtf python i hate you
    def clean(self):
        self.isAList = []
        self.genLList = []
        self.allergens = []

# genL class, subclass of ingredients but also has a list of instances
# list of instances may not actually ever be used
# wanted to keep track of it just in case
class GenL(Ingredient):
    instances = []

    def clean(self):
        self.isAList = []
        self.genLList = []
        self.allergens = []
        self.instances = []

    def instance(self, item):
        self.instances.append(item)


ingredient_list = []

# list of all of our recipes, only five but could add more if we want -- unnecessary
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

# all genLs

milk_product = GenL('milk product')
milk_product.clean()
milk_product.allergen('lactose')

animal_product = GenL('animal product')
animal_product.clean()
animal_product.allergen('vegan')
animal_product.allergen('vegetarian')

meat_product = GenL('meat product')
meat_product.clean()
meat_product.genL(animal_product)

# all ingredients

ketchup = Ingredient('ketchup')
ketchup.clean()
ketchup.isA('condiment')
ingredient_list.append(ketchup)

honey = Ingredient('honey')
honey.clean()
honey.isA('sauce')
ingredient_list.append(honey)

soy_sauce = Ingredient('soy sauce')
soy_sauce.clean()
soy_sauce.isA('sauce')
ingredient_list.append(soy_sauce)

garlic = Ingredient('garlic')
garlic.clean()
garlic.isA('spice')
ingredient_list.append(garlic)

pork_chop = Ingredient('pork chop')
pork_chop.clean()
pork_chop.isA('protein')
pork_chop.genL(meat_product)
ingredient_list.append(pork_chop)

cabbage = Ingredient('cabbage')
cabbage.clean()
cabbage.isA('leafy green')
ingredient_list.append(cabbage)

tomato = Ingredient('tomato')
tomato.clean()
tomato.isA('vegetable')
ingredient_list.append(tomato)

onion = Ingredient('onion')
onion.clean()
onion.isA('alliaceae')
ingredient_list.append(onion)

italian_seasoning = Ingredient('italian seasoning')
italian_seasoning.clean()
italian_seasoning.isA('seasoning')
ingredient_list.append(italian_seasoning)

salt_and_pepper = Ingredient('salt and ground black pepper')
salt_and_pepper.clean()
salt_and_pepper.isA('seasoning')
ingredient_list.append(salt_and_pepper)

chicken_breast = Ingredient('chicken breast')
chicken_breast.clean()
chicken_breast.isA('protein')
chicken_breast.genL(meat_product)
ingredient_list.append(chicken_breast)

barbecue_sauce = Ingredient('barbecue sauce')
barbecue_sauce.clean()
barbecue_sauce.isA('sauce')
ingredient_list.append(barbecue_sauce)

olive_oil = Ingredient('olive oil')
olive_oil.clean()
olive_oil.isA('cooking oil')
ingredient_list.append(olive_oil)

thyme = Ingredient('thyme')
thyme.clean()
thyme.isA('spice')
ingredient_list.append(thyme)

parsley = Ingredient('parsley')
parsley.clean()
parsley.isA('spice')
ingredient_list.append(parsley)

rosemary = Ingredient('rosemary')
rosemary.clean()
rosemary.isA('spice')
ingredient_list.append(rosemary)

apple_cider_vinegar = Ingredient('apple cider vinegar')
apple_cider_vinegar.clean()
apple_cider_vinegar.isA('vinegar')
ingredient_list.append(apple_cider_vinegar)

butter = Ingredient('butter')
butter.clean()
butter.isA('butter')
butter.genL(milk_product)
ingredient_list.append(butter)

chicken_broth = Ingredient('chicken broth')
chicken_broth.clean()
chicken_broth.isA('broth')
chicken_broth.genL(meat_product)
ingredient_list.append(chicken_broth)

red_pepper = Ingredient('red pepper flake')
red_pepper.clean()
red_pepper.isA('spice')
ingredient_list.append(red_pepper)

recipes[0][0] = [ketchup, honey, soy_sauce, garlic, pork_chop]
recipes[1][0] = [cabbage, tomato, onion, italian_seasoning, salt_and_pepper]
recipes[2][0] = [chicken_breast, barbecue_sauce, salt_and_pepper]
recipes[3][0] = [chicken_breast, salt_and_pepper, olive_oil, thyme, parsley, rosemary, apple_cider_vinegar, butter, chicken_broth]
recipes[4][0] = [honey, soy_sauce, red_pepper, olive_oil, chicken_breast]

# user adds new ingredient into database
def new_ingredient(ing_name, lst_of_genLs, lst_of_isAs):
    # do something
    return

# apply forward chaining to determine if an item has an allergy
# first build list of genLs
# then check allergens in all genLs
def find_allergens_helper(ing):
    result = [ing]
    for i in ing.genLList:
        result += find_allergens_helper(i)
    return result


def find_allergens(ing):
    genLs = find_allergens_helper(ing)
    for i in genLs:
        for j in i.allergens:
            if j not in ing.allergens:
                ing.allergen(j)
    return ing.allergens

# example: chicken broth has vegan and vegetarian allergies
# derived from its genLs
print(find_allergens(chicken_broth))
