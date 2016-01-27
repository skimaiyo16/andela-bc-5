def reverse(s) :
 """
 reverse a string
 """
 s = list(s)
 for i in range(len(s) // 2) :
 	temp = s[i]
 	s[i] = s[len(s)-i-1]
 	s[len(s)-i-1] = temp
 print "".join(s)

reverse("Hello")

