ll =["a","b","c","d"]
num = 2**(len(ll))

for i in range(num):
    lll = []
    for j in range(len(ll)):
        print("start")
        print(i)
        print(bin(i))
        print(i >> j)
        print(bin(i >> j))
        print("end")
        if(i >> j & 1):
            lll.append(ll[j])

    print(lll)
    print(len(lll))
