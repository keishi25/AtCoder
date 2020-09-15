ll =["a","b","c","d"]
num = 2**(len(ll))
for i in range(num):
    lll = []
    for j in range(len(ll)):
        if(i >> j & 1):
            lll.append(ll[j])

    print(lll)
    print(len(lll))
