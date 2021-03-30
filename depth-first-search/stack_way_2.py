H, W = list(map(int, input().split()))
C = [list(input()) for i in range(H)]

import sys

# 深さ優先探索
# stackを使用する
stack = []

for i in range(H):
    for j in range(W):
        if C[i][j] == "s":
            stack.append([i, j])

while stack:
    current_pos = stack.pop()  # 後方から取得
    moved_pos_list = [
        [current_pos[0] + 1, current_pos[1]],
        [current_pos[0], current_pos[1] + 1],
        [current_pos[0] - 1, current_pos[1]],
        [current_pos[0], current_pos[1] - 1]
    ]

    for moved_pos in moved_pos_list:
        y = moved_pos[0]
        x = moved_pos[1]
        if 0 <= y < H and 0 <= x < W:
            if C[y][x] == "g":
                print("Yes")
                sys.exit()
            elif C[y][x] == ".":
                C[y][x] = "#"
                stack.append([y, x])

print("No")