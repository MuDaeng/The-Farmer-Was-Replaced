import MoveOrder
import Position

world_size = get_world_size()
half = world_size // 2
quarter = world_size // 4

sector_set = {Entities.Grass, Entities.Tree, Entities.Pumpkin, Entities.Grass, Entities.Treasure, Entities.Cactus}

sectors = {}
sectors[Entities.Sunflower] = { 'start' : (0, 0), 'end' : (quarter, half) }
sectors[Entities.Tree] = { 'start' : (quarter, 0) , 'end' : (half, half) }
sectors[Entities.Pumpkin] = { 'start' : (half, 0), 'end' : (world_size, half) }
sectors[Entities.Treasure] = { 'start' : (0, half),'end' : (half, world_size) }
sectors[Entities.Cactus] = { 'start' : (half, half), 'end' : (world_size, world_size) }


def is_in_sector(entity):
	x, y = Position.get_current_pos()
	sector = sectors[entity]
	start_x, start_y = sector['start']
	end_x, end_y = sector['end']
	return is_between(start_x, end_x, x) and is_between(start_y, end_y, y)

def initialize_sectors():
	for entity in sectors:
		sector = sectors[entity]
		start_x, start_y = sector['start']
		end_x, end_y = sector['end']
		MoveOrder.go_to(start_x, start_y)
		print(entity)
		MoveOrder.go_to(end_x, end_y)
		MoveOrder.go_to(start_x, start_y)

def get_sectors():
	#for i in range(sector_list):
		#index =
	return sectors

def get_sector(x, y):
	for sector in sectors:
		sector = sectors[sector]
		start_x, start_y = sector['start']
		end_x, end_y = sector['end']
		if is_between(start_x, end_x, x) and is_between(start_y, end_y, y):
			return sector
	return None
def is_end_of_sector(x, y):
	sector = get_sector(x, y)
	return (x + 1, y + 1) == sector['end']

def is_between(start, end, pos):
	return pos >= start and pos <= end