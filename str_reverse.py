def reverse(s):
	"""
	 returns the reverse of a stting 
	 one statement uses list comprehension
	 """
	return s[:: -1]



def reversex(s):
	"""
    reverse a string using a loop
    """
    # makes  list from the string; because they are immutable 
 	s = list(s) 
 	# does a floor division (discards remainder) to reverse a string 
 	# you need to do this to avoid reversal of the reverse 
 	for i in range(len(s) // 2) : 
 		temp = s[i]
 		s[i] = s[len(s) - i - 1]
 		s[len(s) - i - 1] = temp
 	# makes the string from the list after reversal 
 	return "".join(s) 


def reversey(s):
	"""
	a reversal without a temporary variable version
	"""
	s = list(s) 
 	for i in range(len(s) // 2) :
 		# swap to avoid using a temporary variable
		s[i], s[len(s) - i - 1]	= s[len(s) - i - 1], s[i] 
 	return "".join(s)
	
def reversez(s):
	"""
	yet another way to swap
	"""
	pass



# examples
print reverse("andela")
print reversex("hello")
print reversey("hello world")

