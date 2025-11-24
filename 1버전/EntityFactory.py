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
		def do_sector():
			sector = Sector.get_sectors()[entity]
			while True:
				factory[entity].do(sector)

		spawn_drone(do_sector)
