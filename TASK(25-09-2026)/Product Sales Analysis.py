#Product Sales Analysis
#A retail company stores the daily sales quantity of a product for several consecutive days. Due to seasonal changes, some days may have negative adjustments. The company wants to identify the period that produced the highest multiplication of sales-related values. Develop a solution to determine this maximum product.
a = [2,3,-2,4]

mx = a[0]
mn = a[0]
ans = a[0]

for i in range(1, len(a)):
    x = a[i]

    if x < 0:
        mx, mn = mn, mx

    mx = max(x, mx * x)
    mn = min(x, mn * x)

    ans = max(ans, mx)

print(ans)