'''
dictionaries are unordered collection of item store data with key value pair . key must be unique and immutable but value can be changed

'''
'''
empty_dict = {}
print(empty_dict)
print(type(empty_dict))
students = {"name":"krish", "age":"22","subject":"Maths"}
print(students)

'''

'''
students = {"name":"krish", "age":"22","subject":"Maths","name":"suraj"} # duplicate key will overide value so key must unique
print(students)


##Accessing dictionary elements
students = {"name":"krish", "age":"22","subject":"Maths"}
print(students['name'])

print(students.get('age'))
print(students.get('last_name',"LNU")) # if key is not present in dictionary it give none so we can give default value as well

##Modify dictionary elements
students = {"name":"krish", "age":"22","subject":"Maths"}
students['name']="swati" #updated value
print(students)
students["address"]="delhi" # added new key and value
print(students)

del students['address'] #remove new key and value
print(students)


students = {"name":"krish", "age":"22","subject":"Maths"}

keys=students.keys()
print(keys)
values = students.values()
print(values)

items = students.items()
print(items)

student_copy = students  #Deep copy allocatie two varibles but point to same memo location
print(student_copy)

students['name']="riya"
print(students)
print(student_copy)

student_copy1 = students.copy() #Shallow copy provide diff memo location 
print(student_copy1)

students["name"]='teesa'
print(students)
print(student_copy)
print(student_copy1)


#Iteration
students = {"name":"krish", "age":"22","subject":"Maths"}

for keys in students.keys():
    print(keys)
    
for values in students.values():
    print(values)

for key,value in students.items():
    print(f"{key}:{value}")
    


#Nested dictionary

students={
    "student1":{'name':"swati","age":"23","subject":"maths"},
    "student2":{'name':"arun","age":"24","subject":"commerce"},
     "student3":{'name':"bubu","age":"25","subject":"Arts"}
}

#print(students)
print(students["student1"]["name"])
print(students["student1"]["subject"])

#Iteration

for student_id, student_info in students.items():
    print(f"{student_id}:{student_info}")
    for key,value in student_info.items():
        print(f"{key}:{value}")


#Dictionary comphresion
#Normal
Dict={}
for i in range(1,6):
    square = i * i
    Dict[i]=square
#print(Dict)

#Comphrension
squares = {x:x**2 for x in range(1,11)}
#print(squares)

#Conditional comphre

evens = {x:x**2 for x in range(1,6) if x % 2==0}
print(evens)
'''

##QUESTIONS
# Use a dict to print fre of ele in list
lis = [1,1,2,3,2,4,3,4,3]
dic = {}
for i in lis:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
    
#print(dic)

##Merge two dictionary

dict1 = {"a":1,"b":2}
dict2= {"b":3,"c":5}

merge_dic = {**dict1,**dict2}
print(merge_dic)


            
        

