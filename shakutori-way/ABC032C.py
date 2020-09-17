import sys


def solve():
    N, K = list(map(int, sys.stdin.readline().split()))
    Ss = []
    for _ in range(N):
        s = int(input())
        Ss.append(s)

    if K == 0:
        # コーナーケース
        if 0 in Ss:
            print(N)
        else:
            print(0)
        return

    left = 0  # 左端
    ans = 0  # 最終的に出力する答え
    accum = 1  # 累積

    for right in range(N):
        accum *= Ss[right]

        if accum == 0:
            # 0を掛けた場合は例外で、Nを出力して終了
            print(N)
            return

        while accum > K:
            accum //= Ss[left]
            left += 1
        length = right - left + 1

        ans = max(ans, length)


if __name__ == "__main__":
    solve()