def number_with_fixed_sum_of_digits(n,k):
        if n == 0 and k > 0:
                return 0
        if n == 0 and k == 0: 
                return 1
        if k > (n * 9):
                return 0
        if k < 0:
                return 0
        answer = 0
        for i in range (10):
                answer += number_with_fixed_sum_of_digits (n-1,k-i)
        return answer
ht_count = 0
for k in range (28):
        ht_count += (number_with_fixed_sum_of_digits(3, k)) ** 2
print(ht_count) 
        

		
