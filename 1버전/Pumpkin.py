import Direction
import Position
import Sector
import MoveOrder

def do(sector):
	start_x, start_y = sector['start']
	end_x, end_y = sector['end']
	dir = East
	dead_pumpkin_list = []
	
	entity = Entities.Pumpkin
	
	if Position.get_current_pos() != sector['start']:
		MoveOrder.go_to(start_x, start_y)
	
	for y in range(end_y - start_y):
		for x in range(end_x - start_x):
			if x > 0:
				move(dir)
				
			if get_ground_type() != Grounds.Soil:
				till()
			plant(entity)

		
		dir = Direction.reverse(dir)
		
		cur_x, cur_y = Position.get_current_pos()
		if not Sector.is_end_of_sector(cur_x, cur_y):
			move(North)
	
	MoveOrder.go_to(start_x, start_y)
	
	dir = East
	for y in range(end_y - start_y):
		for x in range(end_x - start_x):
			if x > 0:
				move(dir)
			
			if get_entity_type() == Entities.Dead_Pumpkin:
				dead_pumpkin_list.append(Position.get_current_pos())
				plant(entity)
			
		dir = Direction.reverse(dir)
			
		cur_x, cur_y = Position.get_current_pos()
		if not Sector.is_end_of_sector(cur_x, cur_y):
			move(North)
		
	while True:		
		for pos in dead_pumpkin_list:
			x, y = pos
			MoveOrder.go_to(x, y)
			if can_harvest():
				dead_pumpkin_list.remove(pos)
			else:
				plant(Entities.Pumpkin)
				
		len_of_list = len(dead_pumpkin_list)
		if len_of_list == 0:
			harvest()
			break
		elif len_of_list >= 2:
			dead_pumpkin_list = dead_pumpkin_list
			#sort_min_distance(dead_pumpkin_list)

def sort_min_distance(dead_pumpkin_list):
	len_of_list = len(dead_pumpkin_list)
	
	list = []

	for i in range(len_of_list - 1):
		cur = dead_pumpkin_list[i]
		if i == 0:
			list.append(cur)
		min = dead_pumpkin_list[i + 1]
		min_x, min_y = Position.get_distance(cur, min)
				
		for j in range(len_of_list):
			if j < 1:
				continue
			next = dead_pumpkin_list[j]
					
			next_x, next_y = Position.get_distance(cur, next)
					
			if (abs(min_x) + abs(min_y)) > (abs(next_x) + abs(next_y)):
				min = next
		
		list.append(min)
	
	return list
		