file1 = str(input())
file2 = str(input())
import random
with open(file1, 'w') as f_write:
    f_write.write('В этом файле\n')
    f_write.write('записано случайное число ' + str(random.random()) + '\n')
with open(file2, 'w') as f1_write:
	f_write.write('В этом файле\n')
    f_write.write('записано случайное число ' + str(random.random()) + '\n')




file2 = file1.translate(str.maketrans({"0":"o"}))
f_write.close()
f1_write.close()