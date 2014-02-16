import sys
sys.setrecursionlimit(1000000)
NO_INFO = -1

def input_params():
    n = int(input())
    k = int(input())
    return n, k

def generate_array(n, k):
    data = []
    for i in range(n + 1):
        data.append([NO_INFO] * (k + 1))
    return data

def triangle(data, i, j):
    if i == 0 or j == 0:
        return 1
    if data[i][j] == NO_INFO:
        data[i][j] = triangle(data, i-1, j) + triangle(data, i, j-1)
    return data[i][j]

def main():
    n, k = input_params()
    data = generate_array(n, k)
    print(triangle(data, n, k))

main()
