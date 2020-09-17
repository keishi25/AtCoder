"""
１．上下左右方向{(1,0),(0,1),(-1,0),(0,-1)}に進める
２．条件を満たさない場合は、処理を中断する
３．再起処理で、処理を回して探索を進める
"""

import sys

h, w = map(int, input().split())
c = [list(input()) for i in range(h)]

# 再帰関数の呼び出し制限
sys.setrecursionlimit(10 ** 7)

# スタート位置の探索
for i in range(h):
    for j in range(w):
        if c[i][j] == "s":
            sx, sy = i, j  # スタート位置


def dfs(x, y):
    # 壁に当たったり、探索範囲外になった場合はreturn
    if not (0 <= x < h) or not (0 <= y < w) or c[x][y] == "#":
        return

    # ゴールを見つけたら”Yes”を出力して終了
    if c[x][y] == "g":
        print("Yes")
        sys.exit()

    # 探索済みを示すためのマーキング
    c[x][y] = "#"

    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)

dfs(sx, sy)
print("No")
