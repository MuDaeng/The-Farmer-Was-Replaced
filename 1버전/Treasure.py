import Position
import Direction
import MoveOrder
import List

maze = {}
size = get_world_size()
list = [East, South, West, North]
def do(sector):
	initialize_maze(sector)
	
	find_treasure(None)

def initialize_maze(sector):
	start_x, start_y = sector['start']
	end_x, end_y = sector['end']
	maze_size = (end_x - start_x) * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
	MoveOrder.go_to(start_x, end_y - 1)
	
	if get_ground_type() != Grounds.Grassland:
		till()
	while get_entity_type() != Entities.Bush:
		plant(Entities.Bush)
	use_item(Items.Weird_Substance, maze_size)
		
def find_treasure(prev_dir):
	moveable_directions = get_can_moves()
	
	if prev_dir != None:
		prev_dir = Direction.reverse(prev_dir)
	
	if Position.get_current_pos() == measure():
		harvest()
		return True
	
	if prev_dir != None and List.contains(moveable_directions, prev_dir):
		moveable_directions.remove(prev_dir)
	
	for dir in moveable_directions:
		if get_entity_type() == Entities.Hedge:
			move(dir)
			finded = find_treasure(dir)
			if finded:
				return True
		else:
			return False
	if prev_dir != None:
		move(prev_dir)
		
def get_can_moves():
	pos = []
	prior = get_priority_dir()
		
	for dir in prior:
		if can_move(dir):
			pos.append(dir)

	for dir in Direction.allDirections:
		if not dir in prior and can_move(dir):
			pos.append(dir)

	return pos

def get_priority_dir():
	x, y = measure()
	dist_x, dist_y = Position.get_distance_of_current(x, y)
	prior = set()
		
	if dist_x > 0:
		prior.add(East)
	elif dist_x < 0:
		prior.add(West)
	
	if dist_y > 0:
		prior.add(North)
	elif dist_y < 0:
		prior.add(South)
	
	return prior
