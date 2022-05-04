def create_tuple(x: int, y: int, z: int):
    smallest = min([x, y, z])
    biggest = max([x, y, z])
    sum = x + y + z
    
    return (smallest, biggest, sum)
