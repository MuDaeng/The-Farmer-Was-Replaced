reverseDirectionDic = {East : West, West : East, North : South, South : North }
allDirections = [East, West, South, North]

def reverse(direction):
	return reverseDirectionDic[direction]
	
