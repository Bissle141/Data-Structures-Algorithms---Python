def merge(lst1, lst2):
    combined = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            combined.append(lst1[i])
            i += 1
        else:
            combined.append(lst2[j])
            j += 1
    while i < len(lst1):
        combined.append(lst1[i])
        i += 1
    while j < len(lst2):
        combined.append(lst2[j])
        j += 1
    return combined
        
            
        




# MERGE REQUIRES TWO SORTED LISTS:
print(merge([1,2,7,8], [3,4,5,6]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7, 8]
 """