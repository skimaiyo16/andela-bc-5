# lambda example

# our usual plain  function
def add(x, y):
	return x + y

# the function as lamda (anomymous functon ) 
y = lambda x, y: x + y 

# example
print y(10, 12)
print'--------------------------------------------------------------'



# anonymous function 
def make_incremetor(n):
	def inc(x):
		return x + n 
	return inc 

z = make_incremetor(10)
print z(20)
print'--------------------------------------------------------------'


# same in lambda avoiding the anonymous function
def make_incrementorl(n):
	 return lambda x: x + n

z1 = make_incrementorl(10)
print z1(20)	
print'--------------------------------------------------------------'


# filter for even numbers in a list
def is_even(n):
	return n%2 == 0 # phython shortcut does not need a if  as the expression always returns true or false

l=[2, 10, 4, 5, 6, 9]
new_list = filter(is_even, l)
print  new_list
print'--------------------------------------------------------------'

# the sane filter with lamda
new_list2 = filter(lambda n: n % 2 == 0 , l)
print new_list2
print'--------------------------------------------------------------'


# immediate invocation - getting square of 4 
print (lambda x: x ** 2)(4)
print'--------------------------------------------------------------'

# list comprehension the lamda way produces a list of squares within the given range of numbers
f = lambda s, e: [i * i for i in range(s, e+1)]

new_listDD = f(2,12)
print new_listDD
print'--------------------------------------------------------------'

# nesting lamda
f = lambda x: (lambda i: x * (i ** 2))
print f(2)(3)
print'--------------------------------------------------------------'


# type checking (examples include str, dict ...)
a = 'good'
# check if variable is a string returning true or false
print isinstance(a, str)
print'--------------------------------------------------------------'
print type(a) is str # another way to test 

