import sys

H, W = list(map(int, input().split()))
c = [list(input()) for i in range(W)]
visited = [[0 for h in range(H)] for w in range(W)]
queue = []

for w in range(W):
    for h in range(H):
        if c[w][h] == "s":
            visited[w][h] = 1
            queue.append([w, h])

while queue:
    # queueから位置取得
    now_pos = queue.pop(0)

    delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    # 移動
    for i in range(4):
        now_x = now_pos[0] + delta[i][0]
        now_y = now_pos[1] + delta[i][1]

        # 移動可能か確認
        if 0 < now_x <= w and 0 < now_y <= h:
            if visited[now_x][now_y] == 0 and not c[now_x][now_y] != "#":

                if c[now_x][now_y] == "g":
                    print("Yes")
                    sys.exit()

                queue.append([now_x, now_y])
                visited[now_x][now_y] == 1

print(visited)
print("No")

