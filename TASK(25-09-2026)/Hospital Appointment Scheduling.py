#Hospital Appointment Scheduling
#A hospital receives appointment requests represented by starting and ending times. Some appointments overlap with each other. The scheduling system needs to combine overlapping appointment periods so that the final schedule contains only non-overlapping time ranges.
a = [[1,3], [2,6], [8,10], [9,12]]

a.sort()

ans = [a[0]]

for x in a[1:]:
    if x[0] <= ans[-1][1]:
        ans[-1][1] = max(ans[-1][1], x[1])
    else:
        ans.append(x)

print(ans)