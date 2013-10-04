"""
"""
from nekrobox.docdecs import params
from . import gateaddr
from . import pathing


@params(origin=(int, "Point of origin symbol"),
        length=(int, "Length of address excluding origin"),
        count=(int, "Number of addresses to generate"),
        symbols=(str, "Symbols for pretty printing"),
        returns=(tuple, "The shortest distance and corresponding address")
def calculate(origin=None, length=6, count=1000, 
              symbols="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """Generate a mass of addresses and find the fastest address to dial."""
    symbolcount = len(symbols)

    shortest = (float('Inf'), [])
    for address in gateaddr.generate(origin, count, length, symbolcount):
        distance = pathing.address_distance(address, symbolcount)
        if distance < shortest[0]:
            shortest = (distance, address)
    return shortest
            
