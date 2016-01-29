
class  PrimeChecker(object):
  
  def __init__(self, number):
    self.number = number

  def is_prime(self):
    if self.number =='':
      return False
    x1 = int(self.number)
    if x1 > 1 :
      lst =[ x1 % x for x in range(2, x1) if x1 % x == 0]
      if len(lst) > 0:
        return False
      else:
        return True
    else:
      return False

yu = PrimeChecker('7')
print yu.is_prime()


class Car(object):
  
  def __init__(self, name ='General', model ='GM', cartype ='salon', num_of_doors = 4, num_of_wheels = 4 **karg):
    
    self.name = name
    self.model = model
    self.num_of_doors = num_of_doors
    self.num_of_wheels = num_of_wheels
    self.cartype = cartype
    
    for k, v in karg.items():
      setattr(self, k, v)
      
    if self.name == 'Porshe' or self.name == 'Koenigsegg':
      self.num_of_doors = 2
    if  self.cartype 
       num_of_wheels