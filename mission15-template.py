# CS1010A --- Programming Methodology
# Mission 15 Template

import csv
import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

###############
# Pre-defined #
###############

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename, 'r', newline='') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows

##########
# Task 1 #
##########

def clean(data):
    f_data = [row for row in data if all(cell != "" for cell in row)]
    new_data = []
    for row in f_data:
        filtered = (row[0], int(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), row[7], row[8] == "yes")
        new_data.append(filtered)
    final = {}
    for row in new_data:
        student_num = row[0]
        if student_num not in final or row[6] > final[student_num][6]:
            final[student_num] = row
    final_data = [final[student_num] for student_num in final]
    return tuple(final_data)



# Do not modify, required for later tasks
raw_data = read_csv("cs1010a.csv")
headers = raw_data[0]
data = clean(raw_data[1:])

# Task 1 Testcase
#print(headers)
#print(data[:3])

##########
# Task 2 #
##########

def value_counts(data, headers, col_name):
    f_data = filter(headers[i] == col_name for i in range(headers), data)
    d = {}
    for rows in f_data

afast_counts = value_counts(data, headers, "is_afast")
faculty_counts = value_counts(data, headers, "faculty")

# Task 2 Testcases
#sns.barplot(x=map(str, afast_counts[0]), y=afast_counts[1])
#plt.title("AFAST Count")
#plt.show() # uncomment to show
#plt.close()

#sns.barplot(x=faculty_counts[0], y=faculty_counts[1])
#plt.title("Number of students from each faculty")
#plt.xticks(rotation=90)
#plt.show() # uncomment to show
#plt.close()

##########
# Task 3 #
##########

def long2wide(data, headers):
    """Your code here"""

# Do not modify, required for later tasks
#wide_data = long2wide(data, headers)

# Task 3 Testcases
#print(long2wide([["apple", "red"],["banana", "yellow"],["banana", "green"],["apple", "green"],["cherry", "red"]], ["fruit", "colour"]))
# {'fruit': ['apple', 'banana', 'banana', 'apple', 'cherry'], 'colour': ['red', 'yellow', 'green', 'green', 'red']}

#sns.histplot(data=wide_data , x="midterm")
#plt.title("Midterm Distribution (default)")
#plt.show() # uncomment to show
#plt.close()

##########
# Task 4 #
##########

# 4A
def bin_sqrt(values):
    """Your code here"""

# 4B
def bin_rice(values):
    """Your code here"""

# 4C
def bin_sturge(values):
    """Your code here"""

# 4D
def bin_scott(values):
    """Your code here"""

# 4E
def bin_fd(values):
    """Your code here"""

# Task 4 Testcases
#print(bin_sqrt(wide_data['midterm']))   # 46
#print(bin_rice(wide_data['midterm']))   # 26
#print(bin_sturge(wide_data['midterm'])) # 12
#print(bin_scott(wide_data['midterm']))  # 19
#print(bin_fd(wide_data['midterm']))     # 98

fig, axes = plt.subplots(2, 3, sharex=True, figsize=(15, 5))
fig.suptitle('Midterm Distribution (various bin strategies)')
sns.histplot(ax=axes[0,0], data=wide_data, x="midterm")
axes[0,0].set_title('default')
sns.histplot(ax=axes[0,1], data=wide_data, x="midterm", bins=bin_sqrt(wide_data["midterm"]))
axes[0,1].set_title('square-root')
sns.histplot(ax=axes[0,2], data=wide_data, x="midterm", bins=bin_rice(wide_data["midterm"]))
axes[0,2].set_title('rice')
sns.histplot(ax=axes[1,0], data=wide_data, x="midterm", bins=bin_sturge(wide_data["midterm"]))
axes[1,0].set_title('sturge')
sns.histplot(ax=axes[1,1], data=wide_data, x="midterm", bins=bin_scott(wide_data["midterm"]))
axes[1,1].set_title('scott')
sns.histplot(ax=axes[1,2], data=wide_data, x="midterm", bins=bin_fd(wide_data["midterm"]))
axes[1,2].set_title('freedman-diaconis')
#plt.show() # uncomment to show
plt.close()

##########
# Task 5 #
##########
"""
5A: Is it meaningful to have a bin-count of 1?
Your answer here.

5B: Is it meaningful to have a bin-count roughly equal
    to length of values N?
Your answer here.
"""

##########
# Task 6 #
##########

def order_by_median(wide_data, cat, num):
    """Your code here"""

"""
6B: Does the data suggest an incoming MED student
    is more likely to perform better than an incoming
    student from another faculty? Explain.
Your answer here.
"""

cat_col = "faculty"
num_col = "total"
cat_order = order_by_median(wide_data, cat_col, num_col)

# Task 6 Testcases
print(cat_order) # ['MED', 'NUSHS', 'LAW', 'SOC', 'FOE', 'FOS', 'BIZ', 'FASS', 'SDE']

sns.boxplot(x=cat_col, y=num_col, data=wide_data, order=cat_order)
plt.title("Distribution of total by faculty")
#plt.show() # uncomment to show
plt.close()

##########
# Task 7 #
##########

# Provided code to produce scatter plot of level and total

#sns.scatterplot(x='level', y='total', data=wide_data, hue='faculty', style='faculty', s=15)
#plt.title("Students' total against Students' level")
#plt.show() # uncomment to show
#plt.close()


# 7A: Your code to complete, to replace the ...
sns.scatterplot(x=..., y=..., data=..., hue='faculty', style='faculty', s=15)
plt.title("Students' final against Students' midterm")
#plt.show() # uncomment to show
plt.close()

"""
7B: State the trend in the scatter plot produced in 7A
Your answer here.

7C: Is your friend's claim justified? Explain.
Your answer here.
"""
