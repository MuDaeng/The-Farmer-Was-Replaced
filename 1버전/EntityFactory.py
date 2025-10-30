import Sunflower
import Tree
import Pumpkin
import Treasure
import Cactus
import Sector
import Position
import MoveOrder

factory = {}
factory[Entities.Sunflower] = Sunflower
factory[Entities.Tree] = Tree
factory[Entities.Pumpkin] = Pumpkin
factory[Entities.Treasure] = Treasure
factory[Entities.Cactus] = Cactus



def do_sectors():
	for entity in factory:
		def task():
			sector = Sector.get_sectors()[entity]
			do_sector(factory[entity], sector)

		spawn_drone(task)
		
def do_sector(component, sector):
	while True:
		component.do(sector)