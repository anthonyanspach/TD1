################################################################
### Note (General)
    # Themes for factions:
        # Humans / Zombies
        # Warewolf / Vampire
        # Samurai / Assassin
        # Knights / Wizards
        # Time Cops / Time Theives
        # Jedi / Sith
        # 

    # Stats to track:
        # Enemies Defeated?
        # Times Attacked?
        # Times Healed by 'X' (heal spell, item, ect..)
        # Times hit by an atk
        #

    # Equipment Ideas (based off theme and factions):
        # Items that increase atk min, atk max, health, healing amount
        # Teired? or just like 1 item for each stat to fine along the way?
        #

## Zkyn's Notes
    # Player Equipment, also whats equiped and held
    # Player Stats, stats tracked ???? (eventually?)
    # Multi story paths / endings, one major choice between
        # two factions, Multi paths / endings in each faction
    # Battles
    # Help: controls / key bindings
    # Exp / Leveling ???? (eventually?)

## Koon's Notes

###############################################################

# Imports
from random import randint


# Hard Variables
game_running = True
game_results = []
faction_a = False
faction_b = False

# Defines
def calc_player_attack():
    return randint(player['atk_min'], player['atk_max'])

# Game Path

while game_running == True:
    new_game = True
    # just setting things up, may not be implemented right away
    enemies_defeated = 0
    times_attacked = 0
    times_healed = 0
    times_hit_by_atk = 0

    player = {'name': 'player', 'atk_min': 10, 'atk_max': 20, 'heal': 15, 'health': 100}

    while new_game == True:
        print('||***||' * 1)
        print('||***||' * 2)
        print('||***||' * 3)
        print('||***||' * 4)
        print('||***||' * 5)
        print('||***||' * 6)
        print('||***||' * 7)
        print('||***||' * 8)
        print('||***||' * 9)
        print('||***||' * 10)

        print('NEW GAME! welcome intro stuffz here.')
        print('***   ***' * 3)
        print('Enter Player Name!:')
        player['name'] = input()

        print('||***||' * 1)
        print('||***||' * 2)
        print('||***||' * 3)
        print('||***||' * 4)
        print('||***||' * 5)
        print('||***||' * 4)
        print('||***||' * 3)
        print('||***||' * 2)
        print('||***||' * 1)

        print('Hello ' + str(player['name']) + ', Type "Help" for a list of other helpful commands and options. Lets begin!')

        # Story Intro
        print('ZZZ...')
        print("You wake up suddenly at your office qubical.")
        print('As usual, absolutly no one noticed you had passed the fuck out again...')
        print("You see two objects sitting on your deck that you've never seen before.")
        print('One is a "A".')
        print('The other is a "B".')
        print('***   ***' * 3)
        print('Which do you choose to inspect?')
        print('Type "A" for "A", or "B"  for "B".')
        player_input = input()

        # if player inputs Help or Stats the game restarts currently.
        # need to find a way to just display with out restart
        if player_input == 'Help':
            print('To See player current stats type "Stats"')

        elif player_input == 'Stats':
            print('Player Name: ' + str(player['name']))
            print('Health: ' + str(player['health']))
            print('Attack Min: ' + str(player['atk_min']))
            print('Attack Max: ' + str(player['atk_max']))
            print('Heal Power: ' + str(player['heal']))

        ## Where independant faction stories begin
        # Faction A story:
        elif player_input == 'A':
            faction_a = True
            
            print('You reach for "A" and it jumps at you!')
            print()

            # test code start
            print('faction_a = ' + str(faction_a))
            print('faction_b = ' + str(faction_b))
            #test code end

        # Faction B story:
        elif player_input == 'B':
            faction_b = True

            #test code start
            print('faction_a = ' + str(faction_a))
            print('faction_b = ' + str(faction_b))
            # test code end

