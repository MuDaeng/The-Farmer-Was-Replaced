import Direction
import Position
import Sector
import MoveOrder
import List

global pumpkins_measure
pumpkins_measure = {}
global dead_pumpkins
dead_pumpkins = set()

def do(sector):
	start_x, start_y = sector['start']
	end_x, end_y = sector['end']
	dir = East
	dead_pumpkin_list = []
	
	global pumpkins_measure
	
	entity = Entities.Pumpkin
	
	if Position.get_current_pos() != sector['start']:
		MoveOrder.go_to(start_x, start_y)
	
	for y in range(end_y - start_y):
		for x in range(end_x - start_x):
			if x > 0:
				move(dir)
				
			if get_ground_type() != Grounds.Soil:
				till()
				
			if get_entity_type() == Entities.Dead_Pumpkin:
				if not List.contains(dead_pumpkin_list, Position.get_current_pos()):
					dead_pumpkin_list.append(Position.get_current_pos())
				dead_pumpkins.add(pumpkins_measure[Position.get_current_pos()])

			plant(entity)
			while measure() in dead_pumpkins:
				harvest()
				plant(entity)
			
			pumpkins_measure[Position.get_current_pos()] = measure()
		
		dir = Direction.reverse(dir)
		
		cur_x, cur_y = Position.get_current_pos()
		if not Sector.is_end_of_sector(cur_x, cur_y):
			move(North)
	
	MoveOrder.go_to(start_x, start_y)
		
	while len(dead_pumpkin_list) > 0:
		remove_list = []
		for pos in dead_pumpkin_list:
			x, y = pos
			MoveOrder.go_to(x, y)
			if can_harvest():
				#dead_pumpkin_list.remove(pos)
				remove_list.append(pos)
			elif get_entity_type() == Entities.Dead_Pumpkin:
				if not List.contains(dead_pumpkin_list, Position.get_current_pos()):
					dead_pumpkin_list.append(Position.get_current_pos())
				dead_pumpkins.add(pumpkins_measure[Position.get_current_pos()])

			plant(entity)
			while measure() in dead_pumpkins:
				harvest()
				plant(entity)
			
			pumpkins_measure[Position.get_current_pos()] = measure()
		
		List.remove_all(dead_pumpkin_list, remove_list)
		len_of_list = len(dead_pumpkin_list)
		if len_of_list == 0:
			harvest()
			pumpkins_measure = {}
		
