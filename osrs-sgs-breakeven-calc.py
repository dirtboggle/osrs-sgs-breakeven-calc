import random
import math

# User inputs or assumed values
player_prayer_level = 92
current_potion_cost = 10000  # Cost of one 4-dose Prayer Potion
current_sgs_price = 38000000  # Current GE price of Saradomin Godsword
standard_max_hit = 65 # Max hit with SGS on standard attacks. Use https://tools.runescape.wiki/osrs-dps/
standard_accuracy = .9631 # Accuracy with SGS on standard attacks. Use https://tools.runescape.wiki/osrs-dps/

# 1% Trading tax of the SGS
tax_sgs = current_sgs_price / 100

# Calculate prayer per dose given a player's prayer level
prayer_per_dose = math.floor(player_prayer_level / 4 + 7)

# Calculate damage required to do with SGS special attack to offset GE tax
# The special attack damage is valued by substituting prayer restored with prayer potions
# Divide the cost of SGS tax by prayer potion price to get cost of SGS tax in prayer potions
required_damage = ((tax_sgs / current_potion_cost) * (prayer_per_dose * 4)) * 4
print(f"New damage calculated to be: {required_damage}")

# Calculate Special DPS
special_max_hit = math.floor(standard_max_hit * 1.10) # max hit increased by 10%, rounded to lowest integer

if (standard_accuracy * 2) >= 1.00: # accuracy doubled and equals 100% if greater than 100%
    special_accuracy = 1.00
else:
    special_accuracy = standard_accuracy * 2 # accuracy doubled

special_average_hit = math.floor(((special_max_hit + 1) / 2) * special_accuracy)
number_of_specials = math.ceil(required_damage / special_average_hit)
required_time = number_of_specials / 2 * 150 # 2 specials per attack energy, attack energy replinishes every 150 seconds with lightbearer

print(f"Number of special attacks: {number_of_specials}")
print(f"Time to restore all specials: {required_time / 3600 } hours")
