x = 4
y = 3
z = y + (x < y and 4 or x == y and 5 or 6)
print(z)  # using logical operators in formulas
print("\nA=========\n")

list1 = [(1, -1), (2, -2), (3, -3)]
print(list1[-1])  # negative indexing
print("\nB=========\n")

for i in list1:
    print(i)  # for loop without len() where i is of type list[n]
print("\nC=========\n")

corners = [(0, 0), (1, 0), (0, 1), (1, 1)]
print(corners[0][0])
print("\nD=========\n")

print(max(list1))
print("\nE=========\n")

for i in range(1, 4):
    print(i)
print("\nF=========\n")

for i in list1:
    print(i[1])
print("\nG=========\n")

print((4, 0) > (3, 100))
print("\nH=========\n")

test = (1, 0)
test2 = (1, 2, 3)
print(type(test[0]) == int)
