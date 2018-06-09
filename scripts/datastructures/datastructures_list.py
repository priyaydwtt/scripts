#array |list

#element list of same data types
element_list = ["apple","orange","grapes"]
#element list of different data types
element_list_multiple_dt=["apple","orange","grapes",0,2.5]

#index starts from 0

print(element_list)
print(element_list_multiple_dt)

# numeric list

age_list=[21,22,23,24,25]

#for loop in one line
#list comprehension

age_list_10 = [i+10 for i in age_list]
print(age_list_10)
print(dir(age_list_10))

#list functions 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
print(help(age_list_10.append))




