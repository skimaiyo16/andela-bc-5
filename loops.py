# for loops
for i in range(0,10):
	print i
print '------------------------------------------- '
		
for i in range(1,11):
	print i
print '------------------------------------------- '

# print on the same line without newline character		
for i in range(2,10):
	print i,

# using format to print output
names = "James Clare Brian Ann Eric Sammy".split()
count = 0
for i in range(20, 26):
	print "I'm {0}, and i'm {1} years old".format(names[count], i)
	count += 1
print '------------------------------------------- '


# loop from ten to Zero - steps is the last parameter that tells which direction to move
for i in range(10, -1, -1):
	print i
print '------------------------------------------- '

# while loop
n = 10
while n >= 0:
	print n
	n -= 1
