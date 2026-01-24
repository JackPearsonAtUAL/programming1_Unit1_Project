"""
Year 1 Programming 1 Final Project
Script for player 2
Jack Pearson
"""
#region Variables
# Imports all scripts and modules used for the game
#import character_script as CS
import random
import time
import os

class Barbarian:
    """
    Barbarian character type
    """
    name = "Barbarian"
    dmgT = 0 # Int denotes that this character dels attack based damage

    #region Stats
    # Life statss
    max_hp = 250 # maximum health value
    current_hp = max_hp # stores current hp value
    dead = False

    # Offensive stats
    base_attack = 7 # non-magic damage variable
    current_attk = base_attack # non-magic damage variable after buffs+debuffs
    base_psych = 1 # magic damage variable
    current_psy = base_psych # non-magic damage variable after buffs+debuffs

    # Defensive stats
    base_defence = 8 # non-magic damage reduction variable 
    current_def = base_defence # non-magic damage reduction variable after buffs+debuffs
    if current_def < 0: # stops the player's defecnce going below 0
        current_def = 0
    base_fortification = 4 # magic damage reduction variable 
    current_fort = base_fortification # non-magic damage reduction variable after buffs+debuffs
    if current_fort < 0: # stops the player's fortification going below 0
        current_def = 0

    # Resource stats
    max_mana =  20
    mana = max_mana # resource for magic skills
    rest_value = 5 # How much mana and stamina are restored during a rest

    # Status stats
    res = 0 # multiplied by 10 gives percentile chance to resist a debuff
    stat_modifs = [0, 0, 0, 0, 0]
    #endregion

    #region Skills
    def Whack(cost):
        global mana
        Barbarian.mana -= cost
        skillDMG = 5 * (1 + (Barbarian.current_attk / 10)) 
        
        return int(skillDMG)

    def FuriousBlow(cost):
        global mana, current_hp
        Barbarian.mana -= cost
        skillCost = 10
        if Barbarian.current_hp - skillCost > 0:
            Barbarian.current_hp -= skillCost
            skillDMG = 20 * (1 + (Barbarian.current_attk / 10))
        else:
            skillDMG = 10 * (1 + (Barbarian.current_attk / 10))
        
        return int(skillDMG)  

    def GreaterRestore(cost):
        global mana
        Barbarian.mana -= cost
        Barbarian.GainHealth(100)

    def Rage(cost):
        global mana, current_hp
        Barbarian.mana -= cost
        skillCost = 50
        if Barbarian.current_hp - skillCost > 0:
            Barbarian.current_hp -= skillCost
            Barbarian.current_attk += 10
            skillDMG = 20 * (1 + (Barbarian.current_attk / 10))
        else:
            Barbarian.current_attk += 10
            skillDMG = 0

        return int(skillDMG)
        
    def Rest(cost):
        global mana
        Barbarian.GainHealth(50)
        Barbarian.mana += Barbarian.rest_value
        if mana > Barbarian.max_mana: # stops mana overflow
            mana = Barbarian.max_mana
        print("The",Barbarian.name+"'s mana is now at",Barbarian.mana)


    skills = [Whack, FuriousBlow, GreaterRestore, Rage, Rest]
    skillCosts = [1, 5, 10, 15, 0]
    skillsDescription = ["[0] "+skills[0].__name__+": consumes 1 mana to deal a small amount of damage to one enemy.",
                        "[1] "+skills[1].__name__+": consumes 5 mana to deal damage to an enemy. If current health is greater then 10, it will consume 10HP and do double damage.",
                        "[2] "+skills[2].__name__+": consumes 10 mana and heals self for 100HP.",
                        "[3] "+skills[3].__name__+": consumes 15 and increases damage delt. If health is above 50 when cast, it will aditionally deal damage.",
                        "[4] "+skills[4].__name__+": heals character for 50HP and restores "+str(rest_value)+" mana."]
    #endregion

    #region Health Functions
    def CheckHealth():        
        if Barbarian.current_hp < 0:
            Barbarian.current_hp = 0        
            Barbarian.dead = True
            print("The",Barbarian.name+"'s health is", Barbarian.current_hp,"and is dead")
        elif Barbarian.current_hp > Barbarian.max_hp:
            Barbarian.current_hp = Barbarian.max_hp
        else:
            print("The",Barbarian.name+"'s health is", Barbarian.current_hp)

    def TakeDamage(self, type, amount):
        if Barbarian.dead:
            Barbarian.CheckHealth()
            return
        
        if type == 0: # Attack based damage
            damage = float(amount) * (1 - Barbarian.current_def/10)
            Barbarian.current_hp -= damage
            print("The",Barbarian.name,"has taken",damage,"damage")   

        elif type == 1: # Pyschic type damage
            damage = float(amount) * (1 - Barbarian.current_fort/10)
            Barbarian.current_hp -= damage
            print("The",Barbarian.name,"has taken",damage,"damage")   

        else:
            Barbarian.current_hp -= amount
            print("The",Barbarian.name,"has taken",amount,"damage")   
        Barbarian.CheckHealth()

    def GainHealth(amount):
        if Barbarian.dead:
            print("The",Barbarian.name,"is dead; they cannot be healed.")
            return
        Barbarian.current_hp += amount
        Barbarian.CheckHealth()
        print("The",Barbarian.name,"was healed for:",amount,"HP and is now at",Barbarian.current_hp,"HP")
        if Barbarian.current_hp > Barbarian.max_hp:
            Barbarian.current_hp = Barbarian.max_hp
    #endregion

