n = input()
k = input()
candies = [input() for _ in range(0,n)]
candies.sort()
min_diff = min([candies[k + i - 1] - candies[i] for i in range(0, n - k)])

print min_diff