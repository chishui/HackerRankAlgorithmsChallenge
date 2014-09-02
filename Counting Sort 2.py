#https://www.hackerrank.com/challenges/countingsort2

N = input()
li = map(int, raw_input().strip().split())

count = [li.count(i) for i in range(0, 100)]
out = [i for i, num in enumerate(count) for j in range(0, num)]
print ' '.join(map(str, out))