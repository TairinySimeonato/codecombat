def find_strongest_enemy():
	strongest_enemy = None

	for enemy in findEnemies():
		if strongest_enemy == None or enemy.maxHealth > strongest_enemy.maxHealth:
			strongest_enemy = enemy
	return strongest_enemy
	
####################################################
def enemy_weight(enemy):
	return enemy.maxHealth/hero.distanceTo(enemy)

def find_strongest_and_closest_enemy():
	strongest_weighted_enemy = None

	for current_enemy in hero.findEnemies():
		# for slow heros
		if hero.distanceTo(current_enemy) > 10:
			continue
	
		if strongest_weighted_enemy == None:
			strongest_weighted_enemy = current_enemy
			continue
		
		if enemy_weight(current_enemy) > enemy_weight(strongest_weighted_enemy):
			strongest_weighted_enemy = current_enemy
			
	return strongest_weighted_enemy
