def  maxXor( l,  r):
	length = len(bin(r)) - 2
	lower = 2 ** (length - 1)
	if l <= lower <= r and l <= lower-1 <= r :
		return 2 ** length - 1
	else:
		l = l - 2 ** (length - 1)
		r = r - 2 ** (length - 1)
		return maxXor(l, r)


_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)
