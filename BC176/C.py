N = input()
A = list(map(int, input().split()))
cnt = 0

for i in(range(len(A) - 1)):
    if A[i] > A[i+1]:
        cnt += (A[i] - A[i+1])
        A[i+1] = A[i]

print(cnt)

