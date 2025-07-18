# exception try catch block
'''
try:
    a = b
except:
    print("variable is not assigned")

try:
    a = b
except NameError as nm:
    print(nm)


# zero division error

try:
    result/=0
except:
    print('cant divide by 0')



try:
    result=1/0
except ZeroDivisionError as z:
    print(z)


# if more than one exceptions may occur so we have to use the parent class exception class rather than single one.

try:
    result=1/2
    a=b
except Exception as e:
    print(e)


# we can put any number of exception but the parent exception should be in the very last

try:
    result=1/2
    a=b
except ZeroDivisionError as z:
    print(z)
except Exception as e:
    print(e)



# if none of exception happen else block will execute and if there exception then it won't execute.
try:
    num= int(input('Enter a number: '))
    result = 10/num
except ValueError as v:
    print("This is not a valid number")
except ZeroDivisionError:
    print("enter denominator greater than 0")
else:
    print(f"ressult is: {result}")


try:
    num= int(input('Enter a number: '))
    result = 10/num
except ValueError as v:
    print("This is not a valid number")
except ZeroDivisionError:
    print("enter denominator greater than 0")
else:
    print(f"ressult is: {result}")
finally:
    print("This is finally block...execute always")

# FILE HANDLING and exception handling

try:
    file=open('example.txt','r')
    content=file.read()
    #a=b
except FileNotFoundError:
    print("file does not exist")
except Exception as ex:
    print(ex)
finally:
    if 'file' in locals() or not file.closed():
        file.close()
        print('file closed')
        
'''



    