N, M, T = list(map(int, input().split()))
out = []
for i in range(M):
    a, b = list(map(int, input().split()))
    out.append([a, b])

import sys
tmp1 = N
tmp2 = 0
for i in out:
    if tmp1 - (i[0] - tmp2) < 0:
        print(tmp1)
        print(i[0])
        print(tmp2)
        print(tmp1 - (i[0] - tmp2))
        print('No')
        sys.exit()
    tmp1 = tmp1 - (i[0] - tmp2) + (i[1] - i[0])
    tmp2 = i[0]
    print("aa")

print('Yes')