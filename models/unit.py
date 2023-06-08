class Unit():

    def __init__(self,
                 id,
                 name,
                 unit_type_id,
                 amount,
                 speed,
                 faction_id,
                 point_cost,
                 owned_amount,
                 health,
                 courage,
                 defense_dice,
                 surge_to_hit,
                 surge_to_crit,
                 surge_to_defend,
                 keyword_id,
                 weapon_id,
                 upgrade_id):

        self.id = id
        self.name = name
        self.unit_type_id = unit_type_id
        self.amount = amount
        self.speed = speed
        self.faction_id = faction_id
        self.point_cost = point_cost
        self.owned_amount = owned_amount
        self.health = health
        self.courage = courage
        self.defense_dice = defense_dice
        self.surge_to_hit = surge_to_hit
        self.surge_to_crit = surge_to_crit
        self.surge_to_defend = surge_to_defend
        self.keyword_id = keyword_id
        self.weapon_id = weapon_id
        self.upgrade_id = upgrade_id


new_unit = Unit(4, "DeathTroopers", 4, 4, 2, 1, 76, 2, 1,
                2, 2, True, False, True, [1, 2], 2, [1, 4])
