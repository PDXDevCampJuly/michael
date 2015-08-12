#Mergesort
from random import randint

l = [4,3,7,4,8,5,4,78,4,3,32,5,7,11,3,2,6,45,7,56,34,23,65,3]
x = [4,5,6]
y = [6,9,3]
def split(local_list):
    split_list = local_list
    lhalf = split_list[:len(split_list)//2]
    rhalf = split_list[len(split_list)//2:]
    return lhalf, rhalf

def sort(nums):
    n=len(nums)
    if n > 1:
        m = n // 2
        left, right = nums[:m], nums[m:]
        sort(left)
        sort(right)
        merge(left, right, nums)

    return nums

def merge(l1, l2, l3):
    #initializes indexes
    i1, i2, i3 = 0, 0, 0
    n1, n2 = len(l1), len(l2)

    while i1 < n1 and i2 < n2:
        if l1[i1] < l2[i2]:
            l3[i3] = l1[i1]
            i1 += 1
        else:
            l3[i3] = l2[i2]
            i2 += 1
        i3 += 1

    while i1 < n1:
        l3[i3] = l1[i1]
        i1 += 1
        i3 += 1

    while i2 < n2:
        l3[i3] = l2[i2]
        i2 += 1
        i3 += 1

print(sort(l))
