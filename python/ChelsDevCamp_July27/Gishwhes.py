# Implimentation of various sorting algorithms for lists
##########################

def selection_sort(ourlist):
    """
    Look through the list.  Find the smallest element.  Swap it to the front.
    Repeat.
    """

    for fillslot in range(len(ourlist)-1, 0, -1):
        postionofmax = 0
        for location in range(1, fillslot+1):
            if ourlist[location] > ourlist[postionofmax]:
                postionofmax = location


        temp = ourlist[fillslot]
        ourlist[fillslot] = ourlist[postionofmax]
        ourlist[postionofmax] = temp

ourlist = [1, 5, 7, 3, 2, 4, 6, 10, 8, 9]
selection_sort(ourlist)
print(ourlist)
    
def insertion_sort(ourlist):
    """
    Insert (via swaps) the next element in the sorted list of the previous
    elements.
    """


    for index in range(1,len(ourlist)):

        currentvalue = ourlist[index]
        postion = index

        while postion > 0 and ourlist[postion-1] > currentvalue:
            ourlist[postion] = ourlist[postion-1]
            postion = postion-1

        ourlist[postion] = currentvalue

ourlist = [1, 5, 7, 3, 2, 4, 6, 10, 8, 9]
insertion_sort(ourlist)
print(ourlist)
    
    
def merge_sort(ourlist):
    """
    Our first recursive algorithm.
    """
#    print("Splitting ",ourlist)
    if len(ourlist)>1:
        mid = len(ourlist)//2
        lefthalf = ourlist[:mid]
        righthalf = ourlist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                ourlist[k]=lefthalf[i]
                i=i+1
            else:
                ourlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            ourlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            ourlist[k]=righthalf[j]
            j=j+1
            k=k+1
 #   print("Merging ",ourlist)

ourlist = [1, 5, 7, 3, 2, 4, 6, 10, 8, 9]
merge_sort(ourlist)
print(ourlist)












