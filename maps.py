'''
maps() functions applies a given function to all of the items in an input list given and returns a map object(an iterator)

'''
'''


number1=[1,2,3]
number2=[3,4,5]

added_num = list(map(lambda a,b: a+b, number1,number2))

print(added_num)

#convert string list to int

str_num=['1','2','3']

str_int = list(map(int,str_num))
print(str_int)

words=['apple','banana']

upper=list(map(str.upper,words))
print(upper)
'''

people=[
    {'name':'swati','age':12},
    {'name':'arun','age':22}
]

def get_name(person):
    return person['name']

list_names=list(map(get_name,people))
print(list_names)
