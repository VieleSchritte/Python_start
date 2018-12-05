# We get file with the link and display it. Then we should get the document from this link and count number of lines in it.

import requests
import os
os.chdir('C:\\Users\\verap\\Desktop\\Python_Stepik')

with open('dataset_3378_2.txt') as example:
    link = example.readline()

print('link is', link)
contain = requests.get('https://stepic.org/media/attachments/course67/3.6.2/324.txt')
contain_text = contain.text
#print(contain_text)

line = contain_text.splitlines()
#print(line)
count = len(line)
print(count)