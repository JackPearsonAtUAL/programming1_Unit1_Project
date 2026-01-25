"""
Year 1 Programming 1 Final Project
Script for player 2
Jack Pearson
"""
#region Variables
import random
import time

class Barbarian:
    """
    Barbarian character type
    """
    def __init__(barbObj):
        barbObj.name = "Barbarian"
        barbObj.dmgT = 0 # Int denotes that this character dels attack based damage

        #region Stats
        # Life statss
        barbObj.max_hp = 200 # maximum health value
        barbObj.current_hp = barbObj.max_hp # stores current hp value
        barbObj.dead = False

        # Offensive stats
        barbObj.base_attack = 7 # non-magic damage variable
        barbObj.current_attk = barbObj.base_attack # non-magic damage variable after buffs+debuffs
        barbObj.base_psych = 1 # magic damage variable
        barbObj.current_psy = barbObj.base_psych # non-magic damage variable after buffs+debuffs

        # Defensive stats
        barbObj.base_defence = 8 # non-magic damage reduction variable 
        barbObj.current_def = barbObj.base_defence # non-magic damage reduction variable after buffs+debuffs
        if barbObj.current_def < 0: # stops the player's defecnce going below 0
            barbObj.current_def = 0
        barbObj.base_fortification = 4 # magic damage reduction variable 
        barbObj.current_fort = barbObj.base_fortification # non-magic damage reduction variable after buffs+debuffs
        if barbObj.current_fort < 0: # stops the player's fortification going below 0
            barbObj.current_def = 0

        # Resource stats
        barbObj.max_mana =  20
        barbObj.mana = barbObj.max_mana # resource for magic skills
        barbObj.rest_value = 5 # How much mana and stamina are restored during a rest
        
        barbObj.skills = ["Whack","Furious Blows","Greater Restore","Rage","Rest"]
        barbObj.skillCosts = [1, 5, 10, 15, 0]
        barbObj.skillsDescription = ["[0] "+barbObj.skills[0]+": consumes 1 mana to deal a small amount of damage to one enemy.",
                        "[1] "+barbObj.skills[1]+": consumes 5 mana to deal damage to an enemy. If current health is greater then 10, it will consume 10HP and do double damage.",
                        "[2] "+barbObj.skills[2]+": consumes 10 mana and heals self for 100HP.",
                        "[3] "+barbObj.skills[3]+": consumes 15 and increases damage delt. If health is above 50 when cast, it will aditionally deal damage.",
                        "[4] "+barbObj.skills[4]+": heals character for 50HP and restores "+str(barbObj.rest_value)+" mana."]

    #endregion

    #region Skills
    def Whack(self, cost):
        self.mana -= cost
        skillDMG = 5 * (1 + (self.current_attk / 10)) 
        
        return int(skillDMG)

    def FuriousBlows(self, cost):
        self.mana -= cost
        skillCost = 10
        if self.current_hp - skillCost > 0:
            self.current_hp -= skillCost
            skillDMG = 20 * (1 + (self.current_attk / 10))
        else:
            skillDMG = 10 * (1 + (self.current_attk / 10))
        
        return int(skillDMG)  

    def GreaterRestore(self, cost):
        print("Healing")
        self.mana -= cost
        self.GainHealth(100)

    def Rage(self, cost):
        self.mana -= cost
        skillCost = 50
        if self.current_hp - skillCost > 0:
            self.current_hp -= skillCost
            self.current_attk += 10
            skillDMG = 20 * (1 + (self.current_attk / 10))
        else:
            self.current_attk += 10
            skillDMG = 0

        return int(skillDMG)
        
    def Rest(self, cost):
        self.GainHealth(50)
        self.mana += self.rest_value
        if self.mana > self.max_mana: # stops mana overflow
            self.mana = self.max_mana
        print("The",self.name+"'s mana is now at",self.mana)

    #skills = [Whack, FuriousBlow, GreaterRestore, Rage, Rest]

    #endregion

    #region Health Functions
    def CheckHealth(self):        
        if self.current_hp < 0:
            self.current_hp = 0        
            self.dead = True
            print("The",self.name+"'s health is", self.current_hp,"and is dead")
        elif self.current_hp > self.max_hp:
            self.current_hp = self.max_hp
        
        if self.current_hp != int(self.current_hp):
            self.current_hp = int(self.current_hp)

        print("The",self.name+"'s health is", self.current_hp)

    def TakeDamage(self, type, amount):
        if self.dead:
            self.CheckHealth()
            return
        
        if type == 0: # Attack based damage
            damage = float(amount) * (1 - self.current_def/10)
            self.current_hp -= damage
            print("The",self.name,"has taken",damage,"damage")   

        elif type == 1: # Pyschic type damage
            damage = float(amount) * (1 - self.current_fort/10)
            self.current_hp -= damage
            print("The",self.name,"has taken",damage,"damage")   

        else:
            self.current_hp -= amount
            print("The",self.name,"has taken",amount,"damage")   
        self.CheckHealth()

    def GainHealth(self, amount):
        print(str(amount))
        if self.dead:
            print("The",self.name,"is dead; they cannot be healed.")
            return
        self.current_hp += amount
        self.CheckHealth()
        print("The",self.name,"was healed for:",amount,"HP and is now at",self.current_hp,"HP")
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp
    #endregion

