from nekrobox.docdecs import params
from six.moves import range


@params(one=(int, "First symbol"),
        two=(int, "Next symbol"),
        symbols=(int, "Number of symbols to choose from")
        returns=(int, "Shortest distance"))
def distance(one, two, symbols=36):
    """Get the shortest distance between two symbols."""
    lowest, highest = (one, two) if one < two else (two, one)

    straight = one - two if one > two else two - one
    
    end = symbols - highest
    loop = end + lowest
    
    return straight if straight < loop else loop


@params(address=(list, "Gate address as generated"),
        symbols=(int, "Number of symbols")
        returns=(int, "Shortest distance"))
def address_distance(address, symbols=36):
    """Get the shortest distance to dial this address."""
    dist = 0
    for pos in range(len(address[:-1])):
        dist += distance(address[pos], address[pos+1], symbols)
    return dist
