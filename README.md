# Q1:
Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010

# Code:
```
import re
inp=input()
nums = re.findall(r'[01]+', inp)
res=[]
for i in nums:
    dec=int(i,2)
    if dec%5==0:
        res.append(i)
print(",".join(res))
```

# Output:
<img width="317" height="247" alt="image" src="https://github.com/user-attachments/assets/980a9337-2364-4687-84fb-8d5e6b336914" />


# Q2:
Write a Python program that accepts a sentence and calculate the number of letters and digits.Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

# Code:
```
n=input()
digit=0
letter=0
for i in n:
    if i.isalpha():
        letter+=1
    elif i.isdigit():
        digit+=1
print("Letters:",let)
print("Digits:",dig)
```

# Output:

<img width="307" height="252" alt="image" src="https://github.com/user-attachments/assets/c6ad7dfc-bbbb-44f5-9c47-f95dc9000223" />

# Q3:
Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program:8
Then, the output should be:40320

# Code:
```
num=int(input())
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)
```

# Output:
<img width="155" height="198" alt="image" src="https://github.com/user-attachments/assets/b3045118-6d37-4aa9-bd49-454e85ed07c4" />

