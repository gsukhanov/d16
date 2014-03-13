file1 = str(input())
file2 = str(input())
f_read = open(file1, 'r')
for line in f_read.readlines():
	line = line.strip()
	r = line.translate(str.maketrans({'а':'в', 'б':'ы','в':'з','д':'а','е':'н', 'ё':'я','ж':'т', 'з':'ч','и':'о','й':'е','к':'с', 'л':'л','м':'и','н':'к','о':'ж', 'п':'г','р':'п', 'с':'р','т':'д','у':'ё','ф':'у', 'х':'м','ц':'й','ч':'ф','ш':'ю', 'щ':'ь','ь':'ц', 'э':'х','ю':'ш','я':'б'}))
f_read.close()
f_read = open(file2, 'w')
f_read.writelines(r)
f_read.close()

f_read = open(file2, 'r')
for line in f_read.readlines():
	line = line.strip()
	print(line)
f_read.close()
