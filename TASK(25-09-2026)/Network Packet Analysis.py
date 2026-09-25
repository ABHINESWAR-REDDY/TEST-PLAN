#Network Packet Analysis
#A network monitoring system receives packet identifiers in chronological order. The system must determine the longest sequence of consecutive packets whose identifiers form a continuous numerical sequence, regardless of their original order in the incoming data.
a = [100,4,200,1,3,2]

s = set(a)
ans = 0

for x in s:
    if x - 1 not in s:
        y = x
        c = 1

        while y + 1 in s:
            y += 1
            c += 1

        ans = max(ans, c)

print(ans)