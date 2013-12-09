print("Input the number of recruits and then their position by R and L")
amm = int(input())
column = amm * [0]
for i in range(amm):
	column[i] = input()
key = 0
mainkey = 1

def move(s1 , s2, key):
	key = 0
	if s1 == "R" and s2 == "L":
		s1 = "L"
		s2 = "R"
		key = 1
	return(s1 , s2, key)

while mainkey :
	a = 1
	mainkey = 0
	while a < amm :
		s1 = column[a - 1]
		s2 = column[a]
		s1, s2, key = move(s1 , s2 , key)
		column[a - 1] = s1
		column[a] = s2
		a = a + 1 + key
		if key == 1 :
			mainkey = 1
	if mainkey == 1:
		print(column)