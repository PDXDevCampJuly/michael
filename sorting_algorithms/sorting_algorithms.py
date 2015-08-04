# Implementation of various sorting algorithms for lists
##########################

from sys import argv
import time

filename = (argv[1])


# python sorting algorithm
def python_sort(our_list):
    return sorted(our_list)


def list_swap(our_list, low, high):
    """
    Uses simultaneous assignment to swap it with the one we are moving.
    """
    our_list[low], our_list[high] = our_list[high], our_list[low]
    return our_list


def selection_sort(our_list):
    """
    Look through the list.  Find the smallest element.  Swap it to the front.
    Repeat.
    """
    # first for-loop grabs the zero index declares it lowest
    # we set the range to perform the calculates for the length of the list minus the last spot of the range because there is nothing to compare to. it will be the largest value of the list
    # begin the first for-loop, declare variables
    for start_index in range(len(our_list) - 1):
        lowest_index = start_index

        # second for-loop grabs the next_index to compare
        for next_index in range(start_index + 1, len(our_list)):
            if our_list[next_index] < our_list[lowest_index]: # values
                lowest_index = next_index
        list_swap(our_list, start_index, lowest_index)

    return our_list


def insertion_sort(our_list):
    """
    Insert (via swaps) the next element in the sorted list of the previous
    elements.
    """
    # we want to begin at the first index and compare to the index before it. if the index is -1, break out of the loop. we first declare our minimum to the index[1] to test backwards. this is opposite from the selection_sort because we know that the last index is the highest so we do not need to run it
    for start_index in range(1, len(our_list)):
        min_value = our_list[start_index] # declare smallest value
        position_index = start_index

        while position_index > 0 and our_list[position_index - 1] > min_value:
            our_list[position_index], position_index = our_list[position_index - 1], position_index - 1
            print(our_list)
        our_list[position_index] = min_value

    return our_list


def merge_sort(our_list):
    """
    Our first recursive algorithm. Divide and conquer
    """
    # base case, single item list
    if len(our_list) == 1:
        return our_list

    # integer division //, floor
    middle = len(our_list) // 2
    list1 = merge_sort(our_list[:middle])
    list2 = merge_sort(our_list[middle:])

    list3 = []

    while len(list1) > 0 and len(list2) > 0:
        if list1[0] < list2[0]:
            list3.append(list1.pop(0))
        else:
            list3.append(list2.pop(0))
    list3 += list1 + list2

    return list3

def linear_search(x, our_list):
    """
    Searching through the list of items one by one until the target value is found.
    """
    for i in range(len(our_list)):
        if our_list[i] == x: # item found, return the index value
            return i

    return -1 # loop finished, item was not in list


# retrieve a file
if __name__ == '__main__':

    with open(filename, "r") as f:
      our_list = eval(f.read())


# print(selection_sort(our_list))
# print(insertion_sort(our_list))
print(merge_sort(our_list))
# print(linear_search(8, our_list))

