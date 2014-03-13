file1 = str(input())
file2 = str(input())
f_read = open(file1, 'r')
for line in f_read.readlines():
	line = line.strip()
	r = line.translate(str.maketrans({'в':'а', 'ы':'б','з':'в','а':'д','н':'е', 'я':'ё','т':'ж', 'ч':'з','о':'и','е':'й','с':'к', 'л':'л','и':'м','н':'к','ж':'о', 'г':'п','п':'р', 'р':'с','д':'т','ё':'у','у':'ф', 'м':'х','й':'ц','ф':'ч','ю':'ш', 'ь':'щ','ц':'ь', 'х':'э','ш':'ю','б':'я'}))
f_read.close()
f_read = open(file2, 'w')
f_read.writelines(r)
f_read.close()

f_read = open(file2, 'r')
for line in f_read.readlines():
	line = line.strip()
	print(line)
f_read.close()
