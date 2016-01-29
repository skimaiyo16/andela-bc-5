# phone book example

# use a  list
class PhoneBookList(object):
	def __init__(self):
		self.book = []

	def add_contact(self, username, phone_number):
		record = [username, phone_number]
		self.book.append(record)

	def search(self, username):
		''' returns a `dict` wih a phone number and
		 the number of loop count eg
		 {'count:20}
		'''
		count = 0
		for  u,p in self.book:
			count += 1
			if u == username:
				result = {'count': count,'phone_number': p}
				return result

		result = {'count': count,'phone_number': None}
		return result


class PhoneBookDict(object):
	def __init__(self):
		self.book = {}

	def add_contact(self, username, phone_number):
		self.book[username] = phone_number

	def search(self, username):
		result = {
		  'count': 1,
		   'phone_number': self.book.get(username,None)
		}
		return result
		



