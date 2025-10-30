def get_current_pos():
	return (get_pos_x(), get_pos_y())

def get_distance(start_pos, target_pos):
	target_x, target_y = target_pos
	start_x, start_y = start_pos
	return (target_x - start_x, target_y - start_y)
	
def get_distance_of_current(x, y):
	return get_distance(get_current_pos(), (x, y))
