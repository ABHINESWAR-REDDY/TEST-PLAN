#Customer Purchase History
#An e-commerce application stores the product IDs purchased by a customer in chronological order. The same product may appear multiple times. The system needs to determine the longest sequence of consecutive purchases in which every product ID is unique
a = [1,2,3,2,1,4]

s = set()
l = 0
ans = 0

for r in range(len(a)):
    while a[r] in s:
        s.remove(a[l])
        l += 1

    s.add(a[r])
    ans = max(ans, r - l + 1)

print(ans)