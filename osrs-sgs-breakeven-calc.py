import random
import math

def calculate_break_even(damage, prayer_level, potion_cost, sgs_price):
    # Constants
    prayer_restore_per_damage = 0.25  # 1/4 damage
    prayer_per_potion = prayer_level * 0.25 + 7  # prayer restored per dose
    doses_per_potion = 4  # typically 4 doses per potion
    
    # Calculate total prayer points restored by SGS for given damage
    total_prayer_restored = damage * prayer_restore_per_damage
    
    # Calculate the number of potions needed to restore the same amount of prayer
    total_potions_needed = total_prayer_restored / (prayer_per_potion * doses_per_potion)
    
    # Cost to restore the same amount of prayer with potions
    total_potion_cost = total_potions_needed * potion_cost
    
    # 1% Trading tax of the SGS
    tax_sgs = 0.01 * sgs_price   
    
    # Output the costs and the required damage to break even
    return total_potion_cost, tax_sgs


# User inputs or assumed values
player_prayer_level = 99
current_potion_cost = 10000  # Cost of one 4-dose Prayer Potion
current_sgs_price = 38000000  # Current GE price of Saradomin Godsword
standard_max_hit = 65 # Max hit with SGS on standard attacks. Use https://tools.runescape.wiki/osrs-dps/
standard_accuracy = .9631 # Accuracy with SGS off on standard attacks. Use https://tools.runescape.wiki/osrs-dps/

# Calculate the damage required
required_damage = 1
potion_cost, tax = calculate_break_even(required_damage, player_prayer_level, current_potion_cost, current_sgs_price)
while potion_cost < tax:
    required_damage += 1
    potion_cost, tax = calculate_break_even(required_damage, player_prayer_level, current_potion_cost, current_sgs_price)

print(f"Damage required to break even: {required_damage}")
print(f"Cost with potions: {potion_cost:.2f}, 1% Tax on SGS: {tax:.2f}")

# Calculate Special DPS
special_max_hit = math.floor(standard_max_hit * 1.10) # max hit increased by 10%, rounded to lowest integer

if (standard_accuracy * 2) >= 1.00: # accuracy doubled and equals 100% of greater than 100%
    special_accuracy = 1.00
else:
    special_accuracy = standard_accuracy * 2 # accuracy doubled

special_average_hit = math.floor(special_max_hit * special_accuracy / 2)
number_of_specials = math.ceil(required_damage / special_average_hit)
required_time = number_of_specials / 2 * 150 # 2 specials per attack energy, attack energy replinishes every 150 seconds with lightbearer

print(f"Number of special attacks: {number_of_specials}")
print(f"Time to restore all specials: {required_time} seconds")
