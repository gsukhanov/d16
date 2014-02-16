def triangle(n, k):
    if n == 0 or k == 0:
        return 1
    else:
        return triangle(n, k-1) + triangle(n-1, k)

print(triangle(int(input()), int(input())))
