
mystring = ["eat", "tea", "tan", "ate", "nat", "bat"]

strings = []
for ele in mystring:
    strings += [ele]

print(strings)

myset = set('a')
myset.add('b')
myset.add('c')
print(myset)
print(''.join(myset)) # unordered

tempstring = 'afdg'
ss = sorted(tempstring)
print(''.join(ss))

mydict = {}
mydict[5] = 1
print(mydict)

test = 'abc'
print(test[:1]) # a, index 0
print(test[1:]) # bc, index 1 to end

print(range(2))
for i in range(2):
    print(i)
for i in range(1, 2):
    print(i)    