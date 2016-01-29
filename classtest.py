class  PrimeChecker(object):
  
    def __init__(self, number):
  	  self.number = number


	def is_prime(self):
	  if (self.number > 1 ):
	  	lst =[ number % x for x in range(2, number) if number % x == 0]
	  	if len(lst) > 0:
	  	    return False
	  	else:
	  	    return True    
	  else:
	  	return False



