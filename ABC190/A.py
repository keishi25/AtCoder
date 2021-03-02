A, B, C = list(map(int, input().split()))

if A > B :
    print("Takahashi")
elif A < B:
    print("Aoki")
elif A == B:
    if C == 0:
        print("Aoki")
    else:
        print("Takahashi")
