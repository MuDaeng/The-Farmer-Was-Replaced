import Position
import Direction
import MoveOrder

maze = {}
size = get_world_size()
list = [East, South, West, North]
def do(sector):
	start_x, start_y = sector['start']
	end_x, end_y = sector['end']
	maze_size = (end_x - start_x) * 2**(num_unlocked(Unlocks.Mazes) - 1)
	MoveOrder.go_to(start_x, end_y-1)
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, maze_size)
	
	find_treasure(None)
		
def contains(collect, obj):
	for i in collect:
		if obj == i:
			return True
	return False

def find_treasure(prev_move):
	moveable_directions = get_can_moves()
	
	if Position.get_current_pos() == measure():
		harvest()
		return True
	
	if prev_move != None and contains(moveable_directions, Direction.reverse(prev_move)):
		moveable_directions.remove(Direction.reverse(prev_move))
	
	for dir in moveable_directions:
		if get_entity_type() == Entities.Hedge:
			move(dir)
			finded = find_treasure(dir)
			if finded:
				return True
		else:
			return False
	if prev_move != None:
		move(Direction.reverse(prev_move))
		
def constructMaze(sector):
	for i in range(size) :
		for j in range(size) :
			maze[(i,j)] = set()
		
def get_can_moves():
	#pos = maze[Position.get_current_pos()]
	
	#if len(pos) > 0 :
		#return pos
	pos = set()	
	for dir in Direction.allDirections:
		if can_move(dir):
			pos.add(dir)

	return pos
	