class Mage:
    
    #Mage character type
    
    def __init__(mageObj):
        mageObj.name = "Mage"
        mageObj.dmgT = 1 # Int denotes that this character dels pyschic based damage


        # Life stats
        mageObj.max_hp = 150 # maximum health value
        mageObj.current_hp = mageObj.max_hp # stores current hp value
        mageObj.dead = False

        # Offensive stats
        mageObj.base_attack = 2 # non-magic damage variable
        mageObj.current_attk = mageObj.base_attack # non-magic damage variable after buffs+debuffs
        mageObj.base_psych = 8 # magic damage variable
        mageObj.current_psy = mageObj.base_psych # non-magic damage variable after buffs+debuffs

        # Defensive stats
        mageObj.base_defence = 2 # non-magic damage reduction variable 
        mageObj.current_def = mageObj.base_defence # non-magic damage reduction variable after buffs+debuffs
        if mageObj.current_def < 0: # stops the player's defecnce going below 0
            mageObj.current_def = 0
        mageObj.base_fortification = 8 # magic damage reduction variable 
        mageObj.current_fort = mageObj.base_fortification # non-magic damage reduction variable after buffs+debuffs
        if mageObj.current_fort < 0: # stops the player's fortification going below 0
            mageObj.current_def = 0

        # Resource stats
        mageObj.max_mana = 25
        mageObj.mana = mageObj.max_mana # resource for magic skills
        mageObj.rest_value = 5 # How much mana and stamina are restored during a rest

        mageObj.skills = ["Spark", "Magic Missile", "Arcane Shield", "Storm", "Rest"]
        mageObj.skillCosts = [1, 5, 10, 15, 0]
        mageObj.skillsDescription = ["[0] "+mageObj.skills[0]+": consumes 1 mana to deal a small amount of damage to one enemy.",
                            "[1] "+mageObj.skills[1]+": consumes 5 mana to deal damage to an enemy",
                            "[2] "+mageObj.skills[2]+": consumes 10 mana and lowers self's incoming damage",
                            "[3] "+mageObj.skills[3]+": consumes 15 and deals very high damage",
                            "[4] "+mageObj.skills[4]+": heals character for 50HP and restores "+str(mageObj.rest_value)+" mana."]

    #region Skills
    def Spark(self, cost):
        self.mana -= cost
        skillDMG = 5 * (1 + (self.current_psy/ 10)) 
        return int(skillDMG)

    def MagicMissile(self, cost):
        self.mana -= cost
        skillDMG = 15 * (1 + (self.current_psy/ 10))
        return int(skillDMG)   

    def ArcaneShield(self, cost):
        self.mana -= cost
        self.GainHealth(75)
        self.current_fort += 2
        self.current_def += 2

    def Storm(self, cost):
        self.mana -= cost
        self.current_psy += 5
        skillDMG = 25 * (1 + (self.current_psy/ 10)) 
        return int(skillDMG)

    def Rest(self, cost):
        self.GainHealth(50)
        self.mana += self.rest_value
        if self.mana > self.max_mana: # stops mana overflow
            self.mana = self.max_mana
        print("The",self.name+"'s mana is now at",self.mana)

    #endregion

    #region Health Functions
    def CheckHealth(self):        
        if self.current_hp < 0:
            self.current_hp = 0        
            self.dead = True
            print("The",self.name+"'s health is", self.current_hp,"and is dead")
        elif self.current_hp > self.max_hp:
            self.current_hp = self.max_hp
        
        if self.current_hp != int(self.current_hp):
            self.current_hp = int(self.current_hp)

        print("The",self.name+"'s health is", self.current_hp)

    def TakeDamage(self, type, amount):
        if self.dead:
            self.CheckHealth()
            return
        
        if type == 0: # Attack based damage
            damage = float(amount) * (1 - self.current_def/10)
            self.current_hp -= damage
            print("The",self.name,"has taken",damage,"damage")   

        elif type == 1: # Pyschic type damage
            damage = float(amount) * (1 - self.current_fort/10)
            self.current_hp -= damage
            print("The",self.ame,"has taken",damage,"damage")   

        else:
            self.current_hp -= amount
            print("The",self.name,"has taken",amount,"damage")   
        self.CheckHealth()

    def GainHealth(self, amount):
        if self.dead:
            print("The",self.name,"is dead; they cannot be healed.")
            return
        self.current_hp += amount
        self.CheckHealth()
        print("The",self.name,"was healed for:",amount,"HP and is now at",self.current_hp,"HP")
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp
    #endregion

