# CS371-Recipes-Project

Run `pip install -r requirements.txt` before running the program

IMPORTANT: This program has only been tested on Windows and is not guaranteed
to work on Mac OS or Linux.

Running database_builder.py will open a window with various options to 
inspect the recipes, add ingredients or genLs, request ingredient substitutions, 
and more.

The Ingredient Info tab will provide a dropdown with a list of all of the 
ingredients in the database. Selecting an ingredient will provide a display 
with all of its isAs, genLs, and allergens. GenLs Info works the same way but 
for genLs.

You can add an ingredient or genL to the database using the next two buttons. 
Your input will be added to the database and accessible via the relevant info 
tabs discussed above. A new genL will have the option of including instances of 
current ingredients. These ingredients will gain the info of the genL through 
forward chaining. 

The Recipes menu allows switching between the five recipes in the database. 
Below that are a list of the ingredients and a button to take you to the 
website of the recipe for more details. 

Below this website button is a status bar that on launch is empty but will 
update to display the last action you have taken. 

The next button, Display Allergens, will display all allergens associated 
with each ingredient in the current recipe. Request Substitution allows you 
to request for an alternative ingredient to one in the recipe. This will 
return all ingredients in the database that have all of the isAs of the 
ingredient to be replaced and do not have any of the allergens that you 
input. Naturally, any ingredients or genLs you have added while the program 
is running will be taken into account.

Finally, there is a link to the GitHub page and a button to close the program.
