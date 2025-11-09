import Direction
import Position

def get_move_orders(x, y):
	dist_x, dist_y = Position.get_distance_of_current(x, y)
	
	dir_x = East
	dir_y = North
	
	if dist_x < 0:
		dir_x = Direction.reverse(dir_x)
		dist_x = abs(dist_x)
	if dist_y < 0:
		dir_y = Direction.reverse(dir_y)
		dist_y = abs(dist_y)
		
	move_orders = {}
	move_orders['X'] = {'dir' : dir_x, 'dist' : dist_x}
	move_orders['Y'] = {'dir' : dir_y, 'dist' : dist_y}

	return move_orders
	
def move_num(dir, num) :
	for i in range(num) :
		move(dir)
		
def go_to(x, y):
	move_orders = get_move_orders(x, y)

	for i in move_orders:
		move_order = move_orders[i]
		move_num(move_order['dir'], move_order['dist'])