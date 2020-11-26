import random
import string


def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    """Random string generator."""
    return "".join(random.choice(chars) for _ in range(size))
