from logging import exception
from operator import is_


from datetime import datetime

def is_it_valid(pic: str):

    if len(pic) != 11:
        return False
    
    marker = pic[6]
    if marker == "+":
        century = "18"
    elif marker == "-":
        century = "19"
    elif marker == "A":
        century = "20"
    else:
        # print("Marker is wonky")
        return False
    
    birth = (int(pic[0:2]), int(pic[2:4]), int(century+pic[4:6]))
    try:
        birth_date = datetime(birth[2], birth[1], birth[0])
    except:
        return False

    if birth_date > datetime.now():
        return False
    
    pid = pic[7:10]
    combined_nums = pic[0:6].lstrip("0") + pid
    remainder = int(combined_nums) % 31

    control_string = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    return control_string[remainder] == pic[-1]
    



# print(is_it_valid("230827-906F"))
# print(is_it_valid("120488+246L"))
# print(is_it_valid("310823A9877"))
# print(is_it_valid("081842-720N"))
# print(80842720%31)
