#!/Users/bracero/code/crashncompile/venv/bin/python

from sys import stdin

remove_new_lines       = True
split_by_char          = True
special_character      = "#"
remove_empty_last_cell = True
remove_all_empty       = True

def get_rid_of_newlines(str1):
	return str1[0:-1]

def split_by_special_char(str_arr):
	accum = [[]]
	for str1 in str_arr:
		if str1 == special_character:
			accum.append([])
		else:
			if remove_all_empty and str1=="":
				pass
			else:
				accum[len(accum)-1].append(str1)
	if remove_empty_last_cell and accum[-1] == []:
		accum.pop()
	return accum

data = stdin.readlines()

if remove_new_lines:
	data = map(get_rid_of_newlines,data)

if split_by_char:
	data = split_by_special_char(data)

print(data)