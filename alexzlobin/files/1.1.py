file_name=input("input file:")
input_file = open(file_name, 'r')
lenkeyword=int(input())
amount=0
for line in input_file:
	line=line.split()
	for words in line:
		if len(words)==lenkeyword:
			amount+=1
print(amount)
