#Example 8: Combining Sets
set1 = {1, 2, 7}
set2 = {5, 8}
set3 = {0, 6}
#using union
res_set1 = set1.union(set2)
print("Resulting set 1:", res_set1)
#using union for multiple sets
res_set2 = set().union(set1).union(set2).union(set3)
print("Resulting set 2:", res_set2)
#using update
set2.update(set3)
print("Updated set2:", set2)
#using |
print('Join set1 and set2:', set1 | set2)
print('Join set2 and set3:', set2 | set3)
#using *
res_set3 = (*set1, *set2, *set3)
print("Resulting set 3:", res_set3)
