list = [1,2,3]

for i in list:
    if i == 1:
        list[list.index(i)] = 3

print(list)

x = 5
for i in range(x):
    print(i)