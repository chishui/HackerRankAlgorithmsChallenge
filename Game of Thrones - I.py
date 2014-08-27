string = raw_input()
 
found = False
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
data = {}

def add(ch) :
	data.setdefault(ch, 0)
	data[ch] = data[ch] + 1

map(add, list(string))

found = True
count = 0
for key, value in data.items():
	if value % 2: 
		count = count + 1
	if count > 1 : 
		found = False
		break

if not found:
    print("NO")
else:
    print("YES")