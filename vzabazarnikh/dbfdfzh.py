
m = [[3, 5], [110,3], [9,0], ]
for i in range(100):
	m.append([0, i])

def f(s):

	return (s[0] * s[0] + s[1] * s[1])

k = sorted(m, key=f)
print(k)