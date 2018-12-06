# Task fro the Stepik educational platform. The script takes a text file from the following link that containes the filename.
# This filename should be taken to the download_link and so we get another text file. The goal is to get the content of the last file.

import requests
 
download_link = 'https://stepic.org/media/attachments/course67/3.6.3/'
filename = '699991.txt'
 
while filename:
 print(filename)
 r = requests.get(download_link+filename)
 filename = None if r.text.startswith('We') else r.text
 
print(r.text)