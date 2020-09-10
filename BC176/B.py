N = list(map(int,input()))
cnt = 0

for i in N:
    cnt += i
cnt %= 9
if cnt == 0:
    print("Yes")
else:
    print("No")

