def fact(num):
   if num == 0
      return 1
   else:
      fact = 1
      for i in range(1,num+1):
         fact = fact * i
      return fact