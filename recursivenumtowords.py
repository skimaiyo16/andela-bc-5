""" moved here to optimize - no need to create this list each time in our recursion"""
words = ["Zero", "one", "Two", "Three", "Four", "Five", "six", "Seven", "Eight", "Nine"]

def num_to_words(n):
	"""
	using recursion to convert a number into num_to_words
	"""
	
	if n < 9 :
		return  words[n]
	else :
		return num_to_words(n//10)+' '+ words[n%10]

print num_to_words(13567)