#Rainwater Collection System
#A city installs buildings of different heights along a straight road. During rainfall, water gets collected between taller buildings. The engineering team needs to calculate the total amount of water that can remain trapped after heavy rainfall based on the heights of the buildings.
a = [3,0,0,2,0,4]

l = 0
r = len(a) - 1
lm = 0
rm = 0
ans = 0

while l <= r:
    if a[l] <= a[r]:
        if a[l] >= lm:
            lm = a[l]
        else:
            ans += lm - a[l]
        l += 1
    else:
        if a[r] >= rm:
            rm = a[r]
        else:
            ans += rm - a[r]
        r -= 1

print(ans)