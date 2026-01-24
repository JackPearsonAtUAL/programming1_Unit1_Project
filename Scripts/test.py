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

ch1 = Barbarian()
ch1.name = "Barbarian1"
ch2 = Barbarian()
print(ch1.name, ch2.name)