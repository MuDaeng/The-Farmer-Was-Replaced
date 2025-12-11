def remove_all(source, target):
	for i in target:
		source.remove(i)
	return source

def add_all(source, target):
	for i in target:
		source.append(i)
	return source

def sublist(list, start, end):
	result = []
	for i in range(start, end):
		result.append(list[i])
	return result

def contains(list, obj):
	return obj in list
