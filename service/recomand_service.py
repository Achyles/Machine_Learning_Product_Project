import re

from evalue_service import *

def recommand_course(depart):

	with open(datapath+fndes+'.json') as fp:
		desDict = json.load(fp)

	scoreDict = {}

	for cnum in desDict.keys():
		scoreDict.update({cnum:evaluate(depart, cnum)})

	top10 = sorted(scoreDict, key=scoreDict.get, reverse=True)[:10]

	return ' '.join(top10)

if __name__ == "__main__":
	print(recommand_course('COMS'))