class Mage:
    """
    Mage character type
    """
    name = "Mage"
    dmgT = 1 # Int denotes that this character dels pyschic based damage


    # Life stats
    max_hp = 150 # maximum health value
    current_hp = max_hp # stores current hp value
    dead = False

    # Offensive stats
    base_attack = 2 # non-magic damage variable
    current_attk = base_attack # non-magic damage variable after buffs+debuffs
    base_psych = 8 # magic damage variable
    current_psy = base_psych # non-magic damage variable after buffs+debuffs

    # Defensive stats
    base_defence = 2 # non-magic damage reduction variable 
    current_def = base_defence # non-magic damage reduction variable after buffs+debuffs
    if current_def < 0: # stops the player's defecnce going below 0
        current_def = 0
    base_fortification = 8 # magic damage reduction variable 
    current_fort = base_fortification # non-magic damage reduction variable after buffs+debuffs
    if current_fort < 0: # stops the player's fortification going below 0
        current_def = 0

    # Resource stats
    max_mana = 25
    mana = max_mana # resource for magic skills
    rest_value = 5 # How much mana and stamina are restored during a rest

    # Status stats
    res = 0 # multiplied by 10 gives percentile chance to resist a debuff
    stat_modifs = [0, 0, 0, 0, 0]

    hasArcaneShield = False

    #region Skills
    def Spark(cost):
        Mage.mana -= cost
        skillDMG = 5 * (1 + (Mage.current_psy/ 10)) 
        return int(skillDMG)

    def MagicMissile(cost):
        Mage.mana -= cost
        skillDMG = 15 * (1 + (Mage.current_psy/ 10))
        return int(skillDMG)   

    def ArcaneShield(cost):
        Mage.mana -= cost
        Mage.GainHealth(75)
        Mage.urrent_fort += 5
        Mage.current_def += 5

    def Storm(cost):
        Mage.mana -= cost
        Mage.current_psy += 5
        skillDMG = 25 * (1 + (Mage.current_psy/ 10)) 
        return int(skillDMG)

    def Rest(cost):
        Mage.GainHealth(50)
        Mage.mana += Mage.rest_value
        if Mage.mana > Mage.max_mana: # stops mana overflow
            Mage.mana = Mage.max_mana
        print("The",Mage.name+"'s mana is now at",Mage.mana)


    skills = [Spark, MagicMissile, ArcaneShield, Storm, Rest]
    skillCosts = [1, 5, 10, 15, 0]
    skillsDescription = ["[0] "+skills[0].__name__+": consumes 1 mana to deal a small amount of damage to one enemy.",
                        "[1] "+skills[1].__name__+": consumes 5 mana to deal damage to an enemy",
                        "[2] "+skills[2].__name__+": consumes 10 mana and lowers self's incoming damage",
                        "[3] "+skills[3].__name__+": consumes 15 and deals very high damage",
                        "[4] "+skills[4].__name__+": heals character for 50HP and restores "+str(rest_value)+" mana."]

    #endregion

    #region Health Functions
    def CheckHealth():        
        if Mage.current_hp < 0:
            Mage.current_hp = 0        
            Mage.dead = True
            print("The",Mage.name+"'s health is", Mage.current_hp,"and is dead")
        elif Mage.current_hp > Mage.max_hp:
            Mage.current_hp = Mage.max_hp
        else:
            print("The",Mage.name+"'s health is", Mage.current_hp)

    def TakeDamage(self, type, amount):
        if Mage.dead:
            Mage.CheckHealth()
            return
        
        if type == 0: # Attack based damage
            damage = float(amount) * (1 - Mage.current_def/10)
            Mage.current_hp -= damage
            print("The",Mage.name,"has taken",damage,"damage")   

        elif type == 1: # Pyschic type damage
            damage = float(amount) * (1 - Mage.current_fort/10)
            Mage.current_hp -= damage
            print("The",Mage.ame,"has taken",damage,"damage")   

        else:
            Mage.current_hp -= amount
            print("The",Mage.name,"has taken",amount,"damage")   
        Mage.CheckHealth()

    def GainHealth(amount):
        if Mage.dead:
            print("The",Mage.name,"is dead; they cannot be healed.")
            return
        Mage.current_hp += amount
        Mage.CheckHealth()
        print("The",Mage.name,"was healed for:",amount,"HP and is now at",Mage.current_hp,"HP")
        if Mage.current_hp > Mage.max_hp:
            Mage.current_hp = Mage.max_hp
    #endregion

