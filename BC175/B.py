#N = input()
#A = list(map(int, input().split()))
N=5
A=[4,4,9,7,5]
cnt=0

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)

    if r > n:
        return

    indices = list(range(r))
    print(indices)
    print(tuple(pool[i] for i in indices))
    yield tuple(pool[i] for i in indices)

    print(range(r))

    while True:
        for i in reversed(range(r)):
            print(i)
            print( i + n - r)
            print("###")
            if indices[i] != i + n - r:
                break
        else:
            return
        print("indices[i]")
        print(indices[i])
        print("###")
        print("###")
        indices[i] += 1

        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1

        yield tuple(pool[i] for i in indices)

cnb = combinations('Adfry', 3)
print(list(cnb))