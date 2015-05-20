#!/usr/bin/env python3
import sys
import json 

def main(w):
	data_list = json.load(open('../Job.json', 'r'))
	parse("INSERT INTO Job (" , data_list, w)
	data_list = json.load(open('../Company.json', 'r'))
	parse("INSERT INTO Company (" , data_list, w)
	data_list = json.load(open('../Language.json', 'r'))
	parse("INSERT INTO Language (" , data_list, w)
	data_list = json.load(open('../Location.json', 'r'))
	parse("INSERT INTO Location (" , data_list, w)
	data_list = json.load(open('../Skillset.json', 'r'))
	parse("INSERT INTO Skillset (" , data_list , w)
	data_list = json.load(open('../Member.json', 'r'))
	parse("INSERT INTO Member (" , data_list , w)
	data_list = json.load(open('../Job_Require_Language.json', 'r'))
	parse("INSERT INTO Job_Require_Language (" , data_list, w)
	data_list = json.load(open('../Job_Require_Skillset.json', 'r'))
	parse("INSERT INTO Job_Require_Skillset (" , data_list, w)

def parse(sql_pre, data_list, w):
	for data in data_list:

		key_lst = []
		v_lst = []
		
		for k,v in data.items():
			if sql_pre == "INSERT INTO Job (" and (k == "language_ID" or k == "skillset_ID") :
				continue
			else :
				#print k
				key_lst.append(k)
				#print v
				v_lst.append(v)

		sql = sql_pre

		
		for i in range(len(key_lst)):
			if i == len(key_lst)-1:
				sql = sql + str(key_lst[i]) + " )" 
			else:
				sql = sql + str(key_lst[i]) + " ,"

		sql = sql + " VALUES ("
		for i in range(len(v_lst)):
			if i == len(v_lst)-1:
				if type( v_lst[i] ) == int:
					sql = sql + str(v_lst[i]) + " );" 
				else:
					sql = sql + '"' + str(v_lst[i]) +  '" );'
			else:
				#print v_lst[i]
				if type( v_lst[i] ) == int:
					sql = sql + str(v_lst[i]) + " , " 
				else:
					sql = sql + '"' + str(v_lst[i]) +  '" , '
		#print sql
		w.write(sql+'\n')

main(sys.stdout)
