#https://www.hackerrank.com/challenges/chocolate-feast

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range (0,T):
    A,B,C1 = [int(x) for x in raw_input().split(' ')]
    
    answer = 0
    # write code to compute answer
    remain = A / B
    answer = remain
    while remain >= C1:
    	answer = answer + remain / C1
    	remain = remain / C1 + remain % C1

    print answer