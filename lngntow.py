def num_to_words(n):
  """
  change a number into words  using a dictonary to map
  """
  nw = {"0":"Zero", "1":"one", "2":"Two", "3":"Three", "4":"Four", "5":"Five", "6":"six", "7":"Seven", "8":"Eight", "9":"Nine"}
  words = []
  n = str(n)
  for i in n :
  	words.append(nw[i])
  return " ".join(words)

print num_to_words(1239)




