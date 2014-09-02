#https://www.hackerrank.com/challenges/acm-icpc-team

import sets

NM = raw_input().strip().split()
N = int(NM[0])
M = int(NM[1])

allset = []
for x in xrange(0, N):
	allset.append(sets.Set([i for i, item in enumerate(list(raw_input().strip())) if item == '1']))

maxcount = 0
teamcount = 0
for i in range(0, len(allset)):
	for j in range(i + 1, len(allset)):
		uni = allset[i].union(allset[j])
		if maxcount < len(uni):
			maxcount = len(uni)
			teamcount = 1
		elif maxcount == len(uni) :
			teamcount = teamcount + 1


print maxcount
print teamcount