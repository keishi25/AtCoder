N = int(input())
A =list(map(int, input().split(" ")))
cnt=0

for i in(range(len(A))):
    for j in(range(len(A) - i - 1)):
        print(A[i])
        print(A[j+i+1])
        print("####")
        cnt += A[i]*A[j+i+1]
cnt %= 1000000000+7
print(cnt)
