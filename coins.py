'''
Find the minimum number of coins to form any value between 1 to N, both inclusive. Cumulative value of coins should not exceed N.
Coin denominations are 1Rupee, 2Rupee, 5Rupee. Let's undersatnd the problem using the following example. Consider the value of N is 13,
then the minimum number of coins required to formulatte any value between 1 and 13, is 6. One 5R coin, three 2R coin and two 1R coins are 
required to realize any value between 1 and 13. Hence this is the answer. However, if one takes two 5R coins, one 2R coin and two 1R coin, then
to all values between 1 and 13 are achieved. But since the cumulative value of all coins equals 14, i.e. exceeds 13, this is not the answer.

Input Format
A single integer value
Output Format
1st - Total Number of coins
2nd - Number of 5 Rupee coins
3rd - Number of 2 Rupee coins
4th - Number of 1 Rupee coins.

Constraints
0<n<[1000

Sample Input:
13
Sample Output
6 1 3 2

Explanation:
The min no of coins required is 6 with in it:
min number of 5 R coins = 1
min number of 2 R coins = 3
min number of 1 R coins = 2
Using these coins, we can form any value with in the given value and itself, like below:
Here the given value is 13
For 1  = one 1 R coin
For 2  = one 2 R coin
For 3  = one 1 R coin and one 2 R coins
For 4  = two 2 R coin
For 5  = one 5 R coin
For 6  = one 5 R coin and one 1 R coin
For 7  = one 5 R coin and one 2 R coin
For 8  = one 5 R coin, one 2 R coin and one 1 R coin
For 9  = one 5 R coin and two 2 R coin
For 10 = one 5 R coin, two 2 R and one 1 R coin
For 11 = one 5 R coin, two 2 R coin and two 1 R coin
For 12 = one 5 R coin, three 2 R coin and one 1 R coin
For 13 = one 5 R coin, three 2 R coin and two 1 R coin
'''


'''
13
temp = {5:0,2:0,1:0}
{5:0,2:0,1:0}
{5:0,2:0,1:0}
{5:0,2:0,1:0}
{5:0,2:0,1:0}
{5:0,2:0,1:0}
1.find all psiible cobniation of 5,2,1 for N store in list of dict
[{5:0,2:0,1:13},{5:2,2:1,1:1}]
2. sort list acending choose top dict
3.  validation list cobination 1-N
    if true:
        print no
    else;
    access second element





1 12 123

1 2 3 4 5 6 7 8 9 0

5*3, 2*1, 1*3

5*23 , 2*2, 1*2

121

121-9=112
112/5=
r=2
q=22


20/5
r 0 q 4

20-9 
11/5
q 2 r 1
1/2
q 0 r 1
'''


def get_min_count(n):
    if n>9:
        count_5 = 1
        count_2 = 1
        count_1 = 2
        quotient_5 = (n-9)//5
        remainder_5 = (n-9)%5
        
        quotient_2 = remainder_5//2
        remainder_2 = remainder_5%2

        count_5+=quotient_5
        count_2+=quotient_2
        count_1+=remainder_2

    else:
        count_5 = 0
        count_2 = 0
        count_1 = 0
        if n<5:
            quotient_2 = n//2
            remainder_2 = n%2
            count_2+=quotient_2
            count_1+=remainder_2
        else:
            count_5+=1
            n-=5
            quotient_2 = n//2
            remainder_2 = n%2
            count_2+=quotient_2
            count_1+=remainder_2

    print ("Total count: ",count_5+count_2+count_1)
    print ("5 count: ",count_5)
    print ("2 count: ",count_2)
    print ("1 count: ",count_1)        


get_min_count(3)