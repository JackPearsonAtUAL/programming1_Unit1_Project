"""
Barbarian character type
"""
name = "Barbarian"

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
max_mana =  1
mana = max_mana # resource for magic skills
max_stamina = 20
stamina = max_stamina # resource for non-magic skills
rest_value = 5 # How much mana and stamina are restored during a rest

# Status stats
res = 0 # multiplied by 10 gives percentile chance to resist a debuff
stat_modifs = [0, 0, 0, 0, 0]
#endregion

#region Skills
def Whack(cost):
    global stamina
    stamina -= cost
    skillDMG = 5 * (1 + (current_attk / 10)) 
    return skillDMG

def FuriousBlow(cost):
    global stamina, current_hp
    stamina -= cost
    skillCost = 10
    if current_hp - skillCost > 0:
        current_hp -= skillCost
        skillDMG = 20 * (1 + (current_attk / 10))
        return skillDMG
    else:
        skillDMG = 10 * (1 + (current_attk / 10))
        return skillDMG   

def GreaterRestore(cost):
    global stamina
    stamina -= cost
    GainHealth(100)

def Rage(cost):
    global stamina, current_hp, current_attk
    stamina -= cost
    skillCost = 50
    if current_hp - skillCost > 0:
        current_hp -= skillCost
        current_attk += 10
        skillDMG = 20 * (1 + (current_attk / 10))
        return skillDMG
    else:
        current_attk += 10
        return 0
    
def Rest():
    global mana, stamina, rest_value
    GainHealth(50)
    mana += rest_value
    if mana > max_mana: # stops mana overflow
        mana = max_mana
    stamina += rest_value
    if stamina > max_stamina: # stops stamina overflow
        stamina = max_stamina
    print("The",name+"'s mana is now at",mana,"and their stamina is",stamina)


skills = [Whack, FuriousBlow, GreaterRestore, Rage, Rest]
skillCosts = [1, 5, 10, 15]
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
      
    if type == 0:
        damage = amount * (1 - current_def/10)
        current_hp -= damage
        print("The",name,"has taken",damage,"damage")   

    elif type == 1:
        damage = amount * (1 - current_fort/10)
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