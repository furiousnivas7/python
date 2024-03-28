#Example 4: Remove set items
set1 = {0, 1, 2, 3, 4, 5, 6}
print("Original set1:", set1)
#discard an element
set1.discard(4)
print("Updated version 1 of set1:", set1)
#remove an element
set1.remove(3)
print("Updated version 2 of set1:", set1)
#remove non existing element
#set1.remove(7) -> This will raise an error
#discard non existing element - leaves set unchanged
set1.discard(7)
print("Updated version 3 of set1:", set1)
print(set1(3))
