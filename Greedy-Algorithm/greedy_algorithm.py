"""
解説サイトリンク
https://nashidos.hatenablog.com/entry/2019/12/30/154116
問題リンク
https://atcoder.jp/contests/abc076/tasks/abc076_b

貪欲法とは、１回の操作ごとにその場での最適な操作方法を選ぶ手法
"""

N = int(input())
K = int(input())
num = 1
for i in range(N):
    if num * 2 < num + K:
        num = num * 2
    else:
        num = num + K

print(num)
