lists = [1,2,3,4,5,6,"hello"]
print(lists)
lists.append(9)
print(lists)
lists.append(9)
print(lists)

print(lists.count(9))
print('numero 5 esiintyy paikassa %s' % lists.index(5))

lists.remove(9)
print(lists)