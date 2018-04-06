def find_strongest_enemy():
	strongest_enemy = None

	for enemy in findEnemies():
		if strongest_enemy == None or enemy.maxHealth > strongest_enemy.maxHealth:
			strongest_enemy = enemy
	return strongest_enemy
	
####################################################
def find_strongest_and_closest_enemy():
	strongest_weighted_enemy = None

	for current_enemy in hero.findEnemies():
		if strongest_weighted_enemy == None:
			strongest_weighted_enemy = current_enemy
			continue
		
    if hero.distanceTo(current_enemy) > 50:
      continue
    
		strongest_enemy_weight = strongest_weighted_enemy.maxHealth/hero.distanceTo(strongest_weighted_enemy)
		current_enemy_weight = current_enemy.maxHealth/hero.distanceTo(current_enemy)
		if current_enemy_weight > strongest_enemy_weight:
			strongest_weighted_enemy = current_enemy      
			
	return strongest_weighted_enemy
