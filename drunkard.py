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