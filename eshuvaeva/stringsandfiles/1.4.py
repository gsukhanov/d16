name = str(input())
m = 0
f_read = open(name, 'r')
for line in f_read.readlines():
	line = line.strip()
	s = line.split(" ")
	print(s)
	for j in range(len(s)):
		word = s[j]
		if word == word[::-1]:
			m = m + 1
print(m)
f_read.close()
