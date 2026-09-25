#1. Student Attendance Analysis
#A college maintains the daily attendance details of its students in the form of a list containing student IDs. Some students may have attended multiple sessions on the same day. The administration wants to identify the longest continuous sequence of sessions in which no student ID is repeated. Develop a solution that determines the maximum length of such a sequence.
a = [1,2,3,1,4,5]

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