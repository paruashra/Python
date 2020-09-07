from random import choice


def eat(food, is_healthy):
    if not isinstance(is_healthy, bool):
        raise ValueError("is_healthy must be a boolean")
    ending = "because YOLO!"
    if is_healthy:
        ending = "because my body is a temple"
    return f"I'm eating {food}, {ending}"


def nap(num):
    if not isinstance(num, int):
        raise ValueError("nap hour should be int")   
    if num >= 2:
        return f"Ugh I overslept.  I didn't mean to nap for {num} hours!"
    return f"I'm feeling refreshed after my {num} hour nap"


def is_funny(name):
    if name is 'tim':
        return False
    return True


def laugh():
    return choice(('lol', 'haha', 'tehehe'))
