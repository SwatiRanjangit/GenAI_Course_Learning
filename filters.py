'''
filters is use to filter out items form list based on a condition.

'''
'''

def even(num):
    if num%2==0:
        return True
    
lst=[1,2,3,4,5,6,7,8,9,22,12]

even_nums=list(filter(even,lst))
#print(even_nums)

greater_than_five = list(filter(lambda x:x>5, lst))
#print(greater_than_five)

even_and_greater_than_five = list(filter(lambda x:x>5 and x%2==0, lst))

print(even_and_greater_than_five)

'''

#FILTER TO CHECK IF AGE IS GREATER THAN 25 IN DICTIONARY

people=[
    {'name':'swati','age':12},
    {'name':'arun','age':26},
    {'name':'tiya','age':30},
    {'name':'Sita','age':28},
    {'name':'kiya','age':11},
]

def get_age_greater_25(person):
    return person['age']>25

people_greater_than_25= list(filter(get_age_greater_25,people))
print(people_greater_than_25)