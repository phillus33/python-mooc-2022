
def balanced_brackets(my_string: str):

    if len(my_string) == 0:
        return True

    if not my_string[0] in "()[]":
        return balanced_brackets(my_string[1:])
    
    if not my_string[-1] in "()[]":
        return balanced_brackets(my_string[:-1])

    if my_string[0] == "(" and my_string[-1] == ")":
        return balanced_brackets(my_string[1:-1])

    if my_string[0] == "[" and my_string[-1] == "]":
        return balanced_brackets(my_string[1:-1])

    return False
    

    # smooth brain version
    # valid = "()[]"
    # my_string = "".join([c for c in my_string if c in valid])
    
    # if len(my_string) == 0:
    #     return True
    # if not ((my_string[0] == '(' and my_string[-1] == ')') or (my_string[0] == '[' and my_string[-1] == ']')):
    #     return False
    # return balanced_brackets(my_string[1:-1])

if __name__ == "__main__":
    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)