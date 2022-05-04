def invert(dictionary: dict):
    # trans = {}
    # for key, val in dictionary.items():
        
    #     trans[val] = key
        
        
    # for k, v in trans.items():   
    #     del dictionary[v]
    #     dictionary[k] = v
    
    copy = {}

    for key in dictionary:
        copy[key] = dictionary[key]
    for key in copy:
        del dictionary[key]
        dictionary[copy[key]] = key

