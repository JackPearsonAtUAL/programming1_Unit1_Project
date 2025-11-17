"""
Year 1 Programming 1 Final Project
Script for character options
Jack Pearson
"""

""" Pseudocode for a character's info
character_name = class charNum(
    max_hp = int
    function Skill0():
        return
    function Skill1():
        return
    function Skill2():
        return
    function Skill3():
        return
)
"""

# Damage deal calculation = skillBaseDamage * (1 + (DamageTypeBonus / 10))
# Damage take calculation = incomingDamage * (1 - (DamageTypeResist / 10))

class Char:
    name = ""
    
    # Life stats
    max_hp = 100 # maximum health value
    current_hp = max_hp # stores current hp value
    
    # Offensive stats
    base_attack = 0 # non-magic damage variable
    current_attk = base_attack # non-magic damage variable after buffs+debuffs
    base_psych = 0 # magic damage variable
    current_psy = base_psych # non-magic damage variable after buffs+debuffs
    
    # Defensive stats
    base_defence = 0 # non-magic damage reduction variable 
    current_def = base_defence # non-magic damage reduction variable after buffs+debuffs
    if current_def < 0: # stops the player's defecnce going below 0
        current_def = 0
    base_fortification = 0 # magic damage reduction variable 
    current_fort = base_fortification # non-magic damage reduction variable after buffs+debuffs
    if current_fort < 0: # stops the player's fortification going below 0
        current_def = 0
    
    # Resource stats
    mana = 0 # resource for magic skills
    stamina = 0 # resource for non-magic skills
    rest_value = 0 # How much mana and stamina are restored during a rest

    # Status stats
    res = 0 # multiplied by 10 gives percentile chance to resist a debuff
    stat_modifs = [0, 0, 0, 0, 0]
    
    #region Skills
    def Skill0():
        return

    def Skill1():
        return

    def Skill2():
        return

    def Skill3():
        return
    #endregion

