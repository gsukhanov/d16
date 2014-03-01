inputFilename = input();
outputFilename = input();
try:
	inputFile = open(inputFilename, "r");
	outputFile = open(outputFilename, "w");
except IOError:
	print ("Input/output error");
	exit();
wordnum = 0;
for line in inputFile:
	line = line.strip();
	for word in line.split():
		wordnum += 1;
		word = word.strip();
		if wordnum % len(word) != 0:
			outputFile.write(word + ' ');
	outputFile.write('\n')