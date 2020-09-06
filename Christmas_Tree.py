'''
Chirag is a pure Desi boy. And his one and only dream is to meet Santa Claus. He decided to decorate a Christmas tree for Santa on coming Christmas. Chirag made an interesting Christmas tree that grows day by day.

The Christmas tree is comprised of the following
Parts
Stand
Each Part is further comprised of Branches. Branches are comprised of Leaves.

How the tree appears as a function of days should be understood. Basis that print the tree as it appears on the given day. Below are the rules that govern how the tree appears on a given day. Write a program to generate such a Christmas tree whose input is number of days.

Rules
If tree is one day old you cannot grow. Print a message "You cannot generate christmas tree"
Tree will die after 20 days; it should give a message "Tree is no more"
Tree will have one part less than the number of days.
E.g.
On 2nd day tree will have 1 part and one stand.
On 3rd day tree will have 2 parts and one stand
On 4th day tree will have 3 parts and one stand and so on.
Top-most part will be the widest and bottom-most part will be the narrowest.
Difference in number of branches between top-most and second from top will be 2
Difference in number of branches between second from top and bottom-most part will be 1
Below is an illustration of how the tree looks like on 4th day

Input Format:

First line of input contains number of days denoted by N
Output Format:

Print Christmas Tree for given N

OR

Print "You cannot generate christmas tree" if N <= 1

OR

Print "Tree is no more" if N > 20
Constraints:
0<= N <=20
'''



import copy

def print_christmas_tree(n):

    if n<=1:
        print("You cannot generate christmas tree")
        return None
    elif n>20:
        print("Tree is no more")
        return None
    else:
        parts = n-1
        branches = n+1
        temp=1
        list_of_parts=[]
        part1=[]
        part1.append(temp)
        
        count=1
        while count<branches:
            part1.append(temp+2)
            temp+=2
            count+=1

        list_of_parts.append(part1)

        part2 = copy.copy(part1)
        part2.pop(0)
        part2.pop(len(part2)-1)

        list_of_parts.append(part2)
        temp_list=part2

        for i in range(0,parts-2):
            new_list = copy.copy(temp_list)
            
            new_list.pop(len(new_list)-1)
            temp_list=copy.copy(new_list)
            list_of_parts.append(new_list)
        print(list_of_parts)

        max=list_of_parts[0][-1]
        for part in list_of_parts:
            for branch in part:
                indent = " "*(((max-branch)//2)*2)
                star = "* "*branch
                print(indent + star)

        print(" "*((max//2)*2)+"*")
        print(" "*((max//2)*2)+"*")
        

print_christmas_tree(20)
  

