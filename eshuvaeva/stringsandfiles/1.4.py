name = str(input())
m = 0
f_read = open(name, 'r')
for line in f_read.readlines():
	line = line.strip()
	print(line)
	for i in range(len(line)):
		s = line.find(" ")
		if s == -1:
			print(m)
			break
		else:
			k = line[:s]
			if k == k[::-1]:
				m = m + 1
			line = line[(s + 1):]
print(m)
f_read.close()
