# Helps figure out what words are the most repeatable :)

import os
os.chdir('C:\\Users\\verap\\Desktop\\Python_Stepik')

with open('my_test.txt', 'a') as my_test:
    my_test.write('\n')

with open('my_test.txt', 'r') as my_test:
    Len_line = 0
    word = ''
    result = {}
    
    for line in my_test:
        
        line = line.strip('') # Удаление пробельных символов в начале и в конце строки
        i = 0
        Len_line = len(line)
        word = ''
        
        for i in range(Len_line):
            
            if (line[i].isspace() == False):
                word += line[i]
            else:
                word = word.lower()
                
                if word in result.keys():
                    result[word] += 1
                else:
                    result[word] = 1
                
                word = ''
            i += 1
            
if result.get(''): result.pop('')
    
most_recent = {}
values = []

for value in result.values():
    values.append(value)
    
max_value = max(values)

for key, value in result.items():
    if value == max_value:
        print(key, value) 