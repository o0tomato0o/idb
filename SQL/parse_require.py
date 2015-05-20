#!/usr/bin/env python3
import sys
import json 

def main(w):
	data_list = json.load(open('../Job.json', 'r'))
	parse(data_list, w)
	'''
	data_list = json.load(open('Job_Require_Language.json', 'r'))
	parse("INSERT INTO Job_Require_Language (" , data_list)
	data_list = json.load(open('Job_Require_Skillset.json', 'r'))
	parse("INSERT INTO Job_Require_Skillset (" , data_list)
	'''

def parse(data_list, w):
	lst = []
	for data in data_list:

		dic = {}
		key_lst = []
		v_lst = []
		
		for k,v in data.items():
			if (k == "job_ID" or k == "skillset_ID" ) :
				dic[k] = v				

		lst.append(dic)

	with open('Job_Require_Skillset.json', 'w') as outfile:
		json.dump(lst, outfile)

main(sys.stdout)
