'''
## list is mixed datatype collection of elements and it is mutable. 
names=["swati","sweety","arun"]
print(names)

names1=["swati",1234,"arun"]
print(names1)

print(names1[0])
print(names1[-1])

print(names[1:2])

#names[1]="riya"
#print(names[1])

##issue related to list:
#names[1:]="riya" # here it consider it as a character not a word so in the below it is replacing with all values.
#print(names)

##LIST METHODS:
names.append("tiya") #item add to end
print(names)

names.insert(1,"kiya")
print(names)

names.remove("kiya") # remove 1st occurence of the word
print(names)

poppedEle = names.pop() # remove and return index of last ele
print(poppedEle)

ind = names.index("swati")
print(ind)

print(names.count("swati"))

names.reverse()
print(names)

names.clear()
print(names)




'''

## SLICING LIST
'''
numbers = [1,2,3,4,5,6,7,8,9]

print(numbers[2:5]) ## 3 , 4 , 5
print(numbers[:5])  ## 1,2,3 , 4,5
print(numbers[5:])  ## 6,7,8,9
print(numbers[::2]) ## 1,3 ,5, 7.9    steps=2
print(numbers[::-1]) ## 9, 8, 7, 6, 5, 4, 3, 2, 1

for num in numbers:
    print(num)

for index,num in enumerate(numbers):
    print(index,num)
'''   
## LIST COMPREHENSION
'''
lst=[]
for x in range(1,10):
    lst.append(x**2)
    
print(lst)

## SYNTAX

BAsic syntax: [expression for item in iterable]
With conditional logic: [expression for item in iterable if condition]
Nested list compreshension: [expression for item1 in iterable1 for item2 in iterable2]

lst1 = [x**2 for x in range(1,11)] ##list comprehension
print(lst1)

##Basic list compheresion

square = [num**2 for num in range(1,11)]
print(square)
'''
## With conditional logic

even_num = [num for num in range(1,11) if num % 2==0]
print(even_num)

##Nested list compreshension

ls = [1,2,3,4,5]
lss=['a','b','c','d','e']

pair = [[i,j] for i in ls for j in lss]
#print(pair)

words=["swatt","is","a","good girl"]
length = [len(word) for word in words]
print(length)