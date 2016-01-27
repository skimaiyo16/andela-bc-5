"""
list comprehension
get squares of numbers from 0 through to 10 
"""
x = [i**2 for i in range(11)]
print x
a = "zero one two three four five six seven eight nine ".split()
print a
n = '123'
y = [a[int(i)] for i  in n ]
print y