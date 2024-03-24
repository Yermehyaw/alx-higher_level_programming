#!/usr/bin/python3
def uniq_add(my_list=[]):
     if my_list is None:
         return None
     else:
         i = 0
         x = my_list[i]
         new_set = {item for item in my_list}
         new_list = list(map(lambda x: x, new_set))
         while i < len(new_list) - 1:
              x = x + new_list[i + 1]
              i += 1
         return x
