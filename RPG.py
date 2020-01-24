################################################################
### Note (General)
    # Theme!: Vampires (Zkyn) / Vampire Hunters (Koon)!

    # Battles
        # Not sure I'm using the randint function correctly.
        # Help and Stats commands dont work in battles (not in IFloop?)
        # Some how Mr. Lumbergh is healing during battles ?!?! so lost

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

    # Stats and Help inputs
        # Before choosing a faction, if you input Help or Stats
            #it will should you the relitive info then restart
            #the game

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
faction_vamp = False
faction_vamphunt = False

# Defines
def calc_player_attack():
    return randint(player['atk_min'], player['atk_max'])

def calc_mrlumbergh_attack():
        return randint(mr_lumbergh['attack_min'], mr_lumbergh['attack_max'])

# Game Path

while game_running == True:
    new_game = True
    # just setting things up, may not be implemented right away
    enemies_defeated = 0
    times_attacked = 0
    times_healed = 0
    times_hit_by_atk = 0

    player = {'name': 'player', 'atk_min': 15, 'atk_max': 25, 'heal': 20, 'health': 100}

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
        print('One looks like a dead bat".')
        print('The other seems like a "crossbow?".')
        print('***   ***' * 3)
        print('Which do you choose to inspect?')
        print('Type "Bat" to reach for the bat, or "Crossbow" to grab for the crossbow.')
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
        # Vampire Story:
        elif player_input == 'Bat':
            faction_vamp = True
            mrlumbergh_fight = True

            print('You reach for the bat and it jumps at you!')
            print('It bites you right in the face!')
            print('You start to feel cold, weak and ache all over.')
            print('Your vision slowly starts to fade as you begin to black out.')
            print('...')
            print('You awaken, and to no surprise, not a single person noticed a damn thing.')
            print('Still in the office but something seems different.')
            print('Maybe the crazy bat thing was just a dream?')
            print('The crossbow is gone.... but now you can hear the heart beats of everyone on the office floor.')
            print('The boss walks by and tells you to get back to work!')
            print("His pulse is so loud you can't control your self!")
            print('You lunge to attack your boss Mr.Lumbergh!')
            while mrlumbergh_fight == True:
                player_won = False
                mr_lumbergh_won = False
                mr_lumbergh = {'name': 'Mr.Lumbergh', 'attack_min': 10, 'attack_max': 20, 'health': 100}
                print('---' * 10)
                print('Please select an action')
                print('1) Attack')
                print('2) Heal')
                print('3) Exit Game')
                print('4) Leader Board')
                print('---' * 10)
                player_choice = input()
                if player_choice == '1':
                    mr_lumbergh['health'] = mr_lumbergh['health'] - calc_player_attack()
                    print('---' * 10)
                    print(player['name'] + ' has Attack!')
                    print(mr_lumbergh['name'] + ' Attacks!')
                    print(player['name'] + ' Has ' + str(player['health']) + ' Health!')
                    print(mr_lumbergh['name'] + ' Has ' + str(mr_lumbergh['health']) + ' Health!')
                    if mr_lumbergh['health'] <= 0:
                        player_won = True
                    else:
                        player['health'] = player['health'] - calc_mrlumbergh_attack()
                        if player['health'] <= 0:
                            monster_won = True
                elif player_choice == '2':
                        player['health'] = player['health'] + player['heal']
                        player['health'] = player['health'] - calc_mrlumbergh_attack()
                        print('---' * 10)
                        print(player['name'] + ' Casts heal on self!')
                        print(mr_lumbergh['name'] + ' Attacks!')
                        print(player['name'] + ' Has ' + str(player['health']) + ' Health!')
                        print(mr_lumbergh['name'] + ' Has ' + str(mr_lumbergh['health']) + ' Health!')
                        if player['health'] <= 0:
                            monster_won = True
                elif player_choice == '3':
                        print('Exiting Game, Thanks for playing')
                        new_round = False
                        game_running = False
                else:
                        print('Invalid Input')
                if player_won == False and mr_lumbergh == False:
                        print(player['name'] + ' Has ' + str(player['health']) + ' Health')
                        print(mr_lumbergh['hame'] + ' Has ' + str(mr_lumbergh['health']) + ' Health')
                elif player_won:
                    print('***' * 10)
                    print(mr_lumbergh['name'] + ' has been Defeted! ' + player['name'] + ' Has Won!')
                    print('***' * 10)
                elif mr_lumbergh_won:
                    print('***' * 10)
                    print(player['name'] + ' has been Defeted! ' + mr_lumbergh['Name'] + ' Has Won!')
                    print('You Lose')
                    print('***' * 10)
                if player_won == True or mr_lumbergh_won == True:
                    new_round = False

            # test code start
            print('faction_vamp = ' + str(faction_a))
            print('faction_vamphunt = ' + str(faction_b))
            #test code end

        # Vampire Hunter Story:
        elif player_input == 'Crossbow':
            faction_vamphunt = True

            #test code start
            print('faction_vamp = ' + str(faction_a))
            print('faction_vamphunt = ' + str(faction_b))
            # test code end

