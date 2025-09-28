a='wa'
b='wb'
c='wc'
d='wd'

zlist=[a,b,c,d]
vlist=zlist[1:3]

# print(zlist, vlist)

# zlist[1] = 'wC'

# del a, b

# print(zlist, vlist)

nlist = list(zlist)

print(zlist, nlist)

nlist[1] = 'wB'

print(zlist, nlist)

liz = [['water']] * 8
print(liz)

liz[1][0] = 'house' # this changes for all because they reference the same object and that object is mutable.

print(liz)

