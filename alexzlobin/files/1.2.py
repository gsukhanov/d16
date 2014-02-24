file_name = input("input file: ")
input_file = open(file_name , 'r')
keyword= input()
amount = 0
for line in input_file:
	words = line.split()
	for word in words:
		if  word == keyword:
			amount += 1
print(amount)
