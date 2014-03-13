n = int(input())
end_zero = [1]
end_one = [1]
for i in range(1, 45):
	end_zero.append(end_zero[i - 1] + end_one[i - 1])
	end_one.append(end_zero[i - 1])
print(end_zero[n - 1] + end_one[n - 1])	 
