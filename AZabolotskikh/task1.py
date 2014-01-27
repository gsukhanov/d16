filename = input();
wordlen = int(input());
try:
	file = open(filename, "r");
except IOError:
	print ("Input/output error");
	exit();
counter = 0;
for line in file:
	line = line.strip();
	for word in line.split():
		word = word.strip();
		if len(word) == wordlen:
			counter += 1;
print (counter);