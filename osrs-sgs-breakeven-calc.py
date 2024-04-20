import random
import math

# User inputs or assumed values
player_prayer_level = 92
current_potion_cost = 10000  # Cost of one 4-dose Prayer Potion
current_sgs_price = 38000000  # Current GE price of Saradomin Godsword
standard_max_hit = 65 # Max hit with SGS on standard attacks, including Super Strength potion and Piety. Use https://tools.runescape.wiki/osrs-dps/
standard_attack_roll = 26512 # Attack roll with SGS on standard attacks, including Piety. Use https://tools.runescape.wiki/osrs-dps/
npc_defense_roll = 19992 # NPC Defense roll. Use https://tools.runescape.wiki/osrs-dps/

# 1% Trading tax of the SGS
tax_sgs = current_sgs_price / 100

# Calculate prayer per dose given a player's prayer level
prayer_per_dose = math.floor(player_prayer_level / 4 + 7)

# Calculate damage required to do with SGS special attack to offset GE tax
# The special attack damage is valued by substituting prayer restored with prayer potions
# Divide the cost of SGS tax by prayer potion price to get cost of SGS tax in prayer potions
required_damage = ((tax_sgs / current_potion_cost) * (prayer_per_dose * 4)) * 4
print(f"SGS Special Attack damage required to offset GE tax : {required_damage}")


# Apply SGS special attack bonuses
special_max_hit = math.floor(standard_max_hit * 1.10) # max hit increased by 10%, rounded to lowest integer
standard_attack_roll = 2 * standard_attack_roll # double accuracy

# Calculate hit chance. Formula from https://oldschool.runescape.wiki/w/Damage_per_second/Melee#Step_six:_Calculate_the_hit_chance
if standard_attack_roll > npc_defense_roll:
    hit_chance = 1 - (npc_defense_roll + 2) / (2 * (standard_attack_roll + 1))
else:
    hit_chance = standard_attack_roll / (2 * (npc_defense_roll + 1))       

special_average_damage = special_max_hit * hit_chance / 2 # Calculate the damage output. Formula from https://oldschool.runescape.wiki/w/Damage_per_second/Melee#Step_six:_Calculate_the_hit_chance
number_of_specials = math.ceil(required_damage / special_average_damage)
required_time = number_of_specials / 2 * 150 # 2 special attacks per energy bar, per 150 seconds because attack energy replinishes 150 seconds with lightbearer



print(f"Number of special attacks: {number_of_specials}")
print(f"Time to restore all specials: {required_time / 3600 } hours")
