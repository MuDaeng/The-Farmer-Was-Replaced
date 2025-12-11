def swap(dict, key1, key2):
	tmp = dict[key1]
	dict[key1] = dict[key2]
	dict[key2] = tmp

def is_empty(dict):
	for i in dict:
		return False
	return True
