#Example 3: Adding item to tuple using +
Tuple1 = (1, 2, 3)
print("Original Tuple:", Tuple1)
Tuple2 = ('ABCD', 'WXYZ', 5, 6, 7)
Tuple1 = Tuple1 + Tuple2
print("Update version 1 of Tuple:", Tuple1)
Tuple2 = (1,'ABC', 2, 'XYZ', 3, 'abc', 'XYZ')
for i, res in enumerate(Tuple2):
    print (i,":",res)
