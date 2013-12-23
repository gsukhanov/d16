summ = 0;
for i in range(1,301):
    summ += (1/i);

print ("first number equals:", summ, "which is ", end="");
if summ > 5:
    print("greater", end='');
else:
    print("less", end='');
print (" than five");