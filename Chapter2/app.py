from flask import Flask
from flask_restful import Api
from resources.recipe import RecipeListResource, RecipeResource, RecipePublic

app = Flask(__name__)
api = Api(app)

# this is called resource routing
api.add_resource(RecipeListResource,'/recipes')
api.add_resource(RecipeResource,'/recipes/<int:recipe_id>')
api.add_resource(RecipePublic, '/recipes/<int:recipe_id>/publish')

if __name__ == "__main__":
    app.run(port=5000, debug = True)