from random import *


class protagonist:

    def __init__(self, perk):
        self.hp = 100
        self.dmgLight = 5
        self.dmgHeavy = 10
        self.cripple = 0
        self.fracture = 0
        self.bleed = 0
        self.isDead = False
        self.artery = 0
        self.i4s = 0
        self.meleeDefenseMulti = 1
        self.rangeDefenseMulti = 1
        self.meleeName = "Fists"
        # Perks give players bonuses
        if perk == 1:
            # Artillerist is good at range but bad at melee
            self.meleeDefenseMulti = 1.1
            self.rangeDefenseMulti = 1.1
        elif perk == 2:
            # Executioner is good at melee but bad at range
            self.meleeDefenseMulti = 0.9
            self.rangeDefenseMulti = 1.2
            self.dmgLight = 6
            self.dmgHeavy = 12

    def debuffProt(self, effectID):
        # Applies debuffs to the player
        if effectID == 1:
            self.bleed = 30
            print("You're bleeding...")
        elif effectID == 2:
            self.artery = 20
            print("Your arteries hurt...")
        elif effectID == 3:
            self.cripple = 45
            print("Your leg is broken. You can't roam far or flee.")
        elif effectID == 4:
            self.fracture = 45
            print("Your arm is broken. You can't use Shove.")
        elif effectID == 5:
            self.dmgLight = self.dmgLight + 1
            self.dmgHeavy = self.dmgHeavy + 2
            print("Honorable applied")
    
    def meleeReplace(self, lightDmg, heavyDmg, meleeName):
        # Replaces the player's melee weapon
        self.dmgLight = lightDmg
        self.dmgHeavy = heavyDmg
        self.meleeName = meleeName
        print(f"You've acquired a new melee weapon. It deals {lightDmg} light damage and {heavyDmg} heavy damage.")
    def meleeClear(self):
        # Resets melee weapon to fists
        self.dmgLight = 5
        self.dmgHeavy = 10
        self.meleeName = "Fists"
        print("You've returned to your fists.")
    def displayStats(self):
        # Displays the player's stats and debuffs
        print(f"Player - {player.hp}/100 HP")
        textBuffer = ""
        # Displays debuffs
        if self.fracture > 0:
            textBuffer = textBuffer + f"[FRACTURE {str(self.fracture)}]     "
        if self.cripple > 0:
            textBuffer = textBuffer + f"[CRIPPLE {str(self.cripple)}]     "
        if self.bleed > 0:
            textBuffer = textBuffer + f"[BLEED {str(self.bleed)}]      "
        if self.artery > 0:
            textBuffer = textBuffer + f"[ARTERY {str(self.artery)}]     "
        print(textBuffer)

    def damageProt(self, dmg):
        # Deals damage to the player
        self.hp = self.hp - dmg
        print(f"You took {str(dmg)} damage.")
        if self.hp <= 0:
            self.isDead = True

    def turn(self):
        # Handles debuffs
        if self.cripple > 0:
            self.cripple = self.cripple - 1
            if self.cripple == 0:
                print("Your leg healed.")
        if self.fracture > 0:
            self.fracture = self.fracture - 1
            if self.fractureEffect == 0:
                print("Your arm healed.")
        if self.bleed > 0:
            self.bleed = self.bleed - 1
            self.hp = self.hp - 1
            if self.bleed == 0:
                print("You're no longer bleeding.")
        if self.artery > 0:
            self.artery = self.artery - 1
            self.hp = self.hp - 2
            self.bleed = 5
            if self.artery == 0:
                print("Your artery healed. You still have a slight bleed.")
        if self.hp <= 0:
            self.isDead = True


class hostileHuman:

    def __init__(self, hp, light, heavy, shove, parry, ranged):
        # Initializes the hostile human with its stats
        self.hp = hp
        self.lightDamage = light
        self.heavyDamage = heavy
        self.shove = shove
        self.parry = parry
        self.ranged = ranged
        self.maxHp = hp
        self.parry = False
        self.resistmulti = 1

    def displayStats(self):
        # Displays the enemy's HP
        print(f"Enemy - HP {self.hp}/{self.maxHp}")

    def beginParry(self):
        # Sets the parry flag to True
        self.parry = True
        print("The enemy is parrying.")

    def takeShove(self):
        # Resets the parry flag and stuns the enemy
        self.parry = False
        self.stunned = True

    def takeDamage(self, amount):
        # Deals damage to the enemy, taking the parry flag into account
        if self.parry == False:
            self.hp = self.hp - round(amount * self.resistmulti)
            print(f"The enemy took {round(amount*self.resistmulti)} damage.")
        elif self.parry:
            print("Enemy blocked the attack ")
            self.parry = False


