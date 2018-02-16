import re

from evalue_service import *

def rank_course(inputstr):
	inputstr = re.findall(r'\w+', inputstr.upper())
	depart = inputstr[0]
	cnums = inputstr[1:]
	sDict = {}
	for cnum in cnums:
		sDict.update({cnum:evaluate(depart, cnum)})

	top5 = sorted(sDict, key=sDict.get, reverse=True)[:5]	
	
	return ' '.join(top5)

if __name__ == "__main__":
	print(rank_course('COMS w1004 w4995 w3136 '))