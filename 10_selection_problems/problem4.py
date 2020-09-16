A = 30
B = 40
C = 50
X = 6000
cnt = 0

for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            total = 500 * i + 100 * j + 50 * k
            if total == X:
                print(i,j,k)
                cnt += 1

print(cnt)