def battle(name, hp, lightDamage, heavyDamage, canShove, canParry, isRanged):
    enemy = hostileHuman(hp, lightDamage, heavyDamage, canShove, canParry,
                         isRanged)
    print(f"{name} blocks your way.")
    parry = False
    shove = False
    while enemy.hp > 0:
        player.displayStats()
        player.turn()
        turns = 4
        print(f"Your turn. Actions: {turns}")
        print("""Actions:
light - 1 turn simple attack
lightc - 3 turn L-L-L*1.5 combo rounded damage
heavy - inefficient, powerful, consumes 2 turns
shove - stun enemy to flee, ends turn
parry - ends turn, block attack chance to stun
flee - REQUIRES STUNNED ENEMY attempt to flee battle""")
        while turns > 0:
            action = input("Your move: ")
            # Player actions
            if action == "light":
                enemy.takeDamage(player.dmgLight)
                print(f"You hit the enemy with a {player.dmgLight} damage light attack.")
                turns = turns - 1
            elif action == "lightc":
                enemy.takeDamage(player.dmgLight)
                print(f"You hit the enemy with a {player.dmgLight} damage light attack.")
                enemy.takeDamage(player.dmgLight)
                print(f"You hit the enemy with a {player.dmgLight} damage light attack.")
                enemy.takeDamage(round(player.dmgLight * 1.5))
                print(f"You hit the enemy with a {round(player.dmgLight * 1.5)} damage light attack.")
                turns = turns - 3
            elif action == "heavy":
                enemy.takeDamage(player.dmgHeavy)
                print(f"You hit the enemy with a {player.dmgHeavy} damage heavy attack.")
                turns = turns - 2
            elif action == "parry":
                parry = True
                turns = 0
            elif action == "shove":
                shove = True
                turns = 0
            elif action == "flee":
                if enemy.hp > enemy.maxHp / 2 and not shove:
                    print("Enemy is too powerful, you can't flee.")
                else:
                    print("You flee, running away.")
                    return
            else:
                print("Invalid action.")
        # Enemy's turn
        turns = 3
        print(f"Enemy's turn: {turns}")
        if turns > 0:
            enemyAction = randint(1, 4)
            # Enemy actions
            if enemyAction == 1 and turns >= 1 and not shove:
                print("Enemy attacked with light attack")
                if parry:
                    print("You blocked the attack.")
                    enemy.takeShove()
                else:
                    player.damageProt(enemy.lightDamage)
                turns = turns - 1
            elif enemyAction == 2 and turns >= 2 and not shove:
                print("Enemy attacked with heavy attack")
                if parry:
                    print("You blocked the attack.")
                    enemy.takeShove()
                else:
                    player.damageProt(enemy.heavyDamage)
                turns = turns - 2
            elif enemyAction == 3 and canShove and turns >= 1 and not shove:
                print("Enemy shoved you")
                if parry:
                    print("You blocked the attack.")
                    enemy.takeShove()
                else:
                    player.damageProt(enemy.lightDamage)
                    player.debuffProt(3)
                turns = 0
            elif enemyAction == 4 and canParry and turns >= 1 and not shove:
                print("Enemy is parrying")
                enemy.beginParry()
                turns = 0
            elif enemyAction == 4 and canParry and turns >= 1 and shove and isRanged:
                print("You think you can parry a bullet?")
                turns = 0
        else:
            print("Enemy ended its turn.")
    print("You have defeated the enemy.")
    scrap = scrap + 5
    print(f"You gained 5 scrap, for a total of {scrap}.")
print("Welcome to Winter's End")
print("""Status effects:
FRACTURE disables shoves.
CRIPPLE disables Castle and Tower locations and fleeing.
BLEED slowly saps your HP.
and ARTERY BLEEDING saps it even faster.""")
input("Enter to continue.")
print("""Choose your perk.
1 - ARTILLERIST has better ranged performance but is weak at melee.
2 - EXECUTIONER has powerful melee performance but suffers from issues with ranged enemies.
Leave Blank - SURVIVALIST doesn't have any special quirk. The recommended beginner class."""
      )

perkChoice = input("Input perk ID: ")
if perkChoice == "":
    perkChoice = "3"
