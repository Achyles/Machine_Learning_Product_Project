import re

from evalue_service import *

def rank_course(inputstr):
	inputstr = re.findall(r'\w+', inputstr.upper())
	depart = inputstr[0]
	cnums = inputstr[1:]
	slist = {}
	for cnum in cnums:
		slist.update({cnum:evaluate(depart, cnum)})

	top5 = sorted(slist, key=slist.get, reverse=True)[:5]
	
	return ' '.join(top5)

if __name__ == "__main__":
	print(rank_course('COMS w1004 w4995 w3136 '))
