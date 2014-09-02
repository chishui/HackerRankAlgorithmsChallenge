#https://www.hackerrank.com/challenges/mark-and-toys
# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_toys(prices, rupees):
  #Compute and return final answer over here
  answer = 0
  prices.sort()
  count = 0
  for i,price in enumerate(prices):
  	if count + price > rupees:
  		answer = i
  		break
  	count = count + price

  return answer

if __name__ == '__main__':
  n, k = map(int, raw_input().split())
  prices = map(int, raw_input().split())
  print max_toys(prices, k)