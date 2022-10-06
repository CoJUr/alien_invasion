# return the remainder from two numbers

# mine:
def remainder(x, y):
    return x % y


# others:
remainder=lambda x,y:x%y



# boolean to string conversion. Create a function that takes a boolean variable
# flag (True) (False) and returns it as a string ("True") ("False").

# mine:
def bool_to_string(flag):
    return str(flag)


# others:
def bool_to_string(flag):
    return "True" if flag == True else "False"


def bool_to_string(flag):
    return "True" if flag else "False"

def bool_to_string(flag):
    if flag:
        return 'True'
    return 'False'

bool_to_string=lambda f:str(f)


# given a dictionary of insults, return the total # of insults used
# total_amount_adjectives({ "a": "moron" }) ➞ 1
# total_amount_adjectives({ "a": "moron", "b": "scumbag" }) ➞ 2

# mine:
def total_amount_adjectives(dct):
    length = len(dct)

    return length


# others:
def total_amount_adjectives(obj):
    return len(obj.values())


def total_amount_adjectives(obj):
    return sum(1 for i in obj.values())

def total_amount_adjectives(obj):
    return len(obj.keys())

