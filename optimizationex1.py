
from data_stuctures import  PhoneBookList, PhoneBookDict

# use a dictonary 
b = PhoneBookList()
b.add_contact('sam', '9889')
b.add_contact('austin','3434')
b.add_contact('esther', '67767')
b.add_contact('claire', '1323')
b.add_contact('maggie', '3121')
b.add_contact('james', '43545')

print b.search('james')
print b.search('jane')
print b.search('esther')
print '--------------------------------------------'

s = PhoneBookDict()
s.add_contact('sam', '9889')
s.add_contact('austin','3434')
s.add_contact('esther', '67767')
s.add_contact('claire', '1323')
s.add_contact('maggie', '3121')
s.add_contact('james', '43545')

print s.search('james')
print s.search('jane')
print s.search('esther')


