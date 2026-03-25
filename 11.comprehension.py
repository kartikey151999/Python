'''datatype comprehension'''

list = [1,2,3,4,5,6,7,8,9,10]
print([num for num in list if num%2 == 0]) # [2, 4, 6, 8, 10]

print([n * n for n in list ])  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

number = [1,2,3]
alphabets = ['a','b','c']



num_alpha = zip(number,alphabets)
list_numalpha = []
for i,j in num_alpha:    
    list_numalpha.append((i,j))

print(list_numalpha)      #[(1, 'a'), (2, 'b'), (3, 'c')]


#---------------list comprehension for this [(1, 'a'), (2, 'b'), (3, 'c')]

print([(num,alpha) for num,alpha in list_numalpha])   #[(1, 'a'), (2, 'b'), (3, 'c')]

#----------dictionary comprehension

print({num:alpha for num , alpha in list_numalpha})  #{1: 'a', 2: 'b', 3: 'c'}




set1 = [0.1,0.1,'a','a','b',1]

# set of above list

myset = set(set1)
print({value for value in set(set1)})   # {0.1, 1, 'a', 'b'}