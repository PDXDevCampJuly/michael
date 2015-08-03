# Implementation of various sorting algorithms for lists
##########################

from sys import argv

filename = (argv[1])

# retrieve the char10.txt file
with open(filename, "r") as f:
  our_list = eval(f.read())


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
    # find the smallest
    # for start in range(len(our_list)):
    #     mindex = start
    #     minimum = our_list[start]
    #     for index in range(start + 1, len(our_list)):
    #         if our_list[index] < minimum:
    #             mindex = index
    #             minimum = our_list[index]
    #     if mindex != start:
    #         list_swap(our_list, start, mindex)
    # return our_list

    # len of the list is len - 1 as you move to the right
    for start_item in range(len(our_list) - 1):
        min_position = start_item
        for i in range(start_item + 1, len(our_list)):
            if our_list[i] < our_list[min_position]:
                min_position = i

        list_swap(our_list, start_item, min_position)
    return our_list
# print(selection_sort(our_list))


def insertion_sort(our_list):
    """
    Insert (via swaps) the next element in the sorted list of the previous
    elements.
    """
    for index in range(1, len(our_list)):
        candidate = our_list[index]
        comparison_index = index - 1
        while index >= 0:
            if candidate < our_list[comparison_index]:
                list_swap(our_list, comparison_index, comparison_index + 1)
                comparison_index -= 1
            else:
                break
    return our_list
# print(insertion_sort(our_list))


def merge_sort(our_list):
    """
    Our first recursive algorithm. Divide and conquer
    """
    middle = len(our_list)
    print(middle)


print()


def linear_search(x, our_list):
    """
    Searching through the list of items one by one until the target value is found.
    """
    for i in range(len(our_list)):
        if our_list[i] == x: # item found, return the index value
            return i
    return -1 # loop finished, item was not in list
# print(linear_search(8, our_list))

