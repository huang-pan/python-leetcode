
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
