
array=[5,4,2,-1,7,0]
maximum	= array[0]
for x in range(len(array)):
	if array[x]>maximum:
		maximum = array[x]
print (maximum)
