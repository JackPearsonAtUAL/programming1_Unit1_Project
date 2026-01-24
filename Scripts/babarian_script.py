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
    mana -= cost
    skillDMG = 5 * (1 + (current_attk / 10)) 
    
    return int(skillDMG)

def FuriousBlow(cost):
    global mana, current_hp
    mana -= cost
    skillCost = 10
    if current_hp - skillCost > 0:
        current_hp -= skillCost
        skillDMG = 20 * (1 + (current_attk / 10))
    else:
        skillDMG = 10 * (1 + (current_attk / 10))
    
    return int(skillDMG)  

def GreaterRestore(cost):
    global mana
    mana -= cost
    GainHealth(100)

def Rage(cost):
    global mana, current_hp, current_attk
    mana -= cost
    skillCost = 50
    if current_hp - skillCost > 0:
        current_hp -= skillCost
        current_attk += 10
        skillDMG = 20 * (1 + (current_attk / 10))
    else:
        current_attk += 10
        skillDMG = 0

    return int(skillDMG)
    
def Rest(cost):
    global mana, mana, rest_value
    GainHealth(50)
    mana += rest_value
    if mana > max_mana: # stops mana overflow
        mana = max_mana
    print("The",name+"'s mana is now at",mana)


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
    global current_hp, max_hp, dead
    
    if current_hp < 0:
        current_hp = 0        
        dead = True
        print("The",name+"'s health is", current_hp,"and is dead")
    elif current_hp > max_hp:
        current_hp = max_hp
    else:
        print("The",name+"'s health is", current_hp)

def TakeDamage(type, amount):
    global current_hp, dead
    if dead:
        CheckHealth()
        return
      
    if type == 0: # Attack based damage
        damage = float(amount) * (1 - current_def/10)
        current_hp -= damage
        print("The",name,"has taken",damage,"damage")   

    elif type == 1: # Pyschic type damage
        damage = float(amount) * (1 - current_fort/10)
        current_hp -= damage
        print("The",name,"has taken",damage,"damage")   

    else:
        current_hp -= amount
        print("The",name,"has taken",amount,"damage")   
    CheckHealth()

def GainHealth(amount):
    global current_hp, max_hp
    if dead:
        print("The",name,"is dead; they cannot be healed.")
        return
    current_hp += amount
    CheckHealth()
    print("The",name,"was healed for:",amount,"HP and is now at",current_hp,"HP")
    if current_hp > max_hp:
        current_hp = max_hp
#endregion