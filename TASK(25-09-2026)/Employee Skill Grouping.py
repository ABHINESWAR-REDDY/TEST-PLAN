#Employee Skill Grouping
#A company receives a list of employee skill codes represented as strings. Employees having the same set of characters in their skill codes belong to the same skill category, even if the characters appear in a different order. The HR system needs to organize employees into appropriate skill groups.
a = ['eat','tea', 'tan', 'ate', 'nat', 'bat']

d = {}

for x in a:
    k = ''.join(sorted(x))

    if k not in d:
        d[k] = []

    d[k].append(x)

print(list(d.values()))