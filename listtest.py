def find_missing(n, m):
  ''' find which elements are missing from a list '''
  # check if both are empty
  if m == [] and n == []:
    return 0
   #sort first to allow index comparison
  m.sort()
  n.sort()
  if  len(m) > len(n):
    lst = [ x for x  in m for y in n if  x not in n]
    return lst[0] 
  else: 
     lst = [ x for x  in n for y in m if x not in m]
     return lst[0]
  

print find_missing([],[])
print '----------------------------------'

print find_missing([1,2,3],[1,3,5,2])
print '----------------------------------'

print find_missing([1,3,5,2], [1,2,3])