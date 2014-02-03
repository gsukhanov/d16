name = str(input())
k = int(input())
m = 0
f_read = open(name, 'r')
for line in f_read.readlines():
	line = line.strip()
	print(line)
	for i in range(len(line)):
		s = line.find(" ")
		if k == s:
			m = m + 1
		line = line[(s + 1):]
print(s)
print(m)
f_read.close()