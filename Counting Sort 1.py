#https://www.hackerrank.com/challenges/countingsort1

N = input()
li = map(int, raw_input().strip().split())

count = [li.count(i) for i in range(0, 100)]
print ' '.join(map(str, count))