# Player 1's data
class Player:
    name = ""
    team = ["Empty", "Empty"]

# Player 1
player_1 = Player()
player_1.name = "Player 1"
player_1.team = ["Empty", "Empty"]

# Player 2
player_2 = Player()
player_2.team = ["Empty", "Empty"]
player_2.name = "Player 2"
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
        print(player.name, "current party:")
        #print 1st party member
        if player.team[0] == "Empty":
            print("[0]: Empty")
        else:
            print("[0]:", player.team[0].name)
        time.sleep(0.5)
       # Print 2nd party member
        if player.team[1] == "Empty":
            print("[1]: Empty")
        else:
            print("[1]:", player.team[1].name)
        time.sleep(0.5)

        # ask player for team position
        teamPos = input("Please enter the team position you would like to edit by either entering 0 or 1: ")
        time.sleep(0.5)
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
                time.sleep(0.5)

        # ask player for charaacter type
        #characterOptions = [CS.Barbarian(), CS.Mage()]
        notValid = True
        while notValid:
            # get input
            choice = input("Please input [0] for Barbarian or [1] for Mage: ")
            time.sleep(0.5)
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
        time.sleep(0.5)
        if repeat.lower() == "y":
            validTeam = CheckValidTeam(player.team)
    print("\n")
#endregion

#region Player Turn Logic
def GetSkill(player, teamMember, skill):
    if player.team[teamMember].name == "Barbarian":
        skillOptions = [player.team[teamMember].Whack, player.team[teamMember].FuriousBlows, 
                        player.team[teamMember].GreaterRestore, player.team[teamMember].Rage, player.team[teamMember].Rest]
        
        if skill == 2 or skill == 4:
            skillOptions[skill](player.team[teamMember].skillCosts[skill])
        else:
            return skillOptions[skill](player.team[teamMember].skillCosts[skill])
    if player.team[teamMember].name == "Mage":
        skillOptions = [player.team[teamMember].Spark, player.team[teamMember].MagicMissile, 
                player.team[teamMember].ArcaneShield, player.team[teamMember].Storm, player.team[teamMember].Rest]
               
        if skill == 2 or skill == 4:
            skillOptions[skill](player.team[teamMember].skillCosts[skill])
        else:
            return skillOptions[skill](player.team[teamMember].skillCosts[skill])

