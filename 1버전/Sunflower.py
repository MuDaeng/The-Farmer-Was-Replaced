import Sector
import Position
import MoveOrder
import Direction
import List

def do(sector):
	leaf_list = []
	start_x, start_y = sector['start']
	end_x, end_y = sector['end']
	dir = East
	
	if Position.get_current_pos() != sector['start']:
		MoveOrder.go_to(start_x, start_y)
		
	for y in range(end_y - start_y):
		for x in range(end_x - start_x):
			if x > 0:
				move(dir)
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Sunflower)
			if get_water() < 0.5:
				use_item(Items.Water)
			num = measure()
			set_leaf_list(leaf_list, num)
		
		dir = Direction.reverse(dir)
			
		cur_x, cur_y = Position.get_current_pos()
		if not Sector.is_end_of_sector(cur_x, cur_y):
			move(North)
	
	#leaf_list = sort_leaf_list_by_nums(leaf_list)
	
	for leaf in leaf_list:
		(x, y) = leaf['pos']
		MoveOrder.go_to(x, y)
		if can_harvest():
			harvest()
	
def set_leaf_list(leaf_list, num):
	index = len(leaf_list)
	list_size = len(leaf_list)
	is_even = num % 2 != 0
	for i in range(list_size):
		current_num = leaf_list[i]['number']
		if(is_even and num > current_num) or (not is_even and num >= current_num) :
			index = i
			break
	
	leaf = {'number' : num, 'pos' : Position.get_current_pos()}
	
	leaf_list.insert(index, leaf)
	
def sort_leaf_list_by_nums(leaf_list):
	leaf_num_dict = get_leaf_nums_count(leaf_list)
	
	i = 0
	result = []
	for leaf_num in leaf_num_dict:
		sublist = List.sublist(leaf_list, i, i + leaf_num_dict[leaf_num])
		sublist = sort_leaf_by_distance(sublist)
		result = List.add_all(result, sublist)
	return result
		
	
def get_leaf_nums_count(leaf_list):
	leaf_num_dict = {}
	
	leaf_num = 0
	leaf_count = 0
	
	for i in range(len(leaf_list)):
		current_leaf = leaf_list[i]
		if i == 0:
			leaf_num = current_leaf['number']
		if leaf_num != current_leaf['number']:
			leaf_num_dict[leaf_num] = i - leaf_count
			leaf_count = i
			leaf_num = current_leaf['number']
	leaf_num_dict[leaf_num] = len(leaf_list) - leaf_count
	return leaf_num_dict
	
def sort_leaf_by_distance(leaf_list):
	result = [leaf_list[0]]
	
	min = 1
	while len(result) < len(leaf_list):
		min_pos = (99, 99)
		prev_pos = result[len(result) - 1]['pos']
		for i in range(1, len(leaf_list)):
			if List.contains(result, leaf_list[i]):
				continue
			min_x, min_y = Position.get_distance(prev_pos, min_pos)
			i_x, i_y = Position.get_distance(prev_pos, leaf_list[i]['pos'])
			
			if (abs(min_x) + abs(min_y)) > (abs(i_x) + abs(i_y)):
				min = i
				prev_pos = leaf_list[i]['pos']
		result.append(leaf_list[min])
	
	return result
