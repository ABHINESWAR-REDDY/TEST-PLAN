#Bank Transaction Analysis
#A bank stores transaction amounts for a customer's account. A continuous group of transactions may add up to a specific target amount. The auditing system needs to determine how many different continuous transaction groups produce exactly the specified amount
a = [1,2,1,2,3]
k = int(input())

d = {0: 1}
s = 0
ans = 0

for x in a:
    s += x

    if s - k in d:
        ans += d[s - k]

    d[s] = d.get(s, 0) + 1

print(ans)