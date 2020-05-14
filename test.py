a = [1,1.1,2,1.2,1.3,5,4,1.4,7,1.5,4]

for i in a:
    print(i)
    print(a)
    if i < 2:
        a.append(a.pop(a.index(1)))
print(a)
