# usual imports

from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.recipe import Recipe, recipe_list


# these guys will handle the methods when recipe is called with the get
# and post methods respectively. 
# localhost:5000/recipes
class RecipeListResource(Resource):
    def get(self):
        data =[]

        for recipe in recipe_list:
            if recipe.is_publish is True:
                data.append(recipe.data)
        return {'data':data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()
        recipe = Recipe(name = data['name'],
                        description = data['description'],
                        num_of_servings= data['num_of_servings'],
                        cook_time = data['cook_time'],
                        directions = data['directions'])
        recipe_list.append(recipe)

        return recipe.data, HTTPStatus.CREATED


# these methods are defined for localhost:5000/recipes/<int>
class RecipeResource(Resource):
    def get(self, recipe_id):
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id and recipe.is_publish == True), None)
        
        if recipe is None:
            return{'message':'recipe is not found'}, HTTPStatus.NOT_FOUND
        
        return recipe.data, HTTPStatus.OK

    def put(self, recipe_id):
        data = request.get_json()
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)
        
        if recipe is None:
            return{'message':'recipe is not found'}, HTTPStatus.NOT_FOUND
        
        recipe.name = data['name']
        recipe.description = data['description']
        recipe.num_of_servings = data['num_of_servings']
        recipe.cook_time = data['cook_time']
        recipe.directions = data['directions']

        return recipe.data, HTTPStatus.OK

# this will define the PUT method to change the publish from False to True
# and also defining the DELETE method to delete a recipe which just means to 
# change the publish from True to False
# both in localhost:5000/recipes/<int> 
class RecipePublic(Resource):
    def put(self, recipe_id):
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)
        
        if recipe is None:
            return{'message':'recipe is not found'}, HTTPStatus.NOT_FOUND

        recipe.is_publish == True

        return {}, HTTPStatus.NO_CONTENT

    def delete(self, recipe_id):
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)
        
        if recipe is None:
            return{'message':'recipe is not found'}, HTTPStatus.NOT_FOUND

        recipe.is_publish == False

        return {}, HTTPStatus.NO_CONTENT
