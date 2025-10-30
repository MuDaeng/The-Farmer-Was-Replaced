import Direction
import Position
import Sector
import MoveOrder

def do(sector):
	start_x, start_y = sector['start']
	end_x, end_y = sector['end']
	dir = East
	if Position.get_current_pos() != sector['start']:
		MoveOrder.go_to(start_x, start_y)
		
	for y in range(end_y - start_y):
		for x in range(end_x - start_y):
			if get_ground_type() != Grounds.Soil:
				till()
			
			if can_harvest():
				harvest()
			plant(Entities.Cactus)
			move(dir)
			
		dir = Direction.reverse(dir)
			
		cur_x, cur_y = Position.get_current_pos()
		if end_y - 1 != cur_y:
			move(North)
	