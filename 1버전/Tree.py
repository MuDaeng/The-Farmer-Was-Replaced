import Sector
import Position
import Direction
import MoveOrder

def do(sector) :
	start_x, start_y = sector['start']
	end_x, end_y = sector['end']
	dir = East
	
	if Position.get_current_pos() != sector['start']:
		MoveOrder.go_to(start_x, start_y)
		
	for y in range(end_y - start_y):
		for x in range(end_x - start_x):
			if x > 0:
				move(dir)

			if can_harvest():
				harvest()
	
			entity = Entities.Tree
			if (get_pos_x() + get_pos_y()) % 2 != 0:
				if get_pos_y() % 2 == 0:
					entity = Entities.Carrot
					if get_ground_type() != Grounds.Soil:
						till()
				else:
					entity = Entities.Grass
			plant(entity)
			
		dir = Direction.reverse(dir)
			
		cur_x, cur_y = Position.get_current_pos()
		if not Sector.is_end_of_sector(cur_x, cur_y):
			move(North)