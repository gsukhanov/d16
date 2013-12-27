print ("Введите строй солдат: 1 - лицом налево, 0 - лицом направо")
recruits = list(input())
n = len(recruits)
recruits_array = []
for j in range (n):
	r = int(recruits[j])
	if r not in [1,0]:
		print ("Таких солдат не бывает! Только 0 или 1")
		exit()
	recruits_array.append(r)
t=0
while True:
	t = t + 1
	print ("Попытка",t)
	i = -1
	k = 0
	while i < (n-2):
		i = i + 1
		if recruits_array[i] == 0:
			if recruits_array[i+1] == 1:
				recruits_array[i] = 1
				recruits_array[i+1] = 0
				i = i + 1
				k = k + 1
	print(recruits_array) 	
	if k == 0:
		break
print("Процесс остановился за",t,"секунд")
