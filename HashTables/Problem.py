def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

def in_common(lst1, lst2):
    lst = lst1+lst2
    if len(lst) == len(set(lst)):
        return False
    return True

def in_common2(lst1, lst2):
    table = {}
    for i in lst1:
        table[i] = True
        
    print(table)
    for i in lst2:
        if i in table:
            return True
    return False

def in_common3(lst1, lst2):
    for i in lst1:
        if i in lst2:
            return True
    return False

list1 = [1,3,6]
list2 = [2,4,6]

print(item_in_common(list1, list2))
print(in_common3(list1, list2))

