CREATE TABLE `DefenseDice` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` TEXT NOT NULL,
    `color` TEXT NOT NULL
);
CREATE TABLE `Faction` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` TEXT NOT NULL
);
CREATE TABLE `Keyword` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `title` TEXT NOT NULL,
    `description` TEXT NOT NULL,
    `type` TEXT NOT NULL
);
CREATE TABLE `List` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `commander_id` INTEGER NOT NULL,
    `operative_id` INTEGER NOT NULL,
    `corps_id` INTEGER NOT NULL,
    `special_forces_id` INTEGER NOT NULL,
    `support_id` INTEGER NOT NULL,
    `heavy_id` INTEGER NOT NULL,
    FOREIGN KEY(`commander_id`) REFERENCES `Unit`(`id`),
    FOREIGN KEY(`operative_id`) REFERENCES `Unit`(`id`),
    FOREIGN KEY(`corps_id`) REFERENCES `Unit`(`id`),
    FOREIGN KEY(`special_forces_id`) REFERENCES `Unit`(`id`),
    FOREIGN KEY(`support_id`) REFERENCES `Unit`(`id`),
    FOREIGN KEY(`heavy_id`) REFERENCES `Unit`(`id`)
);
CREATE TABLE `Unit` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` TEXT NOT NULL,
    `unit_type_id` INTEGER NOT NULL,
    `amount` INTEGER NOT NULL,
    `speed` INTEGER NOT NULL,
    `faction_id` INTEGER NOT NULL,
    `point_cost` INTEGER NOT NULL,
    `owned_amount` INTEGER NOT NULL,
    `health` INTEGER NOT NULL,
    `defense_dice_id` INTEGER NOT NULL,
    `surge_to_hit` INTEGER NOT NULL,
    `surge_to_crit` INTEGER NOT NULL,
    `surge_to_defend` INTEGER NOT NULL,
    `weapon_id` INTEGER NOT NULL,
    `keyword_id` INTEGER NOT NULL,
    `upgrade_id` INTEGER NOT NULL,
    `unit_img` TEXT NOT NULL,
    FOREIGN KEY(`faction_id`) REFERENCES `Faction`(`id`),
    FOREIGN KEY(`defense_dice_id`) REFERENCES `DefenseDice`(`id`),
    FOREIGN KEY(`unit_type_id`) REFERENCES `UnitType`(`id`),
    FOREIGN KEY(`weapon_id`) REFERENCES `Weapon`(`id`),
    FOREIGN KEY(`keyword_id`) REFERENCES `Keyword`(`id`),
    FOREIGN KEY(`upgrade_id`) REFERENCES `Upgrade`(`id`)
);
CREATE TABLE `UnitType` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `description` TEXT NOT NULL
);
CREATE TABLE `Upgrade` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` TEXT NOT NULL,
    `card_id` INTEGER NOT NULL,
    `keyword_id` INTEGER NOT NULL
);
CREATE TABLE `Weapon` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` TEXT NOT NULL,
    `black_dice` INTEGER NOT NULL,
    `red_dice` INTEGER NOT NULL,
    `white_dice` INTEGER NOT NULL,
    `keyword_id` INTEGER NOT NULL,
    `range` TEXT NOT NULL,
    `unique_weapon` INTEGER NOT NULL,
    FOREIGN KEY(`keyword_id`) REFERENCES `Keyword`(`id`)
);