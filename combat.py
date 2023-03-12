from Player import Player
from Monster import Monster
from roll import roll_dice
from Save import Save 
import time

 

def combat(playerCard:Player, monster:Monster):
    while playerCard.hp > 0 and monster.hp > 0:
        die = roll_dice()
        # print(f'Die Value: {die}')
        time.sleep(1)
        dmg = playerCard.atk + die - monster.blkpwr
        monster.healthUpdate(dmg=dmg)
        if dmg <= 0:
            print("You missed!")
        elif dmg > 0 and monster.hp > 0:
            print(f'Player Hit for: {dmg}. {monster.name} health at {monster.hp}')
        if monster.hp <= 0:
            monster.hp = 0
            print(f'Player Hit for: {dmg}. {monster.name} health at {monster.hp}')
            print(f'Congratulations! You have defeated {monster.name}')
            playerCard.set_status('victory')
            Save('save.db').set_option_monster(monster)
            Save('save.db').set_option_player(playerCard)
            print('Heading back home')
            playerCard.addEXP(monster)
            input("Press enter to continue....")
            break
        time.sleep(1)
        die = roll_dice()
        # print(f'Die Value: {die}')
        time.sleep(1)
        dmg = monster.atk + die - playerCard.blkpwr
        playerCard.healthUpdate(dmg=dmg, heal=0)
        if dmg <= 0:
            print(f"{monster.name} missed!")
        elif dmg > 0 and playerCard.hp > 0:
            print(f'{monster.name} Hit for: {dmg}. Player health at {playerCard.hp}')
        if playerCard.hp <= 0:
            playerCard.hp = 0
            print(f'{monster.name} Hit for: {dmg}. Player health at {playerCard.hp}')
            time.sleep(1)
            playerCard.set_status('defeat')
            print(f'The mighty {playerCard.name} has been defeated by {monster.name}. Taking your character to the Hospital')
            Save('save.db').set_option_monster(monster)
            Save('save.db').set_option_player(playerCard)
            input('Press enter to continue....')

        