def PlayerAttack(playerObj, opponentObj):
    loop = True # Used to keep prompting inputs until skill usage is confirmed
    while loop:   
        # Tells player the current team
        print(playerObj.name, "options are: [0]", playerObj.team[0].name, "and [1]", playerObj.team[1].name)

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
        print("skill options are: [0]", playerObj.team[character].skills[0], "[1]", playerObj.team[character].skills[1], 
                "[2]", playerObj.team[character].skills[2], "[3]", playerObj.team[character].skills[3], 
                "[4]", playerObj.team[character].skills[4])
        skill = input("Please select one of your skills by inputting it's number ")
        e = True
        while e:
            if skill.isdigit() == True:
                # Casts string into integer
                skill = int(skill)
                e = False
            
            if skill == int(skill) and 0 <= skill <= 4:
                # Add check for mana/stamina cost
                # If it costs more than the character has the player will have to pick a different skill
                if playerObj.team[character].skillCosts[skill] > playerObj.team[character].mana:
                    skill = input("Please try inputting a different skill ")
            else:
                print(playerObj.team[character].skills[skill].__name__, "has been selected")
                e = False
 

        #-----------------------------------------------------------------------------------------------
        # Condition to make sure it isn't a self target skill
        #-----------------------------------------------------------------------------------------------        
        if skill != 2 and skill != 4:
            # select one of the enemy characters using the character's team number
            print(playerObj.name, "options are: [0]", opponentObj.team[0].name, "and [1]", opponentObj.team[1].name)
            target = input("Please select one of the above target by inputting their position number ") # Stores the targeted chracter's position
            e = True
            while e:
                #Check if input is a number
                if target.isdigit() == True:
                    # Casts string into integer
                    target = int(target)
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
                "with:", playerObj.team[character].skills[int(skill)])
            
            confirm = input("To confirm action please type: y . To cancel, type: n . Any other input will return you to the action menu: ")
            if confirm.lower() == "y":
                # Attacking skills target by using this formula:
                # Target.TakeDamage(currentPlayer[character].skills[skill]
                #opponentObj.team[target].TakeDamage(int(playerObj.team[character].dmgT), int(playerObj.team[character].skills[skill](playerObj.team[character].skillCosts[skill])))
                opponentObj.team[target].TakeDamage(playerObj.team[character].dmgT, GetSkill(playerObj, character, skill))
                loop = False
            elif confirm.lower() == "n":
                print("Re-write action selected.")
            else:
                print("Returning to options menu.")
                loop = False
        else:
            print("Current action is:", playerObj.team[character].name, "is targeting themself with:", playerObj.team[character].skills[skill])
            confirm = input("To confirm action please type: y . To cancel, type: n . Any other input will return you to the action menu ")
            if confirm.lower() == "y":
                print("healing")
                GetSkill(playerObj, character, skill)
                loop = False
            elif confirm.lower() == "n":
                print("Re-write action selected.")
            else:
                print("Returning to options menu.")
                loop = False
    print("Player 1:\n", player_1.team[0].name, "HP =", player_1.team[0].current_hp, "/", player_1.team[0].max_hp,"Mana =", player_1.team[0].mana, "/", player_1.team[0].max_mana,
            "\n", player_1.team[1].name, "HP =", player_1.team[1].current_hp, "/", player_1.team[1].max_hp,"Mana =", player_1.team[1].mana, "/", player_1.team[1].max_mana)
    print("Player 2:\n", player_2.team[0].name, "HP =", player_2.team[0].current_hp, "/", player_2.team[0].max_hp,"Mana =", player_2.team[0].mana, "/", player_2.team[0].max_mana,
            "\n", player_2.team[1].name, "HP =", player_2.team[1].current_hp, "/", player_2.team[1].max_hp,"Mana =", player_2.team[1].mana, "/", player_2.team[1].max_mana)

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

def CheckCanPlay():
    if player_1.team[0].current_hp == 0 and player_1.team[1].current_hp == 0:
        print("Congratulations Player 1 you have won! Player 2, better luck next time.")
        return False
    elif player_2.team[0].current_hp == 0 and player_2.team[1].current_hp == 0:
        print("Congratulations Player 2 you have won! Player 1, better luck next time.")
        return False
    return True