# Player 1's data
class Player_1:
    team = [Mage(), Barbarian()]

Barbarian.name = "barbie"

# Player 2's data
class Player_2:
    team = [Barbarian(), Mage()]
#endregion



#region Team Building
# Boolean function to check if a given player team is valid
def CheckValidTeam(team):
    # Cycles through the given player's team
    for m in range(len(team)):
        # When a part of the player's team is empty return a False value
        if team[m] == "Empty":
            print("Current team is not valid")
            return False
    # Is returned when the player has a fully valid team
    print("Current team is valid")
    return True

def MakeTeam(player):
    # Begin loop to check if party is confirmed and valid
    validTeam = False
    while validTeam == False:
        # print the current party
        print(player.__name__, "current party:")
        #print 1st party member
        if player.team[0] == "Empty":
            print("[0]: Empty")
        else:
            print("[0]:", player.team[0].name)
        time.sleep(1)
       # Print 2nd party member
        if player.team[1] == "Empty":
            print("[1]: Empty")
        else:
            print("[1]:", player.team[1].name)
        time.sleep(1)

        # ask player for team position
        teamPos = input("Please enter the team position you would like to edit by either entering 0 or 1: ")
        time.sleep(1)
        # Check for valid input
        notValid = True
        while notValid:
            # check if position is a number     
            if teamPos.isdigit() == True and 0 <= int(teamPos) <= 1:
                # Casts string into integer
                teamPos = int(teamPos)
                notValid = False       
            # else ask again
            else:
                teamPos = input("Please try a valid input: ")
                time.sleep(1)

        # ask player for charaacter type
        #characterOptions = [CS.Barbarian(), CS.Mage()]
        notValid = True
        while notValid:
            # get input
            choice = input("Please input [0] for Barbarian or [1] for Mage: ")
            time.sleep(1)
            c0 = "Empty"
            c1 = "Empty"
            # check if valid input
            if choice.isdigit() == True and 0 == int(choice):
                choice = int(choice)
                notValid = False
                c0 = Barbarian()
                player.team[teamPos] = c0
            elif choice.isdigit() == True and 1 == int(choice):
                notValid = False
                c1 = Mage()
                player.team[teamPos] = c1
                     

        # check with player if they want to make changes
        repeat = input("Do you wish to finalise team building? y or n: ")
        time.sleep(1)
        if repeat.lower() == "y":
            validTeam = CheckValidTeam(player.team)
#endregion

