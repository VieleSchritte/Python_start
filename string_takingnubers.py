# The string like 'a5b4c2' becomes the string like 'aaaaabbbbcc'. I use functions below

# Firstly, we need to make the sample:
def sampling(sample):
    sample = sample[1:]
    return(sample)

sampling(test_line)

# Then there is a need to get the word we will repeat in the final string:
def lettering(sample):
    letter = sample[0]
    return(letter)

lettering(test_line)

# Then making the number in the star format:
def str_numbering(sample):
    i = 0
    Len_sample = len(sample)
    str_number = ''
    
    for i in range(Len_sample):
        if sample[i].isdigit() == True:
            str_number += sample[i]
        else:
            break
            
    return(str_number)

str_numbering(test_line)

#... And making it int
def numbering(str_number):
    i = 0
    delta = 1
    Len_number = len(str_number)
    number = 0
    
    for i in range(Len_number):
        number += int(str_number[i])*(10**(Len_number - delta))
        delta += 1
        i += 1
    
    return(number)

numbering(test_line)

# So finally they all work together
import os
os.chdir('C:\\Users\\verap\\Desktop\\Python_Stepik')

test = open('dataset_3363_2.txt')

for line in test:
    test_line = line
test.close()

Len_test = len(test_line)
i = 0
counter = 0

for i in range(Len_test):
    if test_line[i].isalpha() == True:
        counter += 1
    i += 1
    
j = 1
result = {}
string = ''

for j in range(1,counter+1):
    if j == 1:
        sample = sampling(test_line)
        letter = lettering(test_line)
        str_number = str_numbering(sample)
        number = numbering(str_number)
        result[letter] = number
        
        sample = sample[len(str_number):]
    else:
        letter = lettering(sample)
        sample = sampling(sample)
        str_number = str_numbering(sample)
        number = numbering(str_number)
        
        sample = sample[len(str_number):]
        
        if letter in result.keys():
            for key in result.keys():
                string += key*result[key]
            result = {}
            
        result[letter] = number
    j += 1
        
for key in result.keys():
    string += result[key]*key

print(string)

with open('test_output.txt', 'w') as output:
    output.write(string)
