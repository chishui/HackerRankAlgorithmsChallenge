
n = input()
matrix = []
matrix[len(matrix) :] = [list(raw_input()) for i in range(0, n)]

cavity = []
for i, line in enumerate(matrix):
	if i == 0 or i == len(matrix) - 1 :
		continue
	for j, x in enumerate(line):
		if j == 0 or j == len(line) - 1 :
			continue

		if int(x) > int(line[j-1]) and int(x) > int(line[j + 1]) and int(x) > int(matrix[i + 1][j]) and int(x) > int(matrix[i - 1][j]) :
			cavity.append((i, j))

for item in cavity:
	matrix[item[0]][item[1]] = 'X'
print '\n'.join([''.join(i) for i in matrix])

	
