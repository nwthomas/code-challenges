"""
Write a function that receives a recipe in the form of a dictionary, as well as all of the ingredients you have available to you, also in the form of a dictionary. Both of these dictionaries will have the same form, and might look something like this:

{
  'eggs': 5,
  'butter': 10,
  'sugar': 8,
  'flour': 15
}

The keys will be the ingredient names, with their associated values being the amounts. In the case of the recipe dictionary, these amounts will represent the amount of each ingredient needed for the recipe, while in the case of the ingredients dictionary, the amounts represent the amounts available to you. 

Your function should output the maximum number of whole batches that can be made for the supplied recipe using the ingredients available to you, as indicated by the second dictionary. 

For example

# should return 0 since we don't have enough butter!
recipe_batches(
  { 'milk': 100, 'butter': 50, 'flour': 5 },
  { 'milk': 138, 'butter': 48, 'flour': 51 }
)

 * If there's a dictionary operation you aren't sure of how to perform in Python, look it up!
 * What's the _minimum_ number of loops we need to perform in order to write a working implementation?

Run the test file by executing `python test_recipe_batches.py`.

You can also test your implementation manually by executing `python recipe_batches.py`.
"""

import math


def recipe_batches(recipe, ingredients):
    if len(list(dict.values(recipe))) is not len(list(dict.values(ingredients))):
        return 0
    total_recipes_completed = None
    for val in recipe:
        total = ingredients[val] // recipe[val]
        if total_recipes_completed is None:
            total_recipes_completed = total
        elif total < total_recipes_completed:
            total_recipes_completed = total
    return total_recipes_completed


if __name__ == '__main__':
        # Change the entries of these dictionaries to test
        # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 52, 'flour': 100}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
