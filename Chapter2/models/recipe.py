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