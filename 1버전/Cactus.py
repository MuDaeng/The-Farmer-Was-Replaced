import Direction
import Position
import Sector
import MoveOrder
import Dictionary

def do(sector):
	sector = Sector.sectors[Entities.Cactus]
	start_x, start_y = sector['start']
	end_x, end_y = sector['end']
	dir = East
	if Position.get_current_pos() != sector['start']:
		MoveOrder.go_to(start_x, start_y)
		
	y_size = end_y - start_y
	x_size = end_x - start_x
	for y in range(y_size):
		for x in range(x_size):
			if get_ground_type() != Grounds.Soil:
				till()
			if can_harvest():
				harvest()
			plant(Entities.Cactus)

			if x != x_size - 1:
				move(dir)
			
		dir = Direction.reverse(dir)
			
		cur_x, cur_y = Position.get_current_pos()
		if end_y - 1 != cur_y:
			move(North)
	
	MoveOrder.go_to(start_x, start_y)
	
	orderd_dict = {}
	for y in range(y_size):
		ordered_dict = {}
		while Dictionary.is_empty(ordered_dict) or not is_ordered_all(ordered_dict, end_x):
			for x in range(x_size):
				if x == x_size - 1:
					continue
					
				cur_x, cur_y = Position.get_current_pos()
				cur_mea = measure()
				nex_mea = measure(dir)
				nex_x = cur_x + 1
				
				if dir == West:
					nex_x = cur_x - 1
					
				ordered_dict[cur_x] = cur_mea
				ordered_dict[nex_x] = nex_mea
				if (dir == East and nex_mea < cur_mea) or (dir == West and nex_mea > cur_mea):
					Dictionary.swap(ordered_dict, cur_x, nex_x)
					swap(dir)
					
				move(dir)
			
			dir = Direction.reverse(dir)
			
		cur_x, cur_y = Position.get_current_pos()
		if end_y - 1 != cur_y:
			move(North)
		if cur_x == start_x:
			dir = East
		elif cur_x == end_x - 1:
			dir = West
	
	dir = North
	MoveOrder.go_to(start_x, start_y)
	
	for x in range(x_size):
		ordered_dict = {}
		while Dictionary.is_empty(ordered_dict) or not is_ordered_all(ordered_dict, end_y):
			for y in range(y_size):
				if y == y_size - 1:
					continue
					
				cur_x, cur_y = Position.get_current_pos()
				cur_mea = measure()
				nex_mea = measure(dir)
				nex_y = cur_y + 1
				
				if dir == South:
					nex_y = cur_y - 1
					
				ordered_dict[cur_y] = cur_mea
				ordered_dict[nex_y] = nex_mea
				
				if (dir == North and nex_mea < cur_mea) or (dir == South and nex_mea > cur_mea):
					Dictionary.swap(ordered_dict, cur_y, nex_y)
					swap(dir)
					
				move(dir)
				
			dir = Direction.reverse(dir)
			
		cur_x, cur_y = Position.get_current_pos()
		if end_x - 1 != cur_x:
			move(East)

		if cur_y == start_y:
			dir = North
		elif cur_y == end_y - 1:
			dir = South
			
	harvest()
	
def is_ordered_all(dict, size):
	for key in dict:
		if key == size - 1:
			continue
		cur_mea = dict[key]
		nex_mea = dict[key + 1]
		if nex_mea < cur_mea:
			return False
	return True