def GameRound(player):   
    turnIncomplete = True
    # player == 0 is player_1; player == 1 is player_2
    if player == 0:
        print("Player 1's Turn")
        time.sleep(0.5)
        while turnIncomplete:
            act = GetAction()
            if act == 0:
                print("Player 1:\n", player_1.team[0].name, "HP =", player_1.team[0].current_hp, "/", player_1.team[0].max_hp,"Mana =", player_1.team[0].mana, "/", player_1.team[0].max_mana,
                    "\n", player_1.team[1].name, "HP =", player_1.team[1].current_hp, "/", player_1.team[1].max_hp,"Mana =", player_1.team[1].mana, "/", player_1.team[1].max_mana)
                print("Player 2:\n", player_2.team[0].name, "HP =", player_2.team[0].current_hp, "/", player_2.team[0].max_hp,"Mana =", player_2.team[0].mana, "/", player_2.team[0].max_mana,
                    "\n", player_2.team[1].name, "HP =", player_2.team[1].current_hp, "/", player_2.team[1].max_hp,"Mana =", player_2.team[1].mana, "/", player_2.team[1].max_mana)
            if act == 1:
                invalidNum = True
                charNum = input("Please input team member's number to see their skill description: ") # Get target character number
                while invalidNum:
                    #Check if input is a number
                    if charNum.isdigit() == True:
                        # Casts string into integer
                        charNum = int(charNum)
                    
                    # Checks if inputted number is valid
                    if charNum != 0 and charNum != 1:
                        charNum = input("Invalid input, please try inputting a different position ")
                    # Checks wheether or not the character is alive
                    elif player_1.team[charNum].dead == True: 
                        charNum = input("Character has perished, please try inputting a different position ")
                    # Character number is valid and attached character is alive
                    else:
                        invalidNum = False
                        print(player_1.team[charNum].name, "has been selected")
                        print("")

                print(player_1.team[charNum].name+"'s skills:")              
                # Prints out each desctription
                for s in range(len(player_1.team[charNum].skillsDescription)):
                    print(player_1.team[charNum].skillsDescription[s])
                    time.sleep(0.5)
                print(" ")
            if act == 2:
                PlayerAttack(player_1, player_2)
                turnIncomplete = False
        canPlay = CheckCanPlay()
        if canPlay == True: 
            GameRound(1) # Next game round is player_2's turn
    else:
        print("Player 2's Turn")
        time.sleep(0.5)
        while turnIncomplete:
            act = GetAction()
            if act == 0:
                print("Player 1:\n", player_1.team[0].name, "HP =", player_1.team[0].current_hp, "/", player_1.team[0].max_hp,
                    "\n", player_1.team[1].name, "HP =", player_1.team[1].current_hp, "/", player_1.team[1].max_hp)
                print("Player 2:\n", player_2.team[0].name, "HP =", player_2.team[0].current_hp, "/", player_2.team[0].max_hp,
                    "\n", player_2.team[1].name, "HP =", player_2.team[1].current_hp, "/", player_2.team[1].max_hp)
            if act == 1:
                invalidNum = True
                charNum = input("Please input team member's number to see their skill description: ") # Get target character number
                while invalidNum:
                    #Check if input is a number
                    if charNum.isdigit() == True:
                        # Casts string into integer
                        charNum = int(charNum)
                    
                    # Checks if inputted number is valid
                    if charNum != 0 and charNum != 1:
                        charNum = input("Invalid input, please try inputting a different position ")
                    # Checks wheether or not the character is alive
                    elif player_1.team[charNum].dead == True: 
                        charNum = input("Character has perished, please try inputting a different position ")
                    # Character number is valid and attached character is alive
                    else:
                        invalidNum = False
                        print(player_1.team[charNum].name, "has been selected")
                        print("")

                print(player_2.team[charNum].name+"'s skills:")
                for s in range(len(player_2.team[charNum].skillsDescription)):
                    print(player_2.team[charNum].skillsDescription[s])
                    time.sleep(0.5)
                print(" ")
            if act == 2:
                PlayerAttack(player_2, player_1)
                turnIncomplete = False
        canPlay = CheckCanPlay()
        if canPlay == True: 
            GameRound(0) # Next game round is player_2's turn 
#endregion
  
MakeTeam(player_1)
MakeTeam(player_2)

p = random.randint(0, 1)
GameRound(random.randint(0, 1))