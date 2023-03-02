from recipe_scrapers import scrape_me
from ingredient_parser import parse_ingredient
import PySimpleGUI as gui
import webbrowser

gui.theme("DarkBlue")

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
genL_list = []

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
    recipes.append([[], scrape_me(i), i])

# all genLs

milk_product = GenL('milk product')
milk_product.clean()
milk_product.allergen('lactose')
genL_list.append(milk_product)

animal_product = GenL('animal product')
animal_product.clean()
animal_product.allergen('vegan')
animal_product.allergen('vegetarian')
genL_list.append(animal_product)

meat_product = GenL('meat product')
meat_product.clean()
meat_product.isA('meat')
meat_product.isA('protein')
meat_product.genL(animal_product)
genL_list.append(meat_product)

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
chicken_broth.genL(animal_product)
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
def new_ingredient(ing_name, lst_of_genLs, lst_of_isAs, lst_of_allergens):
    new_ing = Ingredient(ing_name)
    new_ing.clean()
    for i in lst_of_genLs:
        new_ing.genL(i)
    for j in lst_of_isAs:
        new_ing.isA(j)
    for k in lst_of_allergens:
        new_ing.allergen(k)
    update_allergens(new_ing)
    update_isAs(new_ing)
    ingredient_list.append(new_ing)

# user adds new genL into database
def new_genL(genL_name, lst_of_genLs, lst_of_isAs, lst_of_allergens, lst_of_instances):
    new_gL = GenL(genL_name)
    new_gL.clean()
    for i in lst_of_genLs:
        new_gL.genL(i)
    for j in lst_of_isAs:
        new_gL.isA(j)
    for k in lst_of_allergens:
        new_gL.allergen(k)
    for l in lst_of_instances:
        l.genL(new_gL)
    update_allergens(new_gL)
    update_isAs(new_gL)
    genL_list.append(new_gL)

# apply forward chaining to determine if an item has an allergy
# first build list of genLs
# then check allergens in all genLs
def update_allergens_helper(ing):
    result = [ing]
    for i in ing.genLList:
        result += update_allergens_helper(i)
    return result

def update_allergens(ing):
    genLs = update_allergens_helper(ing)
    for i in genLs:
        for j in i.allergens:
            if j not in ing.allergens:
                ing.allergen(j)
    return ing.allergens

# apply forward chaining to determine if an item is something
def update_isAs(ing):
    isAs = update_isAs_helper(ing)
    for i in isAs:
        if i not in ing.isAList:
            ing.isA(i)
    return ing.isAList

def update_isAs_helper(ing):
    result = ing.isAList
    for i in ing.genLList:
        result += update_isAs_helper(i)
    return result

# display ingredient info in a new window
def show_ing(ing_name):
    ing = False
    for i in ingredient_list: # find the ingredient object from the name
        if i.name == ing_name:
            ing = i
            break
    if ing: # if we found the ingredient, show its info
        update_isAs(ing)
        update_allergens(ing)
        ing_genLs = [] # get list of names of genLs of the ingredient
        for i in ing.genLList: 
            ing_genLs.append(i.name)
        genLs_str = '' # change list to a string
        if len(ing_genLs) > 0:
            ind = -1
            for i in ing_genLs:
                ind += 1
                if ind > 0:
                    genLs_str += ', ' + i
                else:
                    genLs_str += i
        ing_isAs = [] # do same thing for the isAs
        for i in ing.isAList: 
            ing_isAs.append(i)
        isAs_str = ''
        if len(ing_isAs) > 0:
            ind = -1
            for i in ing_isAs:
                ind += 1
                if ind > 0:
                    isAs_str += ', ' + i
                else:
                    isAs_str += i
        ing_allergens = [] # and finally for allergens
        for i in ing.allergens:
            ing_allergens.append(i)
        allergens_str = ''
        if len(ing_allergens) > 0:
            ind = -1
            for i in ing_allergens:
                ind += 1
                if ind > 0:
                    allergens_str += ', ' + i
                else:
                    allergens_str += i
        layout = [
            [gui.Text(ing_name,font=(16))],
            [gui.Text('isAs:'),
             gui.Text(isAs_str)],
            [gui.Text('genLs:'),
             gui.Text(genLs_str)],
            [gui.Text('allergens:'),
             gui.Text(allergens_str)],
            [gui.Button('Close',key='-CLOSE-')]
        ]
        window = gui.Window(ing_name + ' info',layout,size=(400,300),element_justification='center',margins=(6,20))
        while True:
            event, values = window.read()
            if event == gui.WIN_CLOSED or event == '-CLOSE-': # when window closes
                break
        window.close()

