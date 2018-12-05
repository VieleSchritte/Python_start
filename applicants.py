# We have a file with applicants' last names and their math, phys and Russian exams scores. The average score for each applicant and the
# average subject score are displayed.

import os
os.chdir('C:\\Users\\verap\\Desktop\\Python_Stepik')

def marks_num(mark):
    Len_mark = len(mark)
    i = 0
    delta = 1
    mark_digit = 0
    
    for i in range(Len_mark):
        mark_digit += int(mark[i])*(10**(Len_mark - delta))
        i += 1
        delta += 1
    return(mark_digit)
    
def meaning(math, phys, rus):
    mean = (math + phys + rus)/3
    return(mean)

def mean_subj(list_subj):
    Len_subj = len(list_subj)
    i = 0
    counter = 0
    sum_subj = 0
    
    for i in range(Len_subj):
        sum_subj += list_subj[i]
        counter += 1
    
    mean = sum_subj / counter
    return(mean)
    

means = []
math_marks = []
phys_marks = []
rus_marks = []

with open('dataset_3363_4.txt') as abitura:
    for line in abitura:
        list_line = line.split(';')
        
        math_str = list_line[1]
        phys_str = list_line[2]
        should_cut = list_line[3]
        
        Len_cut = len(should_cut)
        i = 0
        rus_str = ''
        
        for i in range(Len_cut):
            if should_cut[i].isdigit() == True:
                rus_str += should_cut[i]
            else:
                break
        
        math = marks_num(math_str)
        phys = marks_num(phys_str)
        rus = marks_num(rus_str)
        
        mean = meaning(math, phys, rus)
        means.append(mean)
        
        math_marks.append(math)
        phys_marks.append(phys)
        rus_marks.append(rus)

math_mean = mean_subj(math_marks)
phys_mean = mean_subj(phys_marks)
rus_mean = mean_subj(rus_marks)

j = 0
for j in range(len(means)):
    print(means[j])
    j += 1

means_mpr = [math_mean, phys_mean, rus_mean]
Len_mpr = len(means_mpr)
i = 0

for i in range(Len_mpr):
    print(means_mpr[i], end = ' ')