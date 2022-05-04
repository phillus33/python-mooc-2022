def search_by_name(filename: str, word: str):
    recipes = {}
    recipe_name = True
    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()
            if line == "":
                recipe_name = True
                continue       
            
            if recipe_name == True:
                recipes[line] = ""

            recipe_name = False
        # print(recipes)
    
    result = []
    for name in recipes:
        if word in name.lower():
            result.append(name)
    return result

def search_by_time(filename: str, prep_time: int):
    recipes = {}
    recipe_name = True
    recipe_time = False
    actual_name = ""
    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()
            if line == "":
                recipe_name = True
                continue       
            
            if recipe_name == True:
                actual_name = line
                recipes[actual_name] = ""

                recipe_name = False
                recipe_time = True
            
            elif recipe_time == True:
                recipes[actual_name] = line
                recipe_time = False

    result = []
    
    for name, time in recipes.items():
        if int(time) <= prep_time:
            result.append(f"{name}, preparation time {time} min")
    return result

def search_by_ingredient(filename: str, ingredient: str):
    
    recipes = {}
    tmp = []
    ingreds = []
    recipe_name = True
    recipe_time = False

    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()

            if line == "":
                recipes[tmp[0], tmp[1]] = ingreds
                tmp = []
                ingreds = []
                recipe_name = True
                continue    

            elif recipe_name == False and recipe_time == False:
                ingreds.append(line)  
            
            elif recipe_name == True:
                tmp.append(line)

                recipe_name = False
                recipe_time = True
            
            elif recipe_time == True:
                tmp.append(line)
                recipe_time = False
        recipes[tmp[0], tmp[1]] = ingreds
    result = []
    for nametime, ingredients in recipes.items():
        # print(nametime, ingredients)
        if ingredient in ingredients:
            result.append(f"{nametime[0]}, preparation time {nametime[1]} min")
    return result

                
    

# found_recipes = search_by_name("recipes1.txt", "cake")
# for recipe in found_recipes:
    # print(recipe)

# found_recipes = search_by_time("recipes1.txt", 20)
# for recipe in found_recipes:
#     print(recipe)

# found_recipes = search_by_ingredient("recipes1.txt", "eggs")
# for recipe in found_recipes:
#     print(recipe)