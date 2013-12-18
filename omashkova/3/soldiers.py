soldiers = list(input())
seconds = 0
while True:
	seconds += 1
	print (soldiers)
	face_to_face = []
	turn_in_process = False
	for n in range (len(soldiers) - 1):
		if soldiers[n] == "1" and soldiers[n+1] == "0":
			face_to_face.append(n)
			face_to_face.append(n+1)
			turn_in_process = True
	for d in face_to_face:
		soldiers[d] = str(1 - int(soldiers[d]))
	if turn_in_process == False:
		break	
print (seconds)		
