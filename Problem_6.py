# Max and Min in a Unsorted Array
def get_min_max(ints):
   min_int = ints[0]
   max_int = ints[0]
   for i in ints:
      if i <min_int:
         min_int = i
      elif i >max_int:
         max_int = i
   return (min_int, max_int)

import random

l = [i for i in range(0, 10)]  
random.shuffle(l)

print(get_min_max(l))
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print('-----------------------------')

print(get_min_max([1]))
print ("Pass" if ((1, 1) == get_min_max([1])) else "Fail")
print('-----------------------------')

print(get_min_max([1,1,1,1,5]))
print ("Pass" if ((1, 5) == get_min_max([1,1,1,1,5])) else "Fail")
print('-----------------------------')

print(get_min_max([0, 45, 5, 8, 9, 123, -10]))
print ("Pass" if ((-10, 123) == get_min_max([0, 45, 5, 8, 9, 123, -10])) else "Fail")