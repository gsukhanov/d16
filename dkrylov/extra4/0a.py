a = [-20,14,1,0,-1,2,9]

m=a[0]

for i in range(len(a)):
	if a[i]>m:
		m=a[i]
	
print(m)