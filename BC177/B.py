S = input()
T = input()
ans = 10000^5
# Tの文字列がSの文字列を左から右にスライドするように、移動する
move = len(S) - len(T) + 1

for i in range(move):
    cnt = 0
    # Tの各単語がSと同じかどうかチェック
    # 異なる場合の数をカウントする
    for j in range(len(T)):
        if S[i+j] != T[j]:
            cnt += 1

    ans = min(ans, cnt)

print(ans)