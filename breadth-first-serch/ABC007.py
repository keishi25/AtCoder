"""
解説
１．visitedはスタート位置からの距離を格納していく二次元配列
２．移動する度に、＋１される
３．未探索の座標に関しては-1が立っている
４．探索後は、visitedに経路合計が記されている
５．移動可能かの判定は、2次元配列ｃを使用する
６．Qに、探索候補のキューが格納される
７．キューから探索候補を取り出す（キューから削除される）
８．次回探索予定の座標をキューに追加する（キューに追加する）
９．6,7を繰り返して、ゴールを目指す
"""

from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy, sx, gy, gx = sy-1, sx-1, gy-1, gx-1
c = [[c for c in input()] for _ in range(R)]
# スタート位置からの距離を格納する2次元配列
visited = [[-1]*C for _ in range(R)]


def bfs(sy,sx,gy,gx,c,visited):
    visited[sy][sx] = 0
    Q = deque([])
    Q.append([sx, sy])

    while Q:
        y,x = Q.popleft()

        if [y, x] == [gy, gx]:
            return visited[y][x]

        for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            # 探索可能かつ未探索の場合
            if c[y+i][x+j] == '.' and visited[y+i][x+j] == -1:
                visited[y+i][x+j] = visited[y][x]+1
                Q.append([y+i,x+j])

print(bfs(sy, sx, gy, gx, c, visited))