player = protagonist(int(perkChoice))
player.displayStats()
night = 1
scrap = 5
while not player.isDead:
    area = input("what area do you want to go to?")
    if area == "castle":
        if player.cripple:
            print("You can't go there.")
        else:
            battle("Hi-Capa Raider", 60, 3, 3, False, False, True)
            battle("Hi-Capa Raider", 60, 3, 3, False, False, True)
            battle("Fire Axe Raider", 60, 7, 25, True, True, False)
    elif area == "tower":
        if player.cripple:
            print("You can't go there.")
    elif area == "mountain":
        battle("Lead Pipe Scav", 50, 3, 5, False, False, False)
    elif area == "outpost":
        battle("Combat Knife Scav", 35, 4, 6, True, False, False)
    print("Storm's coming. Going back to the safe zone.")
    if night == 1:
        print("Night 1. The basic enemies.")
        battle("Combat Knife Scav", 35, 4, 6, True, False, False)
        battle("Combat Knife Scav", 35, 4, 6, True, False, False)
    elif night == 2:
        print("Night 2. They've upped their game a little.")
        battle("Combat Knife Scav", 35, 4, 6, True, False, False)
        battle("Combat Knife Scav", 35, 4, 6, True, False, False)
        battle("Cleaver Scav", 35, 4, 6, True, True, False)
        battle("Crowbar Scav", 100, 4, 6, True, False, False)
    elif night == 3:
        print("Night 3. Things are getting rough. Enemies are harder, and more of them.")
    
def battle(enemy, enemyHP, enemyDMGLight, enemyDMGHeavy, enemyShove, enemyRange, enemyAI):
    global scrap
    enemyHP = enemyHP - player.i4s
    if enemyHP <= 0:
        enemyHP = 0
        print(f"You killed the {enemy}!")
        scrap = scrap + 10
    else:
        print(f"You are fighting a {enemy} with {enemyHP} HP.")
        while player.isDead == False and enemyHP > 0:
            player.displayStats()
            choice = input("What will you do? Attack, Shove, Flee, or Ignore: ")
            if choice == "Attack":
                attackChoice = input("Light or Heavy Attack? ")
                if attackChoice == "Light":
                    if randint(1, 100) <= (player.dmgLight * 10):
                        enemyHP = enemyHP - player.dmgLight
                        print(f"You hit the {enemy} with a light attack! It now has {enemyHP} HP.")
                    else:
                        print(f"You missed the {enemy}.")
                elif attackChoice == "Heavy":
                    if randint(1, 100) <= (player.dmgHeavy * 10):
                        enemyHP = enemyHP - player.dmgHeavy
                        print(f"You hit the {enemy} with a heavy attack! It now has {enemyHP} HP.")
                    else:
                        print(f"You missed the {enemy}.")
                else:
                    print("Invalid choice. Try again.")
            elif choice == "Shove":
                if randint(1, 100) <= 50:
                    if enemyShove:
                        print("You shoved the enemy.")
                    else:
                        print(f"The {enemy} can't be shoved.")
                else:
                    print("You failed to shove the enemy.")
            elif choice == "Flee":
                if randint(1, 100) <= 50:
                    print("You fled from the enemy.")
                    break
                else:
                    print("You failed to flee from the enemy.")
            elif choice == "Ignore":
                print("You stand still and ignore the enemy.")
            else:
                print("Invalid choice. Try again.")

            if enemyAI:
                if enemyHP > 0:
                    enemyChoice = randint(1, 3)
                    if enemyChoice == 1:
                        if randint(1, 100) <= (enemyDMGLight * 10):
                            player.damageProt(enemyDMGLight)
                            print(f"The {enemy} hit you with a light attack!")
                        else:
                            print(f"The {enemy} missed you.")
                    elif enemyChoice == 2:
                        if randint(1, 100) <= (enemyDMGHeavy * 10):
                            player.damageProt(enemyDMGHeavy)
                            print(f"The {enemy} hit you with a heavy attack!")
                        else:
                            print(f"The {enemy} missed you.")
                    else:
                        print(f"The {enemy} ignores you.")
            else:
                if enemyHP > 0:
                    if randint(1, 100) <= (enemyDMGLight * 10):
                        player.damageProt(enemyDMGLight)
                        print(f"The {enemy} hit you with a light attack!")
                    else:
                        print(f"The {enemy} missed you.")
    if player.isDead == True:
        print("You died.")
        gameLoop = False
    elif enemyHP <= 0:
        print(f"You killed the {enemy}!")

