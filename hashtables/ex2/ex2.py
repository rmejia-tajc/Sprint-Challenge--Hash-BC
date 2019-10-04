#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # loop through all tickets...
    for i in range(length):
        # if the current ticket's does not have a source...
        if tickets[i].source == "NONE":
            # then this is the first flight. Add it to the beginning of route
            route[0] = tickets[i].destination
        # add the current value to hashtable (key=source, value=destination)
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
    
    for t in range(length):
        if route[t-1] is not None:
            route[t] = hash_table_retrieve(hashtable, route[t-1])

    return route
