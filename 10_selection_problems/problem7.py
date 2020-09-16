N = int(input())
l = []
for i in range(N):
    l.append(int(input()))
l.sort()
cnt = 1
for i in range(N-1):
    if l[i] < l[i+1]:
        cnt+=1
print(cnt)
print(set(l))

# 別解
# N = int(input())
# l = sorted([input() for _ in range(N)])
# print(len(set(l)))

