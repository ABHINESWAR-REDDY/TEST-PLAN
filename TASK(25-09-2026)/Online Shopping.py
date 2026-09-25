#Online Shopping Price Analysis
#An online shopping application stores the prices of products viewed by a customer during a browsing session. The customer wants to identify a continuous range of products that provides the maximum possible total discount value. Given the discount values, determine the maximum value that can be obtained from any continuous range.
a = [-2, 3, 4, -1, 2, -5]

cur = a[0]
ans = a[0]

for i in range(1, len(a)):
    cur = max(a[i], cur + a[i])
    ans = max(ans, cur)

print(ans)