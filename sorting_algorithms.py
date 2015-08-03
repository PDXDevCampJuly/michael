# Implementation of various sorting algorithms for lists
##########################


def python_sort(our_list):
    return sorted(our_list)


def list_swap(our_list, low, high):
    our_list[low], our_list[high] = our_list[high], our_list[low]
    return our_list


def selection_sort(our_list):
    """
    Look through the list.  Find the smallest element.  Swap it to the front.
    Repeat.
    """
    smallest = 0
    start_index = 0
    tracker = our_list[0]

    # find the smallest
    for item in our_list[start_index:]:
        if smallest in our_list:
            break
        else:
            smallest += 1
            continue
    print("smallest:", smallest)
    print("smallest index[{}]:".format(our_list[smallest] - 1))

    # smallest_index = our_list[smallest] - 1
    # our_list.insert(0, our_list.pop(smallest_index))
    # print(our_list)

    smallest_index = our_list[smallest] - 1
    our_list[0] = smallest
    our_list[smallest_index] = tracker
    print(our_list)

    start_index += 1

selection_sort([20, 10, 4, 5, 3, 8, 11, 6, 9])


def insertion_sort(our_list):
    """
    Insert (via swaps) the next element in the sorted list of the previous
    elements.
    """
    pass


def merge_sort(our_list):
    """
    Our first recursive algorithm.
    """
    pass

