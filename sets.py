#sets

my_sets = {3, 5, 12, 9, 33}

print(my_sets)

my_sets.add(44)
print(my_sets)

my_sets.remove(9)
print(my_sets)

set1 = {2, 4, 6}
set2 = {6, 7, 8}

union_set  = set1.union(set2)
print(union_set)

inter_set = set1.intersection(set2)
print(inter_set)

deff_set = set1.difference(set2)

print(deff_set)
