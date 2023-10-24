# list1 =  [(1,2), (2,1), (1,2), (1,1)]

# def domninocycle(tiles):
#     if len(tiles)==0:
#         return True

#     flag = 0
#     for i in range(len(tiles) - 1):
#         if tiles[i][-1] != tiles[i + 1][0]:
#             flag = 1

#     if flag == 0:
#         if tiles[0][0] == tiles[-1][1]:
#             return True
#         else:
#             return False
#     else:
#         return False
    
# print(domninocycle(list1))



# Program to depict Raising Exception 
  
try:  
    print("Hello")
    raise NameError("Name Erroorroror")  # Raise Error 
except NameError: 
    print ("An exception") 
    raise  # To determine whether the exception was raised or not 