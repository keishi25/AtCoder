given = ["dreamer", "dream", "eraser", "erase"]
S = input()

while len(S) > 0:
    # 後方から、givenと同じ単語を探す。戻り値はTrue
    judge = [S.endswith(i) for i in given]

    # 同じ単語がある場合は、処理を続ける
    if any(judge):
        # 同じ単語を取りだす。戻り値は、任意の単語名
        target = given[judge.index(True)]

        # 単語数だけ、Sから引く
        S = S[:-len(target)]
        if len(S) == 0:
            print("YES")
            break
    else:
        print("NO")
        break
