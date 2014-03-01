import array
import cryptlib as c
keystr = input("enter key:")
key = array.array('B')
key.fromstring(keystr)
file = input('enter input file:')
c.init(key,len(key))
a = array.array('B')
a.fromstring(open(file, 'rb').read())
for i in range(len(a)):
    a[i]^=c.getbyte()
open(file+'enc','wb').write(a.tostring())
