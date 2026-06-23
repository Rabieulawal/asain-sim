from pick import pick
import sys

sneaking = False

def get_stats_string(player_stats):
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
        print('You rebelled too hard and got hit by a flying slipper!\n GAME OVER ')
        sys.exit()
    elif check['FP'] < 0:
        print('Your parents are profoundly disappointed and dealt EMOTIONAL DAMAGE.\n GAME OVER ')
        sys.exit()
    elif check['PAS'] < 0:
        print('You became a neurosurgeon at 21, but lost your passion and now need therapy every week.\n GAME OVER ')
        sys.exit()

print('How the game works:\nYou have 4 stats:\n'
      '- FP is how good you are in your parents eyes\n'
      '- REB is your rebellion\n'
      '- SAN is your sanity\n'
      '- PAS is your passion\n'
      'Your goal is to not get kicked out of your house while keeping your passion!\n')

title = get_stats_string(stats) + 'Please choose your character class: '
options = ['The Firstborn', 'The Middle Child', 'The Youngest']

options, index = pick(options, title, indicator='=>', default_index=0)
print(f"You chose the path of {options}!\n")

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

title = get_stats_string(stats) + '\nInstrument Assignment:'
options = ['Choose piano', 'Choose violin', 'Beg to play football instead']

options, index = pick(options, title, indicator='=>', default_index=0)

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

title = get_stats_string(stats) + '\nYou got your first report card, you have an A-minus:'

options = [
    'Cry and accept the lecture over an A-minus',
    'Argue that the exam was unfairly scaled'
]

if stats['REB'] >= 15:
    options.append('Negotiate a do-over quiz')

options, index = pick(options, title, indicator='=>', default_index=0)

if options == 'Cry and accept the lecture over an A-minus':
    stats['FP'] += 10
    stats['SAN'] -= 10
    print("Effect Applied: +10 FP, -10 SAN\n")
elif options == 'Argue that the exam was unfairly scaled':
    stats['REB'] += 10
    stats['FP'] -= 5
    print("Effect Applied: +10 REB, -5 FP\n")
elif options == 'Negotiate a do-over quiz':
    stats['REB'] += 5
    stats['FP'] += 5
    stats['SAN'] -= 5
    print("Effect Applied: +5 REB, +5 FP, -5 SAN\n")

lose(stats)

title = get_stats_string(stats) + '\n you are on stage to perform :'

options = [
    'Play flawlessly from memory',
    'Freeze up on stage from nerves'
]

if stats['REB'] >= 25:
    options.append('Sabatoge on purpose (becouse you reblion is more then 25)')

options, index = pick(options, title, indicator='=>', default_index=0)

if options == 'Play flawlessly from memory':
    stats['FP'] += 15
    stats['SAN'] -= 10
    print("Effect Applied: +15 FP, -10 SAN\n")
elif options == 'Freeze up on stage from nerves':
    stats['REB'] += 5
    stats['FP'] -= 10
    stats['SAN'] -= 20
    print("Effect Applied: +5 REB, -10 FP, -15 SAN\n")
elif options == 'Sabatoge on purpose (becouse you reblion is more then 25)':
    stats['REB'] += 25
    stats['FP'] -= 20
    stats['PAS'] += 10
    print("Effect Applied: +25 REB, -20 FP, +10 passion\n")

lose(stats)

title = get_stats_string(stats) + '\nSleepover Request:'

opt_a = "Don't even ask (Self-censor)"
opt_b = "Ask directly and endure the interrogation"
opt_c = "Use a 'study-group' cover story"

options = [opt_a, opt_b]

if stats['PAS'] >= 30:
    options.append(opt_c)

options, index = pick(options, title, indicator='=>', default_index=0)

if options == opt_a:
    stats['FP'] += 5
    stats['PAS'] -= 10
    stats['SAN'] -= 5
    print("Effect Applied: +5 FP, -10 PAS, -5 SAN\n")
elif options == opt_b:
    stats['REB'] += 5
    stats['SAN'] -= 5
    print("Effect Applied: +5 REB, -5 SAN\n")
elif options == opt_c:
    stats['PAS'] += 10
    stats['FP'] -= 5
    sneaking = True  
    print("Effect Applied: +10 PAS, -5 FP (Sneaking mode activated! dont get investigated)\n")

lose(stats)

title = get_stats_string(stats) + '\n your mon wants to hijack your group project:'

opt_a = "let mon take over and make you the powerpoint"
opt_b = "push back and do it yourself"
opt_c = "call her out in front the teacher"
opt_d = "redirict using her own logic"

options = [opt_a, opt_b]

if stats['REB'] >= 40:
    options.append(opt_c)

if stats['PAS'] >= 50:
    options.append(opt_d)

options, project_index = pick(options, title, indicator='=>', default_index=0)

if options == opt_a:
    stats['FP'] += 10
    stats['SAN'] -= 10
    stats['PAS'] -= 10
    print("Effect Applied: +10 FP, -10 SAN, -10 PAS\n")
elif options == opt_b:
    stats['REB'] += 10
    stats['SAN'] -= 5
    stats['PAS'] += 5
    print("Effect Applied: +10 REB, -5 SAN, +5 PAS\n")
elif options == opt_c:
    stats['REB'] += 15
    stats['FP'] -= 10
    print("Effect Applied: +15 REB, -10 FP\n")
elif options == opt_d:
    stats['FP'] += 5
    stats['PAS'] += 10
    stats['SAN'] += 5
    print("Effect Applied: +5 FP, +10 PAS, +5 SAN\n")

lose(stats)

title = get_stats_string(stats) + '\n your mom took your devices'

opt_a = "acecpt this senlently"
opt_b = "argue about it"
opt_c = "hide a backup device"

options = [opt_a, opt_b]

if stats['REB'] >= 30 or stats['PAS'] >= 40:
    options.append(opt_c)

options, device_index = pick(options, title, indicator='=>', default_index=0)

if options == opt_a:
    stats['FP'] += 10
    stats['SAN'] -= 5
    print("Effect Applied: +10 FP, -5 SAN\n")
elif options == opt_b:
    stats['REB'] += 10
    stats['FP'] -= 10
    print("Effect Applied: +10 REB, -10 FP\n")
elif options == opt_c:
    stats['PAS'] += 5
    stats['REB'] += 5
    print("Effect Applied: +5 PAS, +5 REB\n")

lose(stats)

