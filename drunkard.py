'''
In state of inebriation, a drunkard sets out to walk home, afoot. As is common knowledge, a drunkard struggles to find balance and ends up taking random steps. Not surprisingly these are steps in both forward as well as backward direction. Funnily enough, these are also repeated movements. Now, it so happens that on this drunkard's path, there are two banana skins - one in forward direction and one in backward direction. There is a real danger that the drunkard's downfall may be accelerated if he accidentally slips over either of those banana skins.

Your task is to find out if he will slip over the banana skin on forward path or banana skin on backward path and in how much time. It is also possible that by his good fortune he might not step over either banana skins. Write a program to calculate the outcome.
Input Format:

First line contains total number of test cases, denoted by N
Next N lines, contain a tuple containing 6 values delimited by space
D FM BM T FBS BBS, where
D denotes direction, either F (Forward) or B (Backward)
FM denotes the magnitude of forward movement in meters
BM denotes the magnitude of backward movement in meters
T denotes time taken to cover 1 meter
FBS denotes distance from Drunkards' starting position and the banana skin in forward direction
BBS denotes distance from Drunkards' starting position and the banana skin in backward direction
Output Format:

For each test case, print time taken by the Drunkard to slip over the forward or backward banana skin. Print F if he slips over forward banana skin and B if he slips over the backward banana skin. Both the outputs must be delimited by whitespace
OR

Print "Hurray" if the Drunkard is lucky to not slip over either banana skin
Constraints:
1 <= N <= 100
forward movement (FM) > 0
backward movement (BM) > 0
time (T) > 0 
Distance to banana skin in forward direction (FBS) > 0
Distance to banana skin in backward direction (BBS) > 0
All input values must be integer only


SNo.                 Input                                     Output
1
                          6
                          B 14 12 7 25 4                     28 B
                         B 11 4 6 10 17                       156 F
                          F 2 3 9 12 15                        675 B
                         F 1 12 3 22 28                       102 B
                         B 8 8 5 9 18                        Hurray
                          F 8 8 5 7 9                           35 F
                          
'''


def drunkard_slip_time(input_recieved):
    position=0
    distance=0
    direction = input_recieved[0]
    forward_mag = input_recieved[1]
    backward_mag = input_recieved[2]
    time = input_recieved[3]
    forward_banana_pos = input_recieved[4]
    backward_banana_pos = input_recieved[5]


    if not(forward_mag>0 or backward_mag>0 or time>0 or forward_banana_pos>0 or backward_banana_pos>0):
        print("Invalid Input")
        return None
    else:

        if forward_mag==backward_mag and forward_banana_pos>forward_mag and backward_banana_pos>backward_mag:
            return None
        
        backward_banana_pos = -(backward_banana_pos)
        backward_mag = -(backward_mag)
        
        while(position!=backward_banana_pos or position!=forward_banana_pos):
            if direction == 'F':
                for i in range(0, forward_mag):
                    if position==backward_banana_pos:
                        return distance*time, 'B'
                    elif position==forward_banana_pos:
                        return distance*time, 'F'
                    else:
                        position+=1
                        distance+=1

                for i in range(backward_mag,0):
                    if position==backward_banana_pos:
                        return distance*time, 'B'
                    elif position==forward_banana_pos:
                        return distance*time, 'F'
                    else:
                        position-=1
                        distance+=1


            else:
                for i in range(backward_mag,0):
                    if position==backward_banana_pos:
                        return distance*time, 'B'
                    elif position==forward_banana_pos:
                        return distance*time, 'F'
                    else:
                        position-=1
                        distance+=1
                        
                for i in range(0, forward_mag):
                    if position==backward_banana_pos:
                        return distance*time, 'B'
                    elif position==forward_banana_pos:
                        return distance*time, 'F'
                    else:
                        position+=1
                        distance+=1

            
        
    
test_case1 = ('B',14,12,7,25,4)             # 28 B
test_case2 = ('B',11,4,6,10,17)             # 156 F
test_case3 = ('F',2,3,9,12,15)              # 675 B
test_case4 = ('F',1,12,3,22,28)             # 102 B
test_case5 = ('B',8,8,5,9,18)               # Hurray
test_case6 = ('F',8,8,5,7,9)                # 35 F


try:
    out_distance, out_direction = drunkard_slip_time(test_case5)
    print(out_distance, out_direction)

except TypeError:
    print("Hurray")

else:
    print("Unknown error")
