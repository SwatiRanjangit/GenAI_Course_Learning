#Read whole file
'''
with open('example.txt','r') as file:
    content=file.read()
    print(content)

    
#Read  file line by line

with open('example.txt','r') as file:
    for line in file:
        print(line.strip())  ##.strip() removes the newline character

# write in a file
#this overwrite all content in exaple.txt

with open('example.txt','w') as file:
    file.write('Hello world!\n')
    file.write('This is a new line.\n')
    



# This will not overwrite but it will append the text in the file
with open('example.txt','a') as file:
    file.write('Hello my name is swati.\n')
    file.write('and i am fine.\n')


#Writting list of lines to a file

lines = ['first line \n','second line \n','Third line \n']

with open('example.txt','a') as file:
    file.writelines(lines) 


#Binary files

#writting to a binary files

data = b'\x00\x01\x02\x03'

with open('example.bin','wb') as file:
    file.write(data)
    
with open('example.bin','rb') as file:
    content=file.read()
    print(content)


# read content from source and write to destination

#copying a textfile

with open('sample.txt','r') as file:
    content=file.read()

with open('destination.txt','w') as file:
    file.write(content)


#Read a textfile and count no of lines words and characters

def count_num_word_char(file_path):
    with open('sample.txt','r') as file:
        lines=file.readlines()
        line_count = len(lines)
        word_count= sum((len(line.split())) for line in lines)
        char_count= sum(len(line) for line in lines)
    return line_count,word_count,char_count

file_path = 'sample.txt'

lines,words,char=count_num_word_char(file_path)
print(f'Lines:{lines}, words:{words}, char:{char}')    
    


# write and then read a file

with open('example.txt','w+') as file:
    file.write("hello\n")
    file.write("tiya\n")
    
    
    #move pointer to start
    file.seek(0)
    
    #read
    content = file.read()
    print(content)
    
'''