# display genL info in a new window
def show_genL(genL_name):
    genL = False
    for i in genL_list: # find the genL object from the name
        if i.name == genL_name:
            genL = i
            break
    if genL: # if we found the genL, show its info
        update_isAs(genL)
        update_allergens(genL)
        genL_genLs = [] # get list of names of genLs of the genL
        for i in genL.genLList: 
            genL_genLs.append(i.name)
        genLs_str = '' # change list to a string
        if len(genL_genLs) > 0:
            ind = -1
            for i in genL_genLs:
                ind += 1
                if ind > 0:
                    genLs_str += ', ' + i
                else:
                    genLs_str += i
        genL_isAs = [] # do same thing for the isAs
        for i in genL.isAList: 
            genL_isAs.append(i)
        isAs_str = ''
        if len(genL_isAs) > 0:
            ind = -1
            for i in genL_isAs:
                ind += 1
                if ind > 0:
                    isAs_str += ', ' + i
                else:
                    isAs_str += i
        genL_allergens = [] # and for allergens
        for i in genL.allergens:
            genL_allergens.append(i)
        allergens_str = ''
        if len(genL_allergens) > 0:
            ind = -1
            for i in genL_allergens:
                ind += 1
                if ind > 0:
                    allergens_str += ', ' + i
                else:
                    allergens_str += i
        genL_instances = [] # and finally for instances
        for i in genL.instances:
            genL_instances.append(i)
        instances_str = ''
        if len(genL_instances) > 0:
            ind = -1
            for i in genL_instances:
                ind += 1
                if ind > 0:
                    instances_str += ', ' + i.name
                else:
                    instances_str += i.name
        layout = [
            [gui.Text(genL_name,font=(16))],
            [gui.Text('isAs:'),
             gui.Text(isAs_str)],
            [gui.Text('genLs:'),
             gui.Text(genLs_str)],
            [gui.Text('allergens:'),
             gui.Text(allergens_str)],
            [gui.Text('instances:'),
             gui.Text(instances_str)],
            [gui.Button('Close',key='-CLOSE-')]
        ]
        window = gui.Window(genL_name + ' info',layout,size=(400,300),element_justification='center',margins=(6,20))
        while True:
            event, values = window.read()
            if event == gui.WIN_CLOSED or event == '-CLOSE-': # when window closes
                break
        window.close()

# get list of ingredient names from ingredients list
def get_ingredient_name(ing_lst):
    result = []
    for i in ing_lst:
        result.append(i.name)
    return result

# get list of recipe names from recipes list
def get_recipe_name(rec_lst):
    result = []
    for i in rec_lst:
        result.append(i[1].title())
    return result

ingredient_menu_def = ['Ingredient', get_ingredient_name(ingredient_list)]
genLs_menu_def = ['GenL', get_ingredient_name(genL_list)]
recipe_menu_def = ['Recipe', get_recipe_name(recipes)]

ing_lst = ''
ind = -1
for i in recipes[0][1].ingredients():
    ind += 1
    if ind > 0:
        ing_lst += '\n' + i
    else:
        ing_lst += i

ins_lst = ''
ind = -1
for i in recipes[0][1].instructions_list():
    ind += 1
    if ind > 0:
        ins_lst += '\n' + i
    else:
        ins_lst += i

# window's layout design
layout_top = [  [gui.Text("Recipe Project",font=(18))]]

layout_middle_top = [gui.Column([[gui.ButtonMenu('Ingredient Info',menu_def=ingredient_menu_def,border_width=5,key='-DISPLAY-INGREDIENT-')]]),
                     gui.Column([[gui.ButtonMenu('GenLs Info',menu_def=genLs_menu_def,border_width=5,key='-DISPLAY-GENL-')]]),
                     gui.Column([[gui.Button('Add Ingredient',key='-ADD-INGREDIENT-')]]),
                     gui.Column([[gui.Button('Add GenL',key='-ADD-GENL-')]])]
            
layout_middle = [  [gui.Text("What recipe would you like?"),
                    gui.ButtonMenu('Recipes',menu_def=recipe_menu_def,border_width=5,key='-RECIPE-',visible=True)]]

layout_middle_bottom = [[gui.Text(recipes[0][1].title(),key='-RECIPE-TITLE-')],
                        [gui.Text('Ingredients')],
                        [gui.Text(ing_lst,key='-INGREDIENT-LIST-')],
                        [gui.Button('Visit Website for More Info',key='-WEBSITE-')]]

layout_bottom = [   [gui.Text('',key='-STATUS-')],
                    gui.Column([[gui.Button('Display Allergens',key='-DISPLAY-ALLERGENS-')]]),
                    gui.Column([[gui.Button('Request Substitution',key='-SUBSTITUTION-')]]),
                    gui.Column([[gui.Button('GitHub',key='-GITHUB-')]]),
                    gui.Column([[gui.Button('Close',key='-CLOSE-')]])
]

layout = [
    [   
        layout_top,
        layout_middle_top,
        layout_middle,
        layout_middle_bottom,
        layout_bottom
    ]
]

# window creation
window = gui.Window('Recipe Project', layout,size=(750,600),element_justification='center')

print(recipes[0][1].host())

# event loop
def win_run():
    # active recipe
    # default to first recipe
    active_recipe = recipes[0]
    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED or event == '-CLOSE-': # when window closes
            break
        elif event == '-DISPLAY-INGREDIENT-': # when the user wants to display an ingredient
            selection = values[event] # get name of ingredient
            show_ing(selection) # display ingredient info in new window
            window['-STATUS-'].update('Displayed info for ' + selection + '.')
        elif event == '-DISPLAY-GENL-': # when the user wants to display a genL
            selection = values[event] # get name of genL
            show_genL(selection) # display genL info in new window
            window['-STATUS-'].update('Displayed info for ' + selection + '.')
        elif event == '-WEBSITE-':
            url = active_recipe[2]
            webbrowser.open(url)
    window.close()

def main():
    print()
    win_run()

if __name__ == "__main__":
    main()
