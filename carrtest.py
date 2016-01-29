class Car(object):
  
  def __init__(self, name='General', model='GM', cartype='saloon', speed=0, num_of_doors=4, num_of_wheels=4, **karg):
    self.name = name
    self.model = model
    self.num_of_doors = num_of_doors
    self.num_of_wheels = num_of_wheels
    self.cartype = cartype
    self.speed = speed
    
    for k, v in karg.items():
      setattr(self, k, v)
      
    if self.name == 'Porshe' or self.name == 'Koenigsegg':
      self.num_of_doors = 2

    if self.cartype =='trailer':
      self.num_of_wheels = 8
      
      
  def drive(self, n):

    if self.cartype =='trailer':
      
      self.speed = (n * 10) + 7
      return self

    else:
      self.speed = (300 * n) + 100
      return self
      
      
  def is_saloon(self):
    if self.cartype == 'saloon':
      return True
      return False


# tests 
honda = Car('Honda')
print type(honda) is Car
print isinstance(honda, Car)
print honda.name 
print honda.model

print '----------------------------------------'
gm = Car()
print gm.name 
print gm.model

print '----------------------------------------'
opel = Car('Opel', 'Omega 3')
porshe = Car('Porshe', '911 Turbo')

print opel.num_of_doors
print porshe.num_of_doors
print    Car('Koenigsegg', 'Agera R').num_of_doors
print '------------------------------------------'

man = Car('MAN', 'Truck', 'trailer')
print dir(man)
koenigsegg = Car('Koenigsegg', 'Agera R')
print man.num_of_wheels
print koenigsegg.num_of_wheels
print '------------------------------------------'

koenigsegg = Car('Koenigsegg', 'Agera R')
print koenigsegg.is_saloon()


man = Car('MAN', 'Truck', 'trailer')
parked_speed = man.speed
moving_speed = man.drive(7).speed
print parked_speed
print moving_speed