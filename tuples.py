'''
Tuples are ordered immutable collection of element


empty_tuple = ('swati','riya','priya',1234)
print(empty_tuple)
print(type(empty_tuple))
print(empty_tuple[1])

#empty_tuple[1]='teesa'
numbers=(1,2,3,4,5,6,7,8,9)
empty_tuple = ('swati','riya','priya',1234)
print(numbers[2:5])
print(numbers[:5])  
print(numbers[5:])  
print(numbers[::2]) 
print(numbers[::-1])

conCat = empty_tuple + numbers
print(conCat)
'''
'''
for ele in empty_tuple:
    print(ele)

numbers=(1,2,3,4,5,6,7,8,9)
print(numbers.count(2))
print(numbers.index(4)) # return 1st index of value passed

# Paking and unpacking tuple

#packing
packed_tuple = 1,"Hello",2.12
print(packed_tuple)

#unpacking
a,b,c=packed_tuple
print(a)
print(b)
print(c)


numbers = (1,2,3,4,5,6,7,8)
first,*middle,last = numbers
print(first)
print(middle)
print(last)


#Nested tuple

#Nested list
lst = [[1,2,3,4],[6,7,8,9],3.12,"swati"]
print(lst[0])
print(lst[0][2])

#Inside list tuples
lst = [[1,2,3,4],[6,7,8,9],(3.12,"swati")]
print(lst[2][0:2])
'''

nested_tup = ((1,2,3,4),(6,7,8,9),(3.12,"swati"))
#print(tup[0][2])

for sub_tup in nested_tup:
    for item in sub_tup:
        print(item,end=" ")
    print()



