import re
import pandas as pd

from evalue_service import *

def rank_course(inputstr):
	inputstr = re.findall(r'\w+', inputstr.upper())
	depart = inputstr[0]
	cnums = inputstr[1:]
	slist = []
	for cnum in cnums:
		slist.append([cnum, evaluate(depart, cnum)])

	df = pd.DataFrame(slist, columns=['cnum','score'])
	df = df.sort_values(by='score', ascending = False)
	
	return df['cnum'].to_string()

if __name__ == "__main__":
	print(rank_course('COMS w1004 w4995 w3136 '))