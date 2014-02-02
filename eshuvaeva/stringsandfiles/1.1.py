name = str(input())
k = int(input())
m = 0
string = name
f_read = open(name, 'r')
for line in f_read:
    line = line.strip()
    for i in range(len(string)):
    	s = name.find(" ")
    	if k == s:
    		m = m + 1
    	string = string[s:]
    print(m)
f_read.close() 

