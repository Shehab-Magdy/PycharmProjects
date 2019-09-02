from classes.game import Person, bcolor

magic = [{'name': 'Fire', 'cost': 10, 'dmg': 60},
         {'name': 'Thunder', 'cost': 12, 'dmg': 80},
         {'name': 'Blizzard', 'cost': 10, 'dmg': 60}, ]
player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0
print(bcolor.FAIL+bcolor.BOLD+'AN ENEMY ATTACKS!'+bcolor.ENDC)
while running:
    print('===========================')
    player.choose_action()
    choise = input('Choose Action: ')
    index = int(choise) -1
    if index==0:
        dmg = player.generate_damage()
        enemy.take_dmg(dmg)
        print('You attacked for',dmg)

    elif index == 1:
        player.choose_magic()
        magic_choise=int(input('Choose Magic:')) -1
        magic_dmg = player.generate_spell_damage(magic_choise)
        spell=player.get_spell_name(magic_choise)
        cost=player.get_spell_mp_cost(magic_choise)
        current_mp=player.get_mp()
        if current_mp<cost:
            print(bcolor.FAIL+'\nYou have not enough MP\n'+bcolor.ENDC)
            continue
        player.reduce_mp(cost)
        enemy.take_dmg(magic_dmg)
        print(bcolor.OKBLUE+'\n'+spell+'deals',str(magic_dmg),'points of damage' + bcolor.ENDC)

    enemychoise = 1
    enemy_dmg=enemy.generate_damage()
    player.take_dmg(enemy_dmg)
    print('Enemy attacked for',enemy_dmg)

    print('--------------------------')
    print('Enemy HP:', bcolor.FAIL + str(enemy.get_hp())+'/'+str(enemy.get_maxhp()+bcolor.ENDC)+'\n')
    print('Your HP:', bcolor.OKGREEN + str(player.get_hp())+'/'+str(player.get_maxhp()+bcolor.ENDC))
    print('Your MP:', bcolor.OKBLUE + str(player.get_mp()) + '/' + str(player.get_maxmp()) + bcolor.ENDC + '\n')

    if enemy.get_hp()==0:
        print(bcolor.OKGREEN + 'You win!'+ bcolor.ENDC)
        running=False
    elif player.get_hp()==0:
        print(bcolor.FAIL+'Enemy has defeated you!'+bcolor.ENDC)
        running=False