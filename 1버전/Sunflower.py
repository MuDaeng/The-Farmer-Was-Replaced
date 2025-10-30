import Sector
import Position
import MoveOrder
import Direction

def do(sector):
	leaf_list = []
	start_x, start_y = sector['start']
	end_x, end_y = sector['end']
	dir = East
	child_leaf_list = []
	
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
			child_leaf_list.append(Position.get_current_pos())
			num = measure()
			set_leaf_list(leaf_list, num)
		
		dir = Direction.reverse(dir)
			
		cur_x, cur_y = Position.get_current_pos()
		if not Sector.is_end_of_sector(cur_x, cur_y):
			move(North)
	while len(child_leaf_list) > 0:
		tmp_list = []
		for child_leaf in child_leaf_list:
			x, y = child_leaf
			MoveOrder.go_to(x, y)
			if not can_harvest():
				tmp_list.append(child_leaf)
		child_leaf_list = tmp_list
		
	for leaf in leaf_list:
		(x, y) = leaf['pos']
		MoveOrder.go_to(x, y)
		if can_harvest():
			harvest()
	
def set_leaf_list(leaf_list, num):
	index = 0
	
	for i in range(len(leaf_list)):
		index = i
		if(num > leaf_list[i]['number']) :
			break
	
	leaf = {'number' : num, 'pos' : Position.get_current_pos()}
	
	leaf_list.insert(index, leaf)
	
	