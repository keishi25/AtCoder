import math
a,b,h,m=list(map(int, input().split()))


th_a = 360/12 * h + 360/12*m/60
th_b = 360*m/60

ab_th = abs(th_a - th_b)
if ab_th > 180:
    ab_th = 360 - ab_th

print(math.sqrt(a*a + b*b -2*a*b*math.cos(math.radians(ab_th))))
