
def even_odd(num):
    if num % 2==0:
        print("Number is even")
    else:
        print("Number is odd")

#even_odd(5)

def add(a,b):
    return a + b

#print(add(2,2))

def greet(name):
    print(f"Hello {name}")

#greet('swati')

def greet(name='Guest'):
    print(f"Hello {name} Welcome to Rajsthan")

#greet()

##Variable length arguments
#Postional and keyword arguments

#Postional arguments
def print_numbers(*args):
    for nums in args:
        print(nums,end=" ")
        
#print_numbers(1,2,3,4,'a','swati')

#keyword arguments
'''
def print_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        
print_details(name="krish",age='32',address="delhi")

'''
def print_details(*args,**kwargs):
    for val in args:
        print(f"Postional arugments: {val}")
        
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        
#print_details(1,2,3,name="krish",age='32',address="delhi") #postional then keyword should be given otherwise give errors

#Return multiple paramters from functions
def multiply(a,b):
    return a*b,a


#print(multiply(2,3))

# PROGRAM TO CHECK STRONG PASSWORD

'''
def is_strong_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '@#$&*^_+' for char in password):
        return False
    return True

print(is_strong_password('swati'))

print(is_strong_password('sw#$atiowy'))

print(is_strong_password('SWATI'))


print(is_strong_password('Swati&$#89jka'))

'''

'''



#Calculate total cost of items in shopping cart

def calculate_total_cost(cart):
    total_cost=0
    for item in cart:
        total_cost+=item['price']*item['quantity']
    return total_cost
    


cart=[
    {'name':'Apple','price':10,'quantity':3},
    {'name':'Banana','price':20,'quantity':2},
    {'name':'Pinapple','price':5,'quantity':3}
]

#print(calculate_total_cost(cart))
'''

'''


#Check if string is pallindrom

def check_pallindrom(sentence):
    sentence=sentence.lower().replace(" ","")
    if sentence==sentence[::-1]:
        return True
    return False

print(check_pallindrom('A man a plan a canal panama'))
print(check_pallindrom('moon is not shown yet'))



#Factorial of number using recursion

def factorial_num(num):
    if num==0:
        return 1
    return num * factorial_num(num-1)

print(factorial_num(5))
'''
# function to read a file and count the frequency of each word

'''


def count_word_freq(file_path):
    word_count={}
    with open(file_path,'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word=word.lower().strip('.,!?;:"\'')
                word_count[word]=word_count.get(word,0)+1
    return word_count

file_path='sample.txt'
word_freq = count_word_freq(file_path)
print(word_freq)
                
'''

# validate email address
import re
def is_valid_email(email):
    pattern=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern,email) is not None

print(is_valid_email('swatirp87@gmail.com'))
print(is_valid_email('invalid-email'))

    

        