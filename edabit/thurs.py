# a function that returns the first el of a list

# mine:
def get_first_value(number_list):
    return number_list[0]

# others:
def get_first_value(number_list):
    if not number_list: return None
    return number_list[0]

get_first_value=lambda l:l[0]

