"""
Compute the nearest larger number by interchanging digits updated. 
Given 2 numbers a and b find the smallest number greater than b by interchanging the digits of a and if not 
possible print -1

Constraints
1<= a,b <= 1,00,00,000

Input Format:
Two numbers a and b, separated by space
if not possible, print -1

Input 
459 500
Output
549

Test Cases:
1. 654757 457765
Output 465577

2. 5964 9984
Output -1
"""

import collections

def digit_exchange(a, b):
    """
    Function to exchange digits of first element and 
    create a combination, compare it with second element and display the smallest largest number
    """

    if ((a<1 or a>10000000) or (b<1 or b>10000000)):
        return -1

    list_a = []
    string_a=str(a)  
   
    # for i in string_a: 
    #     digit=int(i)
    #     list_a.append(digit)
     
    # Alternative for above code snippet
    list_a = list(string_a)

    count_dict = collections.Counter(str(a))
   
    list_a_copy=list_a

    output_list = find_combinations(list_a_copy, list_a, count_dict)
    temp_set = set(output_list)
    output_list=list(temp_set)
    
    while len(str(output_list[0])) < len(str(a)):
        output_list = find_combinations(output_list, list_a,count_dict)
    
    output_set = set(output_list)
    output_list = list(output_set)

    result=[]
    for num in output_list:
        if num>b:
            result.append(num)
    result.sort()
    output=result[0]
    print(output)
   
def find_combinations(num_list, fixed_list, count_dict):
    num_list_new=[]
    
    for num in num_list:         
        for i in fixed_list:     
            count=0 
            for j in str(num):
                if str(i)==j:
                    count+=1    
            
            if count < count_dict[str(i)]:
                temp_str=str(num)+str(i)
                num_list_new.append(int(temp_str))
            
    return num_list_new

digit_exchange(459, 500)

