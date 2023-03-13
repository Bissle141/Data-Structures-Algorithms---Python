def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(lst, pivot_indx, end_indx):
    swap_indx = pivot_indx
    for i in range(pivot_indx + 1, end_indx + 1):
        if lst[pivot_indx] > lst[i]:
            swap_indx += 1
            swap(lst, swap_indx, i)
    swap(lst, swap_indx, pivot_indx)
    return swap_indx
            



my_list = [4,6,1,7,3,2,5]

print('List before running pivot():')
print(my_list)

returned_pivot_index = pivot(my_list, 0, 6)

print('\nList after running pivot():')
print(my_list)

print('\nPivot Index:')
print(returned_pivot_index)



"""
    EXPECTED OUTPUT:
    ----------------
    List before running pivot():
    [4, 6, 1, 7, 3, 2, 5]

    List after running pivot():
    [2, 1, 3, 4, 6, 7, 5]

    Pivot Index:
    3

 """