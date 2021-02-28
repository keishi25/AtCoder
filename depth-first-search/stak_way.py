"""
深さ優先探索をstackで解く方法

探索対象は、stackのため深さ優先で探索されることになる

特徴
・探索済みは、visitedで管理を行う
・範囲と条件で移動可能名場合は、その場所をstackに格納して、探索を行う

問題は、ATC001
https://nashidos.hatenablog.com/entry/2020/01/04/234842
"""

import sys
h,w = map(int,input().split())
c = [list(input()) for i in range(h)]

for i in range(h):
    for j in range(w):
        if c[i][j] == "s":
            sx,sy = i,j #スタート
        elif c[i][j] == "g":
            gx,gy = i,j #ゴール

stack = [[sx,sy]]
visited = [[0 for i in range(w)]for j in range(h)]
visited[sx][sy] = 1

dx_dy = [[1,0],[0,1],[-1,0],[0,-1]]

while stack:
    x,y = stack.pop() #要素を取り出す
    for i in range(4):
        nx,ny = x+dx_dy[i][0], y+dx_dy[i][1] #現在の位置
        if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and c[nx][ny] != '#':
            visited[nx][ny] = 1 #訪れた印をつける
            stack.append([nx,ny]) #スタックに現在位置をpush
    if visited[gx][gy] == 1:
        print("Yes")
        sys.exit()

print("No")