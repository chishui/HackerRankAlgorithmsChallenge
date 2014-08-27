import sets

if __name__ == '__main__' : 
	n = raw_input()
	oset = None
	for i in range(int(n)) :
		s = raw_input()
		if not oset :
			oset = sets.Set(list(s))
		else:
			oset = oset.intersection(sets.Set(list(s)))
		if not len(oset) :
			break

	print len(oset)