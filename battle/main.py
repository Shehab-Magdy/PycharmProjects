from classes.game import Person, bcolor
from classes.magic import Spell
from classes.inventory import Item

# Create black magic
fire = Spell('Fire', 10, 100, 'black')
thunder = Spell('Thunder', 10, 100, 'black')
blizzard = Spell('Blizzard', 10, 100, 'black')
meteor = Spell('Meteor', 20, 200, 'black')
quake = Spell('Quake', 14, 140, 'black')

# Create white magic
cure = Spell('Cure', 12, 120, 'white')
cura = Spell('Cura', 18, 200, 'white')

# Create some Items.
potion = Item('Potion', 'potion', 'Heals 50 HP', 50)
hipotion = Item('Hi-Potion', 'potion', 'Heals 100 HP', 100)
supperpotion = Item('Supper Potion', 'potion', 'Heals 500 HP', 500)
elixer = Item('Elixer', 'elixer', 'Fully restore HP/MP of one party member', 999)
hielixer = Item('Mega Elixer', 'elixer', 'Fully restores partie\'s HP/MP ', 999)

grenade = Item('Grenade', 'atack', 'deals 500 damage', 500)

player_spells = [fire, thunder, blizzard, meteor, cura, cure]
player_items = [potion, hipotion, supperpotion, elixer, hipotion, grenade]

# Instantiate people
player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

running = True
i = 0
print(bcolor.FAIL + bcolor.BOLD + 'AN ENEMY ATTACKS!' + bcolor.ENDC)
while running:
    print('===========================')
    player.choose_action()
    choise = input('Choose Action: ')
    index = int(choise) - 1
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_dmg(dmg)
        print('You attacked for', dmg)

    elif index == 1:
        player.choose_magic()
        magic_choise = int(input('Choose Magic:')) - 1

        if magic_choise == -1:
            continue

        spell = player.magic[magic_choise]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()
        if spell.cost > current_mp:
            print(bcolor.FAIL + '\nYou have not enough MP\n' + bcolor.ENDC)
            continue
        player.reduce_mp(spell.cost)

        if spell.type == 'white':
            player.heal(magic_dmg)
            print(bcolor.OKBLUE, '\n' + spell.name + ' heals for', str(magic_dmg), 'HP', bcolor.ENDC)
        elif spell.type == 'black':
            enemy.take_dmg(magic_dmg)
            print(bcolor.OKBLUE + '\n' + spell.name + ' deals', str(magic_dmg), 'points of damage' + bcolor.ENDC)
    elif index == 2:
        player.choose_item()
        item_choise = int(input('Choose Item:')) - 1

        if item_choise == -1:
            continue
        item = player.items[item_choise]
        if item.type == 'potion':
            player.heal(item.prop)
            print(bcolor.OKGREEN+'\n'+item.name+' Heals for '+str(item.prop)+' hp'+bcolor.ENDC)

    enemychoise = 1
    enemy_dmg = enemy.generate_damage()
    player.take_dmg(enemy_dmg)
    print('Enemy attacked for', enemy_dmg)

    print('--------------------------')
    print('Enemy HP:', bcolor.FAIL + str(enemy.get_hp()) + '/' + str(enemy.get_maxhp()) + bcolor.ENDC + '\n')
    print('Your HP:', bcolor.OKGREEN + str(player.get_hp()) + '/' + str(player.get_maxhp()) + bcolor.ENDC)
    print('Your MP:', bcolor.OKBLUE + str(player.get_mp()) + '/' + str(player.get_maxmp()) + bcolor.ENDC + '\n')

    if enemy.get_hp() == 0:
        print(bcolor.OKGREEN + 'You win!' + bcolor.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolor.FAIL + 'Enemy has defeated you!' + bcolor.ENDC)
        running = False