#region Player Turn Logic
def PlayerAttack(playerObj, opponentObj):
    loop = True # Used to keep prompting inputs until skill usage is confirmed
    while loop:   
        # Tells player the current team
        print(playerObj.__name__, "options are: [0]", playerObj.team[0].name, "and [1]", playerObj.team[1].name)

        # Prompts input to select one of their characters using the character's team number
        character = input("Please select one of the above characters by inputting their position number ")

        #-----------------------------------------------------------------------------------------------
        # Loop to check if the character exists/can be used
        #-----------------------------------------------------------------------------------------------
        e = True
        while e:
            #Check if input is a number
            if character.isdigit() == True:
                # Casts string into integer
                character = int(character)
                e = False
            
            # Checks if inputted number is valid
            if character != 0 and character != 1:
                character = input("Invalid input, please try inputting a different position ")
            # Checks wheether or not the character is alive
            elif playerObj.team[character].dead == True: 
                character = input("Character has perished, please try inputting a different position ")
            # Character number is valid and attached character is alive
            else:
                e = False
                print(playerObj.team[character].name, "has been selected")

        #-----------------------------------------------------------------------------------------------   
        # Selecting a skill
        #-----------------------------------------------------------------------------------------------
        print("skill options are: [0]", playerObj.team[character].skills[0].__name__, "[1]", playerObj.team[character].skills[1].__name__, 
                "[2]", playerObj.team[character].skills[2].__name__, "[3]", playerObj.team[character].skills[3].__name__, 
                "[4]", playerObj.team[character].skills[4].__name__)
        skill = input("Please select one of your skills by inputting it's number ")
        e = True
        while e:
            if skill.isdigit() == True:
                # Casts string into integer
                skill = int(skill)
                e = False
            
            if 0 <= skill <= 4:
                # Add check for mana/stamina cost
                # If it costs more than the character has the player will have to pick a different skill
                if playerObj.team[character].skillCosts[skill] > playerObj.team[character].mana:
                    skill = input("Please try inputting a different skill ")
                else:
                    e = False
            else:
                print(playerObj.team[character].skills[skill].__name__, "has been selected")
                e = False 

        #-----------------------------------------------------------------------------------------------
        # Condition to make sure it isn't a self target skill
        #-----------------------------------------------------------------------------------------------        
        if playerObj.team[character].skills[skill].__name__ != "GreaterRestore" and playerObj.team[character].skills[skill].__name__ != "ArcaneShield":
            # select one of the enemy characters using the character's team number
            print(playerObj.__name__, "options are: [0]", opponentObj.team[0].name, "and [1]", opponentObj.team[1].name)
            target = input("Please select one of the above target by inputting their position number ") # Stores the targeted chracter's position
            e = True
            while e:
                #Check if input is a number
                if target.isdigit() == True:
                    # Casts string into integer
                    target = int(target)
                    e = False
                else:
                    target = input("Not a valid input, please try again: ")
                
                # Checks if target int is valid
                if target != 0 and target != 1:
                    target = input("Invalid target, please try inputting a different position ")
                # Checks target is alive
                elif opponentObj.team[target].dead == True: 
                    target = input("Target has perished, please try inputting a different position ")
                else:
                    e = False
                    print("Enemy's", opponentObj.team[target].name, "has been selected")
        
            # Cofirmation for turn action          
            print("Current action is:", playerObj.team[character].name, "is targeting", opponentObj.team[target].name, 
                "with:", playerObj.team[character].skills[int(skill)].__name__)
            
            confirm = input("To confirm action please type: y . To cancel, type: n . Any other input will return you to the action menu")
            if confirm.lower() == "y":
                # Attacking skills target by using this formula:
                # Target.TakeDamage(currentPlayer[character].skills[skill]
                print(str(playerObj.team[character].dmgT), str(playerObj.team[character].skills[skill](playerObj.team[character].skillCosts[skill])))
                opponentObj.team[target].TakeDamage(int(playerObj.team[character].dmgT), int(playerObj.team[character].skills[skill](playerObj.team[character].skillCosts[skill])))
                loop = False
            elif confirm.lower() == "n":
                print("Re-write action selected.")
            else:
                print("Returning to options menu.")
                loop = False
        else:
            print("Current action is:", playerObj.team[character].name, "is targeting themself with:", playerObj.team[character].skills[skill].__name__)
            confirm = input("To confirm action please type: y . To cancel, type: n . Any other input will return you to the action menu")
            if confirm.lower() == "y":
                playerObj.team[character].skills[skill]
                loop = False
            elif confirm.lower() == "n":
                print("Re-write action selected.")
            else:
                print("Returning to options menu.")
                loop = False
    print("Player 1:\n", Player_1.team[0].name, "HP =", Player_1.team[0].current_hp, "/", Player_1.team[0].max_hp,"Mana =", Player_1.team[0].mana, "/", Player_1.team[0].max_mana,
            "\n", Player_1.team[1].name, "HP =", Player_1.team[1].current_hp, "/", Player_1.team[1].max_hp,"Mana =", Player_1.team[1].mana, "/", Player_1.team[1].max_mana)
    print("Player 2:\n", Player_2.team[0].name, "HP =", Player_2.team[0].current_hp, "/", Player_2.team[0].max_hp,"Mana =", Player_2.team[0].mana, "/", Player_2.team[0].max_mana,
            "\n", Player_2.team[1].name, "HP =", Player_2.team[1].current_hp, "/", Player_2.team[1].max_hp,"Mana =", Player_2.team[1].mana, "/", Player_2.team[1].max_mana)