def shop(player):
    global scrap
    while True:
        player.displayStats()
        shopChoice = input("What do you want to do? Buy, Exit: ")
        if shopChoice == "Buy":
            while True:
                print(f"You have {scrap} scrap. What do you want to buy?")
                print("""
                    1 - Heal 25 HP - 2 Scrap
                    2 - Heal 50 HP - 5 Scrap
                    3 - Heal 75 HP - 8 Scrap
                    4 - Heal to full - 10 Scrap
                    5 - Buy Fire Axe - 15 Scrap - Deals 10 Light Damage 20 Heavy Damage
                    6 - Buy Lead Pipe - 10 Scrap - Deals 7 Light Damage 14 Heavy Damage
                    7 - Clear Melee - Free 
                    """)
                buyChoice = input("What do you want to buy? (1-7, or exit to exit shop): ")
                if buyChoice == "1" and scrap >= 2:
                    player.hp = player.hp + 25
                    scrap = scrap - 2
                    print("You bought a small heal.")
                elif buyChoice == "2" and scrap >= 5:
                    player.hp = player.hp + 50
                    scrap = scrap - 5
                    print("You bought a medium heal.")
                elif buyChoice == "3" and scrap >= 8:
                    player.hp = player.hp + 75
                    scrap = scrap - 8
                    print("You bought a large heal.")
                elif buyChoice == "4" and scrap >= 10:
                    player.hp = 100
                    scrap = scrap - 10
                    print("You bought a full heal.")
                elif buyChoice == "5" and scrap >= 15:
                    player.meleeReplace(10, 20, "Fire Axe")
                    scrap = scrap - 15
                    print("You bought the Fire Axe.")
                elif buyChoice == "6" and scrap >= 10:
                    player.meleeReplace(7, 14, "Lead Pipe")
                    scrap = scrap - 10
                    print("You bought the Lead Pipe.")
                elif buyChoice == "7":
                    player.meleeClear()
                elif buyChoice == "exit":
                    break
                else:
                    print("Invalid choice or not enough scrap. Try again.")
        elif shopChoice == "Exit":
            break
        else:
            print("Invalid choice. Try again.")

night = 1
scrap = 0
player = protagonist(1)
gameLoop = True

while gameLoop:
    if night == 1:
        print("Night 1. The world has just fallen. Be careful.")
        battle("Cleaver Scav", 35, 4, 6, True, True, False)
        battle("Cleaver Scav", 35, 4, 6, True, True, False)
        battle("Crowbar Scav", 100, 4, 6, True, False, False)
        battle("Crowbar Scav", 100, 4, 6, True, False, False)
        battle("Combat Knife Scav", 35, 4, 6, True, False, False)
        battle("Combat Knife Scav", 35, 4, 6, True, False, False)
    elif night == 2:
        print("Night 2. Things are getting rough. Enemies are harder, and more of them.")
        battle("Cleaver Scav", 35, 4, 6, True, True, False)
        battle("Cleaver Scav", 35, 4, 6, True, True, False)
        battle("Crowbar Scav", 100, 4, 6, True, False, False)
        battle("Crowbar Scav", 100, 4, 6, True, False, False)
        battle("Combat Knife Scav", 35, 4, 6, True, False, False)
        battle("Combat Knife Scav", 35, 4, 6, True, False, False)
    elif night == 3:
        print("Night 3.")
        battle("Cleaver Scav", 35, 4, 6, True, True, False)
        battle("Cleaver Scav", 35, 4, 6, True, True, False)
        battle("Broomhandle Scav", 20, 3, 3, False, True, True)
        battle("Crowbar Scav", 100, 4, 6, True, False, False)
    elif night == 4:
        print("Night 4.")
        if randint(1, 100) == 1:
            print("The Bucketman has replaced all other enemies!")
            battle("The Bucketman", 500, 25, 50, True, True, False)
        else:
            print("Bucket Not Detected. Normalcy.")
            battle("Cleaver Scav", 35, 4, 6, True, True, False)
            battle("Cleaver Scav", 35, 4, 6, True, True, False)
            battle("Crowbar Scav", 100, 4, 6, True, False, False)
            battle("Crowbar Scav", 100, 4, 6, True, False, False)
            battle("Combat Knife Scav", 35, 4, 6, True, False, False)
            battle("Combat Knife Scav", 35, 4, 6, True, False, False)
    elif night == 5:
        print("Night 5. Things are getting even tougher. Brace yourself.")
        battle("AK Scav", 45, 5, 5, True, True, False)
        battle("Crowbar Scav", 100, 4, 6, True, False, False, "Gordon Freeman")
        battle("Broomhandle Scav", 20, 3, 3, False, True, True)
        battle("Broomhandle Scav", 20, 3, 3, False, True, True)
        battle("Cleaver Scav", 35, 4, 6, True, True, False)
        battle("Cleaver Scav", 35, 4, 6, True, True, False)
    print("Night is over, the shop is open. You have a chance to spend your scrap.")
    shop(player)
