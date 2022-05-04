def new_person(name: str, age: int):

    parts = name.split(" ")

    if name == "" or len(parts) < 2 or len(name) > 40 or age < 0 or age > 150:
        raise ValueError("This din work")
    
    
    return (name, age)