def GetAction():
    #-----------------------------------------------------------------------------------------------
    """
    Action options:
    [0] Current teams' stats
    [1] Character skills info
    [2] Use Skill
    """
    #-----------------------------------------------------------------------------------------------
    actionChoice = input("Please select one of the following actions:\n[0] Current teams' stats\n[1] Character skills info\n[2] Use Skill\nPlease note that the [] are not part of the input\n")
    while actionChoice.isdigit() == False and 0 <= actionChoice.isdigit() <= 2:
        actionChoice = input("Please try a different input. ")
    actionChoice = int(actionChoice)
    return actionChoice

def GameRound(player):
    # local vars
    playing = True
    victor = ""
    loser = ""
    turnIncomplete = True
    # player == 0 is Player_1; player == 1 is Player_2
    if player == 0:
        print("Player_1's Turn")
        time.sleep(1)
        while turnIncomplete:
            act = GetAction()
            if act == 0:
                print("Player 1:\n", Player_1.team[0].name, "HP =", Player_1.team[0].current_hp, "/", Player_1.team[0].max_hp,"Mana =", Player_1.team[0].mana, "/", Player_1.team[0].max_mana,
                      "\n", Player_1.team[1].name, "HP =", Player_1.team[1].current_hp, "/", Player_1.team[1].max_hp,"Mana =", Player_1.team[1].mana, "/", Player_1.team[1].max_mana)
                print("Player 2:\n", Player_2.team[0].name, "HP =", Player_2.team[0].current_hp, "/", Player_2.team[0].max_hp,"Mana =", Player_2.team[0].mana, "/", Player_2.team[0].max_mana,
                      "\n", Player_2.team[1].name, "HP =", Player_2.team[1].current_hp, "/", Player_2.team[1].max_hp,"Mana =", Player_2.team[1].mana, "/", Player_2.team[1].max_mana)
            if act == 1:
                invalidNum = True
                charNum = 2 # set to 2 so it is invalid
                # Get target character number
                while invalidNum:
                    charNum = input("Please input team member's number to see their skill description: ")
                    if charNum.isdigit() == True and 0 <= charNum.isdigit() <= 1:
                        invalidNum = False
                        charNum = int(charNum)
                print(Player_1.team[charNum].name+"'s skills:")
                for s in range(len(Player_1.team[charNum].skillsDescription)):
                    print(Player_1.team[charNum].skillsDescription[s])
                    time.sleep(1)
                print(" ")
            if act == 2:
                PlayerAttack(Player_1, Player_2)
                GameRound(1) # Next game round is Player_2's turn
    else:
        print("Player_2's Turn")
        time.sleep(1)
        while turnIncomplete:
            act = GetAction()
            if act == 0:
                print("Player 1:\n", Player_1.team[0].name, "HP =", Player_1.team[0].current_hp, "/", Player_1.team[0].max_hp,
                      "\n", Player_1.team[1].name, "HP =", Player_1.team[1].current_hp, "/", Player_1.team[1].max_hp)
                print("Player 2:\n", Player_2.team[0].name, "HP =", Player_2.team[0].current_hp, "/", Player_2.team[0].max_hp,
                      "\n", Player_2.team[1].name, "HP =", Player_2.team[1].current_hp, "/", Player_2.team[1].max_hp)
            if act == 1:
                invalidNum = True
                charNum = 2 # set to 2 so it is invalid
                # Get target character number
                while invalidNum:
                    charNum = input("Please input team member's number to see their skill description: ")
                    if charNum.isdigit() == True and 0 <= charNum.isdigit() <= 1:
                        invalidNum = False
                        charNum = int(charNum)
                print(Player_2.team[charNum].name+"'s skills:")
                for s in range(len(Player_2.team[charNum].skillsDescription)):
                    print(Player_2.team[charNum].skillsDescription[s])
                    time.sleep(1)
                print(" ")
            if act == 2:
                PlayerAttack(Player_2, Player_1)
                GameRound(0) # Next game round is Player_1's turn
    
    
    if Player_1.team[0].dead == True and Player_1.team[1].dead == True:
        victor = "Player 2"
        loser = "Player 1"
        playing = False
        print("Congratulations Player_1 you have won! Player_2, better luck next time.")
    elif Player_2.team[0].dead == True and Player_2.team[1].dead == True:
        victor = "Player 1"
        loser = "Player 2"
        playing = False
        print("Congratulations Player_2 you have won! Player_1, better luck next time.")
#endregion
  
#MakeTeam(Player_1)
#MakeTeam(Player_2)

player = random.randint(0, 1)
GameRound(player)

