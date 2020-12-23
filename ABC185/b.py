"""
https://atcoder.jp/contests/abc185/tasks/abc185_b
"""
import sys

n, m, t = list(map(int, input().split()))
tmp = n
leave = 0

for i in range(m):
    a, b = map(int, input().split())
    tmp -= (a - leave)
    if tmp <= 0:
        print("No")
        sys.exit()
    else:
        leave = b
        tmp += (b - a)
        if tmp > n:
            tmp = n

tmp -= (t - leave)
if tmp <= 0:
    print("No")
else:
    print("Yes")


