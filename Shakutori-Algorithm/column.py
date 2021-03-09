"""
問題リンク
https://atcoder.jp/contests/abc032/tasks/abc032_c

解説リンク
https://nashidos.hatenablog.com/entry/2020/02/02/165319
"""

n, k = list(map(int, input().split()))
s = [int(input()) for i in range(n)]

# ｓの中に０がある場合、積の関係上nが答えとなる
if 0 in s:
    print(n)
else:
    right, ans, tmp = 0, 0, 1

    # # leftは、開始位置。開始位置を最後までスライドさせて、探索を行う
    for left in range(n):

        # rightは、終了位置。終了位置が条件を満たしている限り、右にスライドさせる
        while right < n and tmp*s[right] <= k:
            tmp *= s[right]
            right += 1

        # 前回結果と比較して、大きい方をansに格納する
        ans = max(ans, right - left)

        # 以下次回処理の準備
        if left == right:
            right += 1
        else:
            # 次回順次処理では、leftを右にスライドさせるため、s[left]の積の考慮分を除しておく
            tmp //= s[left]

    print(ans)
