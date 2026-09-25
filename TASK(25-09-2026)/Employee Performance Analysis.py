#Employee Performance Analysis
#A company stores the monthly performance scores of an employee for several months. The scores may contain both positive and negative values depending on the employee's performance. Management wants to identify the continuous period during which the employee achieved the highest overall performance.
a = [-3,5,-2,6,-8]

cur = a[0]
ans = a[0]

for i in range(1, len(a)):
    cur = max(a[i], cur + a[i])
    ans = max(ans, cur)

print(ans)