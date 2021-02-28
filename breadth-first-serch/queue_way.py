"""
幅優先探索をqueueで解く方法

探索対象は、queueのため幅優先で探索されることになる

特徴
・探索済みは、visitedで管理を行う
・範囲と条件で移動可能名場合は、その場所をqueueに格納して、探索を行う
・queueに候補がある限り探索を行う

問題は、ATC001
https://nashidos.hatenablog.com/entry/2020/01/04/234842
"""

import sys
H, W = list(map(int, input().split()))
c = [list(input()) for h in range(H)]
visited = [[0 for w in range(W)] for h in range(H)]
queue = []

for h in range(H):
    for w in range(W):
        if c[h][w] == "s":
            visited[h][w] = 1
            queue.append([h, w])

while queue:
    # queue的な取り出し（配列最後の取得）
    now_pos = queue.pop()

    # 上下左右移動
    move_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for move in move_list:
        moved_y = now_pos[0] + move[0]
        moved_x = now_pos[1] + move[1]

        if 0 <= moved_y < H and 0 <= moved_x < W:
            if c[moved_y][moved_x] == "g":
                print("Yes")
                sys.exit()

            elif c[moved_y][moved_x] == "." and visited[moved_y][moved_x] == 0:
                queue.append([moved_y, moved_x])
                visited[moved_y][moved_x] = 1

print("No")
