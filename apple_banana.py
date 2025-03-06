# get some str
words = input("please enter some string ....")
# split by space
listed_words = words.split()
# make word list___foundation of include "a" word list
filtered_words = []
# check & set ordered list
for a in listed_words:
    a = a.lower()
    if "a" in a:
        #filtered_words += a # having problem
        filtered_words.append(a)
# out put
if filtered_words:
   for  i in filtered_words:
       print(i)
else:
    print("There are no 'a include' your words ...")