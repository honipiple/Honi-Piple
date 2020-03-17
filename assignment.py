#Q 1.Write python program to count the number of character (character) in a string 
test_str = "whatisthis"
  
 
all_freq = {} 
  
for i in test_str: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1
   
print ("Count of all characters in whatisthis is :\n "
                                        +  str(all_freq)) 
output
Count of all characters in whatisthis is :
 {'w': 1, 'h': 2, 'a': 1, 't': 2, 'i': 2, 's': 2}
#Q 3. weite a fnction that takes list of words and  return the length of longest one
from itertools import count 
  
def longest_word(lst, K): 
    cnt = count() 
    return sorted(lst, key = lambda w : (len(w), next(cnt)),  
                                        reverse = True)[:K] 
  

lst = ['am', 'watermelon', 'girl', 'boy', 'colour'] 
K = 3
print(longest_word(lst, K)) 
output
['watermelon', 'colour', 'girl']
#Q 4. write a program to count the occurrence of each word in a given sentance
sentence = "Beauty lies in the eyes of beholder";  
wordCount = 0;  
   
for i in range(0, len(sentence)-1):
    if(sentence[i] == ' ' and sentence[i+1].isalpha() and (i > 0)):  
        wordCount = wordCount + 1;  
          
  

wordCount = wordCount + 1;  
   
 
print("Total number of words in the given string: " + str(wordCount));  
output
Total number of words in the given string: 7
#Q 5. write a python program function to convert a given string to all uppercase if it contain at leasdt 2 uppercase character in the first 4 character
def to_uppercase(str1):
    num_upper = 0
    for letter in str1[:4]: 
        if letter.upper() == letter:
            num_upper += 1
    if num_upper >= 2:
        return str1.upper()
    return str1

print(to_uppercase('Python'))
print(to_uppercase('PyThon'))
output
Python
PYTHON
# Q 6.write a python program to count and diplay the vowels of a given text
def check_vow(string,vowels):
    final = [each for each in string if each in vowels]
    print(len(final))
    print(final)
    string = "i am alexa"
    vowels = "AaEeIiOoUu"
    check_vow(string,vowels);
    output
    #######python data type list Quetion#########
    #Q 1. write a python program to remove duplicate from a list
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
      
 
duplicate = [2, 4, 10, 20, 5, 2, 20, 4] 
print(Remove(duplicate)) 
output
[2, 4, 10, 20, 5]
#Q 2.write a python program to check a list is empty or not
def Enquiry(lis1): 
    if len(lis1) == 0: 
        return 0
    else: 
        return 1
          

lis1 = [] 
if Enquiry(lis1): 
    print ("The list is not empty") 
else: 
    print("Empty List") 
    output
    Empty List
#Q 3. write a python function that takes two and return true if they have at least one common member
def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))
        output
        True
        none
#Q 4. write a python program to get the diffrence betwwen the two list
def Diff(li1, li2): 
    return (list(set(li1) - set(li2))) 
  

li1 = [10, 15, 20, 25, 30, 35, 40] 
li2 = [25, 40, 35] 
print(Diff(li1, li2)) 
output
[10, 20, 30, 15]
#Q 5. write a python program to fined the second smallest number in a list
                        or
    #Q 6. write a python program to fined second laegest number in a list
def find_len(list1):
    length = len(list1)
    list1.sort()
    print("Largest element is:", list1[length-1])
    print("Smallest element is:", list1[0])
    print("Second Largest element is:", list1[length-2])
    print("Second Smallest element is:", list1[1])
    list1=[12, 45, 2, 41, 31, 10, 8, 6, 4]
    Largest = find_len(list1) 
    output
    #Q 7. write a python program  to get the frequency of the elemnt in a list
test_list = [9, 4, 5, 4, 4, 5, 9, 5, 4] 
print ("Original list : " + str(test_list))  
max = 0
res = test_list[0] 
for i in test_list: 
    freq = test_list.count(i) 
    if freq > max: 
        max = freq 
        res = i 
print ("Most frequent number is : " + str(res)) 
output
Original list : [9, 4, 5, 4, 4, 5, 9, 5, 4]
Most frequent number is : 4
#Q 8. write a python program to cenvert a list if multiple integerrs into a single integer
lst = [12, 15, 17] 
  
# iterating each element 
for i in lst: 
    print(i, end="") 
    output
    121517
    #Q 9. write a python program to compute the similarity between two list
list1 = [1, 2, 3, 4]
list2 = [1, 2]
print(list(set(list1) - set(list2)))
output
[3, 4]
#Q 10. write a python program to check if all dictionaries in a list are empty or not
test_dict = {} 
  print("The original dictionary : " + str(test_dict)) 
    res = not bool(test_dict) 
  print("Is dictionary empty ? : " + str(res))
output
The original dictionary : {}
Is dictionary empty ? : True
#####python data type dictionary#####
#Q 1. write a python program to generate and print a dictionary that contains a nuber (between 1 and n) in the from(x,x*x)
number = int(input("Please enter the Maximum Number : "))
myDict = {}

for x in range(1, number + 1):
    myDict[x] = x * x
    
print("\nDictionary = ", myDict)
output
Please enter the Maximum Number : 25

Dictionary =  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400, 21: 441, 22: 484, 23: 529, 24: 576, 25: 625}
#Q 2. write python program  to combine two dictionary adding values common keys
from collections import Counter 
  

dict1 = {'a': 12, 'for': 25, 'c': 9} 
dict2 = {'what': 100, 'this': 200, 'is': 300} 
  
  

          
Cdict = Counter(dict1) + Counter(dict2) 
print(Cdict) 
output
Counter({'is': 300, 'this': 200, 'what': 100, 'for': 25, 'a': 12, 'c': 9})
#Q 3.write a python program to print all uniq value in dictionary
def unique(list1):  
    unique_list = [] 
    for x in list1: 
        if x not in unique_list: 
            unique_list.append(x) 
    for x in unique_list: 
        print(x) 
list1 = [10, 20, 10, 30, 40, 40] 
print("the unique values from 1st list is") 
unique(list1) 
  
  
list2 =[1, 2, 1, 1, 3, 4, 3, 3, 5] 
print("\nthe unique values from 2nd list is") 
unique(list2) 
output
the unique values from 1st list is
10
20
30
40

the unique values from 2nd list is
1
2
3
4
5


#Q 5.write a python prigram to creat a dictionary from string
import json 
  

test_string = '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}' 
  

print("The original string : " + str(test_string)) 
  
 
 
res = json.loads(test_string) 
  

print("The converted dictionary : " + str(res)) 
output
The original string : {"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}
The converted dictionary : {'Nikhil': 1, 'Akshat': 2, 'Akash': 3}
# 6.write a python program to count the values assocuated with key in a dictionary
dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
ctr = sum(map(len, dict.values()))
print(ctr)
output
5
