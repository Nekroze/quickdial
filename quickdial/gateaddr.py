from random import randint
from types import GeneratorType
from nekrobox.docdecs import params
from six.moves import range


@params(origin=(int, "Final origin symbol, if None then random"),
        count=(int, "Number of addresses to generate"),
        length=(int, "Length of a gate address in symbols excluding origin"),
        symbols=(int, "Number of symbols to choose from"),
        returns=(GeneratorType, "Pumps out gate addresses as specified."))
def generate(origin=None, count=1000, length=6, symbols=36):
    """Returns a generator that pumps out randomly generated gate addresses."""
    if origin is None:
        origin = randint(1,symbols)
    return ([randint(1,symbols) for _ in range(length)] + [origin] 
            for _ in range(count))


@params(address=(list, "Gate address as generated"),
        symbols=(str, "Pretty symbols to convert address to"),
        returns=(str, "The gate address converted into a string"))
def pretty(address, symbols="ABCDEFGHIJQLMNOPQRSTUVWXYZ0123456789"):
    """
    Converts the given gate address into a string by converting symbol
    numbers to characters in the symbol string.

    Symbols are grouped in threes.
    """
    characters = []
    for x in address:
        characters.append(symbols[x])
        if len(characters) >= 3:
            characters.append(' ')
    return ''.join(characters)
