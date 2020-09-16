N, Y = list(map(int, input().split()))
M = [10000, 5000, 1000]
ans = "-1 -1 -1"

for i in(range(N+1)):
    for j in(range(N+1-i)):
        total = 10000*i + 5000*j + 1000*(N-i-j)
        if total == Y:
            ans = i,j,N-i-j

print(ans)