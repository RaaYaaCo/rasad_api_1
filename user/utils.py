import random


def code(length: int = 5) -> str:
    """
        The function "code()" takes in "length" and returns a five-length string for default.
    """
    chars = "0123456789"
    ret = ""
    for i in range(length):
        rand = random.choice(chars)
        # print(rand)
        ret += rand

    return ret
