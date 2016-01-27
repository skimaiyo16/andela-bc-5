
#  defining a class  we put object to have it inherit from object if we exclued we will be inheriting
# from Type
class Vehicle (object):

	""" intializer  is optional"""
	def __init__(self, engine_type, **kargs):
		self.engine_type = engine_type
		# fill the properties that the user supplies- since dictonary has two contnet the key and valueS
		for k, v in kargs.items():
		    setattr(self, k, v)

	def set_color(self, color):
		self.color = color



# inheritance (sub classing) the vehicle class
class Car (Vehicle):

	def __init__(self, engine_type, car_category, **kargs):
		# of importance the kargs is being unpacked before sending it to the parent intializer hence the need to use two stars
		super(Car, self).__init__(engine_type, **kargs)
		self.car_category = car_category
		self.doors = 5
		self.wheels = 4
	


# examples :
# instansiate the class	 and printing its color property
my_car = Car('VTL-120','Saloon', engine_cc=1500, color="red", max_speed=320)
print my_car.color
print '------------------------------------------------------'

# a module is a complete phython file
# a package avoid name collision and  to do this in python
		# create a folder
		# put an empty file in it named __init__.py





# -------------------------------------------------------------------------------------------------------------------
#      
#                             CLASS SUPPORTING MATERIAL
# 
#--------------------------------------------------------------------------------------------------------------------

# using  args  to get the sum of multiple number arguments (it is passed as a tuple due to the single dot)
def my_sum(*arg):
	total = 0
	for i in arg:
		total +=i
	return total

print " my sum ", my_sum(10,30)
print " my sum ", my_sum(1, 3, 4, 8, 9, 23)
print '------------------------------------------------------'



# kargs (how to pass variable amount of arguments to the function) it is passed as a dictonary (the two dot )
def output(name, **qua):
	print 'name :' , name 
	for i in qua.keys():
		print i, ": ",qua[i]

output('Angela',age=10, gender='F', loc='NBO')



