from pick import pick
import sys


sneaking = False

def get_stats_string(player_stats):
    """Returns a formatted string of stats to embed inside pick titles."""
    return (
        "=== CURRENT STATS ===\n"
        f"Filial Piety (FP): {player_stats['FP']}\n"
        f"Sanity (SAN):     {player_stats['SAN']}\n"
        f"Rebellion (REB):  {player_stats['REB']}\n"
        f"Passion (PAS):    {player_stats['PAS']}\n"
        "=====================\n"
    )

stats = {
    'FP': 50,
    'SAN': 50,
    'REB': 10,
    'PAS': 50
}

def lose(check):
    if check['REB'] > 100:
        print('You rebelled too hard and got hit by a flying slipper!\n💥 GAME OVER 💥')
        sys.exit()
    elif check['FP'] < 0:
        print('Your parents are profoundly disappointed and dealt EMOTIONAL DAMAGE.\n💔 GAME OVER 💔')
        sys.exit()
    elif check['PAS'] < 0:
        print('You became a neurosurgeon at 21, but lost your passion and now need therapy every week.\n🧠 GAME OVER 🧠')
        sys.exit()

# Introduction
print('How the game works:\nYou have 4 stats:\n'
      '- FP is how good you are in your parents eyes\n'
      '- REB is your rebellion\n'
      '- SAN is your sanity\n'
      '- PAS is your passion\n'
      'Your goal is to not get kicked out of your house while keeping your passion!\n')

# --- 1. Character Selection ---
title1 = get_stats_string(stats) + 'Please choose your character class: '
options1 = ['The Firstborn', 'The Middle Child', 'The Youngest']

option, index = pick(options1, title1, indicator='=>', default_index=0)
print(f"You chose the path of {option}!\n")

if index == 0:    
    stats['FP'] += 10
    stats['SAN'] -= 5
    print("Effect Applied: +10 Filial Piety (FP), -5 Sanity (SAN)\n")
elif index == 1:  
    stats['REB'] += 10
    stats['FP'] -= 5
    print("Effect Applied: +10 Rebellion (REB), -5 FP\n")
elif index == 2:
    stats['PAS'] += 10
    stats['REB'] -= 5
    print("Effect Applied: +10 Passion (PAS), -5 REB\n")

lose(stats)

title2 = get_stats_string(stats) + '\nInstrument Assignment:'
options2 = ['Choose piano', 'Choose violin', 'Beg to play football instead']

option, index = pick(options2, title2, indicator='=>', default_index=0)

if index == 0:
    stats['FP'] += 10
    stats['SAN'] -= 5
    stats['PAS'] -= 5 
    print("Effect Applied: FP +10, Sanity -5, Passion -5\n")
elif index == 1:
    stats['FP'] += 10 
    stats['SAN'] -= 10
    stats['PAS'] += 5 
    print('Effect Applied: FP +10, Sanity -10, Passion +5\n')
elif index == 2:
    stats['FP'] -= 10
    stats['PAS'] += 10
    stats['REB'] += 10
    print('Effect Applied: FP -10, Passion +10, Rebellion +10\n')


lose(stats)

title3 = get_stats_string(stats) + '\nYou got your first report card, you have an A-minus:'


options3 = [
    'Cry and accept the lecture over an A-minus',
    'Argue that the exam was unfairly scaled'
]


if stats['REB'] >= 15:
    options3.append('Negotiate a do-over quiz')

# Run the pick menu
option, index = pick(options3, title3, indicator='=>', default_index=0)

if option == 'Cry and accept the lecture over an A-minus':
    stats['FP'] += 10
    stats['SAN'] -= 10
    print("Effect Applied: +10 FP, -10 SAN\n")

elif option == 'Argue that the exam was unfairly scaled':
    stats['REB'] += 10
    stats['FP'] -= 5
    print("Effect Applied: +10 REB, -5 FP\n")

elif option == 'Negotiate a do-over quiz (rebilion more then 15 made you clever)':
    stats['REB'] += 5
    stats['FP'] += 5
    stats['SAN'] -= 5
    print("Effect Applied: +5 REB, +5 FP, -5 SAN\n")

lose(stats)

title3 = get_stats_string(stats) + '\n you are on stage to perform :'


options3 = [
    'Play flawlessly from memory',
    'Freeze up on stage from nerves'
]


if stats['REB'] >= 25:
    options3.append('Sabatoge on purpose (becouse you reblion is more then 25)')


option, index = pick(options3, title3, indicator='=>', default_index=0)

if option == 'Play flawlessly from memory':
    stats['FP'] += 15
    stats['SAN'] -= 10
    print("Effect Applied: +15 FP, -10 SAN\n")

elif option == 'Freeze up on stage from nerves':
    stats['REB'] += 5
    stats['FP'] -= 10
    stats['SAN'] -=20
    print("Effect Applied: +5 REB, -10 FP, -15 SAN\n")

elif option == 'Sabatoge on purpose (becouse you reblion is more then 25)':
    stats['REB'] += 25
    stats['FP'] -=20
    stats['PAS'] += 10
    print("Effect Applied: +25 REB, -20 FP, +10 passion\n")

    lose(stats)

 title_sleepover = get_stats_string(stats) + '\nSleepover Request:'

# Short variables to save your fingers from typing later
opt_a = "Don't even ask (Self-censor)"
opt_b = "Ask directly and endure the interrogation"
opt_c = "Use a 'study-group' cover story"

options_sleepover = [opt_a, opt_b]

# Hidden Choice Check: Requires Passion (PAS) >= 30
if stats['PAS'] >= 30:
    options_sleepover.append(opt_c)

# Run the menu
option, index = pick(options_sleepover, title_sleepover, indicator='=>', default_index=0)

# Apply effects using our short variables
if option == opt_a:
    stats['FP'] += 5
    stats['PAS'] -= 10
    stats['SAN'] -= 5
    print("Effect Applied: +5 FP, -10 PAS, -5 SAN\n")

elif option == opt_b:
    stats['REB'] += 5
    stats['SAN'] -= 5
    print("Effect Applied: +5 REB, -5 SAN\n")

elif option == opt_c:
    stats['PAS'] += 10
    stats['FP'] -= 5
    sneaking = True  # Activates your sneaky flag for later events!
    print("Effect Applied: +10 PAS, -5 FP (Sneaking mode activated! dont get investigated)\n")

lose(stats)