#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):

    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # loop through all weights...
    for i in range(length):
        # amount needed to reach limit at current index value
        needed_num = hash_table_retrieve(ht, limit - weights[i])
        # if needed_num exists in ht...
        if needed_num is not None:
            # then add it to the answer tuple
            answer = (i, needed_num)
            # answer found. return answer
            return answer
        # if needed_num does NOT exists in ht...
        else:
            # then add current value and index to ht
            hash_table_insert(ht, weights[i], i)
    
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
