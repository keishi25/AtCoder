N, S, D = list(map(int, input().split()))
X_Y_list = [list(map(int, input().split())) for n in range(N)]
import sys

for xy in X_Y_list:
    x = xy[0]
    y = xy[1]

    if x < S and y > D:
        print("Yes")
        sys.exit()

print("No")