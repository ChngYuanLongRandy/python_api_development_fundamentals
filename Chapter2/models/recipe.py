recipe_list =[]

def get_last_id():
    """
    returns the last id. If the list is empty then we
    return 1 else we will return the last available
    recipe's ID + 1
    """
    if recipe_list:
        last_recipe = recipe_list[-1]
    else:
        return 1
    return last_recipe.id + 1

class Recipe:
    def __init__(self, name, description, num_of_servings, cook_time, directions):
        self.id = get_last_id()
        self.name = name
        self.description = description
        self.num_of_servings = num_of_servings
        self.cook_time = cook_time
        self.directions = directions
        self.is_publish = False


