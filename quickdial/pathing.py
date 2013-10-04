from nekrobox.docdecs import params


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
