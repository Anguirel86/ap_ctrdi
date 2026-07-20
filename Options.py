
from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, FreeText, OptionGroup, \
    OptionList, PerGameCommonOptions, Range, Toggle


class XpScale(Range):
    """Factor by which to scale XP earned in battle"""
    display_name = "Xp Scale"
    range_start = 50
    range_end = 1000
    default = 400


class TpScale(Range):
    """Factor by which to scale TP earned in battle"""
    display_name = "Tp Scale"
    range_start = 50
    range_end = 1000
    default = 400


class SplitTp(Toggle):
    """TP is split among living party members rather than shared evenly"""
    display_name = "Split Tp"


class FixTpDoubling(Toggle):
    """TP rewards are not duplicated for every gained tech level"""
    display_name = "Fix Tp Doubling"


class XpPenaltyLevel(Range):
    """Levels past this level become more difficult to obtain"""
    display_name = "Xp Penalty Level"
    range_start = 1
    range_end = 99
    default = 40


class XpPenaltyPercent(Range):
    """For each level beyond the penalty, the requirement grows by this percent"""
    display_name = "Xp Penalty Percent"
    range_start = 0
    range_end = 100
    default = 15


class LevelCap(Range):
    """Levels beyond the level cap will have prohibitively large requirements."""
    display_name = "Level Cap"
    range_start = 1
    range_end = 99
    default = 50


class BossXpFactor(Range):
    """Boss xp is additionally multiplied by this factor"""
    display_name = "Boss Xp Factor"
    range_start = 0
    range_end = 500
    default = 200


class MidbossRewardFactor(Range):
    """Midboss xp/tp is additionally multiplied by this factor"""
    display_name = "Midboss Reward Factor"
    range_start = 0
    range_end = 500
    default = 200


class NormalizeBossXp(Toggle):
    """Boss xp is proportional to their level"""
    display_name = "Normalize Boss Xp"


class DropEnemyPool(Choice):
    """Pool of enemies which can have a dropped item (Group 1)"""
    display_name = "Drop Enemy Pool"

    option_vanilla = 0
    option_all = 1
    option_midbosses = 2
    option_bosses = 3
    option_bosses_no_lavos = 4
    option_normal_enemies = 5
    option_hard_enemies = 6
    option_custom = 7
    default = 0


class DropRewardPool(Choice):
    """Method of choosing enemy dropped items (Group 1)"""
    display_name = "Drop Reward Pool"

    option_vanilla = 0
    option_shuffle = 1
    option_rdi_random = 2
    default = 0


class DropRate(Range):
    """Percentage (decimal) of enemies in the drop pool which have a dropped item (Group 1)"""
    display_name = "Drop Rate"
    range_start = 0
    range_end = 100
    default = 100


class CustomDropEnemyPool(OptionList):
    """Enemies for group 0 drops"""
    display_name = "Custom Drop Enemy Pool"
    valid_keys = {'krawlie', 'yakra', 'twin_boss', 'masa_mune', 'nizbel', 'nizbel_ii', 'slash', 'slash_sword', 'flea', 'dalton', 'dalton_plus', 'super_slash', 'heckran', 'flea_plus', 'rust_tyrano', 'atropos_xr', 'yakra_xiii', 'golem', 'golem_boss', 'zombor_bottom', 'zombor_top', 'lavos_spawn_shell', 'lavos_spawn_head', 'mega_mutant_head', 'mega_mutant_bottom', 'giga_mutant_head', 'giga_mutant_bottom', 'terra_mutant_head', 'terra_mutant_bottom', 'elder_spawn_shell', 'elder_spawn_head', 'retinite_eye', 'retinite_top', 'retinite_bottom', 'son_of_sun_eye', 'son_of_sun_flame', 'nu', 'reptite_green', 'terrasaur', 'kilwala', 'hench_purple', 'omicrone', 'martello', 'bellbird', 'panel', 'mammon_m', 'lavos_3_center_unk_0b', 'blue_imp', 'green_imp', 'stone_imp', 'mud_imp', 'roly', 'poly', 'rolypoly', 'roly_rider', 'lavos_giga_gaia_right', 'blue_eaglet', 'gold_eaglet', 'red_eaglet', 'lavos_giga_gaia_left', 'avian_chaos', 'imp_ace', 'bantam_imp', 'gnasher', 'gnawer', 'naga_ette', 'lavos_support_unk_1f', 'ruminator', 'lavos_support_unk_21', 'octopod', 'octoblush', 'octobino', 'zeal', 'fly_trap', 'meat_eater', 'man_eater', 'krakker', 'egder', 'defunct', 'departed', 'deceased', 'decedent', 'macabre', 'reaper', 'guard', 'sentry', 'free_lancer', 'outlaw', 'juggler', 'mage', 'unknown_3c', 'reptite_purple', 'blue_shield', 'yodu_de', 'incognito', 'peepingdoom', 'boss_orb', 'side_kick', 'unknown_44', 'jinn_bottle', 'evilweevil', 'tempurite', 'diablos', 'gargoyle', 'grimalkin', 'hench_blue', 't_pole', 'croaker', 'amphibite', 'mad_bat', 'vamp', 'scouter', 'flyclops', 'bugger', 'debugger', 'debuggest', 'sorcerer', 'jinn', 'barghest', 'unknown_5a', 'crater', 'volcano', 'shitake', 'hetake', 'rubble', 'dream_devourer', 'shist', 'pahoehoe', 'nereid', 'save_point_enemy', 'mohavor', 'shadow', 'lavos_support_unk_67', 'base', 'acid', 'alkaline', 'ion', 'anion', 'thrasher', 'lasher', 'goblin', 'ogre', 'cave_bat', 'ogan', 'flunky', 'groupie', 'lavos_support_unk_77', 'lavos_support_unk_78', 'winged_ape', 'cave_ape', 'megasaur', 'omnicrone', 'beast', 'blue_beast', 'red_beast', 'turret', 'lizardactyl', 'nu_2', 'avian_rex', 'blob', 'alien', 'rat', 'gremlin', 'runner', 'proto_2', 'proto_3', 'proto_4', 'bug', 'beetle', 'goon', 'cyrus', 'rain_frog', 'gato', 'dragon_tank', 'grinder', 'synchrite', 'masa', 'mune', 'azala', 'flea_plus_trio', 'mutant', 'metal_mute', 'super_slash_trio', 'ozzie_zenan', 'ozzie_fort', 'great_ozzie', 'gigasaur', 'leaper', 'fossil_ape', 'tank_head', 'decedent_ii', 'octorider', 'zeal_2_center', 'zeal_2_left', 'zeal_2_right', 'display', 'blacktyrano', 'motherbrain', 'unknown_bf', 'cybot', 'lavos_guardian', 'lavos_heckran', 'lavos_zombor_upper', 'lavos_masa_mune', 'lavos_nizbel', 'tubster', 'lavos_magus', 'lavos_dragon_tank', 'lavos_2_head', 'lavos_2_left', 'lavos_2_right', 'lavos_3_core', 'guardian_bit', 'byte', 'giga_gaia_head', 'giga_gaia_left', 'giga_gaia_right', 'guardian', 'red_scout', 'blue_scout', 'laser_guard', 'lavos_tank_left_head', 'lavos_tank_right_grinder', 'lavos_guardian_left', 'lavos_guardian_right', 'lavos_zombor_bottom', 'lavos_tyrano_azala', 'spekkio_frog', 'spekkio_kilwala', 'spekkio_ogre', 'spekkio_omnicrone', 'spekkio_masa_mune', 'spekkio_nu', 'lavos_tyrano', 'lavos_giga_gaia_head', 'lavos_unk_e8', 'lavos_unk_e9', 'lavos_unk_ea', 'lavos_ocean_palace', 'lavos_1', 'lavos_3_left', 'hexapod', 'lavos_3_right', 'fake_flea', 'ozzie_magus_chains', 'roly_bomber', 'johnny', 'basher', 'r_series', 'magus', 'magus_north_cape', 'magus_no_name', 'schala', 'unused_fd', 'unused_fe', 'unused_ff'}
    default = []


class CustomDropRewardPool(FreeText):
    """Custom rewards for group 0 drops"""
    display_name = "Custom Drop Reward Pool"
    default = ""


class DropEnemyPool2(Choice):
    """Pool of enemies which can have a dropped item (Group 2)"""
    display_name = "Drop Enemy Pool 2"

    option_vanilla = 0
    option_all = 1
    option_midbosses = 2
    option_bosses = 3
    option_bosses_no_lavos = 4
    option_normal_enemies = 5
    option_hard_enemies = 6
    option_custom = 7
    default = 7


class DropRewardPool2(Choice):
    """Method of choosing enemy dropped items (Group 2)"""
    display_name = "Drop Reward Pool 2"

    option_vanilla = 0
    option_shuffle = 1
    option_rdi_random = 2
    default = 0


class DropRate2(Range):
    """Percentage (decimal) of enemies in the drop pool which have a dropped item (Group 2)"""
    display_name = "Drop Rate 2"
    range_start = 0
    range_end = 100
    default = 100


class CustomDropEnemyPool2(OptionList):
    """Enemies for group 1 drops"""
    display_name = "Custom Drop Enemy Pool 2"
    valid_keys = {'krawlie', 'yakra', 'twin_boss', 'masa_mune', 'nizbel', 'nizbel_ii', 'slash', 'slash_sword', 'flea', 'dalton', 'dalton_plus', 'super_slash', 'heckran', 'flea_plus', 'rust_tyrano', 'atropos_xr', 'yakra_xiii', 'golem', 'golem_boss', 'zombor_bottom', 'zombor_top', 'lavos_spawn_shell', 'lavos_spawn_head', 'mega_mutant_head', 'mega_mutant_bottom', 'giga_mutant_head', 'giga_mutant_bottom', 'terra_mutant_head', 'terra_mutant_bottom', 'elder_spawn_shell', 'elder_spawn_head', 'retinite_eye', 'retinite_top', 'retinite_bottom', 'son_of_sun_eye', 'son_of_sun_flame', 'nu', 'reptite_green', 'terrasaur', 'kilwala', 'hench_purple', 'omicrone', 'martello', 'bellbird', 'panel', 'mammon_m', 'lavos_3_center_unk_0b', 'blue_imp', 'green_imp', 'stone_imp', 'mud_imp', 'roly', 'poly', 'rolypoly', 'roly_rider', 'lavos_giga_gaia_right', 'blue_eaglet', 'gold_eaglet', 'red_eaglet', 'lavos_giga_gaia_left', 'avian_chaos', 'imp_ace', 'bantam_imp', 'gnasher', 'gnawer', 'naga_ette', 'lavos_support_unk_1f', 'ruminator', 'lavos_support_unk_21', 'octopod', 'octoblush', 'octobino', 'zeal', 'fly_trap', 'meat_eater', 'man_eater', 'krakker', 'egder', 'defunct', 'departed', 'deceased', 'decedent', 'macabre', 'reaper', 'guard', 'sentry', 'free_lancer', 'outlaw', 'juggler', 'mage', 'unknown_3c', 'reptite_purple', 'blue_shield', 'yodu_de', 'incognito', 'peepingdoom', 'boss_orb', 'side_kick', 'unknown_44', 'jinn_bottle', 'evilweevil', 'tempurite', 'diablos', 'gargoyle', 'grimalkin', 'hench_blue', 't_pole', 'croaker', 'amphibite', 'mad_bat', 'vamp', 'scouter', 'flyclops', 'bugger', 'debugger', 'debuggest', 'sorcerer', 'jinn', 'barghest', 'unknown_5a', 'crater', 'volcano', 'shitake', 'hetake', 'rubble', 'dream_devourer', 'shist', 'pahoehoe', 'nereid', 'save_point_enemy', 'mohavor', 'shadow', 'lavos_support_unk_67', 'base', 'acid', 'alkaline', 'ion', 'anion', 'thrasher', 'lasher', 'goblin', 'ogre', 'cave_bat', 'ogan', 'flunky', 'groupie', 'lavos_support_unk_77', 'lavos_support_unk_78', 'winged_ape', 'cave_ape', 'megasaur', 'omnicrone', 'beast', 'blue_beast', 'red_beast', 'turret', 'lizardactyl', 'nu_2', 'avian_rex', 'blob', 'alien', 'rat', 'gremlin', 'runner', 'proto_2', 'proto_3', 'proto_4', 'bug', 'beetle', 'goon', 'cyrus', 'rain_frog', 'gato', 'dragon_tank', 'grinder', 'synchrite', 'masa', 'mune', 'azala', 'flea_plus_trio', 'mutant', 'metal_mute', 'super_slash_trio', 'ozzie_zenan', 'ozzie_fort', 'great_ozzie', 'gigasaur', 'leaper', 'fossil_ape', 'tank_head', 'decedent_ii', 'octorider', 'zeal_2_center', 'zeal_2_left', 'zeal_2_right', 'display', 'blacktyrano', 'motherbrain', 'unknown_bf', 'cybot', 'lavos_guardian', 'lavos_heckran', 'lavos_zombor_upper', 'lavos_masa_mune', 'lavos_nizbel', 'tubster', 'lavos_magus', 'lavos_dragon_tank', 'lavos_2_head', 'lavos_2_left', 'lavos_2_right', 'lavos_3_core', 'guardian_bit', 'byte', 'giga_gaia_head', 'giga_gaia_left', 'giga_gaia_right', 'guardian', 'red_scout', 'blue_scout', 'laser_guard', 'lavos_tank_left_head', 'lavos_tank_right_grinder', 'lavos_guardian_left', 'lavos_guardian_right', 'lavos_zombor_bottom', 'lavos_tyrano_azala', 'spekkio_frog', 'spekkio_kilwala', 'spekkio_ogre', 'spekkio_omnicrone', 'spekkio_masa_mune', 'spekkio_nu', 'lavos_tyrano', 'lavos_giga_gaia_head', 'lavos_unk_e8', 'lavos_unk_e9', 'lavos_unk_ea', 'lavos_ocean_palace', 'lavos_1', 'lavos_3_left', 'hexapod', 'lavos_3_right', 'fake_flea', 'ozzie_magus_chains', 'roly_bomber', 'johnny', 'basher', 'r_series', 'magus', 'magus_north_cape', 'magus_no_name', 'schala', 'unused_fd', 'unused_fe', 'unused_ff'}
    default = []


class CustomDropRewardPool2(FreeText):
    """Custom rewards for group 1 drops"""
    display_name = "Custom Drop Reward Pool 2"
    default = ""


class DropEnemyPool3(Choice):
    """Pool of enemies which can have a dropped item (Group 3)"""
    display_name = "Drop Enemy Pool 3"

    option_vanilla = 0
    option_all = 1
    option_midbosses = 2
    option_bosses = 3
    option_bosses_no_lavos = 4
    option_normal_enemies = 5
    option_hard_enemies = 6
    option_custom = 7
    default = 7


class DropRewardPool3(Choice):
    """Method of choosing enemy dropped items (Group 3)"""
    display_name = "Drop Reward Pool 3"

    option_vanilla = 0
    option_shuffle = 1
    option_rdi_random = 2
    default = 0


class DropRate3(Range):
    """Percentage (decimal) of enemies in the drop pool which have a dropped item (Group 3)"""
    display_name = "Drop Rate 3"
    range_start = 0
    range_end = 100
    default = 100


class CustomDropEnemyPool3(OptionList):
    """Enemies for group 2 drops"""
    display_name = "Custom Drop Enemy Pool 3"
    valid_keys = {'krawlie', 'yakra', 'twin_boss', 'masa_mune', 'nizbel', 'nizbel_ii', 'slash', 'slash_sword', 'flea', 'dalton', 'dalton_plus', 'super_slash', 'heckran', 'flea_plus', 'rust_tyrano', 'atropos_xr', 'yakra_xiii', 'golem', 'golem_boss', 'zombor_bottom', 'zombor_top', 'lavos_spawn_shell', 'lavos_spawn_head', 'mega_mutant_head', 'mega_mutant_bottom', 'giga_mutant_head', 'giga_mutant_bottom', 'terra_mutant_head', 'terra_mutant_bottom', 'elder_spawn_shell', 'elder_spawn_head', 'retinite_eye', 'retinite_top', 'retinite_bottom', 'son_of_sun_eye', 'son_of_sun_flame', 'nu', 'reptite_green', 'terrasaur', 'kilwala', 'hench_purple', 'omicrone', 'martello', 'bellbird', 'panel', 'mammon_m', 'lavos_3_center_unk_0b', 'blue_imp', 'green_imp', 'stone_imp', 'mud_imp', 'roly', 'poly', 'rolypoly', 'roly_rider', 'lavos_giga_gaia_right', 'blue_eaglet', 'gold_eaglet', 'red_eaglet', 'lavos_giga_gaia_left', 'avian_chaos', 'imp_ace', 'bantam_imp', 'gnasher', 'gnawer', 'naga_ette', 'lavos_support_unk_1f', 'ruminator', 'lavos_support_unk_21', 'octopod', 'octoblush', 'octobino', 'zeal', 'fly_trap', 'meat_eater', 'man_eater', 'krakker', 'egder', 'defunct', 'departed', 'deceased', 'decedent', 'macabre', 'reaper', 'guard', 'sentry', 'free_lancer', 'outlaw', 'juggler', 'mage', 'unknown_3c', 'reptite_purple', 'blue_shield', 'yodu_de', 'incognito', 'peepingdoom', 'boss_orb', 'side_kick', 'unknown_44', 'jinn_bottle', 'evilweevil', 'tempurite', 'diablos', 'gargoyle', 'grimalkin', 'hench_blue', 't_pole', 'croaker', 'amphibite', 'mad_bat', 'vamp', 'scouter', 'flyclops', 'bugger', 'debugger', 'debuggest', 'sorcerer', 'jinn', 'barghest', 'unknown_5a', 'crater', 'volcano', 'shitake', 'hetake', 'rubble', 'dream_devourer', 'shist', 'pahoehoe', 'nereid', 'save_point_enemy', 'mohavor', 'shadow', 'lavos_support_unk_67', 'base', 'acid', 'alkaline', 'ion', 'anion', 'thrasher', 'lasher', 'goblin', 'ogre', 'cave_bat', 'ogan', 'flunky', 'groupie', 'lavos_support_unk_77', 'lavos_support_unk_78', 'winged_ape', 'cave_ape', 'megasaur', 'omnicrone', 'beast', 'blue_beast', 'red_beast', 'turret', 'lizardactyl', 'nu_2', 'avian_rex', 'blob', 'alien', 'rat', 'gremlin', 'runner', 'proto_2', 'proto_3', 'proto_4', 'bug', 'beetle', 'goon', 'cyrus', 'rain_frog', 'gato', 'dragon_tank', 'grinder', 'synchrite', 'masa', 'mune', 'azala', 'flea_plus_trio', 'mutant', 'metal_mute', 'super_slash_trio', 'ozzie_zenan', 'ozzie_fort', 'great_ozzie', 'gigasaur', 'leaper', 'fossil_ape', 'tank_head', 'decedent_ii', 'octorider', 'zeal_2_center', 'zeal_2_left', 'zeal_2_right', 'display', 'blacktyrano', 'motherbrain', 'unknown_bf', 'cybot', 'lavos_guardian', 'lavos_heckran', 'lavos_zombor_upper', 'lavos_masa_mune', 'lavos_nizbel', 'tubster', 'lavos_magus', 'lavos_dragon_tank', 'lavos_2_head', 'lavos_2_left', 'lavos_2_right', 'lavos_3_core', 'guardian_bit', 'byte', 'giga_gaia_head', 'giga_gaia_left', 'giga_gaia_right', 'guardian', 'red_scout', 'blue_scout', 'laser_guard', 'lavos_tank_left_head', 'lavos_tank_right_grinder', 'lavos_guardian_left', 'lavos_guardian_right', 'lavos_zombor_bottom', 'lavos_tyrano_azala', 'spekkio_frog', 'spekkio_kilwala', 'spekkio_ogre', 'spekkio_omnicrone', 'spekkio_masa_mune', 'spekkio_nu', 'lavos_tyrano', 'lavos_giga_gaia_head', 'lavos_unk_e8', 'lavos_unk_e9', 'lavos_unk_ea', 'lavos_ocean_palace', 'lavos_1', 'lavos_3_left', 'hexapod', 'lavos_3_right', 'fake_flea', 'ozzie_magus_chains', 'roly_bomber', 'johnny', 'basher', 'r_series', 'magus', 'magus_north_cape', 'magus_no_name', 'schala', 'unused_fd', 'unused_fe', 'unused_ff'}
    default = []


class CustomDropRewardPool3(FreeText):
    """Custom rewards for group 2 drops"""
    display_name = "Custom Drop Reward Pool 3"
    default = ""


class DropEnemyPool4(Choice):
    """Pool of enemies which can have a dropped item (Group 4)"""
    display_name = "Drop Enemy Pool 4"

    option_vanilla = 0
    option_all = 1
    option_midbosses = 2
    option_bosses = 3
    option_bosses_no_lavos = 4
    option_normal_enemies = 5
    option_hard_enemies = 6
    option_custom = 7
    default = 7


class DropRewardPool4(Choice):
    """Method of choosing enemy dropped items (Group 4)"""
    display_name = "Drop Reward Pool 4"

    option_vanilla = 0
    option_shuffle = 1
    option_rdi_random = 2
    default = 0


class DropRate4(Range):
    """Percentage (decimal) of enemies in the drop pool which have a dropped item (Group 4)"""
    display_name = "Drop Rate 4"
    range_start = 0
    range_end = 100
    default = 100


class CustomDropEnemyPool4(OptionList):
    """Enemies for group 3 drops"""
    display_name = "Custom Drop Enemy Pool 4"
    valid_keys = {'krawlie', 'yakra', 'twin_boss', 'masa_mune', 'nizbel', 'nizbel_ii', 'slash', 'slash_sword', 'flea', 'dalton', 'dalton_plus', 'super_slash', 'heckran', 'flea_plus', 'rust_tyrano', 'atropos_xr', 'yakra_xiii', 'golem', 'golem_boss', 'zombor_bottom', 'zombor_top', 'lavos_spawn_shell', 'lavos_spawn_head', 'mega_mutant_head', 'mega_mutant_bottom', 'giga_mutant_head', 'giga_mutant_bottom', 'terra_mutant_head', 'terra_mutant_bottom', 'elder_spawn_shell', 'elder_spawn_head', 'retinite_eye', 'retinite_top', 'retinite_bottom', 'son_of_sun_eye', 'son_of_sun_flame', 'nu', 'reptite_green', 'terrasaur', 'kilwala', 'hench_purple', 'omicrone', 'martello', 'bellbird', 'panel', 'mammon_m', 'lavos_3_center_unk_0b', 'blue_imp', 'green_imp', 'stone_imp', 'mud_imp', 'roly', 'poly', 'rolypoly', 'roly_rider', 'lavos_giga_gaia_right', 'blue_eaglet', 'gold_eaglet', 'red_eaglet', 'lavos_giga_gaia_left', 'avian_chaos', 'imp_ace', 'bantam_imp', 'gnasher', 'gnawer', 'naga_ette', 'lavos_support_unk_1f', 'ruminator', 'lavos_support_unk_21', 'octopod', 'octoblush', 'octobino', 'zeal', 'fly_trap', 'meat_eater', 'man_eater', 'krakker', 'egder', 'defunct', 'departed', 'deceased', 'decedent', 'macabre', 'reaper', 'guard', 'sentry', 'free_lancer', 'outlaw', 'juggler', 'mage', 'unknown_3c', 'reptite_purple', 'blue_shield', 'yodu_de', 'incognito', 'peepingdoom', 'boss_orb', 'side_kick', 'unknown_44', 'jinn_bottle', 'evilweevil', 'tempurite', 'diablos', 'gargoyle', 'grimalkin', 'hench_blue', 't_pole', 'croaker', 'amphibite', 'mad_bat', 'vamp', 'scouter', 'flyclops', 'bugger', 'debugger', 'debuggest', 'sorcerer', 'jinn', 'barghest', 'unknown_5a', 'crater', 'volcano', 'shitake', 'hetake', 'rubble', 'dream_devourer', 'shist', 'pahoehoe', 'nereid', 'save_point_enemy', 'mohavor', 'shadow', 'lavos_support_unk_67', 'base', 'acid', 'alkaline', 'ion', 'anion', 'thrasher', 'lasher', 'goblin', 'ogre', 'cave_bat', 'ogan', 'flunky', 'groupie', 'lavos_support_unk_77', 'lavos_support_unk_78', 'winged_ape', 'cave_ape', 'megasaur', 'omnicrone', 'beast', 'blue_beast', 'red_beast', 'turret', 'lizardactyl', 'nu_2', 'avian_rex', 'blob', 'alien', 'rat', 'gremlin', 'runner', 'proto_2', 'proto_3', 'proto_4', 'bug', 'beetle', 'goon', 'cyrus', 'rain_frog', 'gato', 'dragon_tank', 'grinder', 'synchrite', 'masa', 'mune', 'azala', 'flea_plus_trio', 'mutant', 'metal_mute', 'super_slash_trio', 'ozzie_zenan', 'ozzie_fort', 'great_ozzie', 'gigasaur', 'leaper', 'fossil_ape', 'tank_head', 'decedent_ii', 'octorider', 'zeal_2_center', 'zeal_2_left', 'zeal_2_right', 'display', 'blacktyrano', 'motherbrain', 'unknown_bf', 'cybot', 'lavos_guardian', 'lavos_heckran', 'lavos_zombor_upper', 'lavos_masa_mune', 'lavos_nizbel', 'tubster', 'lavos_magus', 'lavos_dragon_tank', 'lavos_2_head', 'lavos_2_left', 'lavos_2_right', 'lavos_3_core', 'guardian_bit', 'byte', 'giga_gaia_head', 'giga_gaia_left', 'giga_gaia_right', 'guardian', 'red_scout', 'blue_scout', 'laser_guard', 'lavos_tank_left_head', 'lavos_tank_right_grinder', 'lavos_guardian_left', 'lavos_guardian_right', 'lavos_zombor_bottom', 'lavos_tyrano_azala', 'spekkio_frog', 'spekkio_kilwala', 'spekkio_ogre', 'spekkio_omnicrone', 'spekkio_masa_mune', 'spekkio_nu', 'lavos_tyrano', 'lavos_giga_gaia_head', 'lavos_unk_e8', 'lavos_unk_e9', 'lavos_unk_ea', 'lavos_ocean_palace', 'lavos_1', 'lavos_3_left', 'hexapod', 'lavos_3_right', 'fake_flea', 'ozzie_magus_chains', 'roly_bomber', 'johnny', 'basher', 'r_series', 'magus', 'magus_north_cape', 'magus_no_name', 'schala', 'unused_fd', 'unused_fe', 'unused_ff'}
    default = []


class CustomDropRewardPool4(FreeText):
    """Custom rewards for group 3 drops"""
    display_name = "Custom Drop Reward Pool 4"
    default = ""


class MarkDroppingEnemies(Toggle):
    """Append a "D" to enemy names which have a drop"""
    display_name = "Mark Dropping Enemies"


class CharmEnemyPool(Choice):
    """Pool of enemies which can have a charmable item (Group 1)"""
    display_name = "Charm Enemy Pool"

    option_vanilla = 0
    option_all = 1
    option_midbosses = 2
    option_bosses = 3
    option_bosses_no_lavos = 4
    option_normal_enemies = 5
    option_hard_enemies = 6
    option_custom = 7
    default = 0


class CharmRewardPool(Choice):
    """Method of choosing enemy charmable items (Group 1)"""
    display_name = "Charm Reward Pool"

    option_vanilla = 0
    option_shuffle = 1
    option_rdi_random = 2
    default = 0


class CharmRate(Range):
    """Percentage (decimal) of enemies in the charm pool which have a charmable item (Group 1)"""
    display_name = "Charm Rate"
    range_start = 0
    range_end = 100
    default = 100


class CustomCharmEnemyPool(OptionList):
    """Enemies for group 0 charms"""
    display_name = "Custom Charm Enemy Pool"
    valid_keys = {'krawlie', 'yakra', 'twin_boss', 'masa_mune', 'nizbel', 'nizbel_ii', 'slash', 'slash_sword', 'flea', 'dalton', 'dalton_plus', 'super_slash', 'heckran', 'flea_plus', 'rust_tyrano', 'atropos_xr', 'yakra_xiii', 'golem', 'golem_boss', 'zombor_bottom', 'zombor_top', 'lavos_spawn_shell', 'lavos_spawn_head', 'mega_mutant_head', 'mega_mutant_bottom', 'giga_mutant_head', 'giga_mutant_bottom', 'terra_mutant_head', 'terra_mutant_bottom', 'elder_spawn_shell', 'elder_spawn_head', 'retinite_eye', 'retinite_top', 'retinite_bottom', 'son_of_sun_eye', 'son_of_sun_flame', 'nu', 'reptite_green', 'terrasaur', 'kilwala', 'hench_purple', 'omicrone', 'martello', 'bellbird', 'panel', 'mammon_m', 'lavos_3_center_unk_0b', 'blue_imp', 'green_imp', 'stone_imp', 'mud_imp', 'roly', 'poly', 'rolypoly', 'roly_rider', 'lavos_giga_gaia_right', 'blue_eaglet', 'gold_eaglet', 'red_eaglet', 'lavos_giga_gaia_left', 'avian_chaos', 'imp_ace', 'bantam_imp', 'gnasher', 'gnawer', 'naga_ette', 'lavos_support_unk_1f', 'ruminator', 'lavos_support_unk_21', 'octopod', 'octoblush', 'octobino', 'zeal', 'fly_trap', 'meat_eater', 'man_eater', 'krakker', 'egder', 'defunct', 'departed', 'deceased', 'decedent', 'macabre', 'reaper', 'guard', 'sentry', 'free_lancer', 'outlaw', 'juggler', 'mage', 'unknown_3c', 'reptite_purple', 'blue_shield', 'yodu_de', 'incognito', 'peepingdoom', 'boss_orb', 'side_kick', 'unknown_44', 'jinn_bottle', 'evilweevil', 'tempurite', 'diablos', 'gargoyle', 'grimalkin', 'hench_blue', 't_pole', 'croaker', 'amphibite', 'mad_bat', 'vamp', 'scouter', 'flyclops', 'bugger', 'debugger', 'debuggest', 'sorcerer', 'jinn', 'barghest', 'unknown_5a', 'crater', 'volcano', 'shitake', 'hetake', 'rubble', 'dream_devourer', 'shist', 'pahoehoe', 'nereid', 'save_point_enemy', 'mohavor', 'shadow', 'lavos_support_unk_67', 'base', 'acid', 'alkaline', 'ion', 'anion', 'thrasher', 'lasher', 'goblin', 'ogre', 'cave_bat', 'ogan', 'flunky', 'groupie', 'lavos_support_unk_77', 'lavos_support_unk_78', 'winged_ape', 'cave_ape', 'megasaur', 'omnicrone', 'beast', 'blue_beast', 'red_beast', 'turret', 'lizardactyl', 'nu_2', 'avian_rex', 'blob', 'alien', 'rat', 'gremlin', 'runner', 'proto_2', 'proto_3', 'proto_4', 'bug', 'beetle', 'goon', 'cyrus', 'rain_frog', 'gato', 'dragon_tank', 'grinder', 'synchrite', 'masa', 'mune', 'azala', 'flea_plus_trio', 'mutant', 'metal_mute', 'super_slash_trio', 'ozzie_zenan', 'ozzie_fort', 'great_ozzie', 'gigasaur', 'leaper', 'fossil_ape', 'tank_head', 'decedent_ii', 'octorider', 'zeal_2_center', 'zeal_2_left', 'zeal_2_right', 'display', 'blacktyrano', 'motherbrain', 'unknown_bf', 'cybot', 'lavos_guardian', 'lavos_heckran', 'lavos_zombor_upper', 'lavos_masa_mune', 'lavos_nizbel', 'tubster', 'lavos_magus', 'lavos_dragon_tank', 'lavos_2_head', 'lavos_2_left', 'lavos_2_right', 'lavos_3_core', 'guardian_bit', 'byte', 'giga_gaia_head', 'giga_gaia_left', 'giga_gaia_right', 'guardian', 'red_scout', 'blue_scout', 'laser_guard', 'lavos_tank_left_head', 'lavos_tank_right_grinder', 'lavos_guardian_left', 'lavos_guardian_right', 'lavos_zombor_bottom', 'lavos_tyrano_azala', 'spekkio_frog', 'spekkio_kilwala', 'spekkio_ogre', 'spekkio_omnicrone', 'spekkio_masa_mune', 'spekkio_nu', 'lavos_tyrano', 'lavos_giga_gaia_head', 'lavos_unk_e8', 'lavos_unk_e9', 'lavos_unk_ea', 'lavos_ocean_palace', 'lavos_1', 'lavos_3_left', 'hexapod', 'lavos_3_right', 'fake_flea', 'ozzie_magus_chains', 'roly_bomber', 'johnny', 'basher', 'r_series', 'magus', 'magus_north_cape', 'magus_no_name', 'schala', 'unused_fd', 'unused_fe', 'unused_ff'}
    default = []


class CustomCharmRewardPool(FreeText):
    """Custom rewards for group 0 charms"""
    display_name = "Custom Charm Reward Pool"
    default = ""


class CharmEnemyPool2(Choice):
    """Pool of enemies which can have a charmable item (Group 2)"""
    display_name = "Charm Enemy Pool 2"

    option_vanilla = 0
    option_all = 1
    option_midbosses = 2
    option_bosses = 3
    option_bosses_no_lavos = 4
    option_normal_enemies = 5
    option_hard_enemies = 6
    option_custom = 7
    default = 7


class CharmRewardPool2(Choice):
    """Method of choosing enemy charmable items (Group 2)"""
    display_name = "Charm Reward Pool 2"

    option_vanilla = 0
    option_shuffle = 1
    option_rdi_random = 2
    default = 0


class CharmRate2(Range):
    """Percentage (decimal) of enemies in the charm pool which have a charmable item (Group 2)"""
    display_name = "Charm Rate 2"
    range_start = 0
    range_end = 100
    default = 100


class CustomCharmEnemyPool2(OptionList):
    """Enemies for group 1 charms"""
    display_name = "Custom Charm Enemy Pool 2"
    valid_keys = {'krawlie', 'yakra', 'twin_boss', 'masa_mune', 'nizbel', 'nizbel_ii', 'slash', 'slash_sword', 'flea', 'dalton', 'dalton_plus', 'super_slash', 'heckran', 'flea_plus', 'rust_tyrano', 'atropos_xr', 'yakra_xiii', 'golem', 'golem_boss', 'zombor_bottom', 'zombor_top', 'lavos_spawn_shell', 'lavos_spawn_head', 'mega_mutant_head', 'mega_mutant_bottom', 'giga_mutant_head', 'giga_mutant_bottom', 'terra_mutant_head', 'terra_mutant_bottom', 'elder_spawn_shell', 'elder_spawn_head', 'retinite_eye', 'retinite_top', 'retinite_bottom', 'son_of_sun_eye', 'son_of_sun_flame', 'nu', 'reptite_green', 'terrasaur', 'kilwala', 'hench_purple', 'omicrone', 'martello', 'bellbird', 'panel', 'mammon_m', 'lavos_3_center_unk_0b', 'blue_imp', 'green_imp', 'stone_imp', 'mud_imp', 'roly', 'poly', 'rolypoly', 'roly_rider', 'lavos_giga_gaia_right', 'blue_eaglet', 'gold_eaglet', 'red_eaglet', 'lavos_giga_gaia_left', 'avian_chaos', 'imp_ace', 'bantam_imp', 'gnasher', 'gnawer', 'naga_ette', 'lavos_support_unk_1f', 'ruminator', 'lavos_support_unk_21', 'octopod', 'octoblush', 'octobino', 'zeal', 'fly_trap', 'meat_eater', 'man_eater', 'krakker', 'egder', 'defunct', 'departed', 'deceased', 'decedent', 'macabre', 'reaper', 'guard', 'sentry', 'free_lancer', 'outlaw', 'juggler', 'mage', 'unknown_3c', 'reptite_purple', 'blue_shield', 'yodu_de', 'incognito', 'peepingdoom', 'boss_orb', 'side_kick', 'unknown_44', 'jinn_bottle', 'evilweevil', 'tempurite', 'diablos', 'gargoyle', 'grimalkin', 'hench_blue', 't_pole', 'croaker', 'amphibite', 'mad_bat', 'vamp', 'scouter', 'flyclops', 'bugger', 'debugger', 'debuggest', 'sorcerer', 'jinn', 'barghest', 'unknown_5a', 'crater', 'volcano', 'shitake', 'hetake', 'rubble', 'dream_devourer', 'shist', 'pahoehoe', 'nereid', 'save_point_enemy', 'mohavor', 'shadow', 'lavos_support_unk_67', 'base', 'acid', 'alkaline', 'ion', 'anion', 'thrasher', 'lasher', 'goblin', 'ogre', 'cave_bat', 'ogan', 'flunky', 'groupie', 'lavos_support_unk_77', 'lavos_support_unk_78', 'winged_ape', 'cave_ape', 'megasaur', 'omnicrone', 'beast', 'blue_beast', 'red_beast', 'turret', 'lizardactyl', 'nu_2', 'avian_rex', 'blob', 'alien', 'rat', 'gremlin', 'runner', 'proto_2', 'proto_3', 'proto_4', 'bug', 'beetle', 'goon', 'cyrus', 'rain_frog', 'gato', 'dragon_tank', 'grinder', 'synchrite', 'masa', 'mune', 'azala', 'flea_plus_trio', 'mutant', 'metal_mute', 'super_slash_trio', 'ozzie_zenan', 'ozzie_fort', 'great_ozzie', 'gigasaur', 'leaper', 'fossil_ape', 'tank_head', 'decedent_ii', 'octorider', 'zeal_2_center', 'zeal_2_left', 'zeal_2_right', 'display', 'blacktyrano', 'motherbrain', 'unknown_bf', 'cybot', 'lavos_guardian', 'lavos_heckran', 'lavos_zombor_upper', 'lavos_masa_mune', 'lavos_nizbel', 'tubster', 'lavos_magus', 'lavos_dragon_tank', 'lavos_2_head', 'lavos_2_left', 'lavos_2_right', 'lavos_3_core', 'guardian_bit', 'byte', 'giga_gaia_head', 'giga_gaia_left', 'giga_gaia_right', 'guardian', 'red_scout', 'blue_scout', 'laser_guard', 'lavos_tank_left_head', 'lavos_tank_right_grinder', 'lavos_guardian_left', 'lavos_guardian_right', 'lavos_zombor_bottom', 'lavos_tyrano_azala', 'spekkio_frog', 'spekkio_kilwala', 'spekkio_ogre', 'spekkio_omnicrone', 'spekkio_masa_mune', 'spekkio_nu', 'lavos_tyrano', 'lavos_giga_gaia_head', 'lavos_unk_e8', 'lavos_unk_e9', 'lavos_unk_ea', 'lavos_ocean_palace', 'lavos_1', 'lavos_3_left', 'hexapod', 'lavos_3_right', 'fake_flea', 'ozzie_magus_chains', 'roly_bomber', 'johnny', 'basher', 'r_series', 'magus', 'magus_north_cape', 'magus_no_name', 'schala', 'unused_fd', 'unused_fe', 'unused_ff'}
    default = []


class CustomCharmRewardPool2(FreeText):
    """Custom rewards for group 1 charms"""
    display_name = "Custom Charm Reward Pool 2"
    default = ""


class CharmEnemyPool3(Choice):
    """Pool of enemies which can have a charmable item (Group 3)"""
    display_name = "Charm Enemy Pool 3"

    option_vanilla = 0
    option_all = 1
    option_midbosses = 2
    option_bosses = 3
    option_bosses_no_lavos = 4
    option_normal_enemies = 5
    option_hard_enemies = 6
    option_custom = 7
    default = 7


class CharmRewardPool3(Choice):
    """Method of choosing enemy charmable items (Group 3)"""
    display_name = "Charm Reward Pool 3"

    option_vanilla = 0
    option_shuffle = 1
    option_rdi_random = 2
    default = 0


class CharmRate3(Range):
    """Percentage (decimal) of enemies in the charm pool which have a charmable item (Group 3)"""
    display_name = "Charm Rate 3"
    range_start = 0
    range_end = 100
    default = 100


class CustomCharmEnemyPool3(OptionList):
    """Enemies for group 2 charms"""
    display_name = "Custom Charm Enemy Pool 3"
    valid_keys = {'krawlie', 'yakra', 'twin_boss', 'masa_mune', 'nizbel', 'nizbel_ii', 'slash', 'slash_sword', 'flea', 'dalton', 'dalton_plus', 'super_slash', 'heckran', 'flea_plus', 'rust_tyrano', 'atropos_xr', 'yakra_xiii', 'golem', 'golem_boss', 'zombor_bottom', 'zombor_top', 'lavos_spawn_shell', 'lavos_spawn_head', 'mega_mutant_head', 'mega_mutant_bottom', 'giga_mutant_head', 'giga_mutant_bottom', 'terra_mutant_head', 'terra_mutant_bottom', 'elder_spawn_shell', 'elder_spawn_head', 'retinite_eye', 'retinite_top', 'retinite_bottom', 'son_of_sun_eye', 'son_of_sun_flame', 'nu', 'reptite_green', 'terrasaur', 'kilwala', 'hench_purple', 'omicrone', 'martello', 'bellbird', 'panel', 'mammon_m', 'lavos_3_center_unk_0b', 'blue_imp', 'green_imp', 'stone_imp', 'mud_imp', 'roly', 'poly', 'rolypoly', 'roly_rider', 'lavos_giga_gaia_right', 'blue_eaglet', 'gold_eaglet', 'red_eaglet', 'lavos_giga_gaia_left', 'avian_chaos', 'imp_ace', 'bantam_imp', 'gnasher', 'gnawer', 'naga_ette', 'lavos_support_unk_1f', 'ruminator', 'lavos_support_unk_21', 'octopod', 'octoblush', 'octobino', 'zeal', 'fly_trap', 'meat_eater', 'man_eater', 'krakker', 'egder', 'defunct', 'departed', 'deceased', 'decedent', 'macabre', 'reaper', 'guard', 'sentry', 'free_lancer', 'outlaw', 'juggler', 'mage', 'unknown_3c', 'reptite_purple', 'blue_shield', 'yodu_de', 'incognito', 'peepingdoom', 'boss_orb', 'side_kick', 'unknown_44', 'jinn_bottle', 'evilweevil', 'tempurite', 'diablos', 'gargoyle', 'grimalkin', 'hench_blue', 't_pole', 'croaker', 'amphibite', 'mad_bat', 'vamp', 'scouter', 'flyclops', 'bugger', 'debugger', 'debuggest', 'sorcerer', 'jinn', 'barghest', 'unknown_5a', 'crater', 'volcano', 'shitake', 'hetake', 'rubble', 'dream_devourer', 'shist', 'pahoehoe', 'nereid', 'save_point_enemy', 'mohavor', 'shadow', 'lavos_support_unk_67', 'base', 'acid', 'alkaline', 'ion', 'anion', 'thrasher', 'lasher', 'goblin', 'ogre', 'cave_bat', 'ogan', 'flunky', 'groupie', 'lavos_support_unk_77', 'lavos_support_unk_78', 'winged_ape', 'cave_ape', 'megasaur', 'omnicrone', 'beast', 'blue_beast', 'red_beast', 'turret', 'lizardactyl', 'nu_2', 'avian_rex', 'blob', 'alien', 'rat', 'gremlin', 'runner', 'proto_2', 'proto_3', 'proto_4', 'bug', 'beetle', 'goon', 'cyrus', 'rain_frog', 'gato', 'dragon_tank', 'grinder', 'synchrite', 'masa', 'mune', 'azala', 'flea_plus_trio', 'mutant', 'metal_mute', 'super_slash_trio', 'ozzie_zenan', 'ozzie_fort', 'great_ozzie', 'gigasaur', 'leaper', 'fossil_ape', 'tank_head', 'decedent_ii', 'octorider', 'zeal_2_center', 'zeal_2_left', 'zeal_2_right', 'display', 'blacktyrano', 'motherbrain', 'unknown_bf', 'cybot', 'lavos_guardian', 'lavos_heckran', 'lavos_zombor_upper', 'lavos_masa_mune', 'lavos_nizbel', 'tubster', 'lavos_magus', 'lavos_dragon_tank', 'lavos_2_head', 'lavos_2_left', 'lavos_2_right', 'lavos_3_core', 'guardian_bit', 'byte', 'giga_gaia_head', 'giga_gaia_left', 'giga_gaia_right', 'guardian', 'red_scout', 'blue_scout', 'laser_guard', 'lavos_tank_left_head', 'lavos_tank_right_grinder', 'lavos_guardian_left', 'lavos_guardian_right', 'lavos_zombor_bottom', 'lavos_tyrano_azala', 'spekkio_frog', 'spekkio_kilwala', 'spekkio_ogre', 'spekkio_omnicrone', 'spekkio_masa_mune', 'spekkio_nu', 'lavos_tyrano', 'lavos_giga_gaia_head', 'lavos_unk_e8', 'lavos_unk_e9', 'lavos_unk_ea', 'lavos_ocean_palace', 'lavos_1', 'lavos_3_left', 'hexapod', 'lavos_3_right', 'fake_flea', 'ozzie_magus_chains', 'roly_bomber', 'johnny', 'basher', 'r_series', 'magus', 'magus_north_cape', 'magus_no_name', 'schala', 'unused_fd', 'unused_fe', 'unused_ff'}
    default = []


class CustomCharmRewardPool3(FreeText):
    """Custom rewards for group 2 charms"""
    display_name = "Custom Charm Reward Pool 3"
    default = ""


class CharmEnemyPool4(Choice):
    """Pool of enemies which can have a charmable item (Group 4)"""
    display_name = "Charm Enemy Pool 4"

    option_vanilla = 0
    option_all = 1
    option_midbosses = 2
    option_bosses = 3
    option_bosses_no_lavos = 4
    option_normal_enemies = 5
    option_hard_enemies = 6
    option_custom = 7
    default = 7


class CharmRewardPool4(Choice):
    """Method of choosing enemy charmable items (Group 4)"""
    display_name = "Charm Reward Pool 4"

    option_vanilla = 0
    option_shuffle = 1
    option_rdi_random = 2
    default = 0


class CharmRate4(Range):
    """Percentage (decimal) of enemies in the charm pool which have a charmable item (Group 4)"""
    display_name = "Charm Rate 4"
    range_start = 0
    range_end = 100
    default = 100


class CustomCharmEnemyPool4(OptionList):
    """Enemies for group 3 charms"""
    display_name = "Custom Charm Enemy Pool 4"
    valid_keys = {'krawlie', 'yakra', 'twin_boss', 'masa_mune', 'nizbel', 'nizbel_ii', 'slash', 'slash_sword', 'flea', 'dalton', 'dalton_plus', 'super_slash', 'heckran', 'flea_plus', 'rust_tyrano', 'atropos_xr', 'yakra_xiii', 'golem', 'golem_boss', 'zombor_bottom', 'zombor_top', 'lavos_spawn_shell', 'lavos_spawn_head', 'mega_mutant_head', 'mega_mutant_bottom', 'giga_mutant_head', 'giga_mutant_bottom', 'terra_mutant_head', 'terra_mutant_bottom', 'elder_spawn_shell', 'elder_spawn_head', 'retinite_eye', 'retinite_top', 'retinite_bottom', 'son_of_sun_eye', 'son_of_sun_flame', 'nu', 'reptite_green', 'terrasaur', 'kilwala', 'hench_purple', 'omicrone', 'martello', 'bellbird', 'panel', 'mammon_m', 'lavos_3_center_unk_0b', 'blue_imp', 'green_imp', 'stone_imp', 'mud_imp', 'roly', 'poly', 'rolypoly', 'roly_rider', 'lavos_giga_gaia_right', 'blue_eaglet', 'gold_eaglet', 'red_eaglet', 'lavos_giga_gaia_left', 'avian_chaos', 'imp_ace', 'bantam_imp', 'gnasher', 'gnawer', 'naga_ette', 'lavos_support_unk_1f', 'ruminator', 'lavos_support_unk_21', 'octopod', 'octoblush', 'octobino', 'zeal', 'fly_trap', 'meat_eater', 'man_eater', 'krakker', 'egder', 'defunct', 'departed', 'deceased', 'decedent', 'macabre', 'reaper', 'guard', 'sentry', 'free_lancer', 'outlaw', 'juggler', 'mage', 'unknown_3c', 'reptite_purple', 'blue_shield', 'yodu_de', 'incognito', 'peepingdoom', 'boss_orb', 'side_kick', 'unknown_44', 'jinn_bottle', 'evilweevil', 'tempurite', 'diablos', 'gargoyle', 'grimalkin', 'hench_blue', 't_pole', 'croaker', 'amphibite', 'mad_bat', 'vamp', 'scouter', 'flyclops', 'bugger', 'debugger', 'debuggest', 'sorcerer', 'jinn', 'barghest', 'unknown_5a', 'crater', 'volcano', 'shitake', 'hetake', 'rubble', 'dream_devourer', 'shist', 'pahoehoe', 'nereid', 'save_point_enemy', 'mohavor', 'shadow', 'lavos_support_unk_67', 'base', 'acid', 'alkaline', 'ion', 'anion', 'thrasher', 'lasher', 'goblin', 'ogre', 'cave_bat', 'ogan', 'flunky', 'groupie', 'lavos_support_unk_77', 'lavos_support_unk_78', 'winged_ape', 'cave_ape', 'megasaur', 'omnicrone', 'beast', 'blue_beast', 'red_beast', 'turret', 'lizardactyl', 'nu_2', 'avian_rex', 'blob', 'alien', 'rat', 'gremlin', 'runner', 'proto_2', 'proto_3', 'proto_4', 'bug', 'beetle', 'goon', 'cyrus', 'rain_frog', 'gato', 'dragon_tank', 'grinder', 'synchrite', 'masa', 'mune', 'azala', 'flea_plus_trio', 'mutant', 'metal_mute', 'super_slash_trio', 'ozzie_zenan', 'ozzie_fort', 'great_ozzie', 'gigasaur', 'leaper', 'fossil_ape', 'tank_head', 'decedent_ii', 'octorider', 'zeal_2_center', 'zeal_2_left', 'zeal_2_right', 'display', 'blacktyrano', 'motherbrain', 'unknown_bf', 'cybot', 'lavos_guardian', 'lavos_heckran', 'lavos_zombor_upper', 'lavos_masa_mune', 'lavos_nizbel', 'tubster', 'lavos_magus', 'lavos_dragon_tank', 'lavos_2_head', 'lavos_2_left', 'lavos_2_right', 'lavos_3_core', 'guardian_bit', 'byte', 'giga_gaia_head', 'giga_gaia_left', 'giga_gaia_right', 'guardian', 'red_scout', 'blue_scout', 'laser_guard', 'lavos_tank_left_head', 'lavos_tank_right_grinder', 'lavos_guardian_left', 'lavos_guardian_right', 'lavos_zombor_bottom', 'lavos_tyrano_azala', 'spekkio_frog', 'spekkio_kilwala', 'spekkio_ogre', 'spekkio_omnicrone', 'spekkio_masa_mune', 'spekkio_nu', 'lavos_tyrano', 'lavos_giga_gaia_head', 'lavos_unk_e8', 'lavos_unk_e9', 'lavos_unk_ea', 'lavos_ocean_palace', 'lavos_1', 'lavos_3_left', 'hexapod', 'lavos_3_right', 'fake_flea', 'ozzie_magus_chains', 'roly_bomber', 'johnny', 'basher', 'r_series', 'magus', 'magus_north_cape', 'magus_no_name', 'schala', 'unused_fd', 'unused_fe', 'unused_ff'}
    default = []


class CustomCharmRewardPool4(FreeText):
    """Custom rewards for group 3 charms"""
    display_name = "Custom Charm Reward Pool 4"
    default = ""


class MarkCharmableEnemies(Toggle):
    """Alter enemy names to indicate a charmable item"""
    display_name = "Mark Charmable Enemies"


class TechOrder(Choice):
    """Order in which techs are learned"""
    display_name = "Tech Order"

    option_vanilla = 0
    option_rdi_random = 1
    option_mp = 2
    option_mp_type = 3
    default = 0


class TechDamage(Choice):
    """Damage dealt by techs"""
    display_name = "Tech Damage"

    option_vanilla = 0
    option_shuffle = 1
    option_rdi_random = 2
    default = 0


class TechDamageRandomFactorMin(Range):
    """Minimum percent (as decimal, default 1.0) which MP costs may shift (ignored if vanilla damage)"""
    display_name = "Tech Damage Random Factor Min"
    range_start = 5
    range_end = 200
    default = 100


class TechDamageRandomFactorMax(Range):
    """Maximum percent (as decimal, default 1.0) which MP costs may shift (ignored if vanilla damage)"""
    display_name = "Tech Damage Random Factor Max"
    range_start = 5
    range_end = 200
    default = 100


class PreserveMagic(Toggle):
    """Keep each PC's first magic tech in its vanilla location (may break specified order)"""
    display_name = "Preserve Magic"


class BlackHoleFactor(Range):
    """Percent kill chance per MP in black hole's cost"""
    display_name = "Black Hole Factor"
    range_start = 0
    range_end = 1000
    default = 200


class BlackHoleMin(Range):
    """Base percent kill chance for black hole, total is base + mp*factor"""
    display_name = "Black Hole Min"
    range_start = 0
    range_end = 10000
    default = 1000


class ShowFullTechList(Toggle):
    """The tech page of the menu will show all single techs"""
    display_name = "Show Full Tech List"


class BalanceTechMps(Toggle):
    """Ensure every character has at least one strong tech."""
    display_name = "Balance Tech Mps"


class CustomDamageMps(OptionList):
    """Custom pool of mps for damage techs"""
    display_name = "Custom Damage Mps"
    valid_keys = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'}
    default = []


class NormalizeTechs(Toggle):
    """Modify tech powers and costs to balance tech utility"""
    display_name = "Normalize Techs"


class DynamicScalingScheme(Choice):
    """Method for dynamically scaling enemies"""
    display_name = "Dynamic Scaling Scheme"

    option_none = 0
    option_progression = 1
    option_logic_depth = 2
    default = 1


class LevelsPerBoss(Range):
    """Scaling levels gained per boss defeated"""
    display_name = "Levels Per Boss"
    range_start = 0
    range_end = 1000
    default = 200


class LevelsPerQuest(Range):
    """Scaling levels gained per quest completed"""
    display_name = "Levels Per Quest"
    range_start = 0
    range_end = 1000
    default = 200


class LevelsPerKeyItem(Range):
    """Scaling levels gained per key item obtained"""
    display_name = "Levels Per Key Item"
    range_start = 0
    range_end = 1000
    default = 0


class LevelsPerObjective(Range):
    """Scaling levels gained per objective completed"""
    display_name = "Levels Per Objective"
    range_start = 0
    range_end = 1000
    default = 200


class LevelsPerCharacter(Range):
    """Scaling levels gained per character recruited"""
    display_name = "Levels Per Character"
    range_start = 0
    range_end = 1000
    default = 200


class MaxScalingLevel(Range):
    """Maximum level to scale to (if not none)"""
    display_name = "Max Scaling Level"
    range_start = 1
    range_end = 99
    default = 50


class DynamicScaleLavos(Toggle):
    """Include Lavos in the dynamic scaling (if not none)"""
    display_name = "Dynamic Scale Lavos"


class DynamicScaleLavosGauntlet(Toggle):
    """Include Lavos attack modes in the dynamic scaling (if not none)"""
    display_name = "Dynamic Scale Lavos Gauntlet"


class DefenseSafetyMinLevel(Range):
    """Level before which enemies have standard phys defense"""
    display_name = "Defense Safety Min Level"
    range_start = 1
    range_end = 99
    default = 10


class DefenseSafetyMaxLevel(Range):
    """Level after which enemies have their normal phys defense"""
    display_name = "Defense Safety Max Level"
    range_start = 1
    range_end = 99
    default = 30


class ObstacleSafetyLevel(Range):
    """Level before which Obstacle is single target"""
    display_name = "Obstacle Safety Level"
    range_start = 1
    range_end = 99
    default = 30


class NormalEnemyHpScale(Range):
    """Multiply non-boss enemy hp by this factor"""
    display_name = "Normal Enemy Hp Scale"
    range_start = 5
    range_end = 200
    default = 100


class StaticBossHpScale(Range):
    """Multiply boss hp by this factor"""
    display_name = "Static Boss Hp Scale"
    range_start = 5
    range_end = 200
    default = 75


class StaticHpScaleLavos(Toggle):
    """Apply static hp scaling to lavos"""
    display_name = "Static Hp Scale Lavos"


class ElementSafetyLevel(Range):
    """Before this level any magic hits Nizbel/Retinite weakness"""
    display_name = "Element Safety Level"
    range_start = 1
    range_end = 99
    default = 30


class MillennialFairMod(Range):
    """Additional scaling levels for millennial_fair"""
    display_name = "Millennial Fair Mod"
    range_start = -50
    range_end = 50
    default = 0


class GuardiaForest1000Mod(Range):
    """Additional scaling levels for guardia_forest_1000"""
    display_name = "Guardia Forest 1000 Mod"
    range_start = -50
    range_end = 50
    default = 0


class GuardiaForest600Mod(Range):
    """Additional scaling levels for guardia_forest_600"""
    display_name = "Guardia Forest 600 Mod"
    range_start = -50
    range_end = 50
    default = 0


class CronoTrialMod(Range):
    """Additional scaling levels for crono_trial"""
    display_name = "Crono Trial Mod"
    range_start = -50
    range_end = 50
    default = 0


class HeckranCaveMod(Range):
    """Additional scaling levels for heckran_cave"""
    display_name = "Heckran Cave Mod"
    range_start = -50
    range_end = 50
    default = 0


class TruceCanyonMod(Range):
    """Additional scaling levels for truce_canyon"""
    display_name = "Truce Canyon Mod"
    range_start = -50
    range_end = 50
    default = 0


class ManoriaCathedralMod(Range):
    """Additional scaling levels for manoria_cathedral"""
    display_name = "Manoria Cathedral Mod"
    range_start = -50
    range_end = 50
    default = 0


class DenadoroMountainsMod(Range):
    """Additional scaling levels for denadoro_mountains"""
    display_name = "Denadoro Mountains Mod"
    range_start = -50
    range_end = 50
    default = 0


class CursedWoodsMod(Range):
    """Additional scaling levels for cursed_woods"""
    display_name = "Cursed Woods Mod"
    range_start = -50
    range_end = 50
    default = 0


class Lab16Mod(Range):
    """Additional scaling levels for lab_16"""
    display_name = "Lab 16 Mod"
    range_start = -50
    range_end = 50
    default = 0


class Lab32Mod(Range):
    """Additional scaling levels for lab_32"""
    display_name = "Lab 32 Mod"
    range_start = -50
    range_end = 50
    default = 0


class SewersMod(Range):
    """Additional scaling levels for sewers"""
    display_name = "Sewers Mod"
    range_start = -50
    range_end = 50
    default = 0


class DeathPeakMod(Range):
    """Additional scaling levels for death_peak"""
    display_name = "Death Peak Mod"
    range_start = -50
    range_end = 50
    default = 0


class ArrisDomeMod(Range):
    """Additional scaling levels for arris_dome"""
    display_name = "Arris Dome Mod"
    range_start = -50
    range_end = 50
    default = 0


class ProtoDomeMod(Range):
    """Additional scaling levels for proto_dome"""
    display_name = "Proto Dome Mod"
    range_start = -50
    range_end = 50
    default = 0


class FactoryRuinsMod(Range):
    """Additional scaling levels for factory_ruins"""
    display_name = "Factory Ruins Mod"
    range_start = -50
    range_end = 50
    default = 0


class MysticMountainsMod(Range):
    """Additional scaling levels for mystic_mountains"""
    display_name = "Mystic Mountains Mod"
    range_start = -50
    range_end = 50
    default = 0


class HuntingRangeMod(Range):
    """Additional scaling levels for hunting_range"""
    display_name = "Hunting Range Mod"
    range_start = -50
    range_end = 50
    default = 0


class DactylNestMod(Range):
    """Additional scaling levels for dactyl_nest"""
    display_name = "Dactyl Nest Mod"
    range_start = -50
    range_end = 50
    default = 0


class ShellTrialMod(Range):
    """Additional scaling levels for shell_trial"""
    display_name = "Shell Trial Mod"
    range_start = -50
    range_end = 50
    default = 0


class ZenanBridgeMod(Range):
    """Additional scaling levels for zenan_bridge"""
    display_name = "Zenan Bridge Mod"
    range_start = -50
    range_end = 50
    default = 0


class NorthernRuinsMod(Range):
    """Additional scaling levels for northern_ruins"""
    display_name = "Northern Ruins Mod"
    range_start = -50
    range_end = 50
    default = 0


class GiantsClawMod(Range):
    """Additional scaling levels for giants_claw"""
    display_name = "Giants Claw Mod"
    range_start = -50
    range_end = 50
    default = 0


class OzziesFortMod(Range):
    """Additional scaling levels for ozzies_fort"""
    display_name = "Ozzies Fort Mod"
    range_start = -50
    range_end = 50
    default = 0


class MagusCastleMod(Range):
    """Additional scaling levels for magus_castle"""
    display_name = "Magus Castle Mod"
    range_start = -50
    range_end = 50
    default = 0


class MagicCaveMod(Range):
    """Additional scaling levels for magic_cave"""
    display_name = "Magic Cave Mod"
    range_start = -50
    range_end = 50
    default = 0


class SunkenDesertMod(Range):
    """Additional scaling levels for sunken_desert"""
    display_name = "Sunken Desert Mod"
    range_start = -50
    range_end = 50
    default = 0


class SunPalaceMod(Range):
    """Additional scaling levels for sun_palace"""
    display_name = "Sun Palace Mod"
    range_start = -50
    range_end = 50
    default = 0


class GenoDomeMod(Range):
    """Additional scaling levels for geno_dome"""
    display_name = "Geno Dome Mod"
    range_start = -50
    range_end = 50
    default = 0


class ForestMazeMod(Range):
    """Additional scaling levels for forest_maze"""
    display_name = "Forest Maze Mod"
    range_start = -50
    range_end = 50
    default = 0


class ReptiteLairMod(Range):
    """Additional scaling levels for reptite_lair"""
    display_name = "Reptite Lair Mod"
    range_start = -50
    range_end = 50
    default = 0


class TyranoLairMod(Range):
    """Additional scaling levels for tyrano_lair"""
    display_name = "Tyrano Lair Mod"
    range_start = -50
    range_end = 50
    default = 0


class BlackOmenMod(Range):
    """Additional scaling levels for black_omen"""
    display_name = "Black Omen Mod"
    range_start = -50
    range_end = 50
    default = 0


class NorthCapeMod(Range):
    """Additional scaling levels for north_cape"""
    display_name = "North Cape Mod"
    range_start = -50
    range_end = 50
    default = 0


class EpochBattleMod(Range):
    """Additional scaling levels for epoch_battle"""
    display_name = "Epoch Battle Mod"
    range_start = -50
    range_end = 50
    default = 0


class BlackbirdMod(Range):
    """Additional scaling levels for blackbird"""
    display_name = "Blackbird Mod"
    range_start = -50
    range_end = 50
    default = 0


class EnhasaMod(Range):
    """Additional scaling levels for enhasa"""
    display_name = "Enhasa Mod"
    range_start = -50
    range_end = 50
    default = 0


class OceanPalaceMod(Range):
    """Additional scaling levels for ocean_palace"""
    display_name = "Ocean Palace Mod"
    range_start = -50
    range_end = 50
    default = 0


class MtWoeMod(Range):
    """Additional scaling levels for mt_woe"""
    display_name = "Mt Woe Mod"
    range_start = -50
    range_end = 50
    default = 0


class AdditionalKeyItems(OptionList):
    """Extra (non-progression) items to add to the key item pool"""
    display_name = "Additional Key Items"
    valid_keys = {'wood_sword', 'iron_blade', 'steelsaber', 'lode_sword', 'red_katana', 'flint_edge', 'dark_saber', 'aeon_blade', 'demon_edge', 'alloyblade', 'star_sword', 'vedicblade', 'kali_blade', 'shiva_edge', 'bolt_sword', 'slasher', 'bronze_bow', 'iron_bow', 'lode_bow', 'robin_bow', 'sage_bow', 'dream_bow', 'cometarrow', 'sonicarrow', 'valkerye', 'siren', 'air_gun', 'dart_gun', 'auto_gun', 'picomagnum', 'plasma_gun', 'ruby_gun', 'dream_gun', 'megablast', 'shock_wave', 'wondershot', 'graedus', 'tin_arm', 'hammer_arm', 'miragehand', 'stone_arm', 'doomfinger', 'magma_hand', 'megatonarm', 'big_hand', 'kaiser_arm', 'giga_arm', 'terra_arm', 'crisis_arm', 'bronzeedge', 'iron_sword', 'masamune_1', 'flashblade', 'pearl_edge', 'rune_blade', 'bravesword', 'masamune_2', 'demon_hit', 'fist', 'fist_2', 'fist_3', 'iron_fist', 'bronzefist', 'pacifist', 'darkscythe', 'hurricane', 'starscythe', 'doomsickle', 'mop', 'bent_sword', 'bent_hilt', 'swallow', 'slasher_2', 'rainbow', 'hide_tunic', 'karate_gi', 'bronzemail', 'maidensuit', 'iron_suit', 'titan_vest', 'gold_suit', 'ruby_vest', 'dark_mail', 'mist_robe', 'meso_mail', 'lumin_robe', 'flash_mail', 'lode_vest', 'aeon_suit', 'zodiaccape', 'nova_armor', 'prismdress', 'moon_armor', 'ruby_armor', 'ravenarmor', 'gloom_cape', 'white_mail', 'black_mail', 'blue_mail', 'red_mail', 'white_vest', 'black_vest', 'blue_vest', 'red_vest', 'taban_vest', 'taban_suit', 'hide_cap', 'bronzehelm', 'iron_helm', 'beret', 'gold_helm', 'rock_helm', 'ceratopper', 'glow_helm', 'lode_helm', 'aeon_helm', 'prism_helm', 'doom_helm', 'dark_helm', 'gloom_helm', 'safe_helm', 'taban_helm', 'sight_cap', 'memory_cap', 'time_hat', 'vigil_hat', 'ozziepants', 'haste_helm', 'rbow_helm', 'mermaidcap', 'bandana', 'ribbon', 'powerglove', 'defender', 'magicscarf', 'amulet', 'dash_ring', 'hit_ring', 'power_ring', 'magic_ring', 'wall_ring', 'silvererng', 'gold_erng', 'silverstud', 'gold_stud', 'sightscope', 'charm_top', 'rage_band', 'frenzyband', 'third_eye', 'wallet', 'greendream', 'berserker', 'powerscarf', 'speed_belt', 'black_rock', 'blue_rock', 'silverrock', 'white_rock', 'gold_rock', 'hero_medal', 'musclering', 'flea_vest', 'magic_seal', 'power_seal', 'valor_crest', 'dragon_tear', 'sun_shades', 'prismspecs', 'tonic', 'mid_tonic', 'full_tonic', 'ether', 'mid_ether', 'full_ether', 'elixir', 'hyperether', 'megaelixir', 'heal', 'revive', 'shelter', 'power_meal', 'lapis', 'barrier', 'shield', 'power_tab', 'magic_tab', 'speed_tab', 'petal', 'fang', 'horn', 'feather', 'seed', 'bike_key', 'pendant', 'gate_key', 'prismshard', 'c_trigger', 'tools', 'jerky', 'dreamstone', 'race_log', 'moon_stone', 'sun_stone', 'ruby_knife', 'yakra_key', 'clone', 'tomas_pop', 'petals_2', 'fangs_2', 'horns_2', 'feathers_2', 'jetsoftime', 'pendant_charge', 'rainbow_shell'}
    default = []


class ForcedSpots(OptionList):
    """Spots forced to have key items (if enough KIs)"""
    display_name = "Forced Spots"
    valid_keys = {'mt_woe_1st_screen', 'mt_woe_2nd_screen_1', 'mt_woe_2nd_screen_2', 'mt_woe_2nd_screen_3', 'mt_woe_2nd_screen_4', 'mt_woe_2nd_screen_5', 'mt_woe_3rd_screen_1', 'mt_woe_3rd_screen_2', 'mt_woe_3rd_screen_3', 'mt_woe_3rd_screen_4', 'mt_woe_3rd_screen_5', 'mt_woe_final_1', 'mt_woe_final_2', 'mt_woe_key', 'fiona_key', 'arris_dome_rats', 'arris_dome_food_store', 'arris_dome_doan_key', 'arris_dome_food_locker_key', 'sun_palace_key', 'sewers_1', 'sewers_2', 'sewers_3', 'lab_16_1', 'lab_16_2', 'lab_16_3', 'lab_16_4', 'lab_32_1', 'prison_tower_1000', 'geno_dome_1f_1', 'geno_dome_1f_2', 'geno_dome_1f_3', 'geno_dome_1f_4', 'geno_dome_room_1', 'geno_dome_room_2', 'geno_dome_proto4_1', 'geno_dome_proto4_2', 'geno_dome_2f_1', 'geno_dome_2f_2', 'geno_dome_2f_3', 'geno_dome_2f_4', 'geno_dome_boss_1', 'geno_dome_boss_2', 'factory_left_aux_console', 'factory_left_security_right', 'factory_left_security_left', 'factory_right_data_core_1', 'factory_right_data_core_2', 'factory_right_floor_top', 'factory_right_floor_left', 'factory_right_floor_bottom', 'factory_right_floor_secret', 'factory_right_crane_lower', 'factory_right_crane_upper', 'factory_right_info_archive', 'giants_claw_traps', 'giants_claw_caves_1', 'giants_claw_caves_2', 'giants_claw_caves_3', 'giants_claw_caves_4', 'giants_claw_caves_5', 'giants_claw_rock', 'giants_claw_key', 'northern_ruins_antechamber_left_600', 'northern_ruins_antechamber_sealed_600', 'northern_ruins_antechamber_left_1000', 'northern_ruins_antechamber_sealed_1000', 'northern_ruins_back_left_sealed_600', 'northern_ruins_back_right_sealed_600', 'northern_ruins_back_left_sealed_1000', 'northern_ruins_back_right_sealed_1000', 'northern_ruins_basement_600', 'northern_ruins_basement_1000', 'guardia_basement_1', 'guardia_basement_2', 'guardia_basement_3', 'guardia_treasury_1', 'guardia_treasury_2', 'guardia_treasury_3', 'kings_trial_key', 'ozzies_fort_guillotines_1', 'ozzies_fort_guillotines_2', 'ozzies_fort_guillotines_3', 'ozzies_fort_guillotines_4', 'ozzies_fort_final_1', 'ozzies_fort_final_2', 'truce_mayor_1f', 'truce_mayor_2f', 'forest_ruins', 'porre_mayor_2f', 'truce_canyon_1', 'truce_canyon_2', 'fionas_house_1', 'fionas_house_2', 'cursed_woods_1', 'cursed_woods_2', 'frogs_burrow_right', 'zenan_bridge_chef', 'zenan_bridge_chef_tab', 'zenan_bridge_captain', 'snail_stop_key', 'lazy_carpenter', 'heckran_cave_sidetrack', 'heckran_cave_entrance', 'heckran_cave_1', 'heckran_cave_2', 'taban_gift_vest', 'kings_room_1000', 'queens_room_1000', 'kings_room_600', 'queens_room_600', 'royal_kitchen', 'queens_tower_600', 'kings_tower_600', 'kings_tower_1000', 'queens_tower_1000', 'guardia_court_tower', 'manoria_cathedral_1', 'manoria_cathedral_2', 'manoria_cathedral_3', 'manoria_interior_1', 'manoria_interior_2', 'manoria_interior_3', 'manoria_interior_4', 'manoria_shrine_sideroom_1', 'manoria_shrine_sideroom_2', 'manoria_bromide_1', 'manoria_bromide_2', 'manoria_bromide_3', 'manoria_shrine_magus_1', 'manoria_shrine_magus_2', 'yakras_room', 'denadoro_mts_screen2_1', 'denadoro_mts_screen2_2', 'denadoro_mts_screen2_3', 'denadoro_mts_final_1', 'denadoro_mts_final_2', 'denadoro_mts_final_3', 'denadoro_mts_waterfall_top_1', 'denadoro_mts_waterfall_top_2', 'denadoro_mts_waterfall_top_3', 'denadoro_mts_waterfall_top_4', 'denadoro_mts_waterfall_top_5', 'denadoro_mts_entrance_1', 'denadoro_mts_entrance_2', 'denadoro_mts_screen3_1', 'denadoro_mts_screen3_2', 'denadoro_mts_screen3_3', 'denadoro_mts_screen3_4', 'denadoro_mts_ambush', 'denadoro_mts_save_pt', 'denadoro_mts_key', 'bangor_dome_seal_1', 'bangor_dome_seal_2', 'bangor_dome_seal_3', 'trann_dome_seal_1', 'trann_dome_seal_2', 'arris_dome_seal_1', 'arris_dome_seal_2', 'arris_dome_seal_3', 'arris_dome_seal_4', 'truce_inn_sealed_600', 'porre_elder_sealed_1', 'porre_elder_sealed_2', 'guardia_castle_sealed_600', 'guardia_forest_sealed_600', 'truce_inn_sealed_1000', 'porre_mayor_sealed_1', 'porre_mayor_sealed_2', 'guardia_forest_sealed_1000', 'guardia_castle_sealed_1000', 'heckran_sealed_1', 'heckran_sealed_2', 'pyramid_left', 'pyramid_right', 'magic_cave_sealed', 'mystic_mt_stream', 'forest_maze_1', 'forest_maze_2', 'forest_maze_3', 'forest_maze_4', 'forest_maze_5', 'forest_maze_6', 'forest_maze_7', 'forest_maze_8', 'forest_maze_9', 'reptite_lair_reptites_1', 'reptite_lair_reptites_2', 'reptite_lair_key', 'dactyl_nest_1', 'dactyl_nest_2', 'dactyl_nest_3', 'melchior_rainbow_shell', 'melchior_sunstone_rainbow', 'melchior_sunstone_specs', 'frogs_burrow_left', 'guardia_jail_fritz_storage', 'guardia_jail_cell', 'guardia_jail_omnicrone_1', 'guardia_jail_omnicrone_2', 'guardia_jail_omnicrone_3', 'guardia_jail_hole_1', 'guardia_jail_hole_2', 'guardia_jail_outer_wall', 'guardia_jail_omnicrone_4', 'guardia_jail_fritz', 'magus_castle_right_hall', 'sunken_desert_b1_nw', 'sunken_desert_b1_ne', 'sunken_desert_b1_se', 'sunken_desert_b1_sw', 'sunken_desert_b2_nw', 'sunken_desert_b2_n', 'sunken_desert_b2_w', 'sunken_desert_b2_sw', 'sunken_desert_b2_se', 'sunken_desert_b2_e', 'sunken_desert_b2_center', 'magus_castle_guillotine_1', 'magus_castle_guillotine_2', 'magus_castle_slash_room_1', 'magus_castle_slash_room_2', 'magus_castle_statue_hall', 'magus_castle_four_kids', 'magus_castle_ozzie_1', 'magus_castle_ozzie_2', 'magus_castle_enemy_elevator', 'reptite_lair_secret_b2_ne_right', 'lab_32_race_log', 'factory_ruins_generator', 'death_peak_south_face_krakker', 'death_peak_south_face_spawn_save', 'death_peak_south_face_summit', 'death_peak_field', 'death_peak_krakker_parade', 'death_peak_caves_left', 'death_peak_caves_center', 'death_peak_caves_right', 'reptite_lair_secret_b1_sw', 'reptite_lair_secret_b1_ne', 'reptite_lair_secret_b1_se', 'reptite_lair_secret_b2_se_right', 'reptite_lair_secret_b2_ne_or_se_left', 'reptite_lair_secret_b2_sw', 'tyrano_lair_throne_1', 'tyrano_lair_throne_2', 'tyrano_lair_trapdoor', 'tyrano_lair_kino_cell', 'tyrano_lair_maze_1', 'tyrano_lair_maze_2', 'tyrano_lair_maze_3', 'tyrano_lair_maze_4', 'black_omen_aux_command_mid', 'black_omen_aux_command_ne', 'black_omen_grand_hall', 'black_omen_nu_hall_nw', 'black_omen_nu_hall_w', 'black_omen_nu_hall_sw', 'black_omen_nu_hall_ne', 'black_omen_nu_hall_e', 'black_omen_nu_hall_se', 'black_omen_royal_path', 'black_omen_ruminator_parade', 'black_omen_eyeball_hall', 'black_omen_tubster_fly', 'black_omen_martello', 'black_omen_alien_sw', 'black_omen_alien_ne', 'black_omen_alien_nw', 'black_omen_terra_w', 'black_omen_terra_rock', 'black_omen_terra_ne', 'ocean_palace_main_s', 'ocean_palace_main_n', 'ocean_palace_e_room', 'ocean_palace_w_room', 'ocean_palace_switch_nw', 'ocean_palace_switch_sw', 'ocean_palace_switch_ne', 'ocean_palace_switch_secret', 'ocean_palace_final', 'magus_castle_left_hall', 'magus_castle_unskippables', 'magus_castle_pit_e', 'magus_castle_pit_ne', 'magus_castle_pit_nw', 'magus_castle_pit_w', 'taban_gift_suit', 'taban_gift_helm', 'trading_post_petal_fang_base', 'trading_post_petal_fang_upgrade', 'trading_post_petal_horn_base', 'trading_post_petal_horn_upgrade', 'trading_post_petal_feather_base', 'trading_post_petal_feather_upgrade', 'trading_post_fang_horn_base', 'trading_post_fang_horn_upgrade', 'trading_post_fang_feather_base', 'trading_post_fang_feather_upgrade', 'trading_post_horn_feather_base', 'trading_post_horn_feather_upgrade', 'trading_post_special', 'jerky_gift', 'denadoro_rock', 'kajar_rock', 'laruba_rock', 'bekkler_key', 'cyrus_grave_key', 'sun_keep_2300', 'lucca_wondershot', 'taban_sunshades', 'fair_pendant', 'tata_reward', 'toma_reward', 'melchior_forge_masa', 'eot_gaspar_reward', 'hunting_range_nu_reward', 'zeal_mammon_machine', 'magus_castle_slash_sword_floor', 'guardia_prison_lunch_bag', 'cronos_mom', 'truce_mayor_2f_old_man', 'ioka_sweetwater_tonic', 'dorino_inn_powermeal', 'yakra_key_chest', 'courtroom_yakra_key', 'johnny_race_power_tab', 'guardia_forest_power_tab_600', 'guardia_forest_power_tab_1000', 'manoria_confinement_power_tab', 'dorino_bromide_magic_tab', 'porre_market_600_power_tab', 'denadoro_mts_speed_tab', 'tomas_grave_speed_tab', 'giants_claw_caverns_power_tab', 'giants_claw_entrance_power_tab', 'giants_claw_traps_power_tab', 'sun_keep_600_power_tab', 'medina_elder_speed_tab', 'medina_elder_magic_tab', 'magus_castle_flea_magic_tab', 'magus_castle_dungeons_magic_tab', 'trann_dome_sealed_magic_tab', 'arris_dome_sealed_power_tab', 'keepers_dome_magic_tab', 'death_peak_power_tab', 'blackbird_ducts_magic_tab', 'geno_dome_atropos_magic_tab', 'geno_dome_corridor_power_tab', 'geno_dome_labs_magic_tab', 'geno_dome_labs_speed_tab', 'enhasa_nu_battle_magic_tab', 'enhasa_nu_battle_speed_tab', 'kajar_speed_tab', 'kajar_nu_scratch_magic_tab', 'last_village_nu_shop_magic_tab', 'sunken_desert_power_tab', 'mountains_re_nice_magic_tab', 'beast_nest_power_tab', 'mt_woe_magic_tab', 'ocean_palace_elevator_magic_tab', 'ozzies_fort_guillotines_tab', 'proto_dome_portal_tab', 'northern_ruins_heros_grave_magic_tab', 'northern_ruins_landing_power_tab'}
    default = ['death_peak_south_face_summit', 'sun_palace_key', 'bekkler_key', 'fair_pendant', 'zeal_mammon_machine', 'mt_woe_key', 'giants_claw_key', 'kings_trial_key', 'yakras_room', 'snail_stop_key', 'denadoro_mts_key', 'frogs_burrow_left', 'melchior_forge_masa', 'cyrus_grave_key', 'tata_reward', 'fiona_key', 'sun_keep_2300', 'jerky_gift', 'arris_dome_doan_key', 'arris_dome_food_locker_key', 'reptite_lair_key', 'taban_gift_vest', 'geno_dome_boss_1']


class LooseKeyItems(OptionList):
    """Key items to place randomly instead of in forced spots (when more items then spots)"""
    display_name = "Loose Key Items"
    valid_keys = {'wood_sword', 'iron_blade', 'steelsaber', 'lode_sword', 'red_katana', 'flint_edge', 'dark_saber', 'aeon_blade', 'demon_edge', 'alloyblade', 'star_sword', 'vedicblade', 'kali_blade', 'shiva_edge', 'bolt_sword', 'slasher', 'bronze_bow', 'iron_bow', 'lode_bow', 'robin_bow', 'sage_bow', 'dream_bow', 'cometarrow', 'sonicarrow', 'valkerye', 'siren', 'air_gun', 'dart_gun', 'auto_gun', 'picomagnum', 'plasma_gun', 'ruby_gun', 'dream_gun', 'megablast', 'shock_wave', 'wondershot', 'graedus', 'tin_arm', 'hammer_arm', 'miragehand', 'stone_arm', 'doomfinger', 'magma_hand', 'megatonarm', 'big_hand', 'kaiser_arm', 'giga_arm', 'terra_arm', 'crisis_arm', 'bronzeedge', 'iron_sword', 'masamune_1', 'flashblade', 'pearl_edge', 'rune_blade', 'bravesword', 'masamune_2', 'demon_hit', 'fist', 'fist_2', 'fist_3', 'iron_fist', 'bronzefist', 'pacifist', 'darkscythe', 'hurricane', 'starscythe', 'doomsickle', 'mop', 'bent_sword', 'bent_hilt', 'swallow', 'slasher_2', 'rainbow', 'hide_tunic', 'karate_gi', 'bronzemail', 'maidensuit', 'iron_suit', 'titan_vest', 'gold_suit', 'ruby_vest', 'dark_mail', 'mist_robe', 'meso_mail', 'lumin_robe', 'flash_mail', 'lode_vest', 'aeon_suit', 'zodiaccape', 'nova_armor', 'prismdress', 'moon_armor', 'ruby_armor', 'ravenarmor', 'gloom_cape', 'white_mail', 'black_mail', 'blue_mail', 'red_mail', 'white_vest', 'black_vest', 'blue_vest', 'red_vest', 'taban_vest', 'taban_suit', 'hide_cap', 'bronzehelm', 'iron_helm', 'beret', 'gold_helm', 'rock_helm', 'ceratopper', 'glow_helm', 'lode_helm', 'aeon_helm', 'prism_helm', 'doom_helm', 'dark_helm', 'gloom_helm', 'safe_helm', 'taban_helm', 'sight_cap', 'memory_cap', 'time_hat', 'vigil_hat', 'ozziepants', 'haste_helm', 'rbow_helm', 'mermaidcap', 'bandana', 'ribbon', 'powerglove', 'defender', 'magicscarf', 'amulet', 'dash_ring', 'hit_ring', 'power_ring', 'magic_ring', 'wall_ring', 'silvererng', 'gold_erng', 'silverstud', 'gold_stud', 'sightscope', 'charm_top', 'rage_band', 'frenzyband', 'third_eye', 'wallet', 'greendream', 'berserker', 'powerscarf', 'speed_belt', 'black_rock', 'blue_rock', 'silverrock', 'white_rock', 'gold_rock', 'hero_medal', 'musclering', 'flea_vest', 'magic_seal', 'power_seal', 'valor_crest', 'dragon_tear', 'sun_shades', 'prismspecs', 'tonic', 'mid_tonic', 'full_tonic', 'ether', 'mid_ether', 'full_ether', 'elixir', 'hyperether', 'megaelixir', 'heal', 'revive', 'shelter', 'power_meal', 'lapis', 'barrier', 'shield', 'power_tab', 'magic_tab', 'speed_tab', 'petal', 'fang', 'horn', 'feather', 'seed', 'bike_key', 'pendant', 'gate_key', 'prismshard', 'c_trigger', 'tools', 'jerky', 'dreamstone', 'race_log', 'moon_stone', 'sun_stone', 'ruby_knife', 'yakra_key', 'clone', 'tomas_pop', 'petals_2', 'fangs_2', 'horns_2', 'feathers_2', 'jetsoftime', 'pendant_charge', 'rainbow_shell'}
    default = ['sun_stone', 'race_log']


class IncentiveSpots(OptionList):
    """Spots (outside forced) with increased probability to have key items"""
    display_name = "Incentive Spots"
    valid_keys = {'mt_woe_1st_screen', 'mt_woe_2nd_screen_1', 'mt_woe_2nd_screen_2', 'mt_woe_2nd_screen_3', 'mt_woe_2nd_screen_4', 'mt_woe_2nd_screen_5', 'mt_woe_3rd_screen_1', 'mt_woe_3rd_screen_2', 'mt_woe_3rd_screen_3', 'mt_woe_3rd_screen_4', 'mt_woe_3rd_screen_5', 'mt_woe_final_1', 'mt_woe_final_2', 'mt_woe_key', 'fiona_key', 'arris_dome_rats', 'arris_dome_food_store', 'arris_dome_doan_key', 'arris_dome_food_locker_key', 'sun_palace_key', 'sewers_1', 'sewers_2', 'sewers_3', 'lab_16_1', 'lab_16_2', 'lab_16_3', 'lab_16_4', 'lab_32_1', 'prison_tower_1000', 'geno_dome_1f_1', 'geno_dome_1f_2', 'geno_dome_1f_3', 'geno_dome_1f_4', 'geno_dome_room_1', 'geno_dome_room_2', 'geno_dome_proto4_1', 'geno_dome_proto4_2', 'geno_dome_2f_1', 'geno_dome_2f_2', 'geno_dome_2f_3', 'geno_dome_2f_4', 'geno_dome_boss_1', 'geno_dome_boss_2', 'factory_left_aux_console', 'factory_left_security_right', 'factory_left_security_left', 'factory_right_data_core_1', 'factory_right_data_core_2', 'factory_right_floor_top', 'factory_right_floor_left', 'factory_right_floor_bottom', 'factory_right_floor_secret', 'factory_right_crane_lower', 'factory_right_crane_upper', 'factory_right_info_archive', 'giants_claw_traps', 'giants_claw_caves_1', 'giants_claw_caves_2', 'giants_claw_caves_3', 'giants_claw_caves_4', 'giants_claw_caves_5', 'giants_claw_rock', 'giants_claw_key', 'northern_ruins_antechamber_left_600', 'northern_ruins_antechamber_sealed_600', 'northern_ruins_antechamber_left_1000', 'northern_ruins_antechamber_sealed_1000', 'northern_ruins_back_left_sealed_600', 'northern_ruins_back_right_sealed_600', 'northern_ruins_back_left_sealed_1000', 'northern_ruins_back_right_sealed_1000', 'northern_ruins_basement_600', 'northern_ruins_basement_1000', 'guardia_basement_1', 'guardia_basement_2', 'guardia_basement_3', 'guardia_treasury_1', 'guardia_treasury_2', 'guardia_treasury_3', 'kings_trial_key', 'ozzies_fort_guillotines_1', 'ozzies_fort_guillotines_2', 'ozzies_fort_guillotines_3', 'ozzies_fort_guillotines_4', 'ozzies_fort_final_1', 'ozzies_fort_final_2', 'truce_mayor_1f', 'truce_mayor_2f', 'forest_ruins', 'porre_mayor_2f', 'truce_canyon_1', 'truce_canyon_2', 'fionas_house_1', 'fionas_house_2', 'cursed_woods_1', 'cursed_woods_2', 'frogs_burrow_right', 'zenan_bridge_chef', 'zenan_bridge_chef_tab', 'zenan_bridge_captain', 'snail_stop_key', 'lazy_carpenter', 'heckran_cave_sidetrack', 'heckran_cave_entrance', 'heckran_cave_1', 'heckran_cave_2', 'taban_gift_vest', 'kings_room_1000', 'queens_room_1000', 'kings_room_600', 'queens_room_600', 'royal_kitchen', 'queens_tower_600', 'kings_tower_600', 'kings_tower_1000', 'queens_tower_1000', 'guardia_court_tower', 'manoria_cathedral_1', 'manoria_cathedral_2', 'manoria_cathedral_3', 'manoria_interior_1', 'manoria_interior_2', 'manoria_interior_3', 'manoria_interior_4', 'manoria_shrine_sideroom_1', 'manoria_shrine_sideroom_2', 'manoria_bromide_1', 'manoria_bromide_2', 'manoria_bromide_3', 'manoria_shrine_magus_1', 'manoria_shrine_magus_2', 'yakras_room', 'denadoro_mts_screen2_1', 'denadoro_mts_screen2_2', 'denadoro_mts_screen2_3', 'denadoro_mts_final_1', 'denadoro_mts_final_2', 'denadoro_mts_final_3', 'denadoro_mts_waterfall_top_1', 'denadoro_mts_waterfall_top_2', 'denadoro_mts_waterfall_top_3', 'denadoro_mts_waterfall_top_4', 'denadoro_mts_waterfall_top_5', 'denadoro_mts_entrance_1', 'denadoro_mts_entrance_2', 'denadoro_mts_screen3_1', 'denadoro_mts_screen3_2', 'denadoro_mts_screen3_3', 'denadoro_mts_screen3_4', 'denadoro_mts_ambush', 'denadoro_mts_save_pt', 'denadoro_mts_key', 'bangor_dome_seal_1', 'bangor_dome_seal_2', 'bangor_dome_seal_3', 'trann_dome_seal_1', 'trann_dome_seal_2', 'arris_dome_seal_1', 'arris_dome_seal_2', 'arris_dome_seal_3', 'arris_dome_seal_4', 'truce_inn_sealed_600', 'porre_elder_sealed_1', 'porre_elder_sealed_2', 'guardia_castle_sealed_600', 'guardia_forest_sealed_600', 'truce_inn_sealed_1000', 'porre_mayor_sealed_1', 'porre_mayor_sealed_2', 'guardia_forest_sealed_1000', 'guardia_castle_sealed_1000', 'heckran_sealed_1', 'heckran_sealed_2', 'pyramid_left', 'pyramid_right', 'magic_cave_sealed', 'mystic_mt_stream', 'forest_maze_1', 'forest_maze_2', 'forest_maze_3', 'forest_maze_4', 'forest_maze_5', 'forest_maze_6', 'forest_maze_7', 'forest_maze_8', 'forest_maze_9', 'reptite_lair_reptites_1', 'reptite_lair_reptites_2', 'reptite_lair_key', 'dactyl_nest_1', 'dactyl_nest_2', 'dactyl_nest_3', 'melchior_rainbow_shell', 'melchior_sunstone_rainbow', 'melchior_sunstone_specs', 'frogs_burrow_left', 'guardia_jail_fritz_storage', 'guardia_jail_cell', 'guardia_jail_omnicrone_1', 'guardia_jail_omnicrone_2', 'guardia_jail_omnicrone_3', 'guardia_jail_hole_1', 'guardia_jail_hole_2', 'guardia_jail_outer_wall', 'guardia_jail_omnicrone_4', 'guardia_jail_fritz', 'magus_castle_right_hall', 'sunken_desert_b1_nw', 'sunken_desert_b1_ne', 'sunken_desert_b1_se', 'sunken_desert_b1_sw', 'sunken_desert_b2_nw', 'sunken_desert_b2_n', 'sunken_desert_b2_w', 'sunken_desert_b2_sw', 'sunken_desert_b2_se', 'sunken_desert_b2_e', 'sunken_desert_b2_center', 'magus_castle_guillotine_1', 'magus_castle_guillotine_2', 'magus_castle_slash_room_1', 'magus_castle_slash_room_2', 'magus_castle_statue_hall', 'magus_castle_four_kids', 'magus_castle_ozzie_1', 'magus_castle_ozzie_2', 'magus_castle_enemy_elevator', 'reptite_lair_secret_b2_ne_right', 'lab_32_race_log', 'factory_ruins_generator', 'death_peak_south_face_krakker', 'death_peak_south_face_spawn_save', 'death_peak_south_face_summit', 'death_peak_field', 'death_peak_krakker_parade', 'death_peak_caves_left', 'death_peak_caves_center', 'death_peak_caves_right', 'reptite_lair_secret_b1_sw', 'reptite_lair_secret_b1_ne', 'reptite_lair_secret_b1_se', 'reptite_lair_secret_b2_se_right', 'reptite_lair_secret_b2_ne_or_se_left', 'reptite_lair_secret_b2_sw', 'tyrano_lair_throne_1', 'tyrano_lair_throne_2', 'tyrano_lair_trapdoor', 'tyrano_lair_kino_cell', 'tyrano_lair_maze_1', 'tyrano_lair_maze_2', 'tyrano_lair_maze_3', 'tyrano_lair_maze_4', 'black_omen_aux_command_mid', 'black_omen_aux_command_ne', 'black_omen_grand_hall', 'black_omen_nu_hall_nw', 'black_omen_nu_hall_w', 'black_omen_nu_hall_sw', 'black_omen_nu_hall_ne', 'black_omen_nu_hall_e', 'black_omen_nu_hall_se', 'black_omen_royal_path', 'black_omen_ruminator_parade', 'black_omen_eyeball_hall', 'black_omen_tubster_fly', 'black_omen_martello', 'black_omen_alien_sw', 'black_omen_alien_ne', 'black_omen_alien_nw', 'black_omen_terra_w', 'black_omen_terra_rock', 'black_omen_terra_ne', 'ocean_palace_main_s', 'ocean_palace_main_n', 'ocean_palace_e_room', 'ocean_palace_w_room', 'ocean_palace_switch_nw', 'ocean_palace_switch_sw', 'ocean_palace_switch_ne', 'ocean_palace_switch_secret', 'ocean_palace_final', 'magus_castle_left_hall', 'magus_castle_unskippables', 'magus_castle_pit_e', 'magus_castle_pit_ne', 'magus_castle_pit_nw', 'magus_castle_pit_w', 'taban_gift_suit', 'taban_gift_helm', 'trading_post_petal_fang_base', 'trading_post_petal_fang_upgrade', 'trading_post_petal_horn_base', 'trading_post_petal_horn_upgrade', 'trading_post_petal_feather_base', 'trading_post_petal_feather_upgrade', 'trading_post_fang_horn_base', 'trading_post_fang_horn_upgrade', 'trading_post_fang_feather_base', 'trading_post_fang_feather_upgrade', 'trading_post_horn_feather_base', 'trading_post_horn_feather_upgrade', 'trading_post_special', 'jerky_gift', 'denadoro_rock', 'kajar_rock', 'laruba_rock', 'bekkler_key', 'cyrus_grave_key', 'sun_keep_2300', 'lucca_wondershot', 'taban_sunshades', 'fair_pendant', 'tata_reward', 'toma_reward', 'melchior_forge_masa', 'eot_gaspar_reward', 'hunting_range_nu_reward', 'zeal_mammon_machine', 'magus_castle_slash_sword_floor', 'guardia_prison_lunch_bag', 'cronos_mom', 'truce_mayor_2f_old_man', 'ioka_sweetwater_tonic', 'dorino_inn_powermeal', 'yakra_key_chest', 'courtroom_yakra_key', 'johnny_race_power_tab', 'guardia_forest_power_tab_600', 'guardia_forest_power_tab_1000', 'manoria_confinement_power_tab', 'dorino_bromide_magic_tab', 'porre_market_600_power_tab', 'denadoro_mts_speed_tab', 'tomas_grave_speed_tab', 'giants_claw_caverns_power_tab', 'giants_claw_entrance_power_tab', 'giants_claw_traps_power_tab', 'sun_keep_600_power_tab', 'medina_elder_speed_tab', 'medina_elder_magic_tab', 'magus_castle_flea_magic_tab', 'magus_castle_dungeons_magic_tab', 'trann_dome_sealed_magic_tab', 'arris_dome_sealed_power_tab', 'keepers_dome_magic_tab', 'death_peak_power_tab', 'blackbird_ducts_magic_tab', 'geno_dome_atropos_magic_tab', 'geno_dome_corridor_power_tab', 'geno_dome_labs_magic_tab', 'geno_dome_labs_speed_tab', 'enhasa_nu_battle_magic_tab', 'enhasa_nu_battle_speed_tab', 'kajar_speed_tab', 'kajar_nu_scratch_magic_tab', 'last_village_nu_shop_magic_tab', 'sunken_desert_power_tab', 'mountains_re_nice_magic_tab', 'beast_nest_power_tab', 'mt_woe_magic_tab', 'ocean_palace_elevator_magic_tab', 'ozzies_fort_guillotines_tab', 'proto_dome_portal_tab', 'northern_ruins_heros_grave_magic_tab', 'northern_ruins_landing_power_tab'}
    default = []


class IncentiveFactor(Range):
    """Factor by which to increase the weight of incentive spots"""
    display_name = "Incentive Factor"
    range_start = 100
    range_end = 1000
    default = 500


class ExcludedSpots(OptionList):
    """Spots which are forbidden to have key items"""
    display_name = "Excluded Spots"
    valid_keys = {'mt_woe_1st_screen', 'mt_woe_2nd_screen_1', 'mt_woe_2nd_screen_2', 'mt_woe_2nd_screen_3', 'mt_woe_2nd_screen_4', 'mt_woe_2nd_screen_5', 'mt_woe_3rd_screen_1', 'mt_woe_3rd_screen_2', 'mt_woe_3rd_screen_3', 'mt_woe_3rd_screen_4', 'mt_woe_3rd_screen_5', 'mt_woe_final_1', 'mt_woe_final_2', 'mt_woe_key', 'fiona_key', 'arris_dome_rats', 'arris_dome_food_store', 'arris_dome_doan_key', 'arris_dome_food_locker_key', 'sun_palace_key', 'sewers_1', 'sewers_2', 'sewers_3', 'lab_16_1', 'lab_16_2', 'lab_16_3', 'lab_16_4', 'lab_32_1', 'prison_tower_1000', 'geno_dome_1f_1', 'geno_dome_1f_2', 'geno_dome_1f_3', 'geno_dome_1f_4', 'geno_dome_room_1', 'geno_dome_room_2', 'geno_dome_proto4_1', 'geno_dome_proto4_2', 'geno_dome_2f_1', 'geno_dome_2f_2', 'geno_dome_2f_3', 'geno_dome_2f_4', 'geno_dome_boss_1', 'geno_dome_boss_2', 'factory_left_aux_console', 'factory_left_security_right', 'factory_left_security_left', 'factory_right_data_core_1', 'factory_right_data_core_2', 'factory_right_floor_top', 'factory_right_floor_left', 'factory_right_floor_bottom', 'factory_right_floor_secret', 'factory_right_crane_lower', 'factory_right_crane_upper', 'factory_right_info_archive', 'giants_claw_traps', 'giants_claw_caves_1', 'giants_claw_caves_2', 'giants_claw_caves_3', 'giants_claw_caves_4', 'giants_claw_caves_5', 'giants_claw_rock', 'giants_claw_key', 'northern_ruins_antechamber_left_600', 'northern_ruins_antechamber_sealed_600', 'northern_ruins_antechamber_left_1000', 'northern_ruins_antechamber_sealed_1000', 'northern_ruins_back_left_sealed_600', 'northern_ruins_back_right_sealed_600', 'northern_ruins_back_left_sealed_1000', 'northern_ruins_back_right_sealed_1000', 'northern_ruins_basement_600', 'northern_ruins_basement_1000', 'guardia_basement_1', 'guardia_basement_2', 'guardia_basement_3', 'guardia_treasury_1', 'guardia_treasury_2', 'guardia_treasury_3', 'kings_trial_key', 'ozzies_fort_guillotines_1', 'ozzies_fort_guillotines_2', 'ozzies_fort_guillotines_3', 'ozzies_fort_guillotines_4', 'ozzies_fort_final_1', 'ozzies_fort_final_2', 'truce_mayor_1f', 'truce_mayor_2f', 'forest_ruins', 'porre_mayor_2f', 'truce_canyon_1', 'truce_canyon_2', 'fionas_house_1', 'fionas_house_2', 'cursed_woods_1', 'cursed_woods_2', 'frogs_burrow_right', 'zenan_bridge_chef', 'zenan_bridge_chef_tab', 'zenan_bridge_captain', 'snail_stop_key', 'lazy_carpenter', 'heckran_cave_sidetrack', 'heckran_cave_entrance', 'heckran_cave_1', 'heckran_cave_2', 'taban_gift_vest', 'kings_room_1000', 'queens_room_1000', 'kings_room_600', 'queens_room_600', 'royal_kitchen', 'queens_tower_600', 'kings_tower_600', 'kings_tower_1000', 'queens_tower_1000', 'guardia_court_tower', 'manoria_cathedral_1', 'manoria_cathedral_2', 'manoria_cathedral_3', 'manoria_interior_1', 'manoria_interior_2', 'manoria_interior_3', 'manoria_interior_4', 'manoria_shrine_sideroom_1', 'manoria_shrine_sideroom_2', 'manoria_bromide_1', 'manoria_bromide_2', 'manoria_bromide_3', 'manoria_shrine_magus_1', 'manoria_shrine_magus_2', 'yakras_room', 'denadoro_mts_screen2_1', 'denadoro_mts_screen2_2', 'denadoro_mts_screen2_3', 'denadoro_mts_final_1', 'denadoro_mts_final_2', 'denadoro_mts_final_3', 'denadoro_mts_waterfall_top_1', 'denadoro_mts_waterfall_top_2', 'denadoro_mts_waterfall_top_3', 'denadoro_mts_waterfall_top_4', 'denadoro_mts_waterfall_top_5', 'denadoro_mts_entrance_1', 'denadoro_mts_entrance_2', 'denadoro_mts_screen3_1', 'denadoro_mts_screen3_2', 'denadoro_mts_screen3_3', 'denadoro_mts_screen3_4', 'denadoro_mts_ambush', 'denadoro_mts_save_pt', 'denadoro_mts_key', 'bangor_dome_seal_1', 'bangor_dome_seal_2', 'bangor_dome_seal_3', 'trann_dome_seal_1', 'trann_dome_seal_2', 'arris_dome_seal_1', 'arris_dome_seal_2', 'arris_dome_seal_3', 'arris_dome_seal_4', 'truce_inn_sealed_600', 'porre_elder_sealed_1', 'porre_elder_sealed_2', 'guardia_castle_sealed_600', 'guardia_forest_sealed_600', 'truce_inn_sealed_1000', 'porre_mayor_sealed_1', 'porre_mayor_sealed_2', 'guardia_forest_sealed_1000', 'guardia_castle_sealed_1000', 'heckran_sealed_1', 'heckran_sealed_2', 'pyramid_left', 'pyramid_right', 'magic_cave_sealed', 'mystic_mt_stream', 'forest_maze_1', 'forest_maze_2', 'forest_maze_3', 'forest_maze_4', 'forest_maze_5', 'forest_maze_6', 'forest_maze_7', 'forest_maze_8', 'forest_maze_9', 'reptite_lair_reptites_1', 'reptite_lair_reptites_2', 'reptite_lair_key', 'dactyl_nest_1', 'dactyl_nest_2', 'dactyl_nest_3', 'melchior_rainbow_shell', 'melchior_sunstone_rainbow', 'melchior_sunstone_specs', 'frogs_burrow_left', 'guardia_jail_fritz_storage', 'guardia_jail_cell', 'guardia_jail_omnicrone_1', 'guardia_jail_omnicrone_2', 'guardia_jail_omnicrone_3', 'guardia_jail_hole_1', 'guardia_jail_hole_2', 'guardia_jail_outer_wall', 'guardia_jail_omnicrone_4', 'guardia_jail_fritz', 'magus_castle_right_hall', 'sunken_desert_b1_nw', 'sunken_desert_b1_ne', 'sunken_desert_b1_se', 'sunken_desert_b1_sw', 'sunken_desert_b2_nw', 'sunken_desert_b2_n', 'sunken_desert_b2_w', 'sunken_desert_b2_sw', 'sunken_desert_b2_se', 'sunken_desert_b2_e', 'sunken_desert_b2_center', 'magus_castle_guillotine_1', 'magus_castle_guillotine_2', 'magus_castle_slash_room_1', 'magus_castle_slash_room_2', 'magus_castle_statue_hall', 'magus_castle_four_kids', 'magus_castle_ozzie_1', 'magus_castle_ozzie_2', 'magus_castle_enemy_elevator', 'reptite_lair_secret_b2_ne_right', 'lab_32_race_log', 'factory_ruins_generator', 'death_peak_south_face_krakker', 'death_peak_south_face_spawn_save', 'death_peak_south_face_summit', 'death_peak_field', 'death_peak_krakker_parade', 'death_peak_caves_left', 'death_peak_caves_center', 'death_peak_caves_right', 'reptite_lair_secret_b1_sw', 'reptite_lair_secret_b1_ne', 'reptite_lair_secret_b1_se', 'reptite_lair_secret_b2_se_right', 'reptite_lair_secret_b2_ne_or_se_left', 'reptite_lair_secret_b2_sw', 'tyrano_lair_throne_1', 'tyrano_lair_throne_2', 'tyrano_lair_trapdoor', 'tyrano_lair_kino_cell', 'tyrano_lair_maze_1', 'tyrano_lair_maze_2', 'tyrano_lair_maze_3', 'tyrano_lair_maze_4', 'black_omen_aux_command_mid', 'black_omen_aux_command_ne', 'black_omen_grand_hall', 'black_omen_nu_hall_nw', 'black_omen_nu_hall_w', 'black_omen_nu_hall_sw', 'black_omen_nu_hall_ne', 'black_omen_nu_hall_e', 'black_omen_nu_hall_se', 'black_omen_royal_path', 'black_omen_ruminator_parade', 'black_omen_eyeball_hall', 'black_omen_tubster_fly', 'black_omen_martello', 'black_omen_alien_sw', 'black_omen_alien_ne', 'black_omen_alien_nw', 'black_omen_terra_w', 'black_omen_terra_rock', 'black_omen_terra_ne', 'ocean_palace_main_s', 'ocean_palace_main_n', 'ocean_palace_e_room', 'ocean_palace_w_room', 'ocean_palace_switch_nw', 'ocean_palace_switch_sw', 'ocean_palace_switch_ne', 'ocean_palace_switch_secret', 'ocean_palace_final', 'magus_castle_left_hall', 'magus_castle_unskippables', 'magus_castle_pit_e', 'magus_castle_pit_ne', 'magus_castle_pit_nw', 'magus_castle_pit_w', 'taban_gift_suit', 'taban_gift_helm', 'trading_post_petal_fang_base', 'trading_post_petal_fang_upgrade', 'trading_post_petal_horn_base', 'trading_post_petal_horn_upgrade', 'trading_post_petal_feather_base', 'trading_post_petal_feather_upgrade', 'trading_post_fang_horn_base', 'trading_post_fang_horn_upgrade', 'trading_post_fang_feather_base', 'trading_post_fang_feather_upgrade', 'trading_post_horn_feather_base', 'trading_post_horn_feather_upgrade', 'trading_post_special', 'jerky_gift', 'denadoro_rock', 'kajar_rock', 'laruba_rock', 'bekkler_key', 'cyrus_grave_key', 'sun_keep_2300', 'lucca_wondershot', 'taban_sunshades', 'fair_pendant', 'tata_reward', 'toma_reward', 'melchior_forge_masa', 'eot_gaspar_reward', 'hunting_range_nu_reward', 'zeal_mammon_machine', 'magus_castle_slash_sword_floor', 'guardia_prison_lunch_bag', 'cronos_mom', 'truce_mayor_2f_old_man', 'ioka_sweetwater_tonic', 'dorino_inn_powermeal', 'yakra_key_chest', 'courtroom_yakra_key', 'johnny_race_power_tab', 'guardia_forest_power_tab_600', 'guardia_forest_power_tab_1000', 'manoria_confinement_power_tab', 'dorino_bromide_magic_tab', 'porre_market_600_power_tab', 'denadoro_mts_speed_tab', 'tomas_grave_speed_tab', 'giants_claw_caverns_power_tab', 'giants_claw_entrance_power_tab', 'giants_claw_traps_power_tab', 'sun_keep_600_power_tab', 'medina_elder_speed_tab', 'medina_elder_magic_tab', 'magus_castle_flea_magic_tab', 'magus_castle_dungeons_magic_tab', 'trann_dome_sealed_magic_tab', 'arris_dome_sealed_power_tab', 'keepers_dome_magic_tab', 'death_peak_power_tab', 'blackbird_ducts_magic_tab', 'geno_dome_atropos_magic_tab', 'geno_dome_corridor_power_tab', 'geno_dome_labs_magic_tab', 'geno_dome_labs_speed_tab', 'enhasa_nu_battle_magic_tab', 'enhasa_nu_battle_speed_tab', 'kajar_speed_tab', 'kajar_nu_scratch_magic_tab', 'last_village_nu_shop_magic_tab', 'sunken_desert_power_tab', 'mountains_re_nice_magic_tab', 'beast_nest_power_tab', 'mt_woe_magic_tab', 'ocean_palace_elevator_magic_tab', 'ozzies_fort_guillotines_tab', 'proto_dome_portal_tab', 'northern_ruins_heros_grave_magic_tab', 'northern_ruins_landing_power_tab'}
    default = ['magus_castle_right_hall', 'magus_castle_guillotine_1', 'magus_castle_guillotine_2', 'magus_castle_slash_room_1', 'magus_castle_slash_room_2', 'magus_castle_slash_sword_floor', 'magus_castle_statue_hall', 'magus_castle_four_kids', 'magus_castle_ozzie_1', 'magus_castle_ozzie_2', 'magus_castle_enemy_elevator', 'magus_castle_left_hall', 'magus_castle_unskippables', 'magus_castle_pit_e', 'magus_castle_pit_ne', 'magus_castle_pit_nw', 'magus_castle_pit_w', 'magus_castle_flea_magic_tab', 'magus_castle_dungeons_magic_tab', 'sunken_desert_b1_ne', 'sunken_desert_b1_se', 'sunken_desert_b1_nw', 'sunken_desert_b1_sw', 'sunken_desert_b2_n', 'sunken_desert_b2_nw', 'sunken_desert_b2_w', 'sunken_desert_b2_sw', 'sunken_desert_b2_se', 'sunken_desert_b2_e', 'sunken_desert_b2_center', 'sunken_desert_power_tab', 'tyrano_lair_maze_1', 'tyrano_lair_maze_2', 'tyrano_lair_maze_3', 'tyrano_lair_maze_4']


class DecayFactor(Range):
    """Factor by which to decrease the weight of regions which have already received items (1.0 = no change)"""
    display_name = "Decay Factor"
    range_start = 0
    range_end = 100
    default = 70


class StarterRewards(OptionList):
    """Rewards to grant at game start"""
    display_name = "Starter Rewards"
    valid_keys = {'wood_sword', 'iron_blade', 'steelsaber', 'lode_sword', 'red_katana', 'flint_edge', 'dark_saber', 'aeon_blade', 'demon_edge', 'alloyblade', 'star_sword', 'vedicblade', 'kali_blade', 'shiva_edge', 'bolt_sword', 'slasher', 'bronze_bow', 'iron_bow', 'lode_bow', 'robin_bow', 'sage_bow', 'dream_bow', 'cometarrow', 'sonicarrow', 'valkerye', 'siren', 'air_gun', 'dart_gun', 'auto_gun', 'picomagnum', 'plasma_gun', 'ruby_gun', 'dream_gun', 'megablast', 'shock_wave', 'wondershot', 'graedus', 'tin_arm', 'hammer_arm', 'miragehand', 'stone_arm', 'doomfinger', 'magma_hand', 'megatonarm', 'big_hand', 'kaiser_arm', 'giga_arm', 'terra_arm', 'crisis_arm', 'bronzeedge', 'iron_sword', 'masamune_1', 'flashblade', 'pearl_edge', 'rune_blade', 'bravesword', 'masamune_2', 'demon_hit', 'fist', 'fist_2', 'fist_3', 'iron_fist', 'bronzefist', 'pacifist', 'darkscythe', 'hurricane', 'starscythe', 'doomsickle', 'mop', 'bent_sword', 'bent_hilt', 'swallow', 'slasher_2', 'rainbow', 'hide_tunic', 'karate_gi', 'bronzemail', 'maidensuit', 'iron_suit', 'titan_vest', 'gold_suit', 'ruby_vest', 'dark_mail', 'mist_robe', 'meso_mail', 'lumin_robe', 'flash_mail', 'lode_vest', 'aeon_suit', 'zodiaccape', 'nova_armor', 'prismdress', 'moon_armor', 'ruby_armor', 'ravenarmor', 'gloom_cape', 'white_mail', 'black_mail', 'blue_mail', 'red_mail', 'white_vest', 'black_vest', 'blue_vest', 'red_vest', 'taban_vest', 'taban_suit', 'hide_cap', 'bronzehelm', 'iron_helm', 'beret', 'gold_helm', 'rock_helm', 'ceratopper', 'glow_helm', 'lode_helm', 'aeon_helm', 'prism_helm', 'doom_helm', 'dark_helm', 'gloom_helm', 'safe_helm', 'taban_helm', 'sight_cap', 'memory_cap', 'time_hat', 'vigil_hat', 'ozziepants', 'haste_helm', 'rbow_helm', 'mermaidcap', 'bandana', 'ribbon', 'powerglove', 'defender', 'magicscarf', 'amulet', 'dash_ring', 'hit_ring', 'power_ring', 'magic_ring', 'wall_ring', 'silvererng', 'gold_erng', 'silverstud', 'gold_stud', 'sightscope', 'charm_top', 'rage_band', 'frenzyband', 'third_eye', 'wallet', 'greendream', 'berserker', 'powerscarf', 'speed_belt', 'black_rock', 'blue_rock', 'silverrock', 'white_rock', 'gold_rock', 'hero_medal', 'musclering', 'flea_vest', 'magic_seal', 'power_seal', 'valor_crest', 'dragon_tear', 'sun_shades', 'prismspecs', 'tonic', 'mid_tonic', 'full_tonic', 'ether', 'mid_ether', 'full_ether', 'elixir', 'hyperether', 'megaelixir', 'heal', 'revive', 'shelter', 'power_meal', 'lapis', 'barrier', 'shield', 'power_tab', 'magic_tab', 'speed_tab', 'petal', 'fang', 'horn', 'feather', 'seed', 'bike_key', 'pendant', 'gate_key', 'prismshard', 'c_trigger', 'tools', 'jerky', 'dreamstone', 'race_log', 'moon_stone', 'sun_stone', 'ruby_knife', 'yakra_key', 'clone', 'tomas_pop', 'petals_2', 'fangs_2', 'horns_2', 'feathers_2', 'jetsoftime', 'pendant_charge', 'rainbow_shell', 'epoch', 'flight', 'dark_ages', 'future', 'last_village_portal', 'end_of_time', 'bucket', 'apocalypse', 'omen_present', 'omen_last_village', 'dark_ages_pillar', 'bangor_pillar', 'truce_pillar', 'desert', 'pacifist'}
    default = ['epoch']


class OutOfLogicStarterRewards(OptionList):
    """Rewards to grant at game start which are not considered by logic"""
    display_name = "Out Of Logic Starter Rewards"
    valid_keys = {'wood_sword', 'iron_blade', 'steelsaber', 'lode_sword', 'red_katana', 'flint_edge', 'dark_saber', 'aeon_blade', 'demon_edge', 'alloyblade', 'star_sword', 'vedicblade', 'kali_blade', 'shiva_edge', 'bolt_sword', 'slasher', 'bronze_bow', 'iron_bow', 'lode_bow', 'robin_bow', 'sage_bow', 'dream_bow', 'cometarrow', 'sonicarrow', 'valkerye', 'siren', 'air_gun', 'dart_gun', 'auto_gun', 'picomagnum', 'plasma_gun', 'ruby_gun', 'dream_gun', 'megablast', 'shock_wave', 'wondershot', 'graedus', 'tin_arm', 'hammer_arm', 'miragehand', 'stone_arm', 'doomfinger', 'magma_hand', 'megatonarm', 'big_hand', 'kaiser_arm', 'giga_arm', 'terra_arm', 'crisis_arm', 'bronzeedge', 'iron_sword', 'masamune_1', 'flashblade', 'pearl_edge', 'rune_blade', 'bravesword', 'masamune_2', 'demon_hit', 'fist', 'fist_2', 'fist_3', 'iron_fist', 'bronzefist', 'pacifist', 'darkscythe', 'hurricane', 'starscythe', 'doomsickle', 'mop', 'bent_sword', 'bent_hilt', 'swallow', 'slasher_2', 'rainbow', 'hide_tunic', 'karate_gi', 'bronzemail', 'maidensuit', 'iron_suit', 'titan_vest', 'gold_suit', 'ruby_vest', 'dark_mail', 'mist_robe', 'meso_mail', 'lumin_robe', 'flash_mail', 'lode_vest', 'aeon_suit', 'zodiaccape', 'nova_armor', 'prismdress', 'moon_armor', 'ruby_armor', 'ravenarmor', 'gloom_cape', 'white_mail', 'black_mail', 'blue_mail', 'red_mail', 'white_vest', 'black_vest', 'blue_vest', 'red_vest', 'taban_vest', 'taban_suit', 'hide_cap', 'bronzehelm', 'iron_helm', 'beret', 'gold_helm', 'rock_helm', 'ceratopper', 'glow_helm', 'lode_helm', 'aeon_helm', 'prism_helm', 'doom_helm', 'dark_helm', 'gloom_helm', 'safe_helm', 'taban_helm', 'sight_cap', 'memory_cap', 'time_hat', 'vigil_hat', 'ozziepants', 'haste_helm', 'rbow_helm', 'mermaidcap', 'bandana', 'ribbon', 'powerglove', 'defender', 'magicscarf', 'amulet', 'dash_ring', 'hit_ring', 'power_ring', 'magic_ring', 'wall_ring', 'silvererng', 'gold_erng', 'silverstud', 'gold_stud', 'sightscope', 'charm_top', 'rage_band', 'frenzyband', 'third_eye', 'wallet', 'greendream', 'berserker', 'powerscarf', 'speed_belt', 'black_rock', 'blue_rock', 'silverrock', 'white_rock', 'gold_rock', 'hero_medal', 'musclering', 'flea_vest', 'magic_seal', 'power_seal', 'valor_crest', 'dragon_tear', 'sun_shades', 'prismspecs', 'tonic', 'mid_tonic', 'full_tonic', 'ether', 'mid_ether', 'full_ether', 'elixir', 'hyperether', 'megaelixir', 'heal', 'revive', 'shelter', 'power_meal', 'lapis', 'barrier', 'shield', 'power_tab', 'magic_tab', 'speed_tab', 'petal', 'fang', 'horn', 'feather', 'seed', 'bike_key', 'pendant', 'gate_key', 'prismshard', 'c_trigger', 'tools', 'jerky', 'dreamstone', 'race_log', 'moon_stone', 'sun_stone', 'ruby_knife', 'yakra_key', 'clone', 'tomas_pop', 'petals_2', 'fangs_2', 'horns_2', 'feathers_2', 'jetsoftime', 'pendant_charge', 'rainbow_shell', 'epoch', 'flight', 'dark_ages', 'future', 'last_village_portal', 'end_of_time', 'bucket', 'apocalypse', 'omen_present', 'omen_last_village', 'dark_ages_pillar', 'bangor_pillar', 'truce_pillar', 'desert', 'pacifist'}
    default = []


class HardLavosEndBoss(Toggle):
    """The game will end if Ocean Palace Lavos is defeated"""
    display_name = "Hard Lavos End Boss"


class BoatsOfTime(Toggle):
    """Additional ferry locations."""
    display_name = "Boats Of Time"


class JetsOfTime(Toggle):
    """Add JetsOfTime item and turn-in on Blackbird scaffolding"""
    display_name = "Jets Of Time"


class MinFlightDepth(Range):
    """Minimum logical depth at which flight can be obtained"""
    display_name = "Min Flight Depth"
    range_start = 0
    range_end = 6
    default = 0


class LockGates(Toggle):
    """Gates require the Gate Key to operate."""
    display_name = "Lock Gates"


class DisableElementLocks(Toggle):
    """Remove elemental requirement from Nizbel and Retinite"""
    display_name = "Disable Element Locks"


class BlockZenan600(Toggle):
    """Prevent overworld travel across Zenan Bridge in 600"""
    display_name = "Block Zenan 600"


class BlockZenan1000(Toggle):
    """Prevent overworld travel across Zenan Bridge in 1000"""
    display_name = "Block Zenan 1000"


class BossRandomizationType(Choice):
    """How bosses should be assigned to spots"""
    display_name = "Boss Randomization Type"

    option_vanilla = 0
    option_shuffle = 1
    option_rdi_random = 2
    default = 0


class MidbossRandomizationType(Choice):
    """How midbosses should be assigned to spots"""
    display_name = "Midboss Randomization Type"

    option_vanilla = 0
    option_shuffle = 1
    option_rdi_random = 2
    default = 0


class VanillaBossSpots(OptionList):
    """Spots which should always have their vanilla boss (or midboss)"""
    display_name = "Vanilla Boss Spots"
    valid_keys = {'manoria_catherdal', 'heckran_cave', 'denadoro_mts', 'zenan_bridge', 'reptite_lair', 'magus_castle_flea', 'magus_castle_slash', 'giants_claw', 'tyrano_lair_nizbel', 'zeal_palace', 'death_peak', 'black_omen_mega_mutant', 'black_omen_giga_mutant', 'black_omen_terra_mutant', 'black_omen_elder_spawn', 'kings_trial', 'sun_palace', 'sunken_desert', 'ocean_palace_twin_golem', 'ocean_palace_twin_golem_alt', 'geno_dome_final', 'beast_cave', 'mt_woe', 'arris_dome', 'factory_ruins', 'prison_catwalks', 'blackbird_left_wing', 'ozzies_fort_trio', 'north_cape', 'epoch_reborn', 'ozzies_fort_flea_plus', 'ozzies_fort_super_slash', 'geno_dome_mid', 'millennial_fair_gato', 'sewers_krawlie', 'black_omen_zeal'}
    default = []


class BossPool(OptionList):
    """Bosses to include in assignment (only when boss type is "random")"""
    display_name = "Boss Pool"
    valid_keys = {'dalton_plus', 'flea', 'flea_plus', 'golem', 'golem_boss', 'heckran', 'masa_mune', 'nizbel', 'nizbel_2', 'rust_tyrano', 'slash_sword', 'super_slash', 'yakra', 'yakra_xiii', 'zombor', 'lavos_spawn', 'elder_spawn', 'mega_mutant', 'giga_mutant', 'terra_mutant', 'retinite', 'son_of_sun', 'mother_brain', 'guardian', 'giga_gaia', 'mud_imp', 'r_series', 'dragon_tank', 'zeal', 'magus_north_cape'}
    default = ['dalton_plus', 'flea', 'flea_plus', 'golem', 'golem_boss', 'heckran', 'masa_mune', 'nizbel', 'nizbel_2', 'rust_tyrano', 'slash_sword', 'super_slash', 'yakra', 'yakra_xiii', 'zombor', 'lavos_spawn', 'elder_spawn', 'mega_mutant', 'giga_mutant', 'terra_mutant', 'retinite', 'son_of_sun', 'mother_brain', 'guardian', 'giga_gaia', 'mud_imp', 'r_series', 'dragon_tank', 'zeal', 'magus_north_cape']


class MidbossPool(OptionList):
    """Midbosses to include in assignment (only when boss type is "random")"""
    display_name = "Midboss Pool"
    valid_keys = {'gato', 'dalton', 'krawlie', 'super_slash', 'flea_plus', 'atropos_xr'}
    default = ['gato', 'dalton', 'krawlie', 'super_slash', 'flea_plus', 'atropos_xr']


class ShopInventoryRandomization(Choice):
    """How shop inventory should be randomized"""
    display_name = "Shop Inventory Randomization"

    option_vanilla = 0
    option_shuffle = 1
    option_full_random = 2
    option_tiered_random = 3
    option_custom_random = 4
    default = 0


class ShopCapacityRandomization(Choice):
    """How shop capacity should be randomized"""
    display_name = "Shop Capacity Randomization"

    option_vanilla = 0
    option_shuffle = 1
    option_rdi_random = 2
    default = 0


class NotBuyableItems(OptionList):
    """Items which can never appear in shops"""
    display_name = "Not Buyable Items"
    valid_keys = {'none', 'wood_sword', 'iron_blade', 'steelsaber', 'lode_sword', 'red_katana', 'flint_edge', 'dark_saber', 'aeon_blade', 'demon_edge', 'alloyblade', 'star_sword', 'vedicblade', 'kali_blade', 'shiva_edge', 'bolt_sword', 'slasher', 'bronze_bow', 'iron_bow', 'lode_bow', 'robin_bow', 'sage_bow', 'dream_bow', 'cometarrow', 'sonicarrow', 'valkerye', 'siren', 'scaling_level', 'objective_1', 'objective_2', 'objective_3', 'air_gun', 'dart_gun', 'auto_gun', 'picomagnum', 'plasma_gun', 'ruby_gun', 'dream_gun', 'megablast', 'shock_wave', 'wondershot', 'graedus', 'objective_4', 'objective_5', 'objective_6', 'objective_7', 'tin_arm', 'hammer_arm', 'miragehand', 'stone_arm', 'doomfinger', 'magma_hand', 'megatonarm', 'big_hand', 'kaiser_arm', 'giga_arm', 'terra_arm', 'crisis_arm', 'objective_8', 'bronzeedge', 'iron_sword', 'masamune_1', 'flashblade', 'pearl_edge', 'rune_blade', 'bravesword', 'masamune_2', 'demon_hit', 'fist', 'fist_2', 'fist_3', 'iron_fist', 'bronzefist', 'pacifist', 'apitem', 'darkscythe', 'hurricane', 'starscythe', 'doomsickle', 'mop', 'bent_sword', 'bent_hilt', 'masamune_0_atk', 'swallow', 'slasher_2', 'rainbow', 'unused_56', 'unused_57', 'unused_58', 'unused_59', 'weapon_end_5a', 'hide_tunic', 'karate_gi', 'bronzemail', 'maidensuit', 'iron_suit', 'titan_vest', 'gold_suit', 'ruby_vest', 'dark_mail', 'mist_robe', 'meso_mail', 'lumin_robe', 'flash_mail', 'lode_vest', 'aeon_suit', 'zodiaccape', 'nova_armor', 'prismdress', 'moon_armor', 'ruby_armor', 'ravenarmor', 'gloom_cape', 'white_mail', 'black_mail', 'blue_mail', 'red_mail', 'white_vest', 'black_vest', 'blue_vest', 'red_vest', 'taban_vest', 'taban_suit', 'armor_end_7b', 'hide_cap', 'bronzehelm', 'iron_helm', 'beret', 'gold_helm', 'rock_helm', 'ceratopper', 'glow_helm', 'lode_helm', 'aeon_helm', 'prism_helm', 'doom_helm', 'dark_helm', 'gloom_helm', 'safe_helm', 'taban_helm', 'sight_cap', 'memory_cap', 'time_hat', 'vigil_hat', 'ozziepants', 'haste_helm', 'rbow_helm', 'mermaidcap', 'helm_end_94', 'bandana', 'ribbon', 'powerglove', 'defender', 'magicscarf', 'amulet', 'dash_ring', 'hit_ring', 'power_ring', 'magic_ring', 'wall_ring', 'silvererng', 'gold_erng', 'silverstud', 'gold_stud', 'sightscope', 'charm_top', 'rage_band', 'frenzyband', 'third_eye', 'wallet', 'greendream', 'berserker', 'powerscarf', 'speed_belt', 'black_rock', 'blue_rock', 'silverrock', 'white_rock', 'gold_rock', 'hero_medal', 'musclering', 'flea_vest', 'magic_seal', 'power_seal', 'valor_crest', 'dragon_tear', 'sun_shades', 'prismspecs', 'accessory_end_bc', 'tonic', 'mid_tonic', 'full_tonic', 'ether', 'mid_ether', 'full_ether', 'elixir', 'hyperether', 'megaelixir', 'heal', 'revive', 'shelter', 'power_meal', 'lapis', 'barrier', 'shield', 'power_tab', 'magic_tab', 'speed_tab', 'petal', 'fang', 'horn', 'feather', 'seed', 'bike_key', 'pendant', 'gate_key', 'prismshard', 'c_trigger', 'tools', 'jerky', 'dreamstone', 'race_log', 'moon_stone', 'sun_stone', 'ruby_knife', 'yakra_key', 'clone', 'tomas_pop', 'petals_2', 'fangs_2', 'horns_2', 'feathers_2', 'bucketfrag', 'jetsoftime', 'pendant_charge', 'rainbow_shell', 'unused_ec', 'unused_ed', 'unused_ee', 'unused_ef', 'unused_f0', 'unused_f1'}
    default = ['slasher', 'masamune_1', 'masamune_2', 'bent_hilt', 'bent_sword', 'slasher_2', 'taban_vest', 'taban_helm', 'taban_suit', 'ozziepants', 'bandana', 'ribbon', 'powerglove', 'defender', 'magicscarf', 'amulet', 'dash_ring', 'hit_ring', 'power_ring', 'magic_ring', 'wall_ring', 'silvererng', 'gold_erng', 'silverstud', 'gold_stud', 'sightscope', 'charm_top', 'rage_band', 'frenzyband', 'third_eye', 'wallet', 'greendream', 'berserker', 'powerscarf', 'speed_belt', 'black_rock', 'blue_rock', 'silverrock', 'white_rock', 'gold_rock', 'hero_medal', 'musclering', 'flea_vest', 'magic_seal', 'power_seal', 'sun_shades', 'prismspecs', 'petal', 'horn', 'fang', 'feather', 'seed', 'bike_key', 'pendant', 'gate_key', 'prismshard', 'c_trigger', 'tools', 'jerky', 'race_log', 'moon_stone', 'sun_stone', 'dreamstone', 'ruby_knife', 'yakra_key', 'clone', 'tomas_pop', 'petals_2', 'fangs_2', 'horns_2', 'feathers_2', 'pendant_charge', 'rainbow_shell', 'jetsoftime', 'dragon_tear', 'valor_crest']


class NotSellableItems(OptionList):
    """Items which can never be sold"""
    display_name = "Not Sellable Items"
    valid_keys = {'wood_sword', 'iron_blade', 'steelsaber', 'lode_sword', 'red_katana', 'flint_edge', 'dark_saber', 'aeon_blade', 'demon_edge', 'alloyblade', 'star_sword', 'vedicblade', 'kali_blade', 'shiva_edge', 'bolt_sword', 'slasher', 'bronze_bow', 'iron_bow', 'lode_bow', 'robin_bow', 'sage_bow', 'dream_bow', 'cometarrow', 'sonicarrow', 'valkerye', 'siren', 'air_gun', 'dart_gun', 'auto_gun', 'picomagnum', 'plasma_gun', 'ruby_gun', 'dream_gun', 'megablast', 'shock_wave', 'wondershot', 'graedus', 'tin_arm', 'hammer_arm', 'miragehand', 'stone_arm', 'doomfinger', 'magma_hand', 'megatonarm', 'big_hand', 'kaiser_arm', 'giga_arm', 'terra_arm', 'crisis_arm', 'bronzeedge', 'iron_sword', 'masamune_1', 'flashblade', 'pearl_edge', 'rune_blade', 'bravesword', 'masamune_2', 'demon_hit', 'fist', 'fist_2', 'fist_3', 'iron_fist', 'bronzefist', 'pacifist', 'darkscythe', 'hurricane', 'starscythe', 'doomsickle', 'mop', 'bent_sword', 'bent_hilt', 'swallow', 'slasher_2', 'rainbow', 'hide_tunic', 'karate_gi', 'bronzemail', 'maidensuit', 'iron_suit', 'titan_vest', 'gold_suit', 'ruby_vest', 'dark_mail', 'mist_robe', 'meso_mail', 'lumin_robe', 'flash_mail', 'lode_vest', 'aeon_suit', 'zodiaccape', 'nova_armor', 'prismdress', 'moon_armor', 'ruby_armor', 'ravenarmor', 'gloom_cape', 'white_mail', 'black_mail', 'blue_mail', 'red_mail', 'white_vest', 'black_vest', 'blue_vest', 'red_vest', 'taban_vest', 'taban_suit', 'hide_cap', 'bronzehelm', 'iron_helm', 'beret', 'gold_helm', 'rock_helm', 'ceratopper', 'glow_helm', 'lode_helm', 'aeon_helm', 'prism_helm', 'doom_helm', 'dark_helm', 'gloom_helm', 'safe_helm', 'taban_helm', 'sight_cap', 'memory_cap', 'time_hat', 'vigil_hat', 'ozziepants', 'haste_helm', 'rbow_helm', 'mermaidcap', 'bandana', 'ribbon', 'powerglove', 'defender', 'magicscarf', 'amulet', 'dash_ring', 'hit_ring', 'power_ring', 'magic_ring', 'wall_ring', 'silvererng', 'gold_erng', 'silverstud', 'gold_stud', 'sightscope', 'charm_top', 'rage_band', 'frenzyband', 'third_eye', 'wallet', 'greendream', 'berserker', 'powerscarf', 'speed_belt', 'black_rock', 'blue_rock', 'silverrock', 'white_rock', 'gold_rock', 'hero_medal', 'musclering', 'flea_vest', 'magic_seal', 'power_seal', 'valor_crest', 'dragon_tear', 'sun_shades', 'prismspecs', 'tonic', 'mid_tonic', 'full_tonic', 'ether', 'mid_ether', 'full_ether', 'elixir', 'hyperether', 'megaelixir', 'heal', 'revive', 'shelter', 'power_meal', 'lapis', 'barrier', 'shield', 'power_tab', 'magic_tab', 'speed_tab', 'petal', 'fang', 'horn', 'feather', 'seed', 'bike_key', 'pendant', 'gate_key', 'prismshard', 'c_trigger', 'tools', 'jerky', 'dreamstone', 'race_log', 'moon_stone', 'sun_stone', 'ruby_knife', 'yakra_key', 'clone', 'tomas_pop', 'petals_2', 'fangs_2', 'horns_2', 'feathers_2', 'jetsoftime', 'pendant_charge', 'rainbow_shell'}
    default = ['slasher', 'masamune_1', 'masamune_2', 'bent_hilt', 'bent_sword', 'slasher_2', 'taban_vest', 'taban_helm', 'taban_suit', 'ozziepants', 'bandana', 'ribbon', 'powerglove', 'defender', 'magicscarf', 'amulet', 'dash_ring', 'hit_ring', 'power_ring', 'magic_ring', 'wall_ring', 'silvererng', 'gold_erng', 'silverstud', 'gold_stud', 'sightscope', 'charm_top', 'rage_band', 'frenzyband', 'third_eye', 'wallet', 'greendream', 'berserker', 'powerscarf', 'speed_belt', 'black_rock', 'blue_rock', 'silverrock', 'white_rock', 'gold_rock', 'hero_medal', 'musclering', 'flea_vest', 'magic_seal', 'power_seal', 'sun_shades', 'prismspecs', 'petal', 'horn', 'fang', 'feather', 'seed', 'bike_key', 'pendant', 'gate_key', 'prismshard', 'c_trigger', 'tools', 'jerky', 'race_log', 'moon_stone', 'sun_stone', 'dreamstone', 'ruby_knife', 'yakra_key', 'clone', 'tomas_pop', 'petals_2', 'fangs_2', 'horns_2', 'feathers_2', 'pendant_charge', 'rainbow_shell', 'jetsoftime', 'dragon_tear', 'valor_crest']


class ItemBasePrices(Choice):
    """Unmodified price of items"""
    display_name = "Item Base Prices"

    option_vanilla = 0
    option_balanced = 1
    option_max = 2
    default = 0


class ItemPriceRandomization(Choice):
    """How item prices should be randomized"""
    display_name = "Item Price Randomization"

    option_vanilla = 0
    option_rdi_random = 1
    option_random_multiplier = 2
    default = 0


class ItemPriceMinMultiplier(Range):
    """minimum price multiplier that an item's price can roll"""
    display_name = "Item Price Min Multiplier"
    range_start = 5
    range_end = 1000
    default = 50


class ItemPriceMaxMultiplier(Range):
    """maximum price multiplier that an item's price can roll"""
    display_name = "Item Price Max Multiplier"
    range_start = 5
    range_end = 1000
    default = 200


class GuaranteedShopItems(OptionList):
    """Items guaranteed to appear in some shop"""
    display_name = "Guaranteed Shop Items"
    valid_keys = {'wood_sword', 'iron_blade', 'steelsaber', 'lode_sword', 'red_katana', 'flint_edge', 'dark_saber', 'aeon_blade', 'demon_edge', 'alloyblade', 'star_sword', 'vedicblade', 'kali_blade', 'shiva_edge', 'bolt_sword', 'slasher', 'bronze_bow', 'iron_bow', 'lode_bow', 'robin_bow', 'sage_bow', 'dream_bow', 'cometarrow', 'sonicarrow', 'valkerye', 'siren', 'air_gun', 'dart_gun', 'auto_gun', 'picomagnum', 'plasma_gun', 'ruby_gun', 'dream_gun', 'megablast', 'shock_wave', 'wondershot', 'graedus', 'tin_arm', 'hammer_arm', 'miragehand', 'stone_arm', 'doomfinger', 'magma_hand', 'megatonarm', 'big_hand', 'kaiser_arm', 'giga_arm', 'terra_arm', 'crisis_arm', 'bronzeedge', 'iron_sword', 'masamune_1', 'flashblade', 'pearl_edge', 'rune_blade', 'bravesword', 'masamune_2', 'demon_hit', 'fist', 'fist_2', 'fist_3', 'iron_fist', 'bronzefist', 'pacifist', 'darkscythe', 'hurricane', 'starscythe', 'doomsickle', 'mop', 'bent_sword', 'bent_hilt', 'swallow', 'slasher_2', 'rainbow', 'hide_tunic', 'karate_gi', 'bronzemail', 'maidensuit', 'iron_suit', 'titan_vest', 'gold_suit', 'ruby_vest', 'dark_mail', 'mist_robe', 'meso_mail', 'lumin_robe', 'flash_mail', 'lode_vest', 'aeon_suit', 'zodiaccape', 'nova_armor', 'prismdress', 'moon_armor', 'ruby_armor', 'ravenarmor', 'gloom_cape', 'white_mail', 'black_mail', 'blue_mail', 'red_mail', 'white_vest', 'black_vest', 'blue_vest', 'red_vest', 'taban_vest', 'taban_suit', 'hide_cap', 'bronzehelm', 'iron_helm', 'beret', 'gold_helm', 'rock_helm', 'ceratopper', 'glow_helm', 'lode_helm', 'aeon_helm', 'prism_helm', 'doom_helm', 'dark_helm', 'gloom_helm', 'safe_helm', 'taban_helm', 'sight_cap', 'memory_cap', 'time_hat', 'vigil_hat', 'ozziepants', 'haste_helm', 'rbow_helm', 'mermaidcap', 'bandana', 'ribbon', 'powerglove', 'defender', 'magicscarf', 'amulet', 'dash_ring', 'hit_ring', 'power_ring', 'magic_ring', 'wall_ring', 'silvererng', 'gold_erng', 'silverstud', 'gold_stud', 'sightscope', 'charm_top', 'rage_band', 'frenzyband', 'third_eye', 'wallet', 'greendream', 'berserker', 'powerscarf', 'speed_belt', 'black_rock', 'blue_rock', 'silverrock', 'white_rock', 'gold_rock', 'hero_medal', 'musclering', 'flea_vest', 'magic_seal', 'power_seal', 'valor_crest', 'dragon_tear', 'sun_shades', 'prismspecs', 'tonic', 'mid_tonic', 'full_tonic', 'ether', 'mid_ether', 'full_ether', 'elixir', 'hyperether', 'megaelixir', 'heal', 'revive', 'shelter', 'power_meal', 'lapis', 'barrier', 'shield', 'power_tab', 'magic_tab', 'speed_tab', 'petal', 'fang', 'horn', 'feather', 'seed', 'bike_key', 'pendant', 'gate_key', 'prismshard', 'c_trigger', 'tools', 'jerky', 'dreamstone', 'race_log', 'moon_stone', 'sun_stone', 'ruby_knife', 'yakra_key', 'clone', 'tomas_pop', 'petals_2', 'fangs_2', 'horns_2', 'feathers_2', 'jetsoftime', 'pendant_charge', 'rainbow_shell'}
    default = []


class CustomShopItemSpec(FreeText):
    """Distribution for shop items"""
    display_name = "Custom Shop Item Spec"
    default = ""


class ShowAllCharsInShop(Toggle):
    """All characters will be shown when shopping."""
    display_name = "Show All Chars In Shop"


class NumAlgettyPortalObjectives(Range):
    """Number of objectives needed to unlock the portal in Algetty's entrance"""
    display_name = "Num Algetty Portal Objectives"
    range_start = 0
    range_end = 8
    default = 3


class NumOmenObjectives(Range):
    """Number of objectives needed to unlock the final door in the Black Omen"""
    display_name = "Num Omen Objectives"
    range_start = 0
    range_end = 8
    default = 4


class NumBucketObjectives(Range):
    """Number of objectives needed to unlock the bucket in the End of Time"""
    display_name = "Num Bucket Objectives"
    range_start = 0
    range_end = 8
    default = 5


class NumGauntletObjectives(Range):
    """Number of objectives needed to remove the lavos boss gauntlet"""
    display_name = "Num Gauntlet Objectives"
    range_start = 0
    range_end = 8
    default = 5


class NumTimegaugeObjectives(Range):
    """Number of objectives needed to unlock the bucket in the End of Time"""
    display_name = "Num Timegauge Objectives"
    range_start = 0
    range_end = 8
    default = 6


class NoOmenGauntlet(Toggle):
    """Lavos Gauntlet is disabled when entering from the Black Omen"""
    display_name = "No Omen Gauntlet"


class Objective1(FreeText):
    """Specifier for objective 1"""
    display_name = "Objective 1"
    default = ""


class Objective2(FreeText):
    """Specifier for objective 2"""
    display_name = "Objective 2"
    default = ""


class Objective3(FreeText):
    """Specifier for objective 3"""
    display_name = "Objective 3"
    default = ""


class Objective4(FreeText):
    """Specifier for objective 4"""
    display_name = "Objective 4"
    default = ""


class Objective5(FreeText):
    """Specifier for objective 5"""
    display_name = "Objective 5"
    default = ""


class Objective6(FreeText):
    """Specifier for objective 6"""
    display_name = "Objective 6"
    default = ""


class Objective7(FreeText):
    """Specifier for objective 7"""
    display_name = "Objective 7"
    default = ""


class Objective8(FreeText):
    """Specifier for objective 8"""
    display_name = "Objective 8"
    default = ""


class ShuffleEntrances(Toggle):
    """Whether to shuffle entrances or not"""
    display_name = "Shuffle Entrances"


class PreserveSpots(OptionList):
    """Spots which are to be shuffled among themselves"""
    display_name = "Preserve Spots"
    valid_keys = {'vortex_pt', 'northern_ruins_1000', 'fionas_shrine', 'cronos_house', 'truce_single_residence', 'truce_inn_1000', 'truce_ticket_office', 'truce_screaming_residence', 'millennial_fair', 'truce_market_1000', 'truce_mayor', 'luccas_house', 'guardia_castle_1000', 'guardia_forest_south_1000', 'guardia_forest_north_1000', 'zenan_bridge_1000_north', 'zenan_bridge_1000_south', 'porre_inn_1000', 'porre_market_1000', 'snail_stop', 'porre_mayor_1000', 'porre_residence_1000', 'porre_ticket_office', 'medina_elder_house', 'medina_inn', 'medina_portal', 'melchiors_hut', 'medina_market', 'medina_square', 'choras_mayor_1000', 'choras_inn_1000', 'choras_carpenter_1000', 'forest_ruins', 'heckran_cave', 'sun_keep_1000', 'west_cape', 'zenan_bridge_600_north', 'zenan_bridge_600_south', 'magic_cave_closed', 'magic_cave_open', 'sunken_desert', 'northern_ruins_600', 'magus_lair', 'giants_claw', 'truce_canyon', 'truce_couple_residence_600', 'truce_smith_residence', 'truce_inn_600', 'truce_market_600', 'guardia_forest_north_600', 'guardia_forest_south_600', 'guardia_castle_600', 'manoria_cathedral', 'dorino_bromide_residence', 'dorino_elder', 'dorino_inn', 'dorino_market', 'tatas_house', 'porre_elder_600', 'porre_cafe_600', 'porre_inn_600', 'porre_market_600', 'fionas_villa', 'choras_old_residence_600', 'choras_inn_600', 'choras_cafe_600', 'choras_carpenter_600', 'choras_market_600', 'cursed_woods', 'denadoro_mts', 'magic_cave_magus', 'ozzies_fort', 'sun_keep_600', 'trann_dome', 'bangor_dome', 'arris_dome', 'proto_dome', 'keepers_dome', 'factory_ruins', 'lab_16_west', 'lab_16_east', 'lab_32_west', 'lab_32_east', 'sewer_access_arris', 'sewer_access_keepers', 'sun_keep_2300', 'geno_dome', 'death_peak', 'sun_palace', 'mystic_mts', 'tyrano_lair', 'forest_maze_north', 'forest_maze_south', 'reptite_lair', 'dactyl_nest', 'sun_keep_prehistory', 'ioka_meeting_south', 'ioka_meeting_north', 'chiefs_hut', 'trading_post', 'ioka_sw_hut', 'ioka_sweet_water_hut', 'hunting_range', 'laruba_ruins', 'lair_ruins', 'terra_cave', 'skyway_enhasa_south', 'skyway_enhasa_north', 'skyway_kajar', 'dark_ages_portal', 'zeal_teleporter_bottom', 'zeal_teleporter_top', 'zeal_palace', 'enhasa', 'land_bridge_enhasa_north', 'land_bridge_enhasa_south', 'land_bridge_kajar', 'kajar', 'blackbird', 'north_cape', 'last_village_commons', 'last_village_empty_hut', 'last_village_shop', 'last_village_residence', 'sun_keep_last_village', 'last_village_portal'}
    default = ['manoria_cathedral', 'guardia_castle_1000', 'millennial_fair', 'guardia_castle_600', 'cursed_woods', 'dactyl_nest', 'proto_dome', 'north_cape', 'death_peak', 'heckran_cave', 'vortex_pt', 'zenan_bridge_600_north', 'denadoro_mts', 'magus_lair', 'arris_dome', 'factory_ruins', 'northern_ruins_600', 'northern_ruins_1000', 'giants_claw', 'ozzies_fort', 'sunken_desert', 'sun_palace', 'geno_dome', 'reptite_lair', 'lair_ruins', 'terra_cave', 'last_village_commons', 'zeal_palace', 'blackbird', 'west_cape', 'choras_carpenter_600', 'luccas_house', 'sun_keep_prehistory', 'sun_keep_2300', 'porre_mayor_1000', 'porre_elder_600', 'fionas_villa', 'fionas_shrine', 'snail_stop', 'keepers_dome', 'tatas_house']


class RestVanilla(Toggle):
    """Only shuffle locations in preserve_spots"""
    display_name = "Rest Vanilla"


class VanillaSpots(OptionList):
    """Spots guaranteed to not be shuffled. Takes precedence over preserve_spots"""
    display_name = "Vanilla Spots"
    valid_keys = {'vortex_pt', 'northern_ruins_1000', 'fionas_shrine', 'cronos_house', 'truce_single_residence', 'truce_inn_1000', 'truce_ticket_office', 'truce_screaming_residence', 'millennial_fair', 'truce_market_1000', 'truce_mayor', 'luccas_house', 'guardia_castle_1000', 'guardia_forest_south_1000', 'guardia_forest_north_1000', 'zenan_bridge_1000_north', 'zenan_bridge_1000_south', 'porre_inn_1000', 'porre_market_1000', 'snail_stop', 'porre_mayor_1000', 'porre_residence_1000', 'porre_ticket_office', 'medina_elder_house', 'medina_inn', 'medina_portal', 'melchiors_hut', 'medina_market', 'medina_square', 'choras_mayor_1000', 'choras_inn_1000', 'choras_carpenter_1000', 'forest_ruins', 'heckran_cave', 'sun_keep_1000', 'west_cape', 'zenan_bridge_600_north', 'zenan_bridge_600_south', 'magic_cave_closed', 'magic_cave_open', 'sunken_desert', 'northern_ruins_600', 'magus_lair', 'giants_claw', 'truce_canyon', 'truce_couple_residence_600', 'truce_smith_residence', 'truce_inn_600', 'truce_market_600', 'guardia_forest_north_600', 'guardia_forest_south_600', 'guardia_castle_600', 'manoria_cathedral', 'dorino_bromide_residence', 'dorino_elder', 'dorino_inn', 'dorino_market', 'tatas_house', 'porre_elder_600', 'porre_cafe_600', 'porre_inn_600', 'porre_market_600', 'fionas_villa', 'choras_old_residence_600', 'choras_inn_600', 'choras_cafe_600', 'choras_carpenter_600', 'choras_market_600', 'cursed_woods', 'denadoro_mts', 'magic_cave_magus', 'ozzies_fort', 'sun_keep_600', 'trann_dome', 'bangor_dome', 'arris_dome', 'proto_dome', 'keepers_dome', 'factory_ruins', 'lab_16_west', 'lab_16_east', 'lab_32_west', 'lab_32_east', 'sewer_access_arris', 'sewer_access_keepers', 'sun_keep_2300', 'geno_dome', 'death_peak', 'sun_palace', 'mystic_mts', 'tyrano_lair', 'forest_maze_north', 'forest_maze_south', 'reptite_lair', 'dactyl_nest', 'sun_keep_prehistory', 'ioka_meeting_south', 'ioka_meeting_north', 'chiefs_hut', 'trading_post', 'ioka_sw_hut', 'ioka_sweet_water_hut', 'hunting_range', 'laruba_ruins', 'lair_ruins', 'terra_cave', 'skyway_enhasa_south', 'skyway_enhasa_north', 'skyway_kajar', 'dark_ages_portal', 'zeal_teleporter_bottom', 'zeal_teleporter_top', 'zeal_palace', 'enhasa', 'land_bridge_enhasa_north', 'land_bridge_enhasa_south', 'land_bridge_kajar', 'kajar', 'blackbird', 'north_cape', 'last_village_commons', 'last_village_empty_hut', 'last_village_shop', 'last_village_residence', 'sun_keep_last_village', 'last_village_portal'}
    default = []


class ShuffleGates(Toggle):
    """Shuffle where (non-algetty) portals lead to"""
    display_name = "Shuffle Gates"


class SeparateGateEras(Toggle):
    """Shuffled gates must go to different eras"""
    display_name = "Separate Gate Eras"


class LairRuinsDefaultSpot(Choice):
    """Default (vanilla) overworld exit to lair ruins portal"""
    display_name = "Lair Ruins Default Spot"

    option_vortex_pt = 0
    option_northern_ruins_1000 = 1
    option_fionas_shrine = 2
    option_cronos_house = 3
    option_truce_single_residence = 4
    option_truce_inn_1000 = 5
    option_truce_ticket_office = 6
    option_truce_screaming_residence = 7
    option_millennial_fair = 8
    option_truce_market_1000 = 9
    option_truce_mayor = 10
    option_luccas_house = 11
    option_guardia_castle_1000 = 12
    option_guardia_forest_south_1000 = 13
    option_guardia_forest_north_1000 = 14
    option_zenan_bridge_1000_north = 15
    option_zenan_bridge_1000_south = 16
    option_porre_inn_1000 = 17
    option_porre_market_1000 = 18
    option_snail_stop = 19
    option_porre_mayor_1000 = 20
    option_porre_residence_1000 = 21
    option_porre_ticket_office = 22
    option_medina_elder_house = 23
    option_medina_inn = 24
    option_medina_portal = 25
    option_melchiors_hut = 26
    option_medina_market = 27
    option_medina_square = 28
    option_choras_mayor_1000 = 29
    option_choras_inn_1000 = 30
    option_choras_carpenter_1000 = 31
    option_forest_ruins = 32
    option_heckran_cave = 33
    option_sun_keep_1000 = 34
    option_west_cape = 35
    option_zenan_bridge_600_north = 36
    option_zenan_bridge_600_south = 37
    option_magic_cave_closed = 38
    option_magic_cave_open = 39
    option_sunken_desert = 40
    option_northern_ruins_600 = 41
    option_magus_lair = 42
    option_giants_claw = 43
    option_truce_canyon = 44
    option_truce_couple_residence_600 = 45
    option_truce_smith_residence = 46
    option_truce_inn_600 = 47
    option_truce_market_600 = 48
    option_guardia_forest_north_600 = 49
    option_guardia_forest_south_600 = 50
    option_guardia_castle_600 = 51
    option_manoria_cathedral = 52
    option_dorino_bromide_residence = 53
    option_dorino_elder = 54
    option_dorino_inn = 55
    option_dorino_market = 56
    option_tatas_house = 57
    option_porre_elder_600 = 58
    option_porre_cafe_600 = 59
    option_porre_inn_600 = 60
    option_porre_market_600 = 61
    option_fionas_villa = 62
    option_choras_old_residence_600 = 63
    option_choras_inn_600 = 64
    option_choras_cafe_600 = 65
    option_choras_carpenter_600 = 66
    option_choras_market_600 = 67
    option_cursed_woods = 68
    option_denadoro_mts = 69
    option_magic_cave_magus = 70
    option_ozzies_fort = 71
    option_sun_keep_600 = 72
    option_trann_dome = 73
    option_bangor_dome = 74
    option_arris_dome = 75
    option_proto_dome = 76
    option_keepers_dome = 77
    option_factory_ruins = 78
    option_lab_16_west = 79
    option_lab_16_east = 80
    option_lab_32_west = 81
    option_lab_32_east = 82
    option_sewer_access_arris = 83
    option_sewer_access_keepers = 84
    option_sun_keep_2300 = 85
    option_geno_dome = 86
    option_death_peak = 87
    option_sun_palace = 88
    option_mystic_mts = 89
    option_tyrano_lair = 90
    option_forest_maze_north = 91
    option_forest_maze_south = 92
    option_reptite_lair = 93
    option_dactyl_nest = 94
    option_sun_keep_prehistory = 95
    option_ioka_meeting_south = 96
    option_ioka_meeting_north = 97
    option_chiefs_hut = 98
    option_trading_post = 99
    option_ioka_sw_hut = 100
    option_ioka_sweet_water_hut = 101
    option_hunting_range = 102
    option_laruba_ruins = 103
    option_lair_ruins = 104
    option_terra_cave = 105
    option_skyway_enhasa_south = 106
    option_skyway_enhasa_north = 107
    option_skyway_kajar = 108
    option_dark_ages_portal = 109
    option_zeal_teleporter_bottom = 110
    option_zeal_teleporter_top = 111
    option_zeal_palace = 112
    option_enhasa = 113
    option_land_bridge_enhasa_north = 114
    option_land_bridge_enhasa_south = 115
    option_land_bridge_kajar = 116
    option_kajar = 117
    option_blackbird = 118
    option_north_cape = 119
    option_last_village_commons = 120
    option_last_village_empty_hut = 121
    option_last_village_shop = 122
    option_last_village_residence = 123
    option_sun_keep_last_village = 124
    option_last_village_portal = 125
    default = 123


class PreserveSpots1(OptionList):
    """Spots which are to be shuffled among themselves (Group 1)"""
    display_name = "Preserve Spots 1"
    valid_keys = {'vortex_pt', 'northern_ruins_1000', 'fionas_shrine', 'cronos_house', 'truce_single_residence', 'truce_inn_1000', 'truce_ticket_office', 'truce_screaming_residence', 'millennial_fair', 'truce_market_1000', 'truce_mayor', 'luccas_house', 'guardia_castle_1000', 'guardia_forest_south_1000', 'guardia_forest_north_1000', 'zenan_bridge_1000_north', 'zenan_bridge_1000_south', 'porre_inn_1000', 'porre_market_1000', 'snail_stop', 'porre_mayor_1000', 'porre_residence_1000', 'porre_ticket_office', 'medina_elder_house', 'medina_inn', 'medina_portal', 'melchiors_hut', 'medina_market', 'medina_square', 'choras_mayor_1000', 'choras_inn_1000', 'choras_carpenter_1000', 'forest_ruins', 'heckran_cave', 'sun_keep_1000', 'west_cape', 'zenan_bridge_600_north', 'zenan_bridge_600_south', 'magic_cave_closed', 'magic_cave_open', 'sunken_desert', 'northern_ruins_600', 'magus_lair', 'giants_claw', 'truce_canyon', 'truce_couple_residence_600', 'truce_smith_residence', 'truce_inn_600', 'truce_market_600', 'guardia_forest_north_600', 'guardia_forest_south_600', 'guardia_castle_600', 'manoria_cathedral', 'dorino_bromide_residence', 'dorino_elder', 'dorino_inn', 'dorino_market', 'tatas_house', 'porre_elder_600', 'porre_cafe_600', 'porre_inn_600', 'porre_market_600', 'fionas_villa', 'choras_old_residence_600', 'choras_inn_600', 'choras_cafe_600', 'choras_carpenter_600', 'choras_market_600', 'cursed_woods', 'denadoro_mts', 'magic_cave_magus', 'ozzies_fort', 'sun_keep_600', 'trann_dome', 'bangor_dome', 'arris_dome', 'proto_dome', 'keepers_dome', 'factory_ruins', 'lab_16_west', 'lab_16_east', 'lab_32_west', 'lab_32_east', 'sewer_access_arris', 'sewer_access_keepers', 'sun_keep_2300', 'geno_dome', 'death_peak', 'sun_palace', 'mystic_mts', 'tyrano_lair', 'forest_maze_north', 'forest_maze_south', 'reptite_lair', 'dactyl_nest', 'sun_keep_prehistory', 'ioka_meeting_south', 'ioka_meeting_north', 'chiefs_hut', 'trading_post', 'ioka_sw_hut', 'ioka_sweet_water_hut', 'hunting_range', 'laruba_ruins', 'lair_ruins', 'terra_cave', 'skyway_enhasa_south', 'skyway_enhasa_north', 'skyway_kajar', 'dark_ages_portal', 'zeal_teleporter_bottom', 'zeal_teleporter_top', 'zeal_palace', 'enhasa', 'land_bridge_enhasa_north', 'land_bridge_enhasa_south', 'land_bridge_kajar', 'kajar', 'blackbird', 'north_cape', 'last_village_commons', 'last_village_empty_hut', 'last_village_shop', 'last_village_residence', 'sun_keep_last_village', 'last_village_portal'}
    default = []


class PreserveSpots2(OptionList):
    """Spots which are to be shuffled among themselves (Group 2)"""
    display_name = "Preserve Spots 2"
    valid_keys = {'vortex_pt', 'northern_ruins_1000', 'fionas_shrine', 'cronos_house', 'truce_single_residence', 'truce_inn_1000', 'truce_ticket_office', 'truce_screaming_residence', 'millennial_fair', 'truce_market_1000', 'truce_mayor', 'luccas_house', 'guardia_castle_1000', 'guardia_forest_south_1000', 'guardia_forest_north_1000', 'zenan_bridge_1000_north', 'zenan_bridge_1000_south', 'porre_inn_1000', 'porre_market_1000', 'snail_stop', 'porre_mayor_1000', 'porre_residence_1000', 'porre_ticket_office', 'medina_elder_house', 'medina_inn', 'medina_portal', 'melchiors_hut', 'medina_market', 'medina_square', 'choras_mayor_1000', 'choras_inn_1000', 'choras_carpenter_1000', 'forest_ruins', 'heckran_cave', 'sun_keep_1000', 'west_cape', 'zenan_bridge_600_north', 'zenan_bridge_600_south', 'magic_cave_closed', 'magic_cave_open', 'sunken_desert', 'northern_ruins_600', 'magus_lair', 'giants_claw', 'truce_canyon', 'truce_couple_residence_600', 'truce_smith_residence', 'truce_inn_600', 'truce_market_600', 'guardia_forest_north_600', 'guardia_forest_south_600', 'guardia_castle_600', 'manoria_cathedral', 'dorino_bromide_residence', 'dorino_elder', 'dorino_inn', 'dorino_market', 'tatas_house', 'porre_elder_600', 'porre_cafe_600', 'porre_inn_600', 'porre_market_600', 'fionas_villa', 'choras_old_residence_600', 'choras_inn_600', 'choras_cafe_600', 'choras_carpenter_600', 'choras_market_600', 'cursed_woods', 'denadoro_mts', 'magic_cave_magus', 'ozzies_fort', 'sun_keep_600', 'trann_dome', 'bangor_dome', 'arris_dome', 'proto_dome', 'keepers_dome', 'factory_ruins', 'lab_16_west', 'lab_16_east', 'lab_32_west', 'lab_32_east', 'sewer_access_arris', 'sewer_access_keepers', 'sun_keep_2300', 'geno_dome', 'death_peak', 'sun_palace', 'mystic_mts', 'tyrano_lair', 'forest_maze_north', 'forest_maze_south', 'reptite_lair', 'dactyl_nest', 'sun_keep_prehistory', 'ioka_meeting_south', 'ioka_meeting_north', 'chiefs_hut', 'trading_post', 'ioka_sw_hut', 'ioka_sweet_water_hut', 'hunting_range', 'laruba_ruins', 'lair_ruins', 'terra_cave', 'skyway_enhasa_south', 'skyway_enhasa_north', 'skyway_kajar', 'dark_ages_portal', 'zeal_teleporter_bottom', 'zeal_teleporter_top', 'zeal_palace', 'enhasa', 'land_bridge_enhasa_north', 'land_bridge_enhasa_south', 'land_bridge_kajar', 'kajar', 'blackbird', 'north_cape', 'last_village_commons', 'last_village_empty_hut', 'last_village_shop', 'last_village_residence', 'sun_keep_last_village', 'last_village_portal'}
    default = []


class PreserveSpots3(OptionList):
    """Spots which are to be shuffled among themselves (Group 3)"""
    display_name = "Preserve Spots 3"
    valid_keys = {'vortex_pt', 'northern_ruins_1000', 'fionas_shrine', 'cronos_house', 'truce_single_residence', 'truce_inn_1000', 'truce_ticket_office', 'truce_screaming_residence', 'millennial_fair', 'truce_market_1000', 'truce_mayor', 'luccas_house', 'guardia_castle_1000', 'guardia_forest_south_1000', 'guardia_forest_north_1000', 'zenan_bridge_1000_north', 'zenan_bridge_1000_south', 'porre_inn_1000', 'porre_market_1000', 'snail_stop', 'porre_mayor_1000', 'porre_residence_1000', 'porre_ticket_office', 'medina_elder_house', 'medina_inn', 'medina_portal', 'melchiors_hut', 'medina_market', 'medina_square', 'choras_mayor_1000', 'choras_inn_1000', 'choras_carpenter_1000', 'forest_ruins', 'heckran_cave', 'sun_keep_1000', 'west_cape', 'zenan_bridge_600_north', 'zenan_bridge_600_south', 'magic_cave_closed', 'magic_cave_open', 'sunken_desert', 'northern_ruins_600', 'magus_lair', 'giants_claw', 'truce_canyon', 'truce_couple_residence_600', 'truce_smith_residence', 'truce_inn_600', 'truce_market_600', 'guardia_forest_north_600', 'guardia_forest_south_600', 'guardia_castle_600', 'manoria_cathedral', 'dorino_bromide_residence', 'dorino_elder', 'dorino_inn', 'dorino_market', 'tatas_house', 'porre_elder_600', 'porre_cafe_600', 'porre_inn_600', 'porre_market_600', 'fionas_villa', 'choras_old_residence_600', 'choras_inn_600', 'choras_cafe_600', 'choras_carpenter_600', 'choras_market_600', 'cursed_woods', 'denadoro_mts', 'magic_cave_magus', 'ozzies_fort', 'sun_keep_600', 'trann_dome', 'bangor_dome', 'arris_dome', 'proto_dome', 'keepers_dome', 'factory_ruins', 'lab_16_west', 'lab_16_east', 'lab_32_west', 'lab_32_east', 'sewer_access_arris', 'sewer_access_keepers', 'sun_keep_2300', 'geno_dome', 'death_peak', 'sun_palace', 'mystic_mts', 'tyrano_lair', 'forest_maze_north', 'forest_maze_south', 'reptite_lair', 'dactyl_nest', 'sun_keep_prehistory', 'ioka_meeting_south', 'ioka_meeting_north', 'chiefs_hut', 'trading_post', 'ioka_sw_hut', 'ioka_sweet_water_hut', 'hunting_range', 'laruba_ruins', 'lair_ruins', 'terra_cave', 'skyway_enhasa_south', 'skyway_enhasa_north', 'skyway_kajar', 'dark_ages_portal', 'zeal_teleporter_bottom', 'zeal_teleporter_top', 'zeal_palace', 'enhasa', 'land_bridge_enhasa_north', 'land_bridge_enhasa_south', 'land_bridge_kajar', 'kajar', 'blackbird', 'north_cape', 'last_village_commons', 'last_village_empty_hut', 'last_village_shop', 'last_village_residence', 'sun_keep_last_village', 'last_village_portal'}
    default = []


class PreserveSpots4(OptionList):
    """Spots which are to be shuffled among themselves (Group 4)"""
    display_name = "Preserve Spots 4"
    valid_keys = {'vortex_pt', 'northern_ruins_1000', 'fionas_shrine', 'cronos_house', 'truce_single_residence', 'truce_inn_1000', 'truce_ticket_office', 'truce_screaming_residence', 'millennial_fair', 'truce_market_1000', 'truce_mayor', 'luccas_house', 'guardia_castle_1000', 'guardia_forest_south_1000', 'guardia_forest_north_1000', 'zenan_bridge_1000_north', 'zenan_bridge_1000_south', 'porre_inn_1000', 'porre_market_1000', 'snail_stop', 'porre_mayor_1000', 'porre_residence_1000', 'porre_ticket_office', 'medina_elder_house', 'medina_inn', 'medina_portal', 'melchiors_hut', 'medina_market', 'medina_square', 'choras_mayor_1000', 'choras_inn_1000', 'choras_carpenter_1000', 'forest_ruins', 'heckran_cave', 'sun_keep_1000', 'west_cape', 'zenan_bridge_600_north', 'zenan_bridge_600_south', 'magic_cave_closed', 'magic_cave_open', 'sunken_desert', 'northern_ruins_600', 'magus_lair', 'giants_claw', 'truce_canyon', 'truce_couple_residence_600', 'truce_smith_residence', 'truce_inn_600', 'truce_market_600', 'guardia_forest_north_600', 'guardia_forest_south_600', 'guardia_castle_600', 'manoria_cathedral', 'dorino_bromide_residence', 'dorino_elder', 'dorino_inn', 'dorino_market', 'tatas_house', 'porre_elder_600', 'porre_cafe_600', 'porre_inn_600', 'porre_market_600', 'fionas_villa', 'choras_old_residence_600', 'choras_inn_600', 'choras_cafe_600', 'choras_carpenter_600', 'choras_market_600', 'cursed_woods', 'denadoro_mts', 'magic_cave_magus', 'ozzies_fort', 'sun_keep_600', 'trann_dome', 'bangor_dome', 'arris_dome', 'proto_dome', 'keepers_dome', 'factory_ruins', 'lab_16_west', 'lab_16_east', 'lab_32_west', 'lab_32_east', 'sewer_access_arris', 'sewer_access_keepers', 'sun_keep_2300', 'geno_dome', 'death_peak', 'sun_palace', 'mystic_mts', 'tyrano_lair', 'forest_maze_north', 'forest_maze_south', 'reptite_lair', 'dactyl_nest', 'sun_keep_prehistory', 'ioka_meeting_south', 'ioka_meeting_north', 'chiefs_hut', 'trading_post', 'ioka_sw_hut', 'ioka_sweet_water_hut', 'hunting_range', 'laruba_ruins', 'lair_ruins', 'terra_cave', 'skyway_enhasa_south', 'skyway_enhasa_north', 'skyway_kajar', 'dark_ages_portal', 'zeal_teleporter_bottom', 'zeal_teleporter_top', 'zeal_palace', 'enhasa', 'land_bridge_enhasa_north', 'land_bridge_enhasa_south', 'land_bridge_kajar', 'kajar', 'blackbird', 'north_cape', 'last_village_commons', 'last_village_empty_hut', 'last_village_shop', 'last_village_residence', 'sun_keep_last_village', 'last_village_portal'}
    default = []


class StarterMinLevel(Range):
    """Minimum level at which the starter recruit can join (default: 1)"""
    display_name = "Starter Min Level"
    range_start = 1
    range_end = 99
    default = 1


class StarterMinTechlevel(Range):
    """Minimum techlevel at which the starter recruit can join (default: 0)"""
    display_name = "Starter Min Techlevel"
    range_start = 0
    range_end = 8
    default = 0


class FairMinLevel(Range):
    """Minimum level at which the fair recruit can join (default: 1)"""
    display_name = "Fair Min Level"
    range_start = 1
    range_end = 99
    default = 1


class FairMinTechlevel(Range):
    """Minimum techlevel at which the fair recruit can join (default: 0)"""
    display_name = "Fair Min Techlevel"
    range_start = 0
    range_end = 8
    default = 0


class CathedralMinLevel(Range):
    """Minimum level at which the cathedral recruit can join (default: 5)"""
    display_name = "Cathedral Min Level"
    range_start = 1
    range_end = 99
    default = 5


class CathedralMinTechlevel(Range):
    """Minimum techlevel at which the cathedral recruit can join (default: 0)"""
    display_name = "Cathedral Min Techlevel"
    range_start = 0
    range_end = 8
    default = 0


class CastleMinLevel(Range):
    """Minimum level at which the castle recruit can join (default: 5)"""
    display_name = "Castle Min Level"
    range_start = 1
    range_end = 99
    default = 5


class CastleMinTechlevel(Range):
    """Minimum techlevel at which the castle recruit can join (default: 1)"""
    display_name = "Castle Min Techlevel"
    range_start = 0
    range_end = 8
    default = 1


class TrialMinLevel(Range):
    """Minimum level at which the trial recruit can join (default: 7)"""
    display_name = "Trial Min Level"
    range_start = 1
    range_end = 99
    default = 7


class TrialMinTechlevel(Range):
    """Minimum techlevel at which the trial recruit can join (default: 1)"""
    display_name = "Trial Min Techlevel"
    range_start = 0
    range_end = 8
    default = 1


class ProtoMinLevel(Range):
    """Minimum level at which the proto recruit can join (default: 10)"""
    display_name = "Proto Min Level"
    range_start = 1
    range_end = 99
    default = 10


class ProtoMinTechlevel(Range):
    """Minimum techlevel at which the proto recruit can join (default: 2)"""
    display_name = "Proto Min Techlevel"
    range_start = 0
    range_end = 8
    default = 2


class NorthCapeMinLevel(Range):
    """Minimum level at which the north_cape recruit can join (default: 37)"""
    display_name = "North Cape Min Level"
    range_start = 1
    range_end = 99
    default = 37


class NorthCapeMinTechlevel(Range):
    """Minimum techlevel at which the north_cape recruit can join (default: 3)"""
    display_name = "North Cape Min Techlevel"
    range_start = 0
    range_end = 8
    default = 3


class BurrowMinLevel(Range):
    """Minimum level at which the burrow recruit can join (default: 18)"""
    display_name = "Burrow Min Level"
    range_start = 1
    range_end = 99
    default = 18


class BurrowMinTechlevel(Range):
    """Minimum techlevel at which the burrow recruit can join (default: 2)"""
    display_name = "Burrow Min Techlevel"
    range_start = 0
    range_end = 8
    default = 2


class DactylMinLevel(Range):
    """Minimum level at which the dactyl recruit can join (default: 20)"""
    display_name = "Dactyl Min Level"
    range_start = 1
    range_end = 99
    default = 20


class DactylMinTechlevel(Range):
    """Minimum techlevel at which the dactyl recruit can join (default: 2)"""
    display_name = "Dactyl Min Techlevel"
    range_start = 0
    range_end = 8
    default = 2


class DeathPeakMinLevel(Range):
    """Minimum level at which the death_peak recruit can join (default: 37)"""
    display_name = "Death Peak Min Level"
    range_start = 1
    range_end = 99
    default = 37


class DeathPeakMinTechlevel(Range):
    """Minimum techlevel at which the death_peak recruit can join (default: 8)"""
    display_name = "Death Peak Min Techlevel"
    range_start = 0
    range_end = 8
    default = 8


class YakraBoxMinLevel(Range):
    """Minimum level at which the yakra_box recruit can join (default: 25)"""
    display_name = "Yakra Box Min Level"
    range_start = 1
    range_end = 99
    default = 25


class YakraBoxMinTechlevel(Range):
    """Minimum techlevel at which the yakra_box recruit can join (default: 3)"""
    display_name = "Yakra Box Min Techlevel"
    range_start = 0
    range_end = 8
    default = 3


class MinimumRecruits(Toggle):
    """All recruits are given a min level of 1 and min tech level of 0, overrides other settings"""
    display_name = "Minimum Recruits"


class ScaleLevelToLeader(Toggle):
    """Recruits are scaled to the level of the lead character (but not below the spot minimum)"""
    display_name = "Scale Level To Leader"


class ScaleTechlevelToLeader(Toggle):
    """Recruits are scaled to the tech level of the lead character (but not below the spot minimum)"""
    display_name = "Scale Techlevel To Leader"


class ScaleGear(Toggle):
    """Recruit gear is scaled based on the level at which they are recruited"""
    display_name = "Scale Gear"


class LootPool(Choice):
    """Method to determine which loot is available for assignment"""
    display_name = "Loot Pool"

    option_vanilla = 0
    option_rdi_random = 1
    option_tiered_random = 2
    default = 0


class CustomLootPool(FreeText):
    """Custom distribution for loot pool (e.g. 75:"vanilla", 25:"random"). Overrides loot_pool.  Leave "none" to ignore."""
    display_name = "Custom Loot Pool"
    default = ""


class LootAssignmentScheme(Choice):
    """Method used to assign loot."""
    display_name = "Loot Assignment Scheme"

    option_shuffle = 0
    option_logic_depth = 1
    default = 0


class GoodLoot(OptionList):
    """Loot that is considered to be good (ignored by vanilla)"""
    display_name = "Good Loot"
    valid_keys = {'wood_sword', 'iron_blade', 'steelsaber', 'lode_sword', 'red_katana', 'flint_edge', 'dark_saber', 'aeon_blade', 'demon_edge', 'alloyblade', 'star_sword', 'vedicblade', 'kali_blade', 'shiva_edge', 'bolt_sword', 'slasher', 'bronze_bow', 'iron_bow', 'lode_bow', 'robin_bow', 'sage_bow', 'dream_bow', 'cometarrow', 'sonicarrow', 'valkerye', 'siren', 'air_gun', 'dart_gun', 'auto_gun', 'picomagnum', 'plasma_gun', 'ruby_gun', 'dream_gun', 'megablast', 'shock_wave', 'wondershot', 'graedus', 'tin_arm', 'hammer_arm', 'miragehand', 'stone_arm', 'doomfinger', 'magma_hand', 'megatonarm', 'big_hand', 'kaiser_arm', 'giga_arm', 'terra_arm', 'crisis_arm', 'bronzeedge', 'iron_sword', 'masamune_1', 'flashblade', 'pearl_edge', 'rune_blade', 'bravesword', 'masamune_2', 'demon_hit', 'fist', 'fist_2', 'fist_3', 'iron_fist', 'bronzefist', 'pacifist', 'darkscythe', 'hurricane', 'starscythe', 'doomsickle', 'mop', 'bent_sword', 'bent_hilt', 'swallow', 'slasher_2', 'rainbow', 'hide_tunic', 'karate_gi', 'bronzemail', 'maidensuit', 'iron_suit', 'titan_vest', 'gold_suit', 'ruby_vest', 'dark_mail', 'mist_robe', 'meso_mail', 'lumin_robe', 'flash_mail', 'lode_vest', 'aeon_suit', 'zodiaccape', 'nova_armor', 'prismdress', 'moon_armor', 'ruby_armor', 'ravenarmor', 'gloom_cape', 'white_mail', 'black_mail', 'blue_mail', 'red_mail', 'white_vest', 'black_vest', 'blue_vest', 'red_vest', 'taban_vest', 'taban_suit', 'hide_cap', 'bronzehelm', 'iron_helm', 'beret', 'gold_helm', 'rock_helm', 'ceratopper', 'glow_helm', 'lode_helm', 'aeon_helm', 'prism_helm', 'doom_helm', 'dark_helm', 'gloom_helm', 'safe_helm', 'taban_helm', 'sight_cap', 'memory_cap', 'time_hat', 'vigil_hat', 'ozziepants', 'haste_helm', 'rbow_helm', 'mermaidcap', 'bandana', 'ribbon', 'powerglove', 'defender', 'magicscarf', 'amulet', 'dash_ring', 'hit_ring', 'power_ring', 'magic_ring', 'wall_ring', 'silvererng', 'gold_erng', 'silverstud', 'gold_stud', 'sightscope', 'charm_top', 'rage_band', 'frenzyband', 'third_eye', 'wallet', 'greendream', 'berserker', 'powerscarf', 'speed_belt', 'black_rock', 'blue_rock', 'silverrock', 'white_rock', 'gold_rock', 'hero_medal', 'musclering', 'flea_vest', 'magic_seal', 'power_seal', 'valor_crest', 'dragon_tear', 'sun_shades', 'prismspecs', 'tonic', 'mid_tonic', 'full_tonic', 'ether', 'mid_ether', 'full_ether', 'elixir', 'hyperether', 'megaelixir', 'heal', 'revive', 'shelter', 'power_meal', 'lapis', 'barrier', 'shield', 'power_tab', 'magic_tab', 'speed_tab', 'petal', 'fang', 'horn', 'feather', 'seed', 'bike_key', 'pendant', 'gate_key', 'prismshard', 'c_trigger', 'tools', 'jerky', 'dreamstone', 'race_log', 'moon_stone', 'sun_stone', 'ruby_knife', 'yakra_key', 'clone', 'tomas_pop', 'petals_2', 'fangs_2', 'horns_2', 'feathers_2', 'jetsoftime', 'pendant_charge', 'rainbow_shell'}
    default = ['megaelixir', 'hyperether', 'elixir', 'speed_tab', 'rainbow', 'shiva_edge', 'swallow', 'valkerye', 'siren', 'wondershot', 'taban_suit', 'crisis_arm', 'terra_arm', 'masamune_2', 'bronzefist', 'doomsickle', 'gloom_helm', 'gloom_cape', 'prismspecs', 'prismdress', 'prism_helm', 'sun_shades', 'vigil_hat', 'safe_helm', 'haste_helm', 'flea_vest', 'rbow_helm', 'mermaidcap', 'dark_helm', 'nova_armor', 'moon_armor', 'zodiaccape', 'gold_stud', 'gold_erng', 'blue_rock', 'gold_rock', 'black_rock', 'white_rock', 'silverrock', 'dragon_tear', 'valor_crest']


class GoodLootSpots(OptionList):
    """Spots which will be given a random good reward (ignored by vanilla)"""
    display_name = "Good Loot Spots"
    valid_keys = {'mt_woe_1st_screen', 'mt_woe_2nd_screen_1', 'mt_woe_2nd_screen_2', 'mt_woe_2nd_screen_3', 'mt_woe_2nd_screen_4', 'mt_woe_2nd_screen_5', 'mt_woe_3rd_screen_1', 'mt_woe_3rd_screen_2', 'mt_woe_3rd_screen_3', 'mt_woe_3rd_screen_4', 'mt_woe_3rd_screen_5', 'mt_woe_final_1', 'mt_woe_final_2', 'mt_woe_key', 'fiona_key', 'arris_dome_rats', 'arris_dome_food_store', 'arris_dome_doan_key', 'arris_dome_food_locker_key', 'sun_palace_key', 'sewers_1', 'sewers_2', 'sewers_3', 'lab_16_1', 'lab_16_2', 'lab_16_3', 'lab_16_4', 'lab_32_1', 'prison_tower_1000', 'geno_dome_1f_1', 'geno_dome_1f_2', 'geno_dome_1f_3', 'geno_dome_1f_4', 'geno_dome_room_1', 'geno_dome_room_2', 'geno_dome_proto4_1', 'geno_dome_proto4_2', 'geno_dome_2f_1', 'geno_dome_2f_2', 'geno_dome_2f_3', 'geno_dome_2f_4', 'geno_dome_boss_1', 'geno_dome_boss_2', 'factory_left_aux_console', 'factory_left_security_right', 'factory_left_security_left', 'factory_right_data_core_1', 'factory_right_data_core_2', 'factory_right_floor_top', 'factory_right_floor_left', 'factory_right_floor_bottom', 'factory_right_floor_secret', 'factory_right_crane_lower', 'factory_right_crane_upper', 'factory_right_info_archive', 'giants_claw_traps', 'giants_claw_caves_1', 'giants_claw_caves_2', 'giants_claw_caves_3', 'giants_claw_caves_4', 'giants_claw_caves_5', 'giants_claw_rock', 'giants_claw_key', 'northern_ruins_antechamber_left_600', 'northern_ruins_antechamber_sealed_600', 'northern_ruins_antechamber_left_1000', 'northern_ruins_antechamber_sealed_1000', 'northern_ruins_back_left_sealed_600', 'northern_ruins_back_right_sealed_600', 'northern_ruins_back_left_sealed_1000', 'northern_ruins_back_right_sealed_1000', 'northern_ruins_basement_600', 'northern_ruins_basement_1000', 'guardia_basement_1', 'guardia_basement_2', 'guardia_basement_3', 'guardia_treasury_1', 'guardia_treasury_2', 'guardia_treasury_3', 'kings_trial_key', 'ozzies_fort_guillotines_1', 'ozzies_fort_guillotines_2', 'ozzies_fort_guillotines_3', 'ozzies_fort_guillotines_4', 'ozzies_fort_final_1', 'ozzies_fort_final_2', 'truce_mayor_1f', 'truce_mayor_2f', 'forest_ruins', 'porre_mayor_2f', 'truce_canyon_1', 'truce_canyon_2', 'fionas_house_1', 'fionas_house_2', 'cursed_woods_1', 'cursed_woods_2', 'frogs_burrow_right', 'zenan_bridge_chef', 'zenan_bridge_chef_tab', 'zenan_bridge_captain', 'snail_stop_key', 'lazy_carpenter', 'heckran_cave_sidetrack', 'heckran_cave_entrance', 'heckran_cave_1', 'heckran_cave_2', 'taban_gift_vest', 'kings_room_1000', 'queens_room_1000', 'kings_room_600', 'queens_room_600', 'royal_kitchen', 'queens_tower_600', 'kings_tower_600', 'kings_tower_1000', 'queens_tower_1000', 'guardia_court_tower', 'manoria_cathedral_1', 'manoria_cathedral_2', 'manoria_cathedral_3', 'manoria_interior_1', 'manoria_interior_2', 'manoria_interior_3', 'manoria_interior_4', 'manoria_shrine_sideroom_1', 'manoria_shrine_sideroom_2', 'manoria_bromide_1', 'manoria_bromide_2', 'manoria_bromide_3', 'manoria_shrine_magus_1', 'manoria_shrine_magus_2', 'yakras_room', 'denadoro_mts_screen2_1', 'denadoro_mts_screen2_2', 'denadoro_mts_screen2_3', 'denadoro_mts_final_1', 'denadoro_mts_final_2', 'denadoro_mts_final_3', 'denadoro_mts_waterfall_top_1', 'denadoro_mts_waterfall_top_2', 'denadoro_mts_waterfall_top_3', 'denadoro_mts_waterfall_top_4', 'denadoro_mts_waterfall_top_5', 'denadoro_mts_entrance_1', 'denadoro_mts_entrance_2', 'denadoro_mts_screen3_1', 'denadoro_mts_screen3_2', 'denadoro_mts_screen3_3', 'denadoro_mts_screen3_4', 'denadoro_mts_ambush', 'denadoro_mts_save_pt', 'denadoro_mts_key', 'bangor_dome_seal_1', 'bangor_dome_seal_2', 'bangor_dome_seal_3', 'trann_dome_seal_1', 'trann_dome_seal_2', 'arris_dome_seal_1', 'arris_dome_seal_2', 'arris_dome_seal_3', 'arris_dome_seal_4', 'truce_inn_sealed_600', 'porre_elder_sealed_1', 'porre_elder_sealed_2', 'guardia_castle_sealed_600', 'guardia_forest_sealed_600', 'truce_inn_sealed_1000', 'porre_mayor_sealed_1', 'porre_mayor_sealed_2', 'guardia_forest_sealed_1000', 'guardia_castle_sealed_1000', 'heckran_sealed_1', 'heckran_sealed_2', 'pyramid_left', 'pyramid_right', 'magic_cave_sealed', 'mystic_mt_stream', 'forest_maze_1', 'forest_maze_2', 'forest_maze_3', 'forest_maze_4', 'forest_maze_5', 'forest_maze_6', 'forest_maze_7', 'forest_maze_8', 'forest_maze_9', 'reptite_lair_reptites_1', 'reptite_lair_reptites_2', 'reptite_lair_key', 'dactyl_nest_1', 'dactyl_nest_2', 'dactyl_nest_3', 'melchior_rainbow_shell', 'melchior_sunstone_rainbow', 'melchior_sunstone_specs', 'frogs_burrow_left', 'guardia_jail_fritz_storage', 'guardia_jail_cell', 'guardia_jail_omnicrone_1', 'guardia_jail_omnicrone_2', 'guardia_jail_omnicrone_3', 'guardia_jail_hole_1', 'guardia_jail_hole_2', 'guardia_jail_outer_wall', 'guardia_jail_omnicrone_4', 'guardia_jail_fritz', 'magus_castle_right_hall', 'sunken_desert_b1_nw', 'sunken_desert_b1_ne', 'sunken_desert_b1_se', 'sunken_desert_b1_sw', 'sunken_desert_b2_nw', 'sunken_desert_b2_n', 'sunken_desert_b2_w', 'sunken_desert_b2_sw', 'sunken_desert_b2_se', 'sunken_desert_b2_e', 'sunken_desert_b2_center', 'magus_castle_guillotine_1', 'magus_castle_guillotine_2', 'magus_castle_slash_room_1', 'magus_castle_slash_room_2', 'magus_castle_statue_hall', 'magus_castle_four_kids', 'magus_castle_ozzie_1', 'magus_castle_ozzie_2', 'magus_castle_enemy_elevator', 'reptite_lair_secret_b2_ne_right', 'lab_32_race_log', 'factory_ruins_generator', 'death_peak_south_face_krakker', 'death_peak_south_face_spawn_save', 'death_peak_south_face_summit', 'death_peak_field', 'death_peak_krakker_parade', 'death_peak_caves_left', 'death_peak_caves_center', 'death_peak_caves_right', 'reptite_lair_secret_b1_sw', 'reptite_lair_secret_b1_ne', 'reptite_lair_secret_b1_se', 'reptite_lair_secret_b2_se_right', 'reptite_lair_secret_b2_ne_or_se_left', 'reptite_lair_secret_b2_sw', 'tyrano_lair_throne_1', 'tyrano_lair_throne_2', 'tyrano_lair_trapdoor', 'tyrano_lair_kino_cell', 'tyrano_lair_maze_1', 'tyrano_lair_maze_2', 'tyrano_lair_maze_3', 'tyrano_lair_maze_4', 'black_omen_aux_command_mid', 'black_omen_aux_command_ne', 'black_omen_grand_hall', 'black_omen_nu_hall_nw', 'black_omen_nu_hall_w', 'black_omen_nu_hall_sw', 'black_omen_nu_hall_ne', 'black_omen_nu_hall_e', 'black_omen_nu_hall_se', 'black_omen_royal_path', 'black_omen_ruminator_parade', 'black_omen_eyeball_hall', 'black_omen_tubster_fly', 'black_omen_martello', 'black_omen_alien_sw', 'black_omen_alien_ne', 'black_omen_alien_nw', 'black_omen_terra_w', 'black_omen_terra_rock', 'black_omen_terra_ne', 'ocean_palace_main_s', 'ocean_palace_main_n', 'ocean_palace_e_room', 'ocean_palace_w_room', 'ocean_palace_switch_nw', 'ocean_palace_switch_sw', 'ocean_palace_switch_ne', 'ocean_palace_switch_secret', 'ocean_palace_final', 'magus_castle_left_hall', 'magus_castle_unskippables', 'magus_castle_pit_e', 'magus_castle_pit_ne', 'magus_castle_pit_nw', 'magus_castle_pit_w', 'taban_gift_suit', 'taban_gift_helm', 'trading_post_petal_fang_base', 'trading_post_petal_fang_upgrade', 'trading_post_petal_horn_base', 'trading_post_petal_horn_upgrade', 'trading_post_petal_feather_base', 'trading_post_petal_feather_upgrade', 'trading_post_fang_horn_base', 'trading_post_fang_horn_upgrade', 'trading_post_fang_feather_base', 'trading_post_fang_feather_upgrade', 'trading_post_horn_feather_base', 'trading_post_horn_feather_upgrade', 'trading_post_special', 'jerky_gift', 'denadoro_rock', 'kajar_rock', 'laruba_rock', 'bekkler_key', 'cyrus_grave_key', 'sun_keep_2300', 'lucca_wondershot', 'taban_sunshades', 'fair_pendant', 'tata_reward', 'toma_reward', 'melchior_forge_masa', 'eot_gaspar_reward', 'hunting_range_nu_reward', 'zeal_mammon_machine', 'magus_castle_slash_sword_floor', 'guardia_prison_lunch_bag', 'cronos_mom', 'truce_mayor_2f_old_man', 'ioka_sweetwater_tonic', 'dorino_inn_powermeal', 'yakra_key_chest', 'courtroom_yakra_key', 'johnny_race_power_tab', 'guardia_forest_power_tab_600', 'guardia_forest_power_tab_1000', 'manoria_confinement_power_tab', 'dorino_bromide_magic_tab', 'porre_market_600_power_tab', 'denadoro_mts_speed_tab', 'tomas_grave_speed_tab', 'giants_claw_caverns_power_tab', 'giants_claw_entrance_power_tab', 'giants_claw_traps_power_tab', 'sun_keep_600_power_tab', 'medina_elder_speed_tab', 'medina_elder_magic_tab', 'magus_castle_flea_magic_tab', 'magus_castle_dungeons_magic_tab', 'trann_dome_sealed_magic_tab', 'arris_dome_sealed_power_tab', 'keepers_dome_magic_tab', 'death_peak_power_tab', 'blackbird_ducts_magic_tab', 'geno_dome_atropos_magic_tab', 'geno_dome_corridor_power_tab', 'geno_dome_labs_magic_tab', 'geno_dome_labs_speed_tab', 'enhasa_nu_battle_magic_tab', 'enhasa_nu_battle_speed_tab', 'kajar_speed_tab', 'kajar_nu_scratch_magic_tab', 'last_village_nu_shop_magic_tab', 'sunken_desert_power_tab', 'mountains_re_nice_magic_tab', 'beast_nest_power_tab', 'mt_woe_magic_tab', 'ocean_palace_elevator_magic_tab', 'ozzies_fort_guillotines_tab', 'proto_dome_portal_tab', 'northern_ruins_heros_grave_magic_tab', 'northern_ruins_landing_power_tab'}
    default = ['eot_gaspar_reward', 'bekkler_key', 'fair_pendant', 'zeal_mammon_machine', 'mt_woe_key', 'giants_claw_key', 'kings_trial_key', 'yakras_room', 'snail_stop_key', 'denadoro_mts_key', 'frogs_burrow_left', 'melchior_forge_masa', 'cyrus_grave_key', 'tata_reward', 'fiona_key', 'sun_keep_2300', 'jerky_gift', 'arris_dome_doan_key', 'arris_dome_food_locker_key', 'reptite_lair_key', 'taban_gift_vest', 'geno_dome_boss_1', 'sun_palace_key', 'prison_tower_1000', 'ozzies_fort_final_2', 'zenan_bridge_chef', 'zenan_bridge_captain', 'lazy_carpenter', 'pyramid_left', 'melchior_sunstone_specs', 'melchior_sunstone_rainbow', 'melchior_rainbow_shell', 'factory_ruins_generator', 'death_peak_south_face_summit', 'lucca_wondershot', 'hunting_range_nu_reward', 'enhasa_nu_battle_magic_tab', 'sewers_3', 'lab_32_race_log', 'dorino_bromide_magic_tab', 'factory_right_info_archive', 'heckran_cave_sidetrack', 'taban_sunshades', 'geno_dome_boss_2', 'pyramid_right', 'ozzies_fort_final_1', 'black_omen_terra_rock', 'giants_claw_rock', 'denadoro_rock', 'denadoro_mts_waterfall_top_1', 'kajar_rock', 'laruba_rock', 'black_omen_nu_hall_w', 'black_omen_nu_hall_e', 'black_omen_nu_hall_ne', 'black_omen_nu_hall_se', 'black_omen_nu_hall_sw', 'black_omen_nu_hall_nw', 'arris_dome_seal_1', 'arris_dome_seal_2', 'arris_dome_seal_3', 'arris_dome_seal_4', 'bangor_dome_seal_1', 'bangor_dome_seal_2', 'bangor_dome_seal_3', 'trann_dome_seal_1', 'trann_dome_seal_2', 'ozzies_fort_guillotines_2', 'ozzies_fort_guillotines_3', 'ozzies_fort_guillotines_4', 'blackbird_ducts_magic_tab', 'ocean_palace_switch_secret', 'cronos_mom']


class GoodLootRate(Range):
    """Percent chance to fill a good loot spot with good loot"""
    display_name = "Good Loot Rate"
    range_start = 0
    range_end = 100
    default = 75


class PostAssignShuffleRate(Range):
    """Percent chance to shuffle after basic assignment"""
    display_name = "Post Assign Shuffle Rate"
    range_start = 0
    range_end = 100
    default = 50


class TradingPostBaseCost(Range):
    """Number of materials of each type required for base trade"""
    display_name = "Trading Post Base Cost"
    range_start = 1
    range_end = 10
    default = 3


class TradingPostUpgradeCost(Range):
    """Number of materials of each type required for upgraded trade"""
    display_name = "Trading Post Upgrade Cost"
    range_start = 1
    range_end = 10
    default = 3


class TradingPostSpecialCost(Range):
    """Number of materials of each type required for special trade"""
    display_name = "Trading Post Special Cost"
    range_start = 1
    range_end = 15
    default = 10


class JohnnyKeyThreshold(Range):
    """Points needed for the Johnny key item"""
    display_name = "Johnny Key Threshold"
    range_start = 0
    range_end = 2500
    default = 1500


class JohnnyLowThreshold(Range):
    """Points needed for the low tier Johnny rewards"""
    display_name = "Johnny Low Threshold"
    range_start = 0
    range_end = 2500
    default = 1200


class JohnnyLowItem(Choice):
    """Low tier Johnny item reward"""
    display_name = "Johnny Low Item"

    option_wood_sword = 0
    option_iron_blade = 1
    option_steelsaber = 2
    option_lode_sword = 3
    option_red_katana = 4
    option_flint_edge = 5
    option_dark_saber = 6
    option_aeon_blade = 7
    option_demon_edge = 8
    option_alloyblade = 9
    option_star_sword = 10
    option_vedicblade = 11
    option_kali_blade = 12
    option_shiva_edge = 13
    option_bolt_sword = 14
    option_slasher = 15
    option_bronze_bow = 16
    option_iron_bow = 17
    option_lode_bow = 18
    option_robin_bow = 19
    option_sage_bow = 20
    option_dream_bow = 21
    option_cometarrow = 22
    option_sonicarrow = 23
    option_valkerye = 24
    option_siren = 25
    option_air_gun = 26
    option_dart_gun = 27
    option_auto_gun = 28
    option_picomagnum = 29
    option_plasma_gun = 30
    option_ruby_gun = 31
    option_dream_gun = 32
    option_megablast = 33
    option_shock_wave = 34
    option_wondershot = 35
    option_graedus = 36
    option_tin_arm = 37
    option_hammer_arm = 38
    option_miragehand = 39
    option_stone_arm = 40
    option_doomfinger = 41
    option_magma_hand = 42
    option_megatonarm = 43
    option_big_hand = 44
    option_kaiser_arm = 45
    option_giga_arm = 46
    option_terra_arm = 47
    option_crisis_arm = 48
    option_bronzeedge = 49
    option_iron_sword = 50
    option_masamune_1 = 51
    option_flashblade = 52
    option_pearl_edge = 53
    option_rune_blade = 54
    option_bravesword = 55
    option_masamune_2 = 56
    option_demon_hit = 57
    option_fist = 58
    option_fist_2 = 59
    option_fist_3 = 60
    option_iron_fist = 61
    option_bronzefist = 62
    option_pacifist = 63
    option_darkscythe = 64
    option_hurricane = 65
    option_starscythe = 66
    option_doomsickle = 67
    option_mop = 68
    option_bent_sword = 69
    option_bent_hilt = 70
    option_swallow = 71
    option_slasher_2 = 72
    option_rainbow = 73
    option_hide_tunic = 74
    option_karate_gi = 75
    option_bronzemail = 76
    option_maidensuit = 77
    option_iron_suit = 78
    option_titan_vest = 79
    option_gold_suit = 80
    option_ruby_vest = 81
    option_dark_mail = 82
    option_mist_robe = 83
    option_meso_mail = 84
    option_lumin_robe = 85
    option_flash_mail = 86
    option_lode_vest = 87
    option_aeon_suit = 88
    option_zodiaccape = 89
    option_nova_armor = 90
    option_prismdress = 91
    option_moon_armor = 92
    option_ruby_armor = 93
    option_ravenarmor = 94
    option_gloom_cape = 95
    option_white_mail = 96
    option_black_mail = 97
    option_blue_mail = 98
    option_red_mail = 99
    option_white_vest = 100
    option_black_vest = 101
    option_blue_vest = 102
    option_red_vest = 103
    option_taban_vest = 104
    option_taban_suit = 105
    option_hide_cap = 106
    option_bronzehelm = 107
    option_iron_helm = 108
    option_beret = 109
    option_gold_helm = 110
    option_rock_helm = 111
    option_ceratopper = 112
    option_glow_helm = 113
    option_lode_helm = 114
    option_aeon_helm = 115
    option_prism_helm = 116
    option_doom_helm = 117
    option_dark_helm = 118
    option_gloom_helm = 119
    option_safe_helm = 120
    option_taban_helm = 121
    option_sight_cap = 122
    option_memory_cap = 123
    option_time_hat = 124
    option_vigil_hat = 125
    option_ozziepants = 126
    option_haste_helm = 127
    option_rbow_helm = 128
    option_mermaidcap = 129
    option_bandana = 130
    option_ribbon = 131
    option_powerglove = 132
    option_defender = 133
    option_magicscarf = 134
    option_amulet = 135
    option_dash_ring = 136
    option_hit_ring = 137
    option_power_ring = 138
    option_magic_ring = 139
    option_wall_ring = 140
    option_silvererng = 141
    option_gold_erng = 142
    option_silverstud = 143
    option_gold_stud = 144
    option_sightscope = 145
    option_charm_top = 146
    option_rage_band = 147
    option_frenzyband = 148
    option_third_eye = 149
    option_wallet = 150
    option_greendream = 151
    option_berserker = 152
    option_powerscarf = 153
    option_speed_belt = 154
    option_black_rock = 155
    option_blue_rock = 156
    option_silverrock = 157
    option_white_rock = 158
    option_gold_rock = 159
    option_hero_medal = 160
    option_musclering = 161
    option_flea_vest = 162
    option_magic_seal = 163
    option_power_seal = 164
    option_valor_crest = 165
    option_dragon_tear = 166
    option_sun_shades = 167
    option_prismspecs = 168
    option_tonic = 169
    option_mid_tonic = 170
    option_full_tonic = 171
    option_ether = 172
    option_mid_ether = 173
    option_full_ether = 174
    option_elixir = 175
    option_hyperether = 176
    option_megaelixir = 177
    option_heal = 178
    option_revive = 179
    option_shelter = 180
    option_power_meal = 181
    option_lapis = 182
    option_barrier = 183
    option_shield = 184
    option_power_tab = 185
    option_magic_tab = 186
    option_speed_tab = 187
    option_petal = 188
    option_fang = 189
    option_horn = 190
    option_feather = 191
    option_seed = 192
    option_bike_key = 193
    option_pendant = 194
    option_gate_key = 195
    option_prismshard = 196
    option_c_trigger = 197
    option_tools = 198
    option_jerky = 199
    option_dreamstone = 200
    option_race_log = 201
    option_moon_stone = 202
    option_sun_stone = 203
    option_ruby_knife = 204
    option_yakra_key = 205
    option_clone = 206
    option_tomas_pop = 207
    option_petals_2 = 208
    option_fangs_2 = 209
    option_horns_2 = 210
    option_feathers_2 = 211
    option_jetsoftime = 212
    option_pendant_charge = 213
    option_rainbow_shell = 214
    default = 170


class JohnnyLowQuantity(Range):
    """Number of items for the low tier Johnny reward"""
    display_name = "Johnny Low Quantity"
    range_start = 1
    range_end = 10
    default = 5


class JohnnyMidThreshold(Range):
    """Points needed for the mid tier Johnny rewards"""
    display_name = "Johnny Mid Threshold"
    range_start = 0
    range_end = 2500
    default = 2000


class JohnnyMidItem(Choice):
    """Mid tier Johnny item reward"""
    display_name = "Johnny Mid Item"

    option_wood_sword = 0
    option_iron_blade = 1
    option_steelsaber = 2
    option_lode_sword = 3
    option_red_katana = 4
    option_flint_edge = 5
    option_dark_saber = 6
    option_aeon_blade = 7
    option_demon_edge = 8
    option_alloyblade = 9
    option_star_sword = 10
    option_vedicblade = 11
    option_kali_blade = 12
    option_shiva_edge = 13
    option_bolt_sword = 14
    option_slasher = 15
    option_bronze_bow = 16
    option_iron_bow = 17
    option_lode_bow = 18
    option_robin_bow = 19
    option_sage_bow = 20
    option_dream_bow = 21
    option_cometarrow = 22
    option_sonicarrow = 23
    option_valkerye = 24
    option_siren = 25
    option_air_gun = 26
    option_dart_gun = 27
    option_auto_gun = 28
    option_picomagnum = 29
    option_plasma_gun = 30
    option_ruby_gun = 31
    option_dream_gun = 32
    option_megablast = 33
    option_shock_wave = 34
    option_wondershot = 35
    option_graedus = 36
    option_tin_arm = 37
    option_hammer_arm = 38
    option_miragehand = 39
    option_stone_arm = 40
    option_doomfinger = 41
    option_magma_hand = 42
    option_megatonarm = 43
    option_big_hand = 44
    option_kaiser_arm = 45
    option_giga_arm = 46
    option_terra_arm = 47
    option_crisis_arm = 48
    option_bronzeedge = 49
    option_iron_sword = 50
    option_masamune_1 = 51
    option_flashblade = 52
    option_pearl_edge = 53
    option_rune_blade = 54
    option_bravesword = 55
    option_masamune_2 = 56
    option_demon_hit = 57
    option_fist = 58
    option_fist_2 = 59
    option_fist_3 = 60
    option_iron_fist = 61
    option_bronzefist = 62
    option_pacifist = 63
    option_darkscythe = 64
    option_hurricane = 65
    option_starscythe = 66
    option_doomsickle = 67
    option_mop = 68
    option_bent_sword = 69
    option_bent_hilt = 70
    option_swallow = 71
    option_slasher_2 = 72
    option_rainbow = 73
    option_hide_tunic = 74
    option_karate_gi = 75
    option_bronzemail = 76
    option_maidensuit = 77
    option_iron_suit = 78
    option_titan_vest = 79
    option_gold_suit = 80
    option_ruby_vest = 81
    option_dark_mail = 82
    option_mist_robe = 83
    option_meso_mail = 84
    option_lumin_robe = 85
    option_flash_mail = 86
    option_lode_vest = 87
    option_aeon_suit = 88
    option_zodiaccape = 89
    option_nova_armor = 90
    option_prismdress = 91
    option_moon_armor = 92
    option_ruby_armor = 93
    option_ravenarmor = 94
    option_gloom_cape = 95
    option_white_mail = 96
    option_black_mail = 97
    option_blue_mail = 98
    option_red_mail = 99
    option_white_vest = 100
    option_black_vest = 101
    option_blue_vest = 102
    option_red_vest = 103
    option_taban_vest = 104
    option_taban_suit = 105
    option_hide_cap = 106
    option_bronzehelm = 107
    option_iron_helm = 108
    option_beret = 109
    option_gold_helm = 110
    option_rock_helm = 111
    option_ceratopper = 112
    option_glow_helm = 113
    option_lode_helm = 114
    option_aeon_helm = 115
    option_prism_helm = 116
    option_doom_helm = 117
    option_dark_helm = 118
    option_gloom_helm = 119
    option_safe_helm = 120
    option_taban_helm = 121
    option_sight_cap = 122
    option_memory_cap = 123
    option_time_hat = 124
    option_vigil_hat = 125
    option_ozziepants = 126
    option_haste_helm = 127
    option_rbow_helm = 128
    option_mermaidcap = 129
    option_bandana = 130
    option_ribbon = 131
    option_powerglove = 132
    option_defender = 133
    option_magicscarf = 134
    option_amulet = 135
    option_dash_ring = 136
    option_hit_ring = 137
    option_power_ring = 138
    option_magic_ring = 139
    option_wall_ring = 140
    option_silvererng = 141
    option_gold_erng = 142
    option_silverstud = 143
    option_gold_stud = 144
    option_sightscope = 145
    option_charm_top = 146
    option_rage_band = 147
    option_frenzyband = 148
    option_third_eye = 149
    option_wallet = 150
    option_greendream = 151
    option_berserker = 152
    option_powerscarf = 153
    option_speed_belt = 154
    option_black_rock = 155
    option_blue_rock = 156
    option_silverrock = 157
    option_white_rock = 158
    option_gold_rock = 159
    option_hero_medal = 160
    option_musclering = 161
    option_flea_vest = 162
    option_magic_seal = 163
    option_power_seal = 164
    option_valor_crest = 165
    option_dragon_tear = 166
    option_sun_shades = 167
    option_prismspecs = 168
    option_tonic = 169
    option_mid_tonic = 170
    option_full_tonic = 171
    option_ether = 172
    option_mid_ether = 173
    option_full_ether = 174
    option_elixir = 175
    option_hyperether = 176
    option_megaelixir = 177
    option_heal = 178
    option_revive = 179
    option_shelter = 180
    option_power_meal = 181
    option_lapis = 182
    option_barrier = 183
    option_shield = 184
    option_power_tab = 185
    option_magic_tab = 186
    option_speed_tab = 187
    option_petal = 188
    option_fang = 189
    option_horn = 190
    option_feather = 191
    option_seed = 192
    option_bike_key = 193
    option_pendant = 194
    option_gate_key = 195
    option_prismshard = 196
    option_c_trigger = 197
    option_tools = 198
    option_jerky = 199
    option_dreamstone = 200
    option_race_log = 201
    option_moon_stone = 202
    option_sun_stone = 203
    option_ruby_knife = 204
    option_yakra_key = 205
    option_clone = 206
    option_tomas_pop = 207
    option_petals_2 = 208
    option_fangs_2 = 209
    option_horns_2 = 210
    option_feathers_2 = 211
    option_jetsoftime = 212
    option_pendant_charge = 213
    option_rainbow_shell = 214
    default = 172


class JohnnyMidQuantity(Range):
    """Number of items for the mid tier Johnny reward"""
    display_name = "Johnny Mid Quantity"
    range_start = 1
    range_end = 10
    default = 5


class JohnnyHighThreshold(Range):
    """Points needed for the high tier Johnny rewards"""
    display_name = "Johnny High Threshold"
    range_start = 0
    range_end = 2500
    default = 2300


class JohnnyHighItem(Choice):
    """High tier Johnny item reward"""
    display_name = "Johnny High Item"

    option_wood_sword = 0
    option_iron_blade = 1
    option_steelsaber = 2
    option_lode_sword = 3
    option_red_katana = 4
    option_flint_edge = 5
    option_dark_saber = 6
    option_aeon_blade = 7
    option_demon_edge = 8
    option_alloyblade = 9
    option_star_sword = 10
    option_vedicblade = 11
    option_kali_blade = 12
    option_shiva_edge = 13
    option_bolt_sword = 14
    option_slasher = 15
    option_bronze_bow = 16
    option_iron_bow = 17
    option_lode_bow = 18
    option_robin_bow = 19
    option_sage_bow = 20
    option_dream_bow = 21
    option_cometarrow = 22
    option_sonicarrow = 23
    option_valkerye = 24
    option_siren = 25
    option_air_gun = 26
    option_dart_gun = 27
    option_auto_gun = 28
    option_picomagnum = 29
    option_plasma_gun = 30
    option_ruby_gun = 31
    option_dream_gun = 32
    option_megablast = 33
    option_shock_wave = 34
    option_wondershot = 35
    option_graedus = 36
    option_tin_arm = 37
    option_hammer_arm = 38
    option_miragehand = 39
    option_stone_arm = 40
    option_doomfinger = 41
    option_magma_hand = 42
    option_megatonarm = 43
    option_big_hand = 44
    option_kaiser_arm = 45
    option_giga_arm = 46
    option_terra_arm = 47
    option_crisis_arm = 48
    option_bronzeedge = 49
    option_iron_sword = 50
    option_masamune_1 = 51
    option_flashblade = 52
    option_pearl_edge = 53
    option_rune_blade = 54
    option_bravesword = 55
    option_masamune_2 = 56
    option_demon_hit = 57
    option_fist = 58
    option_fist_2 = 59
    option_fist_3 = 60
    option_iron_fist = 61
    option_bronzefist = 62
    option_pacifist = 63
    option_darkscythe = 64
    option_hurricane = 65
    option_starscythe = 66
    option_doomsickle = 67
    option_mop = 68
    option_bent_sword = 69
    option_bent_hilt = 70
    option_swallow = 71
    option_slasher_2 = 72
    option_rainbow = 73
    option_hide_tunic = 74
    option_karate_gi = 75
    option_bronzemail = 76
    option_maidensuit = 77
    option_iron_suit = 78
    option_titan_vest = 79
    option_gold_suit = 80
    option_ruby_vest = 81
    option_dark_mail = 82
    option_mist_robe = 83
    option_meso_mail = 84
    option_lumin_robe = 85
    option_flash_mail = 86
    option_lode_vest = 87
    option_aeon_suit = 88
    option_zodiaccape = 89
    option_nova_armor = 90
    option_prismdress = 91
    option_moon_armor = 92
    option_ruby_armor = 93
    option_ravenarmor = 94
    option_gloom_cape = 95
    option_white_mail = 96
    option_black_mail = 97
    option_blue_mail = 98
    option_red_mail = 99
    option_white_vest = 100
    option_black_vest = 101
    option_blue_vest = 102
    option_red_vest = 103
    option_taban_vest = 104
    option_taban_suit = 105
    option_hide_cap = 106
    option_bronzehelm = 107
    option_iron_helm = 108
    option_beret = 109
    option_gold_helm = 110
    option_rock_helm = 111
    option_ceratopper = 112
    option_glow_helm = 113
    option_lode_helm = 114
    option_aeon_helm = 115
    option_prism_helm = 116
    option_doom_helm = 117
    option_dark_helm = 118
    option_gloom_helm = 119
    option_safe_helm = 120
    option_taban_helm = 121
    option_sight_cap = 122
    option_memory_cap = 123
    option_time_hat = 124
    option_vigil_hat = 125
    option_ozziepants = 126
    option_haste_helm = 127
    option_rbow_helm = 128
    option_mermaidcap = 129
    option_bandana = 130
    option_ribbon = 131
    option_powerglove = 132
    option_defender = 133
    option_magicscarf = 134
    option_amulet = 135
    option_dash_ring = 136
    option_hit_ring = 137
    option_power_ring = 138
    option_magic_ring = 139
    option_wall_ring = 140
    option_silvererng = 141
    option_gold_erng = 142
    option_silverstud = 143
    option_gold_stud = 144
    option_sightscope = 145
    option_charm_top = 146
    option_rage_band = 147
    option_frenzyband = 148
    option_third_eye = 149
    option_wallet = 150
    option_greendream = 151
    option_berserker = 152
    option_powerscarf = 153
    option_speed_belt = 154
    option_black_rock = 155
    option_blue_rock = 156
    option_silverrock = 157
    option_white_rock = 158
    option_gold_rock = 159
    option_hero_medal = 160
    option_musclering = 161
    option_flea_vest = 162
    option_magic_seal = 163
    option_power_seal = 164
    option_valor_crest = 165
    option_dragon_tear = 166
    option_sun_shades = 167
    option_prismspecs = 168
    option_tonic = 169
    option_mid_tonic = 170
    option_full_tonic = 171
    option_ether = 172
    option_mid_ether = 173
    option_full_ether = 174
    option_elixir = 175
    option_hyperether = 176
    option_megaelixir = 177
    option_heal = 178
    option_revive = 179
    option_shelter = 180
    option_power_meal = 181
    option_lapis = 182
    option_barrier = 183
    option_shield = 184
    option_power_tab = 185
    option_magic_tab = 186
    option_speed_tab = 187
    option_petal = 188
    option_fang = 189
    option_horn = 190
    option_feather = 191
    option_seed = 192
    option_bike_key = 193
    option_pendant = 194
    option_gate_key = 195
    option_prismshard = 196
    option_c_trigger = 197
    option_tools = 198
    option_jerky = 199
    option_dreamstone = 200
    option_race_log = 201
    option_moon_stone = 202
    option_sun_stone = 203
    option_ruby_knife = 204
    option_yakra_key = 205
    option_clone = 206
    option_tomas_pop = 207
    option_petals_2 = 208
    option_fangs_2 = 209
    option_horns_2 = 210
    option_feathers_2 = 211
    option_jetsoftime = 212
    option_pendant_charge = 213
    option_rainbow_shell = 214
    default = 174


class JohnnyHighQuantity(Range):
    """Number of items for the high tier Johnny reward"""
    display_name = "Johnny High Quantity"
    range_start = 1
    range_end = 10
    default = 5


class UseTechLevelTreasures(Toggle):
    """Allow character tech levels to appear in treasure spots"""
    display_name = "Use Tech Level Treasures"


class ExtraTechLevelsPerChar(Range):
    """Number of extra Tech Level increases to include for each character"""
    display_name = "Extra Tech Levels Per Char"
    range_start = 0
    range_end = 5
    default = 0


class TechLevelForcedSpots(OptionList):
    """Spots guaranteed to have a tech level (unless KI assignment)"""
    display_name = "Tech Level Forced Spots"
    valid_keys = {'mt_woe_1st_screen', 'mt_woe_2nd_screen_1', 'mt_woe_2nd_screen_2', 'mt_woe_2nd_screen_3', 'mt_woe_2nd_screen_4', 'mt_woe_2nd_screen_5', 'mt_woe_3rd_screen_1', 'mt_woe_3rd_screen_2', 'mt_woe_3rd_screen_3', 'mt_woe_3rd_screen_4', 'mt_woe_3rd_screen_5', 'mt_woe_final_1', 'mt_woe_final_2', 'mt_woe_key', 'fiona_key', 'arris_dome_rats', 'arris_dome_food_store', 'arris_dome_doan_key', 'arris_dome_food_locker_key', 'sun_palace_key', 'sewers_1', 'sewers_2', 'sewers_3', 'lab_16_1', 'lab_16_2', 'lab_16_3', 'lab_16_4', 'lab_32_1', 'prison_tower_1000', 'geno_dome_1f_1', 'geno_dome_1f_2', 'geno_dome_1f_3', 'geno_dome_1f_4', 'geno_dome_room_1', 'geno_dome_room_2', 'geno_dome_proto4_1', 'geno_dome_proto4_2', 'geno_dome_2f_1', 'geno_dome_2f_2', 'geno_dome_2f_3', 'geno_dome_2f_4', 'geno_dome_boss_1', 'geno_dome_boss_2', 'factory_left_aux_console', 'factory_left_security_right', 'factory_left_security_left', 'factory_right_data_core_1', 'factory_right_data_core_2', 'factory_right_floor_top', 'factory_right_floor_left', 'factory_right_floor_bottom', 'factory_right_floor_secret', 'factory_right_crane_lower', 'factory_right_crane_upper', 'factory_right_info_archive', 'giants_claw_traps', 'giants_claw_caves_1', 'giants_claw_caves_2', 'giants_claw_caves_3', 'giants_claw_caves_4', 'giants_claw_caves_5', 'giants_claw_rock', 'giants_claw_key', 'northern_ruins_antechamber_left_600', 'northern_ruins_antechamber_sealed_600', 'northern_ruins_antechamber_left_1000', 'northern_ruins_antechamber_sealed_1000', 'northern_ruins_back_left_sealed_600', 'northern_ruins_back_right_sealed_600', 'northern_ruins_back_left_sealed_1000', 'northern_ruins_back_right_sealed_1000', 'northern_ruins_basement_600', 'northern_ruins_basement_1000', 'guardia_basement_1', 'guardia_basement_2', 'guardia_basement_3', 'guardia_treasury_1', 'guardia_treasury_2', 'guardia_treasury_3', 'kings_trial_key', 'ozzies_fort_guillotines_1', 'ozzies_fort_guillotines_2', 'ozzies_fort_guillotines_3', 'ozzies_fort_guillotines_4', 'ozzies_fort_final_1', 'ozzies_fort_final_2', 'truce_mayor_1f', 'truce_mayor_2f', 'forest_ruins', 'porre_mayor_2f', 'truce_canyon_1', 'truce_canyon_2', 'fionas_house_1', 'fionas_house_2', 'cursed_woods_1', 'cursed_woods_2', 'frogs_burrow_right', 'zenan_bridge_chef', 'zenan_bridge_chef_tab', 'zenan_bridge_captain', 'snail_stop_key', 'lazy_carpenter', 'heckran_cave_sidetrack', 'heckran_cave_entrance', 'heckran_cave_1', 'heckran_cave_2', 'taban_gift_vest', 'kings_room_1000', 'queens_room_1000', 'kings_room_600', 'queens_room_600', 'royal_kitchen', 'queens_tower_600', 'kings_tower_600', 'kings_tower_1000', 'queens_tower_1000', 'guardia_court_tower', 'manoria_cathedral_1', 'manoria_cathedral_2', 'manoria_cathedral_3', 'manoria_interior_1', 'manoria_interior_2', 'manoria_interior_3', 'manoria_interior_4', 'manoria_shrine_sideroom_1', 'manoria_shrine_sideroom_2', 'manoria_bromide_1', 'manoria_bromide_2', 'manoria_bromide_3', 'manoria_shrine_magus_1', 'manoria_shrine_magus_2', 'yakras_room', 'denadoro_mts_screen2_1', 'denadoro_mts_screen2_2', 'denadoro_mts_screen2_3', 'denadoro_mts_final_1', 'denadoro_mts_final_2', 'denadoro_mts_final_3', 'denadoro_mts_waterfall_top_1', 'denadoro_mts_waterfall_top_2', 'denadoro_mts_waterfall_top_3', 'denadoro_mts_waterfall_top_4', 'denadoro_mts_waterfall_top_5', 'denadoro_mts_entrance_1', 'denadoro_mts_entrance_2', 'denadoro_mts_screen3_1', 'denadoro_mts_screen3_2', 'denadoro_mts_screen3_3', 'denadoro_mts_screen3_4', 'denadoro_mts_ambush', 'denadoro_mts_save_pt', 'denadoro_mts_key', 'bangor_dome_seal_1', 'bangor_dome_seal_2', 'bangor_dome_seal_3', 'trann_dome_seal_1', 'trann_dome_seal_2', 'arris_dome_seal_1', 'arris_dome_seal_2', 'arris_dome_seal_3', 'arris_dome_seal_4', 'truce_inn_sealed_600', 'porre_elder_sealed_1', 'porre_elder_sealed_2', 'guardia_castle_sealed_600', 'guardia_forest_sealed_600', 'truce_inn_sealed_1000', 'porre_mayor_sealed_1', 'porre_mayor_sealed_2', 'guardia_forest_sealed_1000', 'guardia_castle_sealed_1000', 'heckran_sealed_1', 'heckran_sealed_2', 'pyramid_left', 'pyramid_right', 'magic_cave_sealed', 'mystic_mt_stream', 'forest_maze_1', 'forest_maze_2', 'forest_maze_3', 'forest_maze_4', 'forest_maze_5', 'forest_maze_6', 'forest_maze_7', 'forest_maze_8', 'forest_maze_9', 'reptite_lair_reptites_1', 'reptite_lair_reptites_2', 'reptite_lair_key', 'dactyl_nest_1', 'dactyl_nest_2', 'dactyl_nest_3', 'melchior_rainbow_shell', 'melchior_sunstone_rainbow', 'melchior_sunstone_specs', 'frogs_burrow_left', 'guardia_jail_fritz_storage', 'guardia_jail_cell', 'guardia_jail_omnicrone_1', 'guardia_jail_omnicrone_2', 'guardia_jail_omnicrone_3', 'guardia_jail_hole_1', 'guardia_jail_hole_2', 'guardia_jail_outer_wall', 'guardia_jail_omnicrone_4', 'guardia_jail_fritz', 'magus_castle_right_hall', 'sunken_desert_b1_nw', 'sunken_desert_b1_ne', 'sunken_desert_b1_se', 'sunken_desert_b1_sw', 'sunken_desert_b2_nw', 'sunken_desert_b2_n', 'sunken_desert_b2_w', 'sunken_desert_b2_sw', 'sunken_desert_b2_se', 'sunken_desert_b2_e', 'sunken_desert_b2_center', 'magus_castle_guillotine_1', 'magus_castle_guillotine_2', 'magus_castle_slash_room_1', 'magus_castle_slash_room_2', 'magus_castle_statue_hall', 'magus_castle_four_kids', 'magus_castle_ozzie_1', 'magus_castle_ozzie_2', 'magus_castle_enemy_elevator', 'reptite_lair_secret_b2_ne_right', 'lab_32_race_log', 'factory_ruins_generator', 'death_peak_south_face_krakker', 'death_peak_south_face_spawn_save', 'death_peak_south_face_summit', 'death_peak_field', 'death_peak_krakker_parade', 'death_peak_caves_left', 'death_peak_caves_center', 'death_peak_caves_right', 'reptite_lair_secret_b1_sw', 'reptite_lair_secret_b1_ne', 'reptite_lair_secret_b1_se', 'reptite_lair_secret_b2_se_right', 'reptite_lair_secret_b2_ne_or_se_left', 'reptite_lair_secret_b2_sw', 'tyrano_lair_throne_1', 'tyrano_lair_throne_2', 'tyrano_lair_trapdoor', 'tyrano_lair_kino_cell', 'tyrano_lair_maze_1', 'tyrano_lair_maze_2', 'tyrano_lair_maze_3', 'tyrano_lair_maze_4', 'black_omen_aux_command_mid', 'black_omen_aux_command_ne', 'black_omen_grand_hall', 'black_omen_nu_hall_nw', 'black_omen_nu_hall_w', 'black_omen_nu_hall_sw', 'black_omen_nu_hall_ne', 'black_omen_nu_hall_e', 'black_omen_nu_hall_se', 'black_omen_royal_path', 'black_omen_ruminator_parade', 'black_omen_eyeball_hall', 'black_omen_tubster_fly', 'black_omen_martello', 'black_omen_alien_sw', 'black_omen_alien_ne', 'black_omen_alien_nw', 'black_omen_terra_w', 'black_omen_terra_rock', 'black_omen_terra_ne', 'ocean_palace_main_s', 'ocean_palace_main_n', 'ocean_palace_e_room', 'ocean_palace_w_room', 'ocean_palace_switch_nw', 'ocean_palace_switch_sw', 'ocean_palace_switch_ne', 'ocean_palace_switch_secret', 'ocean_palace_final', 'magus_castle_left_hall', 'magus_castle_unskippables', 'magus_castle_pit_e', 'magus_castle_pit_ne', 'magus_castle_pit_nw', 'magus_castle_pit_w', 'taban_gift_suit', 'taban_gift_helm', 'jerky_gift', 'denadoro_rock', 'kajar_rock', 'laruba_rock', 'bekkler_key', 'cyrus_grave_key', 'sun_keep_2300', 'lucca_wondershot', 'taban_sunshades', 'fair_pendant', 'tata_reward', 'toma_reward', 'melchior_forge_masa', 'eot_gaspar_reward', 'hunting_range_nu_reward', 'zeal_mammon_machine', 'magus_castle_slash_sword_floor', 'guardia_prison_lunch_bag', 'cronos_mom', 'truce_mayor_2f_old_man', 'ioka_sweetwater_tonic', 'dorino_inn_powermeal', 'yakra_key_chest', 'courtroom_yakra_key', 'johnny_race_power_tab', 'guardia_forest_power_tab_600', 'guardia_forest_power_tab_1000', 'manoria_confinement_power_tab', 'dorino_bromide_magic_tab', 'porre_market_600_power_tab', 'denadoro_mts_speed_tab', 'tomas_grave_speed_tab', 'giants_claw_caverns_power_tab', 'giants_claw_entrance_power_tab', 'giants_claw_traps_power_tab', 'sun_keep_600_power_tab', 'medina_elder_speed_tab', 'medina_elder_magic_tab', 'magus_castle_flea_magic_tab', 'magus_castle_dungeons_magic_tab', 'trann_dome_sealed_magic_tab', 'arris_dome_sealed_power_tab', 'keepers_dome_magic_tab', 'death_peak_power_tab', 'blackbird_ducts_magic_tab', 'geno_dome_atropos_magic_tab', 'geno_dome_corridor_power_tab', 'geno_dome_labs_magic_tab', 'geno_dome_labs_speed_tab', 'enhasa_nu_battle_magic_tab', 'enhasa_nu_battle_speed_tab', 'kajar_speed_tab', 'kajar_nu_scratch_magic_tab', 'last_village_nu_shop_magic_tab', 'sunken_desert_power_tab', 'mountains_re_nice_magic_tab', 'beast_nest_power_tab', 'mt_woe_magic_tab', 'ocean_palace_elevator_magic_tab', 'ozzies_fort_guillotines_tab', 'proto_dome_portal_tab', 'northern_ruins_heros_grave_magic_tab', 'northern_ruins_landing_power_tab'}
    default = []


class GuaranteedLoot(OptionList):
    """Items guaranteed to appear in the loot pool"""
    display_name = "Guaranteed Loot"
    valid_keys = {'wood_sword', 'iron_blade', 'steelsaber', 'lode_sword', 'red_katana', 'flint_edge', 'dark_saber', 'aeon_blade', 'demon_edge', 'alloyblade', 'star_sword', 'vedicblade', 'kali_blade', 'shiva_edge', 'bolt_sword', 'slasher', 'bronze_bow', 'iron_bow', 'lode_bow', 'robin_bow', 'sage_bow', 'dream_bow', 'cometarrow', 'sonicarrow', 'valkerye', 'siren', 'air_gun', 'dart_gun', 'auto_gun', 'picomagnum', 'plasma_gun', 'ruby_gun', 'dream_gun', 'megablast', 'shock_wave', 'wondershot', 'graedus', 'tin_arm', 'hammer_arm', 'miragehand', 'stone_arm', 'doomfinger', 'magma_hand', 'megatonarm', 'big_hand', 'kaiser_arm', 'giga_arm', 'terra_arm', 'crisis_arm', 'bronzeedge', 'iron_sword', 'masamune_1', 'flashblade', 'pearl_edge', 'rune_blade', 'bravesword', 'masamune_2', 'demon_hit', 'fist', 'fist_2', 'fist_3', 'iron_fist', 'bronzefist', 'pacifist', 'darkscythe', 'hurricane', 'starscythe', 'doomsickle', 'mop', 'bent_sword', 'bent_hilt', 'swallow', 'slasher_2', 'rainbow', 'hide_tunic', 'karate_gi', 'bronzemail', 'maidensuit', 'iron_suit', 'titan_vest', 'gold_suit', 'ruby_vest', 'dark_mail', 'mist_robe', 'meso_mail', 'lumin_robe', 'flash_mail', 'lode_vest', 'aeon_suit', 'zodiaccape', 'nova_armor', 'prismdress', 'moon_armor', 'ruby_armor', 'ravenarmor', 'gloom_cape', 'white_mail', 'black_mail', 'blue_mail', 'red_mail', 'white_vest', 'black_vest', 'blue_vest', 'red_vest', 'taban_vest', 'taban_suit', 'hide_cap', 'bronzehelm', 'iron_helm', 'beret', 'gold_helm', 'rock_helm', 'ceratopper', 'glow_helm', 'lode_helm', 'aeon_helm', 'prism_helm', 'doom_helm', 'dark_helm', 'gloom_helm', 'safe_helm', 'taban_helm', 'sight_cap', 'memory_cap', 'time_hat', 'vigil_hat', 'ozziepants', 'haste_helm', 'rbow_helm', 'mermaidcap', 'bandana', 'ribbon', 'powerglove', 'defender', 'magicscarf', 'amulet', 'dash_ring', 'hit_ring', 'power_ring', 'magic_ring', 'wall_ring', 'silvererng', 'gold_erng', 'silverstud', 'gold_stud', 'sightscope', 'charm_top', 'rage_band', 'frenzyband', 'third_eye', 'wallet', 'greendream', 'berserker', 'powerscarf', 'speed_belt', 'black_rock', 'blue_rock', 'silverrock', 'white_rock', 'gold_rock', 'hero_medal', 'musclering', 'flea_vest', 'magic_seal', 'power_seal', 'valor_crest', 'dragon_tear', 'sun_shades', 'prismspecs', 'tonic', 'mid_tonic', 'full_tonic', 'ether', 'mid_ether', 'full_ether', 'elixir', 'hyperether', 'megaelixir', 'heal', 'revive', 'shelter', 'power_meal', 'lapis', 'barrier', 'shield', 'power_tab', 'magic_tab', 'speed_tab', 'petal', 'fang', 'horn', 'feather', 'seed', 'bike_key', 'pendant', 'gate_key', 'prismshard', 'c_trigger', 'tools', 'jerky', 'dreamstone', 'race_log', 'moon_stone', 'sun_stone', 'ruby_knife', 'yakra_key', 'clone', 'tomas_pop', 'petals_2', 'fangs_2', 'horns_2', 'feathers_2', 'jetsoftime', 'pendant_charge', 'rainbow_shell'}
    default = []


class GuaranteedLootExact(OptionList):
    """Items guaranteed to appear in the loot pool (including count)"""
    display_name = "Guaranteed Loot Exact"
    valid_keys = {'wood_sword', 'iron_blade', 'steelsaber', 'lode_sword', 'red_katana', 'flint_edge', 'dark_saber', 'aeon_blade', 'demon_edge', 'alloyblade', 'star_sword', 'vedicblade', 'kali_blade', 'shiva_edge', 'bolt_sword', 'slasher', 'bronze_bow', 'iron_bow', 'lode_bow', 'robin_bow', 'sage_bow', 'dream_bow', 'cometarrow', 'sonicarrow', 'valkerye', 'siren', 'air_gun', 'dart_gun', 'auto_gun', 'picomagnum', 'plasma_gun', 'ruby_gun', 'dream_gun', 'megablast', 'shock_wave', 'wondershot', 'graedus', 'tin_arm', 'hammer_arm', 'miragehand', 'stone_arm', 'doomfinger', 'magma_hand', 'megatonarm', 'big_hand', 'kaiser_arm', 'giga_arm', 'terra_arm', 'crisis_arm', 'bronzeedge', 'iron_sword', 'masamune_1', 'flashblade', 'pearl_edge', 'rune_blade', 'bravesword', 'masamune_2', 'demon_hit', 'fist', 'fist_2', 'fist_3', 'iron_fist', 'bronzefist', 'pacifist', 'darkscythe', 'hurricane', 'starscythe', 'doomsickle', 'mop', 'bent_sword', 'bent_hilt', 'swallow', 'slasher_2', 'rainbow', 'hide_tunic', 'karate_gi', 'bronzemail', 'maidensuit', 'iron_suit', 'titan_vest', 'gold_suit', 'ruby_vest', 'dark_mail', 'mist_robe', 'meso_mail', 'lumin_robe', 'flash_mail', 'lode_vest', 'aeon_suit', 'zodiaccape', 'nova_armor', 'prismdress', 'moon_armor', 'ruby_armor', 'ravenarmor', 'gloom_cape', 'white_mail', 'black_mail', 'blue_mail', 'red_mail', 'white_vest', 'black_vest', 'blue_vest', 'red_vest', 'taban_vest', 'taban_suit', 'hide_cap', 'bronzehelm', 'iron_helm', 'beret', 'gold_helm', 'rock_helm', 'ceratopper', 'glow_helm', 'lode_helm', 'aeon_helm', 'prism_helm', 'doom_helm', 'dark_helm', 'gloom_helm', 'safe_helm', 'taban_helm', 'sight_cap', 'memory_cap', 'time_hat', 'vigil_hat', 'ozziepants', 'haste_helm', 'rbow_helm', 'mermaidcap', 'bandana', 'ribbon', 'powerglove', 'defender', 'magicscarf', 'amulet', 'dash_ring', 'hit_ring', 'power_ring', 'magic_ring', 'wall_ring', 'silvererng', 'gold_erng', 'silverstud', 'gold_stud', 'sightscope', 'charm_top', 'rage_band', 'frenzyband', 'third_eye', 'wallet', 'greendream', 'berserker', 'powerscarf', 'speed_belt', 'black_rock', 'blue_rock', 'silverrock', 'white_rock', 'gold_rock', 'hero_medal', 'musclering', 'flea_vest', 'magic_seal', 'power_seal', 'valor_crest', 'dragon_tear', 'sun_shades', 'prismspecs', 'tonic', 'mid_tonic', 'full_tonic', 'ether', 'mid_ether', 'full_ether', 'elixir', 'hyperether', 'megaelixir', 'heal', 'revive', 'shelter', 'power_meal', 'lapis', 'barrier', 'shield', 'power_tab', 'magic_tab', 'speed_tab', 'petal', 'fang', 'horn', 'feather', 'seed', 'bike_key', 'pendant', 'gate_key', 'prismshard', 'c_trigger', 'tools', 'jerky', 'dreamstone', 'race_log', 'moon_stone', 'sun_stone', 'ruby_knife', 'yakra_key', 'clone', 'tomas_pop', 'petals_2', 'fangs_2', 'horns_2', 'feathers_2', 'jetsoftime', 'pendant_charge', 'rainbow_shell'}
    default = []


class GoodLoot2(OptionList):
    """Loot that is considered to be good for pool 2 (ignored by vanilla)"""
    display_name = "Good Loot 2"
    valid_keys = {'wood_sword', 'iron_blade', 'steelsaber', 'lode_sword', 'red_katana', 'flint_edge', 'dark_saber', 'aeon_blade', 'demon_edge', 'alloyblade', 'star_sword', 'vedicblade', 'kali_blade', 'shiva_edge', 'bolt_sword', 'slasher', 'bronze_bow', 'iron_bow', 'lode_bow', 'robin_bow', 'sage_bow', 'dream_bow', 'cometarrow', 'sonicarrow', 'valkerye', 'siren', 'air_gun', 'dart_gun', 'auto_gun', 'picomagnum', 'plasma_gun', 'ruby_gun', 'dream_gun', 'megablast', 'shock_wave', 'wondershot', 'graedus', 'tin_arm', 'hammer_arm', 'miragehand', 'stone_arm', 'doomfinger', 'magma_hand', 'megatonarm', 'big_hand', 'kaiser_arm', 'giga_arm', 'terra_arm', 'crisis_arm', 'bronzeedge', 'iron_sword', 'masamune_1', 'flashblade', 'pearl_edge', 'rune_blade', 'bravesword', 'masamune_2', 'demon_hit', 'fist', 'fist_2', 'fist_3', 'iron_fist', 'bronzefist', 'pacifist', 'darkscythe', 'hurricane', 'starscythe', 'doomsickle', 'mop', 'bent_sword', 'bent_hilt', 'swallow', 'slasher_2', 'rainbow', 'hide_tunic', 'karate_gi', 'bronzemail', 'maidensuit', 'iron_suit', 'titan_vest', 'gold_suit', 'ruby_vest', 'dark_mail', 'mist_robe', 'meso_mail', 'lumin_robe', 'flash_mail', 'lode_vest', 'aeon_suit', 'zodiaccape', 'nova_armor', 'prismdress', 'moon_armor', 'ruby_armor', 'ravenarmor', 'gloom_cape', 'white_mail', 'black_mail', 'blue_mail', 'red_mail', 'white_vest', 'black_vest', 'blue_vest', 'red_vest', 'taban_vest', 'taban_suit', 'hide_cap', 'bronzehelm', 'iron_helm', 'beret', 'gold_helm', 'rock_helm', 'ceratopper', 'glow_helm', 'lode_helm', 'aeon_helm', 'prism_helm', 'doom_helm', 'dark_helm', 'gloom_helm', 'safe_helm', 'taban_helm', 'sight_cap', 'memory_cap', 'time_hat', 'vigil_hat', 'ozziepants', 'haste_helm', 'rbow_helm', 'mermaidcap', 'bandana', 'ribbon', 'powerglove', 'defender', 'magicscarf', 'amulet', 'dash_ring', 'hit_ring', 'power_ring', 'magic_ring', 'wall_ring', 'silvererng', 'gold_erng', 'silverstud', 'gold_stud', 'sightscope', 'charm_top', 'rage_band', 'frenzyband', 'third_eye', 'wallet', 'greendream', 'berserker', 'powerscarf', 'speed_belt', 'black_rock', 'blue_rock', 'silverrock', 'white_rock', 'gold_rock', 'hero_medal', 'musclering', 'flea_vest', 'magic_seal', 'power_seal', 'valor_crest', 'dragon_tear', 'sun_shades', 'prismspecs', 'tonic', 'mid_tonic', 'full_tonic', 'ether', 'mid_ether', 'full_ether', 'elixir', 'hyperether', 'megaelixir', 'heal', 'revive', 'shelter', 'power_meal', 'lapis', 'barrier', 'shield', 'power_tab', 'magic_tab', 'speed_tab', 'petal', 'fang', 'horn', 'feather', 'seed', 'bike_key', 'pendant', 'gate_key', 'prismshard', 'c_trigger', 'tools', 'jerky', 'dreamstone', 'race_log', 'moon_stone', 'sun_stone', 'ruby_knife', 'yakra_key', 'clone', 'tomas_pop', 'petals_2', 'fangs_2', 'horns_2', 'feathers_2', 'jetsoftime', 'pendant_charge', 'rainbow_shell'}
    default = []


class GoodLootSpots2(OptionList):
    """Spots for pool 2 which will be given a random good reward (ignored by vanilla)"""
    display_name = "Good Loot Spots 2"
    valid_keys = {'mt_woe_1st_screen', 'mt_woe_2nd_screen_1', 'mt_woe_2nd_screen_2', 'mt_woe_2nd_screen_3', 'mt_woe_2nd_screen_4', 'mt_woe_2nd_screen_5', 'mt_woe_3rd_screen_1', 'mt_woe_3rd_screen_2', 'mt_woe_3rd_screen_3', 'mt_woe_3rd_screen_4', 'mt_woe_3rd_screen_5', 'mt_woe_final_1', 'mt_woe_final_2', 'mt_woe_key', 'fiona_key', 'arris_dome_rats', 'arris_dome_food_store', 'arris_dome_doan_key', 'arris_dome_food_locker_key', 'sun_palace_key', 'sewers_1', 'sewers_2', 'sewers_3', 'lab_16_1', 'lab_16_2', 'lab_16_3', 'lab_16_4', 'lab_32_1', 'prison_tower_1000', 'geno_dome_1f_1', 'geno_dome_1f_2', 'geno_dome_1f_3', 'geno_dome_1f_4', 'geno_dome_room_1', 'geno_dome_room_2', 'geno_dome_proto4_1', 'geno_dome_proto4_2', 'geno_dome_2f_1', 'geno_dome_2f_2', 'geno_dome_2f_3', 'geno_dome_2f_4', 'geno_dome_boss_1', 'geno_dome_boss_2', 'factory_left_aux_console', 'factory_left_security_right', 'factory_left_security_left', 'factory_right_data_core_1', 'factory_right_data_core_2', 'factory_right_floor_top', 'factory_right_floor_left', 'factory_right_floor_bottom', 'factory_right_floor_secret', 'factory_right_crane_lower', 'factory_right_crane_upper', 'factory_right_info_archive', 'giants_claw_traps', 'giants_claw_caves_1', 'giants_claw_caves_2', 'giants_claw_caves_3', 'giants_claw_caves_4', 'giants_claw_caves_5', 'giants_claw_rock', 'giants_claw_key', 'northern_ruins_antechamber_left_600', 'northern_ruins_antechamber_sealed_600', 'northern_ruins_antechamber_left_1000', 'northern_ruins_antechamber_sealed_1000', 'northern_ruins_back_left_sealed_600', 'northern_ruins_back_right_sealed_600', 'northern_ruins_back_left_sealed_1000', 'northern_ruins_back_right_sealed_1000', 'northern_ruins_basement_600', 'northern_ruins_basement_1000', 'guardia_basement_1', 'guardia_basement_2', 'guardia_basement_3', 'guardia_treasury_1', 'guardia_treasury_2', 'guardia_treasury_3', 'kings_trial_key', 'ozzies_fort_guillotines_1', 'ozzies_fort_guillotines_2', 'ozzies_fort_guillotines_3', 'ozzies_fort_guillotines_4', 'ozzies_fort_final_1', 'ozzies_fort_final_2', 'truce_mayor_1f', 'truce_mayor_2f', 'forest_ruins', 'porre_mayor_2f', 'truce_canyon_1', 'truce_canyon_2', 'fionas_house_1', 'fionas_house_2', 'cursed_woods_1', 'cursed_woods_2', 'frogs_burrow_right', 'zenan_bridge_chef', 'zenan_bridge_chef_tab', 'zenan_bridge_captain', 'snail_stop_key', 'lazy_carpenter', 'heckran_cave_sidetrack', 'heckran_cave_entrance', 'heckran_cave_1', 'heckran_cave_2', 'taban_gift_vest', 'kings_room_1000', 'queens_room_1000', 'kings_room_600', 'queens_room_600', 'royal_kitchen', 'queens_tower_600', 'kings_tower_600', 'kings_tower_1000', 'queens_tower_1000', 'guardia_court_tower', 'manoria_cathedral_1', 'manoria_cathedral_2', 'manoria_cathedral_3', 'manoria_interior_1', 'manoria_interior_2', 'manoria_interior_3', 'manoria_interior_4', 'manoria_shrine_sideroom_1', 'manoria_shrine_sideroom_2', 'manoria_bromide_1', 'manoria_bromide_2', 'manoria_bromide_3', 'manoria_shrine_magus_1', 'manoria_shrine_magus_2', 'yakras_room', 'denadoro_mts_screen2_1', 'denadoro_mts_screen2_2', 'denadoro_mts_screen2_3', 'denadoro_mts_final_1', 'denadoro_mts_final_2', 'denadoro_mts_final_3', 'denadoro_mts_waterfall_top_1', 'denadoro_mts_waterfall_top_2', 'denadoro_mts_waterfall_top_3', 'denadoro_mts_waterfall_top_4', 'denadoro_mts_waterfall_top_5', 'denadoro_mts_entrance_1', 'denadoro_mts_entrance_2', 'denadoro_mts_screen3_1', 'denadoro_mts_screen3_2', 'denadoro_mts_screen3_3', 'denadoro_mts_screen3_4', 'denadoro_mts_ambush', 'denadoro_mts_save_pt', 'denadoro_mts_key', 'bangor_dome_seal_1', 'bangor_dome_seal_2', 'bangor_dome_seal_3', 'trann_dome_seal_1', 'trann_dome_seal_2', 'arris_dome_seal_1', 'arris_dome_seal_2', 'arris_dome_seal_3', 'arris_dome_seal_4', 'truce_inn_sealed_600', 'porre_elder_sealed_1', 'porre_elder_sealed_2', 'guardia_castle_sealed_600', 'guardia_forest_sealed_600', 'truce_inn_sealed_1000', 'porre_mayor_sealed_1', 'porre_mayor_sealed_2', 'guardia_forest_sealed_1000', 'guardia_castle_sealed_1000', 'heckran_sealed_1', 'heckran_sealed_2', 'pyramid_left', 'pyramid_right', 'magic_cave_sealed', 'mystic_mt_stream', 'forest_maze_1', 'forest_maze_2', 'forest_maze_3', 'forest_maze_4', 'forest_maze_5', 'forest_maze_6', 'forest_maze_7', 'forest_maze_8', 'forest_maze_9', 'reptite_lair_reptites_1', 'reptite_lair_reptites_2', 'reptite_lair_key', 'dactyl_nest_1', 'dactyl_nest_2', 'dactyl_nest_3', 'melchior_rainbow_shell', 'melchior_sunstone_rainbow', 'melchior_sunstone_specs', 'frogs_burrow_left', 'guardia_jail_fritz_storage', 'guardia_jail_cell', 'guardia_jail_omnicrone_1', 'guardia_jail_omnicrone_2', 'guardia_jail_omnicrone_3', 'guardia_jail_hole_1', 'guardia_jail_hole_2', 'guardia_jail_outer_wall', 'guardia_jail_omnicrone_4', 'guardia_jail_fritz', 'magus_castle_right_hall', 'sunken_desert_b1_nw', 'sunken_desert_b1_ne', 'sunken_desert_b1_se', 'sunken_desert_b1_sw', 'sunken_desert_b2_nw', 'sunken_desert_b2_n', 'sunken_desert_b2_w', 'sunken_desert_b2_sw', 'sunken_desert_b2_se', 'sunken_desert_b2_e', 'sunken_desert_b2_center', 'magus_castle_guillotine_1', 'magus_castle_guillotine_2', 'magus_castle_slash_room_1', 'magus_castle_slash_room_2', 'magus_castle_statue_hall', 'magus_castle_four_kids', 'magus_castle_ozzie_1', 'magus_castle_ozzie_2', 'magus_castle_enemy_elevator', 'reptite_lair_secret_b2_ne_right', 'lab_32_race_log', 'factory_ruins_generator', 'death_peak_south_face_krakker', 'death_peak_south_face_spawn_save', 'death_peak_south_face_summit', 'death_peak_field', 'death_peak_krakker_parade', 'death_peak_caves_left', 'death_peak_caves_center', 'death_peak_caves_right', 'reptite_lair_secret_b1_sw', 'reptite_lair_secret_b1_ne', 'reptite_lair_secret_b1_se', 'reptite_lair_secret_b2_se_right', 'reptite_lair_secret_b2_ne_or_se_left', 'reptite_lair_secret_b2_sw', 'tyrano_lair_throne_1', 'tyrano_lair_throne_2', 'tyrano_lair_trapdoor', 'tyrano_lair_kino_cell', 'tyrano_lair_maze_1', 'tyrano_lair_maze_2', 'tyrano_lair_maze_3', 'tyrano_lair_maze_4', 'black_omen_aux_command_mid', 'black_omen_aux_command_ne', 'black_omen_grand_hall', 'black_omen_nu_hall_nw', 'black_omen_nu_hall_w', 'black_omen_nu_hall_sw', 'black_omen_nu_hall_ne', 'black_omen_nu_hall_e', 'black_omen_nu_hall_se', 'black_omen_royal_path', 'black_omen_ruminator_parade', 'black_omen_eyeball_hall', 'black_omen_tubster_fly', 'black_omen_martello', 'black_omen_alien_sw', 'black_omen_alien_ne', 'black_omen_alien_nw', 'black_omen_terra_w', 'black_omen_terra_rock', 'black_omen_terra_ne', 'ocean_palace_main_s', 'ocean_palace_main_n', 'ocean_palace_e_room', 'ocean_palace_w_room', 'ocean_palace_switch_nw', 'ocean_palace_switch_sw', 'ocean_palace_switch_ne', 'ocean_palace_switch_secret', 'ocean_palace_final', 'magus_castle_left_hall', 'magus_castle_unskippables', 'magus_castle_pit_e', 'magus_castle_pit_ne', 'magus_castle_pit_nw', 'magus_castle_pit_w', 'taban_gift_suit', 'taban_gift_helm', 'trading_post_petal_fang_base', 'trading_post_petal_fang_upgrade', 'trading_post_petal_horn_base', 'trading_post_petal_horn_upgrade', 'trading_post_petal_feather_base', 'trading_post_petal_feather_upgrade', 'trading_post_fang_horn_base', 'trading_post_fang_horn_upgrade', 'trading_post_fang_feather_base', 'trading_post_fang_feather_upgrade', 'trading_post_horn_feather_base', 'trading_post_horn_feather_upgrade', 'trading_post_special', 'jerky_gift', 'denadoro_rock', 'kajar_rock', 'laruba_rock', 'bekkler_key', 'cyrus_grave_key', 'sun_keep_2300', 'lucca_wondershot', 'taban_sunshades', 'fair_pendant', 'tata_reward', 'toma_reward', 'melchior_forge_masa', 'eot_gaspar_reward', 'hunting_range_nu_reward', 'zeal_mammon_machine', 'magus_castle_slash_sword_floor', 'guardia_prison_lunch_bag', 'cronos_mom', 'truce_mayor_2f_old_man', 'ioka_sweetwater_tonic', 'dorino_inn_powermeal', 'yakra_key_chest', 'courtroom_yakra_key', 'johnny_race_power_tab', 'guardia_forest_power_tab_600', 'guardia_forest_power_tab_1000', 'manoria_confinement_power_tab', 'dorino_bromide_magic_tab', 'porre_market_600_power_tab', 'denadoro_mts_speed_tab', 'tomas_grave_speed_tab', 'giants_claw_caverns_power_tab', 'giants_claw_entrance_power_tab', 'giants_claw_traps_power_tab', 'sun_keep_600_power_tab', 'medina_elder_speed_tab', 'medina_elder_magic_tab', 'magus_castle_flea_magic_tab', 'magus_castle_dungeons_magic_tab', 'trann_dome_sealed_magic_tab', 'arris_dome_sealed_power_tab', 'keepers_dome_magic_tab', 'death_peak_power_tab', 'blackbird_ducts_magic_tab', 'geno_dome_atropos_magic_tab', 'geno_dome_corridor_power_tab', 'geno_dome_labs_magic_tab', 'geno_dome_labs_speed_tab', 'enhasa_nu_battle_magic_tab', 'enhasa_nu_battle_speed_tab', 'kajar_speed_tab', 'kajar_nu_scratch_magic_tab', 'last_village_nu_shop_magic_tab', 'sunken_desert_power_tab', 'mountains_re_nice_magic_tab', 'beast_nest_power_tab', 'mt_woe_magic_tab', 'ocean_palace_elevator_magic_tab', 'ozzies_fort_guillotines_tab', 'proto_dome_portal_tab', 'northern_ruins_heros_grave_magic_tab', 'northern_ruins_landing_power_tab'}
    default = []


class GoodLootRate2(Range):
    """Percent chance to fill a good loot spot with good loot for pool 2"""
    display_name = "Good Loot Rate 2"
    range_start = 0
    range_end = 100
    default = 75


class GoodLoot3(OptionList):
    """Loot that is considered to be good for pool 3 (ignored by vanilla)"""
    display_name = "Good Loot 3"
    valid_keys = {'wood_sword', 'iron_blade', 'steelsaber', 'lode_sword', 'red_katana', 'flint_edge', 'dark_saber', 'aeon_blade', 'demon_edge', 'alloyblade', 'star_sword', 'vedicblade', 'kali_blade', 'shiva_edge', 'bolt_sword', 'slasher', 'bronze_bow', 'iron_bow', 'lode_bow', 'robin_bow', 'sage_bow', 'dream_bow', 'cometarrow', 'sonicarrow', 'valkerye', 'siren', 'air_gun', 'dart_gun', 'auto_gun', 'picomagnum', 'plasma_gun', 'ruby_gun', 'dream_gun', 'megablast', 'shock_wave', 'wondershot', 'graedus', 'tin_arm', 'hammer_arm', 'miragehand', 'stone_arm', 'doomfinger', 'magma_hand', 'megatonarm', 'big_hand', 'kaiser_arm', 'giga_arm', 'terra_arm', 'crisis_arm', 'bronzeedge', 'iron_sword', 'masamune_1', 'flashblade', 'pearl_edge', 'rune_blade', 'bravesword', 'masamune_2', 'demon_hit', 'fist', 'fist_2', 'fist_3', 'iron_fist', 'bronzefist', 'pacifist', 'darkscythe', 'hurricane', 'starscythe', 'doomsickle', 'mop', 'bent_sword', 'bent_hilt', 'swallow', 'slasher_2', 'rainbow', 'hide_tunic', 'karate_gi', 'bronzemail', 'maidensuit', 'iron_suit', 'titan_vest', 'gold_suit', 'ruby_vest', 'dark_mail', 'mist_robe', 'meso_mail', 'lumin_robe', 'flash_mail', 'lode_vest', 'aeon_suit', 'zodiaccape', 'nova_armor', 'prismdress', 'moon_armor', 'ruby_armor', 'ravenarmor', 'gloom_cape', 'white_mail', 'black_mail', 'blue_mail', 'red_mail', 'white_vest', 'black_vest', 'blue_vest', 'red_vest', 'taban_vest', 'taban_suit', 'hide_cap', 'bronzehelm', 'iron_helm', 'beret', 'gold_helm', 'rock_helm', 'ceratopper', 'glow_helm', 'lode_helm', 'aeon_helm', 'prism_helm', 'doom_helm', 'dark_helm', 'gloom_helm', 'safe_helm', 'taban_helm', 'sight_cap', 'memory_cap', 'time_hat', 'vigil_hat', 'ozziepants', 'haste_helm', 'rbow_helm', 'mermaidcap', 'bandana', 'ribbon', 'powerglove', 'defender', 'magicscarf', 'amulet', 'dash_ring', 'hit_ring', 'power_ring', 'magic_ring', 'wall_ring', 'silvererng', 'gold_erng', 'silverstud', 'gold_stud', 'sightscope', 'charm_top', 'rage_band', 'frenzyband', 'third_eye', 'wallet', 'greendream', 'berserker', 'powerscarf', 'speed_belt', 'black_rock', 'blue_rock', 'silverrock', 'white_rock', 'gold_rock', 'hero_medal', 'musclering', 'flea_vest', 'magic_seal', 'power_seal', 'valor_crest', 'dragon_tear', 'sun_shades', 'prismspecs', 'tonic', 'mid_tonic', 'full_tonic', 'ether', 'mid_ether', 'full_ether', 'elixir', 'hyperether', 'megaelixir', 'heal', 'revive', 'shelter', 'power_meal', 'lapis', 'barrier', 'shield', 'power_tab', 'magic_tab', 'speed_tab', 'petal', 'fang', 'horn', 'feather', 'seed', 'bike_key', 'pendant', 'gate_key', 'prismshard', 'c_trigger', 'tools', 'jerky', 'dreamstone', 'race_log', 'moon_stone', 'sun_stone', 'ruby_knife', 'yakra_key', 'clone', 'tomas_pop', 'petals_2', 'fangs_2', 'horns_2', 'feathers_2', 'jetsoftime', 'pendant_charge', 'rainbow_shell'}
    default = []


class GoodLootSpots3(OptionList):
    """Spots for pool 3 which will be given a random good reward (ignored by vanilla)"""
    display_name = "Good Loot Spots 3"
    valid_keys = {'mt_woe_1st_screen', 'mt_woe_2nd_screen_1', 'mt_woe_2nd_screen_2', 'mt_woe_2nd_screen_3', 'mt_woe_2nd_screen_4', 'mt_woe_2nd_screen_5', 'mt_woe_3rd_screen_1', 'mt_woe_3rd_screen_2', 'mt_woe_3rd_screen_3', 'mt_woe_3rd_screen_4', 'mt_woe_3rd_screen_5', 'mt_woe_final_1', 'mt_woe_final_2', 'mt_woe_key', 'fiona_key', 'arris_dome_rats', 'arris_dome_food_store', 'arris_dome_doan_key', 'arris_dome_food_locker_key', 'sun_palace_key', 'sewers_1', 'sewers_2', 'sewers_3', 'lab_16_1', 'lab_16_2', 'lab_16_3', 'lab_16_4', 'lab_32_1', 'prison_tower_1000', 'geno_dome_1f_1', 'geno_dome_1f_2', 'geno_dome_1f_3', 'geno_dome_1f_4', 'geno_dome_room_1', 'geno_dome_room_2', 'geno_dome_proto4_1', 'geno_dome_proto4_2', 'geno_dome_2f_1', 'geno_dome_2f_2', 'geno_dome_2f_3', 'geno_dome_2f_4', 'geno_dome_boss_1', 'geno_dome_boss_2', 'factory_left_aux_console', 'factory_left_security_right', 'factory_left_security_left', 'factory_right_data_core_1', 'factory_right_data_core_2', 'factory_right_floor_top', 'factory_right_floor_left', 'factory_right_floor_bottom', 'factory_right_floor_secret', 'factory_right_crane_lower', 'factory_right_crane_upper', 'factory_right_info_archive', 'giants_claw_traps', 'giants_claw_caves_1', 'giants_claw_caves_2', 'giants_claw_caves_3', 'giants_claw_caves_4', 'giants_claw_caves_5', 'giants_claw_rock', 'giants_claw_key', 'northern_ruins_antechamber_left_600', 'northern_ruins_antechamber_sealed_600', 'northern_ruins_antechamber_left_1000', 'northern_ruins_antechamber_sealed_1000', 'northern_ruins_back_left_sealed_600', 'northern_ruins_back_right_sealed_600', 'northern_ruins_back_left_sealed_1000', 'northern_ruins_back_right_sealed_1000', 'northern_ruins_basement_600', 'northern_ruins_basement_1000', 'guardia_basement_1', 'guardia_basement_2', 'guardia_basement_3', 'guardia_treasury_1', 'guardia_treasury_2', 'guardia_treasury_3', 'kings_trial_key', 'ozzies_fort_guillotines_1', 'ozzies_fort_guillotines_2', 'ozzies_fort_guillotines_3', 'ozzies_fort_guillotines_4', 'ozzies_fort_final_1', 'ozzies_fort_final_2', 'truce_mayor_1f', 'truce_mayor_2f', 'forest_ruins', 'porre_mayor_2f', 'truce_canyon_1', 'truce_canyon_2', 'fionas_house_1', 'fionas_house_2', 'cursed_woods_1', 'cursed_woods_2', 'frogs_burrow_right', 'zenan_bridge_chef', 'zenan_bridge_chef_tab', 'zenan_bridge_captain', 'snail_stop_key', 'lazy_carpenter', 'heckran_cave_sidetrack', 'heckran_cave_entrance', 'heckran_cave_1', 'heckran_cave_2', 'taban_gift_vest', 'kings_room_1000', 'queens_room_1000', 'kings_room_600', 'queens_room_600', 'royal_kitchen', 'queens_tower_600', 'kings_tower_600', 'kings_tower_1000', 'queens_tower_1000', 'guardia_court_tower', 'manoria_cathedral_1', 'manoria_cathedral_2', 'manoria_cathedral_3', 'manoria_interior_1', 'manoria_interior_2', 'manoria_interior_3', 'manoria_interior_4', 'manoria_shrine_sideroom_1', 'manoria_shrine_sideroom_2', 'manoria_bromide_1', 'manoria_bromide_2', 'manoria_bromide_3', 'manoria_shrine_magus_1', 'manoria_shrine_magus_2', 'yakras_room', 'denadoro_mts_screen2_1', 'denadoro_mts_screen2_2', 'denadoro_mts_screen2_3', 'denadoro_mts_final_1', 'denadoro_mts_final_2', 'denadoro_mts_final_3', 'denadoro_mts_waterfall_top_1', 'denadoro_mts_waterfall_top_2', 'denadoro_mts_waterfall_top_3', 'denadoro_mts_waterfall_top_4', 'denadoro_mts_waterfall_top_5', 'denadoro_mts_entrance_1', 'denadoro_mts_entrance_2', 'denadoro_mts_screen3_1', 'denadoro_mts_screen3_2', 'denadoro_mts_screen3_3', 'denadoro_mts_screen3_4', 'denadoro_mts_ambush', 'denadoro_mts_save_pt', 'denadoro_mts_key', 'bangor_dome_seal_1', 'bangor_dome_seal_2', 'bangor_dome_seal_3', 'trann_dome_seal_1', 'trann_dome_seal_2', 'arris_dome_seal_1', 'arris_dome_seal_2', 'arris_dome_seal_3', 'arris_dome_seal_4', 'truce_inn_sealed_600', 'porre_elder_sealed_1', 'porre_elder_sealed_2', 'guardia_castle_sealed_600', 'guardia_forest_sealed_600', 'truce_inn_sealed_1000', 'porre_mayor_sealed_1', 'porre_mayor_sealed_2', 'guardia_forest_sealed_1000', 'guardia_castle_sealed_1000', 'heckran_sealed_1', 'heckran_sealed_2', 'pyramid_left', 'pyramid_right', 'magic_cave_sealed', 'mystic_mt_stream', 'forest_maze_1', 'forest_maze_2', 'forest_maze_3', 'forest_maze_4', 'forest_maze_5', 'forest_maze_6', 'forest_maze_7', 'forest_maze_8', 'forest_maze_9', 'reptite_lair_reptites_1', 'reptite_lair_reptites_2', 'reptite_lair_key', 'dactyl_nest_1', 'dactyl_nest_2', 'dactyl_nest_3', 'melchior_rainbow_shell', 'melchior_sunstone_rainbow', 'melchior_sunstone_specs', 'frogs_burrow_left', 'guardia_jail_fritz_storage', 'guardia_jail_cell', 'guardia_jail_omnicrone_1', 'guardia_jail_omnicrone_2', 'guardia_jail_omnicrone_3', 'guardia_jail_hole_1', 'guardia_jail_hole_2', 'guardia_jail_outer_wall', 'guardia_jail_omnicrone_4', 'guardia_jail_fritz', 'magus_castle_right_hall', 'sunken_desert_b1_nw', 'sunken_desert_b1_ne', 'sunken_desert_b1_se', 'sunken_desert_b1_sw', 'sunken_desert_b2_nw', 'sunken_desert_b2_n', 'sunken_desert_b2_w', 'sunken_desert_b2_sw', 'sunken_desert_b2_se', 'sunken_desert_b2_e', 'sunken_desert_b2_center', 'magus_castle_guillotine_1', 'magus_castle_guillotine_2', 'magus_castle_slash_room_1', 'magus_castle_slash_room_2', 'magus_castle_statue_hall', 'magus_castle_four_kids', 'magus_castle_ozzie_1', 'magus_castle_ozzie_2', 'magus_castle_enemy_elevator', 'reptite_lair_secret_b2_ne_right', 'lab_32_race_log', 'factory_ruins_generator', 'death_peak_south_face_krakker', 'death_peak_south_face_spawn_save', 'death_peak_south_face_summit', 'death_peak_field', 'death_peak_krakker_parade', 'death_peak_caves_left', 'death_peak_caves_center', 'death_peak_caves_right', 'reptite_lair_secret_b1_sw', 'reptite_lair_secret_b1_ne', 'reptite_lair_secret_b1_se', 'reptite_lair_secret_b2_se_right', 'reptite_lair_secret_b2_ne_or_se_left', 'reptite_lair_secret_b2_sw', 'tyrano_lair_throne_1', 'tyrano_lair_throne_2', 'tyrano_lair_trapdoor', 'tyrano_lair_kino_cell', 'tyrano_lair_maze_1', 'tyrano_lair_maze_2', 'tyrano_lair_maze_3', 'tyrano_lair_maze_4', 'black_omen_aux_command_mid', 'black_omen_aux_command_ne', 'black_omen_grand_hall', 'black_omen_nu_hall_nw', 'black_omen_nu_hall_w', 'black_omen_nu_hall_sw', 'black_omen_nu_hall_ne', 'black_omen_nu_hall_e', 'black_omen_nu_hall_se', 'black_omen_royal_path', 'black_omen_ruminator_parade', 'black_omen_eyeball_hall', 'black_omen_tubster_fly', 'black_omen_martello', 'black_omen_alien_sw', 'black_omen_alien_ne', 'black_omen_alien_nw', 'black_omen_terra_w', 'black_omen_terra_rock', 'black_omen_terra_ne', 'ocean_palace_main_s', 'ocean_palace_main_n', 'ocean_palace_e_room', 'ocean_palace_w_room', 'ocean_palace_switch_nw', 'ocean_palace_switch_sw', 'ocean_palace_switch_ne', 'ocean_palace_switch_secret', 'ocean_palace_final', 'magus_castle_left_hall', 'magus_castle_unskippables', 'magus_castle_pit_e', 'magus_castle_pit_ne', 'magus_castle_pit_nw', 'magus_castle_pit_w', 'taban_gift_suit', 'taban_gift_helm', 'trading_post_petal_fang_base', 'trading_post_petal_fang_upgrade', 'trading_post_petal_horn_base', 'trading_post_petal_horn_upgrade', 'trading_post_petal_feather_base', 'trading_post_petal_feather_upgrade', 'trading_post_fang_horn_base', 'trading_post_fang_horn_upgrade', 'trading_post_fang_feather_base', 'trading_post_fang_feather_upgrade', 'trading_post_horn_feather_base', 'trading_post_horn_feather_upgrade', 'trading_post_special', 'jerky_gift', 'denadoro_rock', 'kajar_rock', 'laruba_rock', 'bekkler_key', 'cyrus_grave_key', 'sun_keep_2300', 'lucca_wondershot', 'taban_sunshades', 'fair_pendant', 'tata_reward', 'toma_reward', 'melchior_forge_masa', 'eot_gaspar_reward', 'hunting_range_nu_reward', 'zeal_mammon_machine', 'magus_castle_slash_sword_floor', 'guardia_prison_lunch_bag', 'cronos_mom', 'truce_mayor_2f_old_man', 'ioka_sweetwater_tonic', 'dorino_inn_powermeal', 'yakra_key_chest', 'courtroom_yakra_key', 'johnny_race_power_tab', 'guardia_forest_power_tab_600', 'guardia_forest_power_tab_1000', 'manoria_confinement_power_tab', 'dorino_bromide_magic_tab', 'porre_market_600_power_tab', 'denadoro_mts_speed_tab', 'tomas_grave_speed_tab', 'giants_claw_caverns_power_tab', 'giants_claw_entrance_power_tab', 'giants_claw_traps_power_tab', 'sun_keep_600_power_tab', 'medina_elder_speed_tab', 'medina_elder_magic_tab', 'magus_castle_flea_magic_tab', 'magus_castle_dungeons_magic_tab', 'trann_dome_sealed_magic_tab', 'arris_dome_sealed_power_tab', 'keepers_dome_magic_tab', 'death_peak_power_tab', 'blackbird_ducts_magic_tab', 'geno_dome_atropos_magic_tab', 'geno_dome_corridor_power_tab', 'geno_dome_labs_magic_tab', 'geno_dome_labs_speed_tab', 'enhasa_nu_battle_magic_tab', 'enhasa_nu_battle_speed_tab', 'kajar_speed_tab', 'kajar_nu_scratch_magic_tab', 'last_village_nu_shop_magic_tab', 'sunken_desert_power_tab', 'mountains_re_nice_magic_tab', 'beast_nest_power_tab', 'mt_woe_magic_tab', 'ocean_palace_elevator_magic_tab', 'ozzies_fort_guillotines_tab', 'proto_dome_portal_tab', 'northern_ruins_heros_grave_magic_tab', 'northern_ruins_landing_power_tab'}
    default = []


class GoodLootRate3(Range):
    """Percent chance to fill a good loot spot with good loot for pool 3"""
    display_name = "Good Loot Rate 3"
    range_start = 0
    range_end = 100
    default = 75


class GoodLoot4(OptionList):
    """Loot that is considered to be good for pool 4 (ignored by vanilla)"""
    display_name = "Good Loot 4"
    valid_keys = {'wood_sword', 'iron_blade', 'steelsaber', 'lode_sword', 'red_katana', 'flint_edge', 'dark_saber', 'aeon_blade', 'demon_edge', 'alloyblade', 'star_sword', 'vedicblade', 'kali_blade', 'shiva_edge', 'bolt_sword', 'slasher', 'bronze_bow', 'iron_bow', 'lode_bow', 'robin_bow', 'sage_bow', 'dream_bow', 'cometarrow', 'sonicarrow', 'valkerye', 'siren', 'air_gun', 'dart_gun', 'auto_gun', 'picomagnum', 'plasma_gun', 'ruby_gun', 'dream_gun', 'megablast', 'shock_wave', 'wondershot', 'graedus', 'tin_arm', 'hammer_arm', 'miragehand', 'stone_arm', 'doomfinger', 'magma_hand', 'megatonarm', 'big_hand', 'kaiser_arm', 'giga_arm', 'terra_arm', 'crisis_arm', 'bronzeedge', 'iron_sword', 'masamune_1', 'flashblade', 'pearl_edge', 'rune_blade', 'bravesword', 'masamune_2', 'demon_hit', 'fist', 'fist_2', 'fist_3', 'iron_fist', 'bronzefist', 'pacifist', 'darkscythe', 'hurricane', 'starscythe', 'doomsickle', 'mop', 'bent_sword', 'bent_hilt', 'swallow', 'slasher_2', 'rainbow', 'hide_tunic', 'karate_gi', 'bronzemail', 'maidensuit', 'iron_suit', 'titan_vest', 'gold_suit', 'ruby_vest', 'dark_mail', 'mist_robe', 'meso_mail', 'lumin_robe', 'flash_mail', 'lode_vest', 'aeon_suit', 'zodiaccape', 'nova_armor', 'prismdress', 'moon_armor', 'ruby_armor', 'ravenarmor', 'gloom_cape', 'white_mail', 'black_mail', 'blue_mail', 'red_mail', 'white_vest', 'black_vest', 'blue_vest', 'red_vest', 'taban_vest', 'taban_suit', 'hide_cap', 'bronzehelm', 'iron_helm', 'beret', 'gold_helm', 'rock_helm', 'ceratopper', 'glow_helm', 'lode_helm', 'aeon_helm', 'prism_helm', 'doom_helm', 'dark_helm', 'gloom_helm', 'safe_helm', 'taban_helm', 'sight_cap', 'memory_cap', 'time_hat', 'vigil_hat', 'ozziepants', 'haste_helm', 'rbow_helm', 'mermaidcap', 'bandana', 'ribbon', 'powerglove', 'defender', 'magicscarf', 'amulet', 'dash_ring', 'hit_ring', 'power_ring', 'magic_ring', 'wall_ring', 'silvererng', 'gold_erng', 'silverstud', 'gold_stud', 'sightscope', 'charm_top', 'rage_band', 'frenzyband', 'third_eye', 'wallet', 'greendream', 'berserker', 'powerscarf', 'speed_belt', 'black_rock', 'blue_rock', 'silverrock', 'white_rock', 'gold_rock', 'hero_medal', 'musclering', 'flea_vest', 'magic_seal', 'power_seal', 'valor_crest', 'dragon_tear', 'sun_shades', 'prismspecs', 'tonic', 'mid_tonic', 'full_tonic', 'ether', 'mid_ether', 'full_ether', 'elixir', 'hyperether', 'megaelixir', 'heal', 'revive', 'shelter', 'power_meal', 'lapis', 'barrier', 'shield', 'power_tab', 'magic_tab', 'speed_tab', 'petal', 'fang', 'horn', 'feather', 'seed', 'bike_key', 'pendant', 'gate_key', 'prismshard', 'c_trigger', 'tools', 'jerky', 'dreamstone', 'race_log', 'moon_stone', 'sun_stone', 'ruby_knife', 'yakra_key', 'clone', 'tomas_pop', 'petals_2', 'fangs_2', 'horns_2', 'feathers_2', 'jetsoftime', 'pendant_charge', 'rainbow_shell'}
    default = []


class GoodLootSpots4(OptionList):
    """Spots for pool 4 which will be given a random good reward (ignored by vanilla)"""
    display_name = "Good Loot Spots 4"
    valid_keys = {'mt_woe_1st_screen', 'mt_woe_2nd_screen_1', 'mt_woe_2nd_screen_2', 'mt_woe_2nd_screen_3', 'mt_woe_2nd_screen_4', 'mt_woe_2nd_screen_5', 'mt_woe_3rd_screen_1', 'mt_woe_3rd_screen_2', 'mt_woe_3rd_screen_3', 'mt_woe_3rd_screen_4', 'mt_woe_3rd_screen_5', 'mt_woe_final_1', 'mt_woe_final_2', 'mt_woe_key', 'fiona_key', 'arris_dome_rats', 'arris_dome_food_store', 'arris_dome_doan_key', 'arris_dome_food_locker_key', 'sun_palace_key', 'sewers_1', 'sewers_2', 'sewers_3', 'lab_16_1', 'lab_16_2', 'lab_16_3', 'lab_16_4', 'lab_32_1', 'prison_tower_1000', 'geno_dome_1f_1', 'geno_dome_1f_2', 'geno_dome_1f_3', 'geno_dome_1f_4', 'geno_dome_room_1', 'geno_dome_room_2', 'geno_dome_proto4_1', 'geno_dome_proto4_2', 'geno_dome_2f_1', 'geno_dome_2f_2', 'geno_dome_2f_3', 'geno_dome_2f_4', 'geno_dome_boss_1', 'geno_dome_boss_2', 'factory_left_aux_console', 'factory_left_security_right', 'factory_left_security_left', 'factory_right_data_core_1', 'factory_right_data_core_2', 'factory_right_floor_top', 'factory_right_floor_left', 'factory_right_floor_bottom', 'factory_right_floor_secret', 'factory_right_crane_lower', 'factory_right_crane_upper', 'factory_right_info_archive', 'giants_claw_traps', 'giants_claw_caves_1', 'giants_claw_caves_2', 'giants_claw_caves_3', 'giants_claw_caves_4', 'giants_claw_caves_5', 'giants_claw_rock', 'giants_claw_key', 'northern_ruins_antechamber_left_600', 'northern_ruins_antechamber_sealed_600', 'northern_ruins_antechamber_left_1000', 'northern_ruins_antechamber_sealed_1000', 'northern_ruins_back_left_sealed_600', 'northern_ruins_back_right_sealed_600', 'northern_ruins_back_left_sealed_1000', 'northern_ruins_back_right_sealed_1000', 'northern_ruins_basement_600', 'northern_ruins_basement_1000', 'guardia_basement_1', 'guardia_basement_2', 'guardia_basement_3', 'guardia_treasury_1', 'guardia_treasury_2', 'guardia_treasury_3', 'kings_trial_key', 'ozzies_fort_guillotines_1', 'ozzies_fort_guillotines_2', 'ozzies_fort_guillotines_3', 'ozzies_fort_guillotines_4', 'ozzies_fort_final_1', 'ozzies_fort_final_2', 'truce_mayor_1f', 'truce_mayor_2f', 'forest_ruins', 'porre_mayor_2f', 'truce_canyon_1', 'truce_canyon_2', 'fionas_house_1', 'fionas_house_2', 'cursed_woods_1', 'cursed_woods_2', 'frogs_burrow_right', 'zenan_bridge_chef', 'zenan_bridge_chef_tab', 'zenan_bridge_captain', 'snail_stop_key', 'lazy_carpenter', 'heckran_cave_sidetrack', 'heckran_cave_entrance', 'heckran_cave_1', 'heckran_cave_2', 'taban_gift_vest', 'kings_room_1000', 'queens_room_1000', 'kings_room_600', 'queens_room_600', 'royal_kitchen', 'queens_tower_600', 'kings_tower_600', 'kings_tower_1000', 'queens_tower_1000', 'guardia_court_tower', 'manoria_cathedral_1', 'manoria_cathedral_2', 'manoria_cathedral_3', 'manoria_interior_1', 'manoria_interior_2', 'manoria_interior_3', 'manoria_interior_4', 'manoria_shrine_sideroom_1', 'manoria_shrine_sideroom_2', 'manoria_bromide_1', 'manoria_bromide_2', 'manoria_bromide_3', 'manoria_shrine_magus_1', 'manoria_shrine_magus_2', 'yakras_room', 'denadoro_mts_screen2_1', 'denadoro_mts_screen2_2', 'denadoro_mts_screen2_3', 'denadoro_mts_final_1', 'denadoro_mts_final_2', 'denadoro_mts_final_3', 'denadoro_mts_waterfall_top_1', 'denadoro_mts_waterfall_top_2', 'denadoro_mts_waterfall_top_3', 'denadoro_mts_waterfall_top_4', 'denadoro_mts_waterfall_top_5', 'denadoro_mts_entrance_1', 'denadoro_mts_entrance_2', 'denadoro_mts_screen3_1', 'denadoro_mts_screen3_2', 'denadoro_mts_screen3_3', 'denadoro_mts_screen3_4', 'denadoro_mts_ambush', 'denadoro_mts_save_pt', 'denadoro_mts_key', 'bangor_dome_seal_1', 'bangor_dome_seal_2', 'bangor_dome_seal_3', 'trann_dome_seal_1', 'trann_dome_seal_2', 'arris_dome_seal_1', 'arris_dome_seal_2', 'arris_dome_seal_3', 'arris_dome_seal_4', 'truce_inn_sealed_600', 'porre_elder_sealed_1', 'porre_elder_sealed_2', 'guardia_castle_sealed_600', 'guardia_forest_sealed_600', 'truce_inn_sealed_1000', 'porre_mayor_sealed_1', 'porre_mayor_sealed_2', 'guardia_forest_sealed_1000', 'guardia_castle_sealed_1000', 'heckran_sealed_1', 'heckran_sealed_2', 'pyramid_left', 'pyramid_right', 'magic_cave_sealed', 'mystic_mt_stream', 'forest_maze_1', 'forest_maze_2', 'forest_maze_3', 'forest_maze_4', 'forest_maze_5', 'forest_maze_6', 'forest_maze_7', 'forest_maze_8', 'forest_maze_9', 'reptite_lair_reptites_1', 'reptite_lair_reptites_2', 'reptite_lair_key', 'dactyl_nest_1', 'dactyl_nest_2', 'dactyl_nest_3', 'melchior_rainbow_shell', 'melchior_sunstone_rainbow', 'melchior_sunstone_specs', 'frogs_burrow_left', 'guardia_jail_fritz_storage', 'guardia_jail_cell', 'guardia_jail_omnicrone_1', 'guardia_jail_omnicrone_2', 'guardia_jail_omnicrone_3', 'guardia_jail_hole_1', 'guardia_jail_hole_2', 'guardia_jail_outer_wall', 'guardia_jail_omnicrone_4', 'guardia_jail_fritz', 'magus_castle_right_hall', 'sunken_desert_b1_nw', 'sunken_desert_b1_ne', 'sunken_desert_b1_se', 'sunken_desert_b1_sw', 'sunken_desert_b2_nw', 'sunken_desert_b2_n', 'sunken_desert_b2_w', 'sunken_desert_b2_sw', 'sunken_desert_b2_se', 'sunken_desert_b2_e', 'sunken_desert_b2_center', 'magus_castle_guillotine_1', 'magus_castle_guillotine_2', 'magus_castle_slash_room_1', 'magus_castle_slash_room_2', 'magus_castle_statue_hall', 'magus_castle_four_kids', 'magus_castle_ozzie_1', 'magus_castle_ozzie_2', 'magus_castle_enemy_elevator', 'reptite_lair_secret_b2_ne_right', 'lab_32_race_log', 'factory_ruins_generator', 'death_peak_south_face_krakker', 'death_peak_south_face_spawn_save', 'death_peak_south_face_summit', 'death_peak_field', 'death_peak_krakker_parade', 'death_peak_caves_left', 'death_peak_caves_center', 'death_peak_caves_right', 'reptite_lair_secret_b1_sw', 'reptite_lair_secret_b1_ne', 'reptite_lair_secret_b1_se', 'reptite_lair_secret_b2_se_right', 'reptite_lair_secret_b2_ne_or_se_left', 'reptite_lair_secret_b2_sw', 'tyrano_lair_throne_1', 'tyrano_lair_throne_2', 'tyrano_lair_trapdoor', 'tyrano_lair_kino_cell', 'tyrano_lair_maze_1', 'tyrano_lair_maze_2', 'tyrano_lair_maze_3', 'tyrano_lair_maze_4', 'black_omen_aux_command_mid', 'black_omen_aux_command_ne', 'black_omen_grand_hall', 'black_omen_nu_hall_nw', 'black_omen_nu_hall_w', 'black_omen_nu_hall_sw', 'black_omen_nu_hall_ne', 'black_omen_nu_hall_e', 'black_omen_nu_hall_se', 'black_omen_royal_path', 'black_omen_ruminator_parade', 'black_omen_eyeball_hall', 'black_omen_tubster_fly', 'black_omen_martello', 'black_omen_alien_sw', 'black_omen_alien_ne', 'black_omen_alien_nw', 'black_omen_terra_w', 'black_omen_terra_rock', 'black_omen_terra_ne', 'ocean_palace_main_s', 'ocean_palace_main_n', 'ocean_palace_e_room', 'ocean_palace_w_room', 'ocean_palace_switch_nw', 'ocean_palace_switch_sw', 'ocean_palace_switch_ne', 'ocean_palace_switch_secret', 'ocean_palace_final', 'magus_castle_left_hall', 'magus_castle_unskippables', 'magus_castle_pit_e', 'magus_castle_pit_ne', 'magus_castle_pit_nw', 'magus_castle_pit_w', 'taban_gift_suit', 'taban_gift_helm', 'trading_post_petal_fang_base', 'trading_post_petal_fang_upgrade', 'trading_post_petal_horn_base', 'trading_post_petal_horn_upgrade', 'trading_post_petal_feather_base', 'trading_post_petal_feather_upgrade', 'trading_post_fang_horn_base', 'trading_post_fang_horn_upgrade', 'trading_post_fang_feather_base', 'trading_post_fang_feather_upgrade', 'trading_post_horn_feather_base', 'trading_post_horn_feather_upgrade', 'trading_post_special', 'jerky_gift', 'denadoro_rock', 'kajar_rock', 'laruba_rock', 'bekkler_key', 'cyrus_grave_key', 'sun_keep_2300', 'lucca_wondershot', 'taban_sunshades', 'fair_pendant', 'tata_reward', 'toma_reward', 'melchior_forge_masa', 'eot_gaspar_reward', 'hunting_range_nu_reward', 'zeal_mammon_machine', 'magus_castle_slash_sword_floor', 'guardia_prison_lunch_bag', 'cronos_mom', 'truce_mayor_2f_old_man', 'ioka_sweetwater_tonic', 'dorino_inn_powermeal', 'yakra_key_chest', 'courtroom_yakra_key', 'johnny_race_power_tab', 'guardia_forest_power_tab_600', 'guardia_forest_power_tab_1000', 'manoria_confinement_power_tab', 'dorino_bromide_magic_tab', 'porre_market_600_power_tab', 'denadoro_mts_speed_tab', 'tomas_grave_speed_tab', 'giants_claw_caverns_power_tab', 'giants_claw_entrance_power_tab', 'giants_claw_traps_power_tab', 'sun_keep_600_power_tab', 'medina_elder_speed_tab', 'medina_elder_magic_tab', 'magus_castle_flea_magic_tab', 'magus_castle_dungeons_magic_tab', 'trann_dome_sealed_magic_tab', 'arris_dome_sealed_power_tab', 'keepers_dome_magic_tab', 'death_peak_power_tab', 'blackbird_ducts_magic_tab', 'geno_dome_atropos_magic_tab', 'geno_dome_corridor_power_tab', 'geno_dome_labs_magic_tab', 'geno_dome_labs_speed_tab', 'enhasa_nu_battle_magic_tab', 'enhasa_nu_battle_speed_tab', 'kajar_speed_tab', 'kajar_nu_scratch_magic_tab', 'last_village_nu_shop_magic_tab', 'sunken_desert_power_tab', 'mountains_re_nice_magic_tab', 'beast_nest_power_tab', 'mt_woe_magic_tab', 'ocean_palace_elevator_magic_tab', 'ozzies_fort_guillotines_tab', 'proto_dome_portal_tab', 'northern_ruins_heros_grave_magic_tab', 'northern_ruins_landing_power_tab'}
    default = []


class GoodLootRate4(Range):
    """Percent chance to fill a good loot spot with good loot for pool 4"""
    display_name = "Good Loot Rate 4"
    range_start = 0
    range_end = 100
    default = 75


class GoodLoot5(OptionList):
    """Loot that is considered to be good for pool 5 (ignored by vanilla)"""
    display_name = "Good Loot 5"
    valid_keys = {'wood_sword', 'iron_blade', 'steelsaber', 'lode_sword', 'red_katana', 'flint_edge', 'dark_saber', 'aeon_blade', 'demon_edge', 'alloyblade', 'star_sword', 'vedicblade', 'kali_blade', 'shiva_edge', 'bolt_sword', 'slasher', 'bronze_bow', 'iron_bow', 'lode_bow', 'robin_bow', 'sage_bow', 'dream_bow', 'cometarrow', 'sonicarrow', 'valkerye', 'siren', 'air_gun', 'dart_gun', 'auto_gun', 'picomagnum', 'plasma_gun', 'ruby_gun', 'dream_gun', 'megablast', 'shock_wave', 'wondershot', 'graedus', 'tin_arm', 'hammer_arm', 'miragehand', 'stone_arm', 'doomfinger', 'magma_hand', 'megatonarm', 'big_hand', 'kaiser_arm', 'giga_arm', 'terra_arm', 'crisis_arm', 'bronzeedge', 'iron_sword', 'masamune_1', 'flashblade', 'pearl_edge', 'rune_blade', 'bravesword', 'masamune_2', 'demon_hit', 'fist', 'fist_2', 'fist_3', 'iron_fist', 'bronzefist', 'pacifist', 'darkscythe', 'hurricane', 'starscythe', 'doomsickle', 'mop', 'bent_sword', 'bent_hilt', 'swallow', 'slasher_2', 'rainbow', 'hide_tunic', 'karate_gi', 'bronzemail', 'maidensuit', 'iron_suit', 'titan_vest', 'gold_suit', 'ruby_vest', 'dark_mail', 'mist_robe', 'meso_mail', 'lumin_robe', 'flash_mail', 'lode_vest', 'aeon_suit', 'zodiaccape', 'nova_armor', 'prismdress', 'moon_armor', 'ruby_armor', 'ravenarmor', 'gloom_cape', 'white_mail', 'black_mail', 'blue_mail', 'red_mail', 'white_vest', 'black_vest', 'blue_vest', 'red_vest', 'taban_vest', 'taban_suit', 'hide_cap', 'bronzehelm', 'iron_helm', 'beret', 'gold_helm', 'rock_helm', 'ceratopper', 'glow_helm', 'lode_helm', 'aeon_helm', 'prism_helm', 'doom_helm', 'dark_helm', 'gloom_helm', 'safe_helm', 'taban_helm', 'sight_cap', 'memory_cap', 'time_hat', 'vigil_hat', 'ozziepants', 'haste_helm', 'rbow_helm', 'mermaidcap', 'bandana', 'ribbon', 'powerglove', 'defender', 'magicscarf', 'amulet', 'dash_ring', 'hit_ring', 'power_ring', 'magic_ring', 'wall_ring', 'silvererng', 'gold_erng', 'silverstud', 'gold_stud', 'sightscope', 'charm_top', 'rage_band', 'frenzyband', 'third_eye', 'wallet', 'greendream', 'berserker', 'powerscarf', 'speed_belt', 'black_rock', 'blue_rock', 'silverrock', 'white_rock', 'gold_rock', 'hero_medal', 'musclering', 'flea_vest', 'magic_seal', 'power_seal', 'valor_crest', 'dragon_tear', 'sun_shades', 'prismspecs', 'tonic', 'mid_tonic', 'full_tonic', 'ether', 'mid_ether', 'full_ether', 'elixir', 'hyperether', 'megaelixir', 'heal', 'revive', 'shelter', 'power_meal', 'lapis', 'barrier', 'shield', 'power_tab', 'magic_tab', 'speed_tab', 'petal', 'fang', 'horn', 'feather', 'seed', 'bike_key', 'pendant', 'gate_key', 'prismshard', 'c_trigger', 'tools', 'jerky', 'dreamstone', 'race_log', 'moon_stone', 'sun_stone', 'ruby_knife', 'yakra_key', 'clone', 'tomas_pop', 'petals_2', 'fangs_2', 'horns_2', 'feathers_2', 'jetsoftime', 'pendant_charge', 'rainbow_shell'}
    default = []


class GoodLootSpots5(OptionList):
    """Spots for pool 5 which will be given a random good reward (ignored by vanilla)"""
    display_name = "Good Loot Spots 5"
    valid_keys = {'mt_woe_1st_screen', 'mt_woe_2nd_screen_1', 'mt_woe_2nd_screen_2', 'mt_woe_2nd_screen_3', 'mt_woe_2nd_screen_4', 'mt_woe_2nd_screen_5', 'mt_woe_3rd_screen_1', 'mt_woe_3rd_screen_2', 'mt_woe_3rd_screen_3', 'mt_woe_3rd_screen_4', 'mt_woe_3rd_screen_5', 'mt_woe_final_1', 'mt_woe_final_2', 'mt_woe_key', 'fiona_key', 'arris_dome_rats', 'arris_dome_food_store', 'arris_dome_doan_key', 'arris_dome_food_locker_key', 'sun_palace_key', 'sewers_1', 'sewers_2', 'sewers_3', 'lab_16_1', 'lab_16_2', 'lab_16_3', 'lab_16_4', 'lab_32_1', 'prison_tower_1000', 'geno_dome_1f_1', 'geno_dome_1f_2', 'geno_dome_1f_3', 'geno_dome_1f_4', 'geno_dome_room_1', 'geno_dome_room_2', 'geno_dome_proto4_1', 'geno_dome_proto4_2', 'geno_dome_2f_1', 'geno_dome_2f_2', 'geno_dome_2f_3', 'geno_dome_2f_4', 'geno_dome_boss_1', 'geno_dome_boss_2', 'factory_left_aux_console', 'factory_left_security_right', 'factory_left_security_left', 'factory_right_data_core_1', 'factory_right_data_core_2', 'factory_right_floor_top', 'factory_right_floor_left', 'factory_right_floor_bottom', 'factory_right_floor_secret', 'factory_right_crane_lower', 'factory_right_crane_upper', 'factory_right_info_archive', 'giants_claw_traps', 'giants_claw_caves_1', 'giants_claw_caves_2', 'giants_claw_caves_3', 'giants_claw_caves_4', 'giants_claw_caves_5', 'giants_claw_rock', 'giants_claw_key', 'northern_ruins_antechamber_left_600', 'northern_ruins_antechamber_sealed_600', 'northern_ruins_antechamber_left_1000', 'northern_ruins_antechamber_sealed_1000', 'northern_ruins_back_left_sealed_600', 'northern_ruins_back_right_sealed_600', 'northern_ruins_back_left_sealed_1000', 'northern_ruins_back_right_sealed_1000', 'northern_ruins_basement_600', 'northern_ruins_basement_1000', 'guardia_basement_1', 'guardia_basement_2', 'guardia_basement_3', 'guardia_treasury_1', 'guardia_treasury_2', 'guardia_treasury_3', 'kings_trial_key', 'ozzies_fort_guillotines_1', 'ozzies_fort_guillotines_2', 'ozzies_fort_guillotines_3', 'ozzies_fort_guillotines_4', 'ozzies_fort_final_1', 'ozzies_fort_final_2', 'truce_mayor_1f', 'truce_mayor_2f', 'forest_ruins', 'porre_mayor_2f', 'truce_canyon_1', 'truce_canyon_2', 'fionas_house_1', 'fionas_house_2', 'cursed_woods_1', 'cursed_woods_2', 'frogs_burrow_right', 'zenan_bridge_chef', 'zenan_bridge_chef_tab', 'zenan_bridge_captain', 'snail_stop_key', 'lazy_carpenter', 'heckran_cave_sidetrack', 'heckran_cave_entrance', 'heckran_cave_1', 'heckran_cave_2', 'taban_gift_vest', 'kings_room_1000', 'queens_room_1000', 'kings_room_600', 'queens_room_600', 'royal_kitchen', 'queens_tower_600', 'kings_tower_600', 'kings_tower_1000', 'queens_tower_1000', 'guardia_court_tower', 'manoria_cathedral_1', 'manoria_cathedral_2', 'manoria_cathedral_3', 'manoria_interior_1', 'manoria_interior_2', 'manoria_interior_3', 'manoria_interior_4', 'manoria_shrine_sideroom_1', 'manoria_shrine_sideroom_2', 'manoria_bromide_1', 'manoria_bromide_2', 'manoria_bromide_3', 'manoria_shrine_magus_1', 'manoria_shrine_magus_2', 'yakras_room', 'denadoro_mts_screen2_1', 'denadoro_mts_screen2_2', 'denadoro_mts_screen2_3', 'denadoro_mts_final_1', 'denadoro_mts_final_2', 'denadoro_mts_final_3', 'denadoro_mts_waterfall_top_1', 'denadoro_mts_waterfall_top_2', 'denadoro_mts_waterfall_top_3', 'denadoro_mts_waterfall_top_4', 'denadoro_mts_waterfall_top_5', 'denadoro_mts_entrance_1', 'denadoro_mts_entrance_2', 'denadoro_mts_screen3_1', 'denadoro_mts_screen3_2', 'denadoro_mts_screen3_3', 'denadoro_mts_screen3_4', 'denadoro_mts_ambush', 'denadoro_mts_save_pt', 'denadoro_mts_key', 'bangor_dome_seal_1', 'bangor_dome_seal_2', 'bangor_dome_seal_3', 'trann_dome_seal_1', 'trann_dome_seal_2', 'arris_dome_seal_1', 'arris_dome_seal_2', 'arris_dome_seal_3', 'arris_dome_seal_4', 'truce_inn_sealed_600', 'porre_elder_sealed_1', 'porre_elder_sealed_2', 'guardia_castle_sealed_600', 'guardia_forest_sealed_600', 'truce_inn_sealed_1000', 'porre_mayor_sealed_1', 'porre_mayor_sealed_2', 'guardia_forest_sealed_1000', 'guardia_castle_sealed_1000', 'heckran_sealed_1', 'heckran_sealed_2', 'pyramid_left', 'pyramid_right', 'magic_cave_sealed', 'mystic_mt_stream', 'forest_maze_1', 'forest_maze_2', 'forest_maze_3', 'forest_maze_4', 'forest_maze_5', 'forest_maze_6', 'forest_maze_7', 'forest_maze_8', 'forest_maze_9', 'reptite_lair_reptites_1', 'reptite_lair_reptites_2', 'reptite_lair_key', 'dactyl_nest_1', 'dactyl_nest_2', 'dactyl_nest_3', 'melchior_rainbow_shell', 'melchior_sunstone_rainbow', 'melchior_sunstone_specs', 'frogs_burrow_left', 'guardia_jail_fritz_storage', 'guardia_jail_cell', 'guardia_jail_omnicrone_1', 'guardia_jail_omnicrone_2', 'guardia_jail_omnicrone_3', 'guardia_jail_hole_1', 'guardia_jail_hole_2', 'guardia_jail_outer_wall', 'guardia_jail_omnicrone_4', 'guardia_jail_fritz', 'magus_castle_right_hall', 'sunken_desert_b1_nw', 'sunken_desert_b1_ne', 'sunken_desert_b1_se', 'sunken_desert_b1_sw', 'sunken_desert_b2_nw', 'sunken_desert_b2_n', 'sunken_desert_b2_w', 'sunken_desert_b2_sw', 'sunken_desert_b2_se', 'sunken_desert_b2_e', 'sunken_desert_b2_center', 'magus_castle_guillotine_1', 'magus_castle_guillotine_2', 'magus_castle_slash_room_1', 'magus_castle_slash_room_2', 'magus_castle_statue_hall', 'magus_castle_four_kids', 'magus_castle_ozzie_1', 'magus_castle_ozzie_2', 'magus_castle_enemy_elevator', 'reptite_lair_secret_b2_ne_right', 'lab_32_race_log', 'factory_ruins_generator', 'death_peak_south_face_krakker', 'death_peak_south_face_spawn_save', 'death_peak_south_face_summit', 'death_peak_field', 'death_peak_krakker_parade', 'death_peak_caves_left', 'death_peak_caves_center', 'death_peak_caves_right', 'reptite_lair_secret_b1_sw', 'reptite_lair_secret_b1_ne', 'reptite_lair_secret_b1_se', 'reptite_lair_secret_b2_se_right', 'reptite_lair_secret_b2_ne_or_se_left', 'reptite_lair_secret_b2_sw', 'tyrano_lair_throne_1', 'tyrano_lair_throne_2', 'tyrano_lair_trapdoor', 'tyrano_lair_kino_cell', 'tyrano_lair_maze_1', 'tyrano_lair_maze_2', 'tyrano_lair_maze_3', 'tyrano_lair_maze_4', 'black_omen_aux_command_mid', 'black_omen_aux_command_ne', 'black_omen_grand_hall', 'black_omen_nu_hall_nw', 'black_omen_nu_hall_w', 'black_omen_nu_hall_sw', 'black_omen_nu_hall_ne', 'black_omen_nu_hall_e', 'black_omen_nu_hall_se', 'black_omen_royal_path', 'black_omen_ruminator_parade', 'black_omen_eyeball_hall', 'black_omen_tubster_fly', 'black_omen_martello', 'black_omen_alien_sw', 'black_omen_alien_ne', 'black_omen_alien_nw', 'black_omen_terra_w', 'black_omen_terra_rock', 'black_omen_terra_ne', 'ocean_palace_main_s', 'ocean_palace_main_n', 'ocean_palace_e_room', 'ocean_palace_w_room', 'ocean_palace_switch_nw', 'ocean_palace_switch_sw', 'ocean_palace_switch_ne', 'ocean_palace_switch_secret', 'ocean_palace_final', 'magus_castle_left_hall', 'magus_castle_unskippables', 'magus_castle_pit_e', 'magus_castle_pit_ne', 'magus_castle_pit_nw', 'magus_castle_pit_w', 'taban_gift_suit', 'taban_gift_helm', 'trading_post_petal_fang_base', 'trading_post_petal_fang_upgrade', 'trading_post_petal_horn_base', 'trading_post_petal_horn_upgrade', 'trading_post_petal_feather_base', 'trading_post_petal_feather_upgrade', 'trading_post_fang_horn_base', 'trading_post_fang_horn_upgrade', 'trading_post_fang_feather_base', 'trading_post_fang_feather_upgrade', 'trading_post_horn_feather_base', 'trading_post_horn_feather_upgrade', 'trading_post_special', 'jerky_gift', 'denadoro_rock', 'kajar_rock', 'laruba_rock', 'bekkler_key', 'cyrus_grave_key', 'sun_keep_2300', 'lucca_wondershot', 'taban_sunshades', 'fair_pendant', 'tata_reward', 'toma_reward', 'melchior_forge_masa', 'eot_gaspar_reward', 'hunting_range_nu_reward', 'zeal_mammon_machine', 'magus_castle_slash_sword_floor', 'guardia_prison_lunch_bag', 'cronos_mom', 'truce_mayor_2f_old_man', 'ioka_sweetwater_tonic', 'dorino_inn_powermeal', 'yakra_key_chest', 'courtroom_yakra_key', 'johnny_race_power_tab', 'guardia_forest_power_tab_600', 'guardia_forest_power_tab_1000', 'manoria_confinement_power_tab', 'dorino_bromide_magic_tab', 'porre_market_600_power_tab', 'denadoro_mts_speed_tab', 'tomas_grave_speed_tab', 'giants_claw_caverns_power_tab', 'giants_claw_entrance_power_tab', 'giants_claw_traps_power_tab', 'sun_keep_600_power_tab', 'medina_elder_speed_tab', 'medina_elder_magic_tab', 'magus_castle_flea_magic_tab', 'magus_castle_dungeons_magic_tab', 'trann_dome_sealed_magic_tab', 'arris_dome_sealed_power_tab', 'keepers_dome_magic_tab', 'death_peak_power_tab', 'blackbird_ducts_magic_tab', 'geno_dome_atropos_magic_tab', 'geno_dome_corridor_power_tab', 'geno_dome_labs_magic_tab', 'geno_dome_labs_speed_tab', 'enhasa_nu_battle_magic_tab', 'enhasa_nu_battle_speed_tab', 'kajar_speed_tab', 'kajar_nu_scratch_magic_tab', 'last_village_nu_shop_magic_tab', 'sunken_desert_power_tab', 'mountains_re_nice_magic_tab', 'beast_nest_power_tab', 'mt_woe_magic_tab', 'ocean_palace_elevator_magic_tab', 'ozzies_fort_guillotines_tab', 'proto_dome_portal_tab', 'northern_ruins_heros_grave_magic_tab', 'northern_ruins_landing_power_tab'}
    default = []


class GoodLootRate5(Range):
    """Percent chance to fill a good loot spot with good loot for pool 5"""
    display_name = "Good Loot Rate 5"
    range_start = 0
    range_end = 100
    default = 75


class GoodLoot6(OptionList):
    """Loot that is considered to be good for pool 6 (ignored by vanilla)"""
    display_name = "Good Loot 6"
    valid_keys = {'wood_sword', 'iron_blade', 'steelsaber', 'lode_sword', 'red_katana', 'flint_edge', 'dark_saber', 'aeon_blade', 'demon_edge', 'alloyblade', 'star_sword', 'vedicblade', 'kali_blade', 'shiva_edge', 'bolt_sword', 'slasher', 'bronze_bow', 'iron_bow', 'lode_bow', 'robin_bow', 'sage_bow', 'dream_bow', 'cometarrow', 'sonicarrow', 'valkerye', 'siren', 'air_gun', 'dart_gun', 'auto_gun', 'picomagnum', 'plasma_gun', 'ruby_gun', 'dream_gun', 'megablast', 'shock_wave', 'wondershot', 'graedus', 'tin_arm', 'hammer_arm', 'miragehand', 'stone_arm', 'doomfinger', 'magma_hand', 'megatonarm', 'big_hand', 'kaiser_arm', 'giga_arm', 'terra_arm', 'crisis_arm', 'bronzeedge', 'iron_sword', 'masamune_1', 'flashblade', 'pearl_edge', 'rune_blade', 'bravesword', 'masamune_2', 'demon_hit', 'fist', 'fist_2', 'fist_3', 'iron_fist', 'bronzefist', 'pacifist', 'darkscythe', 'hurricane', 'starscythe', 'doomsickle', 'mop', 'bent_sword', 'bent_hilt', 'swallow', 'slasher_2', 'rainbow', 'hide_tunic', 'karate_gi', 'bronzemail', 'maidensuit', 'iron_suit', 'titan_vest', 'gold_suit', 'ruby_vest', 'dark_mail', 'mist_robe', 'meso_mail', 'lumin_robe', 'flash_mail', 'lode_vest', 'aeon_suit', 'zodiaccape', 'nova_armor', 'prismdress', 'moon_armor', 'ruby_armor', 'ravenarmor', 'gloom_cape', 'white_mail', 'black_mail', 'blue_mail', 'red_mail', 'white_vest', 'black_vest', 'blue_vest', 'red_vest', 'taban_vest', 'taban_suit', 'hide_cap', 'bronzehelm', 'iron_helm', 'beret', 'gold_helm', 'rock_helm', 'ceratopper', 'glow_helm', 'lode_helm', 'aeon_helm', 'prism_helm', 'doom_helm', 'dark_helm', 'gloom_helm', 'safe_helm', 'taban_helm', 'sight_cap', 'memory_cap', 'time_hat', 'vigil_hat', 'ozziepants', 'haste_helm', 'rbow_helm', 'mermaidcap', 'bandana', 'ribbon', 'powerglove', 'defender', 'magicscarf', 'amulet', 'dash_ring', 'hit_ring', 'power_ring', 'magic_ring', 'wall_ring', 'silvererng', 'gold_erng', 'silverstud', 'gold_stud', 'sightscope', 'charm_top', 'rage_band', 'frenzyband', 'third_eye', 'wallet', 'greendream', 'berserker', 'powerscarf', 'speed_belt', 'black_rock', 'blue_rock', 'silverrock', 'white_rock', 'gold_rock', 'hero_medal', 'musclering', 'flea_vest', 'magic_seal', 'power_seal', 'valor_crest', 'dragon_tear', 'sun_shades', 'prismspecs', 'tonic', 'mid_tonic', 'full_tonic', 'ether', 'mid_ether', 'full_ether', 'elixir', 'hyperether', 'megaelixir', 'heal', 'revive', 'shelter', 'power_meal', 'lapis', 'barrier', 'shield', 'power_tab', 'magic_tab', 'speed_tab', 'petal', 'fang', 'horn', 'feather', 'seed', 'bike_key', 'pendant', 'gate_key', 'prismshard', 'c_trigger', 'tools', 'jerky', 'dreamstone', 'race_log', 'moon_stone', 'sun_stone', 'ruby_knife', 'yakra_key', 'clone', 'tomas_pop', 'petals_2', 'fangs_2', 'horns_2', 'feathers_2', 'jetsoftime', 'pendant_charge', 'rainbow_shell'}
    default = []


class GoodLootSpots6(OptionList):
    """Spots for pool 6 which will be given a random good reward (ignored by vanilla)"""
    display_name = "Good Loot Spots 6"
    valid_keys = {'mt_woe_1st_screen', 'mt_woe_2nd_screen_1', 'mt_woe_2nd_screen_2', 'mt_woe_2nd_screen_3', 'mt_woe_2nd_screen_4', 'mt_woe_2nd_screen_5', 'mt_woe_3rd_screen_1', 'mt_woe_3rd_screen_2', 'mt_woe_3rd_screen_3', 'mt_woe_3rd_screen_4', 'mt_woe_3rd_screen_5', 'mt_woe_final_1', 'mt_woe_final_2', 'mt_woe_key', 'fiona_key', 'arris_dome_rats', 'arris_dome_food_store', 'arris_dome_doan_key', 'arris_dome_food_locker_key', 'sun_palace_key', 'sewers_1', 'sewers_2', 'sewers_3', 'lab_16_1', 'lab_16_2', 'lab_16_3', 'lab_16_4', 'lab_32_1', 'prison_tower_1000', 'geno_dome_1f_1', 'geno_dome_1f_2', 'geno_dome_1f_3', 'geno_dome_1f_4', 'geno_dome_room_1', 'geno_dome_room_2', 'geno_dome_proto4_1', 'geno_dome_proto4_2', 'geno_dome_2f_1', 'geno_dome_2f_2', 'geno_dome_2f_3', 'geno_dome_2f_4', 'geno_dome_boss_1', 'geno_dome_boss_2', 'factory_left_aux_console', 'factory_left_security_right', 'factory_left_security_left', 'factory_right_data_core_1', 'factory_right_data_core_2', 'factory_right_floor_top', 'factory_right_floor_left', 'factory_right_floor_bottom', 'factory_right_floor_secret', 'factory_right_crane_lower', 'factory_right_crane_upper', 'factory_right_info_archive', 'giants_claw_traps', 'giants_claw_caves_1', 'giants_claw_caves_2', 'giants_claw_caves_3', 'giants_claw_caves_4', 'giants_claw_caves_5', 'giants_claw_rock', 'giants_claw_key', 'northern_ruins_antechamber_left_600', 'northern_ruins_antechamber_sealed_600', 'northern_ruins_antechamber_left_1000', 'northern_ruins_antechamber_sealed_1000', 'northern_ruins_back_left_sealed_600', 'northern_ruins_back_right_sealed_600', 'northern_ruins_back_left_sealed_1000', 'northern_ruins_back_right_sealed_1000', 'northern_ruins_basement_600', 'northern_ruins_basement_1000', 'guardia_basement_1', 'guardia_basement_2', 'guardia_basement_3', 'guardia_treasury_1', 'guardia_treasury_2', 'guardia_treasury_3', 'kings_trial_key', 'ozzies_fort_guillotines_1', 'ozzies_fort_guillotines_2', 'ozzies_fort_guillotines_3', 'ozzies_fort_guillotines_4', 'ozzies_fort_final_1', 'ozzies_fort_final_2', 'truce_mayor_1f', 'truce_mayor_2f', 'forest_ruins', 'porre_mayor_2f', 'truce_canyon_1', 'truce_canyon_2', 'fionas_house_1', 'fionas_house_2', 'cursed_woods_1', 'cursed_woods_2', 'frogs_burrow_right', 'zenan_bridge_chef', 'zenan_bridge_chef_tab', 'zenan_bridge_captain', 'snail_stop_key', 'lazy_carpenter', 'heckran_cave_sidetrack', 'heckran_cave_entrance', 'heckran_cave_1', 'heckran_cave_2', 'taban_gift_vest', 'kings_room_1000', 'queens_room_1000', 'kings_room_600', 'queens_room_600', 'royal_kitchen', 'queens_tower_600', 'kings_tower_600', 'kings_tower_1000', 'queens_tower_1000', 'guardia_court_tower', 'manoria_cathedral_1', 'manoria_cathedral_2', 'manoria_cathedral_3', 'manoria_interior_1', 'manoria_interior_2', 'manoria_interior_3', 'manoria_interior_4', 'manoria_shrine_sideroom_1', 'manoria_shrine_sideroom_2', 'manoria_bromide_1', 'manoria_bromide_2', 'manoria_bromide_3', 'manoria_shrine_magus_1', 'manoria_shrine_magus_2', 'yakras_room', 'denadoro_mts_screen2_1', 'denadoro_mts_screen2_2', 'denadoro_mts_screen2_3', 'denadoro_mts_final_1', 'denadoro_mts_final_2', 'denadoro_mts_final_3', 'denadoro_mts_waterfall_top_1', 'denadoro_mts_waterfall_top_2', 'denadoro_mts_waterfall_top_3', 'denadoro_mts_waterfall_top_4', 'denadoro_mts_waterfall_top_5', 'denadoro_mts_entrance_1', 'denadoro_mts_entrance_2', 'denadoro_mts_screen3_1', 'denadoro_mts_screen3_2', 'denadoro_mts_screen3_3', 'denadoro_mts_screen3_4', 'denadoro_mts_ambush', 'denadoro_mts_save_pt', 'denadoro_mts_key', 'bangor_dome_seal_1', 'bangor_dome_seal_2', 'bangor_dome_seal_3', 'trann_dome_seal_1', 'trann_dome_seal_2', 'arris_dome_seal_1', 'arris_dome_seal_2', 'arris_dome_seal_3', 'arris_dome_seal_4', 'truce_inn_sealed_600', 'porre_elder_sealed_1', 'porre_elder_sealed_2', 'guardia_castle_sealed_600', 'guardia_forest_sealed_600', 'truce_inn_sealed_1000', 'porre_mayor_sealed_1', 'porre_mayor_sealed_2', 'guardia_forest_sealed_1000', 'guardia_castle_sealed_1000', 'heckran_sealed_1', 'heckran_sealed_2', 'pyramid_left', 'pyramid_right', 'magic_cave_sealed', 'mystic_mt_stream', 'forest_maze_1', 'forest_maze_2', 'forest_maze_3', 'forest_maze_4', 'forest_maze_5', 'forest_maze_6', 'forest_maze_7', 'forest_maze_8', 'forest_maze_9', 'reptite_lair_reptites_1', 'reptite_lair_reptites_2', 'reptite_lair_key', 'dactyl_nest_1', 'dactyl_nest_2', 'dactyl_nest_3', 'melchior_rainbow_shell', 'melchior_sunstone_rainbow', 'melchior_sunstone_specs', 'frogs_burrow_left', 'guardia_jail_fritz_storage', 'guardia_jail_cell', 'guardia_jail_omnicrone_1', 'guardia_jail_omnicrone_2', 'guardia_jail_omnicrone_3', 'guardia_jail_hole_1', 'guardia_jail_hole_2', 'guardia_jail_outer_wall', 'guardia_jail_omnicrone_4', 'guardia_jail_fritz', 'magus_castle_right_hall', 'sunken_desert_b1_nw', 'sunken_desert_b1_ne', 'sunken_desert_b1_se', 'sunken_desert_b1_sw', 'sunken_desert_b2_nw', 'sunken_desert_b2_n', 'sunken_desert_b2_w', 'sunken_desert_b2_sw', 'sunken_desert_b2_se', 'sunken_desert_b2_e', 'sunken_desert_b2_center', 'magus_castle_guillotine_1', 'magus_castle_guillotine_2', 'magus_castle_slash_room_1', 'magus_castle_slash_room_2', 'magus_castle_statue_hall', 'magus_castle_four_kids', 'magus_castle_ozzie_1', 'magus_castle_ozzie_2', 'magus_castle_enemy_elevator', 'reptite_lair_secret_b2_ne_right', 'lab_32_race_log', 'factory_ruins_generator', 'death_peak_south_face_krakker', 'death_peak_south_face_spawn_save', 'death_peak_south_face_summit', 'death_peak_field', 'death_peak_krakker_parade', 'death_peak_caves_left', 'death_peak_caves_center', 'death_peak_caves_right', 'reptite_lair_secret_b1_sw', 'reptite_lair_secret_b1_ne', 'reptite_lair_secret_b1_se', 'reptite_lair_secret_b2_se_right', 'reptite_lair_secret_b2_ne_or_se_left', 'reptite_lair_secret_b2_sw', 'tyrano_lair_throne_1', 'tyrano_lair_throne_2', 'tyrano_lair_trapdoor', 'tyrano_lair_kino_cell', 'tyrano_lair_maze_1', 'tyrano_lair_maze_2', 'tyrano_lair_maze_3', 'tyrano_lair_maze_4', 'black_omen_aux_command_mid', 'black_omen_aux_command_ne', 'black_omen_grand_hall', 'black_omen_nu_hall_nw', 'black_omen_nu_hall_w', 'black_omen_nu_hall_sw', 'black_omen_nu_hall_ne', 'black_omen_nu_hall_e', 'black_omen_nu_hall_se', 'black_omen_royal_path', 'black_omen_ruminator_parade', 'black_omen_eyeball_hall', 'black_omen_tubster_fly', 'black_omen_martello', 'black_omen_alien_sw', 'black_omen_alien_ne', 'black_omen_alien_nw', 'black_omen_terra_w', 'black_omen_terra_rock', 'black_omen_terra_ne', 'ocean_palace_main_s', 'ocean_palace_main_n', 'ocean_palace_e_room', 'ocean_palace_w_room', 'ocean_palace_switch_nw', 'ocean_palace_switch_sw', 'ocean_palace_switch_ne', 'ocean_palace_switch_secret', 'ocean_palace_final', 'magus_castle_left_hall', 'magus_castle_unskippables', 'magus_castle_pit_e', 'magus_castle_pit_ne', 'magus_castle_pit_nw', 'magus_castle_pit_w', 'taban_gift_suit', 'taban_gift_helm', 'trading_post_petal_fang_base', 'trading_post_petal_fang_upgrade', 'trading_post_petal_horn_base', 'trading_post_petal_horn_upgrade', 'trading_post_petal_feather_base', 'trading_post_petal_feather_upgrade', 'trading_post_fang_horn_base', 'trading_post_fang_horn_upgrade', 'trading_post_fang_feather_base', 'trading_post_fang_feather_upgrade', 'trading_post_horn_feather_base', 'trading_post_horn_feather_upgrade', 'trading_post_special', 'jerky_gift', 'denadoro_rock', 'kajar_rock', 'laruba_rock', 'bekkler_key', 'cyrus_grave_key', 'sun_keep_2300', 'lucca_wondershot', 'taban_sunshades', 'fair_pendant', 'tata_reward', 'toma_reward', 'melchior_forge_masa', 'eot_gaspar_reward', 'hunting_range_nu_reward', 'zeal_mammon_machine', 'magus_castle_slash_sword_floor', 'guardia_prison_lunch_bag', 'cronos_mom', 'truce_mayor_2f_old_man', 'ioka_sweetwater_tonic', 'dorino_inn_powermeal', 'yakra_key_chest', 'courtroom_yakra_key', 'johnny_race_power_tab', 'guardia_forest_power_tab_600', 'guardia_forest_power_tab_1000', 'manoria_confinement_power_tab', 'dorino_bromide_magic_tab', 'porre_market_600_power_tab', 'denadoro_mts_speed_tab', 'tomas_grave_speed_tab', 'giants_claw_caverns_power_tab', 'giants_claw_entrance_power_tab', 'giants_claw_traps_power_tab', 'sun_keep_600_power_tab', 'medina_elder_speed_tab', 'medina_elder_magic_tab', 'magus_castle_flea_magic_tab', 'magus_castle_dungeons_magic_tab', 'trann_dome_sealed_magic_tab', 'arris_dome_sealed_power_tab', 'keepers_dome_magic_tab', 'death_peak_power_tab', 'blackbird_ducts_magic_tab', 'geno_dome_atropos_magic_tab', 'geno_dome_corridor_power_tab', 'geno_dome_labs_magic_tab', 'geno_dome_labs_speed_tab', 'enhasa_nu_battle_magic_tab', 'enhasa_nu_battle_speed_tab', 'kajar_speed_tab', 'kajar_nu_scratch_magic_tab', 'last_village_nu_shop_magic_tab', 'sunken_desert_power_tab', 'mountains_re_nice_magic_tab', 'beast_nest_power_tab', 'mt_woe_magic_tab', 'ocean_palace_elevator_magic_tab', 'ozzies_fort_guillotines_tab', 'proto_dome_portal_tab', 'northern_ruins_heros_grave_magic_tab', 'northern_ruins_landing_power_tab'}
    default = []


class GoodLootRate6(Range):
    """Percent chance to fill a good loot spot with good loot for pool 6"""
    display_name = "Good Loot Rate 6"
    range_start = 0
    range_end = 100
    default = 75


class GoodLoot7(OptionList):
    """Loot that is considered to be good for pool 7 (ignored by vanilla)"""
    display_name = "Good Loot 7"
    valid_keys = {'wood_sword', 'iron_blade', 'steelsaber', 'lode_sword', 'red_katana', 'flint_edge', 'dark_saber', 'aeon_blade', 'demon_edge', 'alloyblade', 'star_sword', 'vedicblade', 'kali_blade', 'shiva_edge', 'bolt_sword', 'slasher', 'bronze_bow', 'iron_bow', 'lode_bow', 'robin_bow', 'sage_bow', 'dream_bow', 'cometarrow', 'sonicarrow', 'valkerye', 'siren', 'air_gun', 'dart_gun', 'auto_gun', 'picomagnum', 'plasma_gun', 'ruby_gun', 'dream_gun', 'megablast', 'shock_wave', 'wondershot', 'graedus', 'tin_arm', 'hammer_arm', 'miragehand', 'stone_arm', 'doomfinger', 'magma_hand', 'megatonarm', 'big_hand', 'kaiser_arm', 'giga_arm', 'terra_arm', 'crisis_arm', 'bronzeedge', 'iron_sword', 'masamune_1', 'flashblade', 'pearl_edge', 'rune_blade', 'bravesword', 'masamune_2', 'demon_hit', 'fist', 'fist_2', 'fist_3', 'iron_fist', 'bronzefist', 'pacifist', 'darkscythe', 'hurricane', 'starscythe', 'doomsickle', 'mop', 'bent_sword', 'bent_hilt', 'swallow', 'slasher_2', 'rainbow', 'hide_tunic', 'karate_gi', 'bronzemail', 'maidensuit', 'iron_suit', 'titan_vest', 'gold_suit', 'ruby_vest', 'dark_mail', 'mist_robe', 'meso_mail', 'lumin_robe', 'flash_mail', 'lode_vest', 'aeon_suit', 'zodiaccape', 'nova_armor', 'prismdress', 'moon_armor', 'ruby_armor', 'ravenarmor', 'gloom_cape', 'white_mail', 'black_mail', 'blue_mail', 'red_mail', 'white_vest', 'black_vest', 'blue_vest', 'red_vest', 'taban_vest', 'taban_suit', 'hide_cap', 'bronzehelm', 'iron_helm', 'beret', 'gold_helm', 'rock_helm', 'ceratopper', 'glow_helm', 'lode_helm', 'aeon_helm', 'prism_helm', 'doom_helm', 'dark_helm', 'gloom_helm', 'safe_helm', 'taban_helm', 'sight_cap', 'memory_cap', 'time_hat', 'vigil_hat', 'ozziepants', 'haste_helm', 'rbow_helm', 'mermaidcap', 'bandana', 'ribbon', 'powerglove', 'defender', 'magicscarf', 'amulet', 'dash_ring', 'hit_ring', 'power_ring', 'magic_ring', 'wall_ring', 'silvererng', 'gold_erng', 'silverstud', 'gold_stud', 'sightscope', 'charm_top', 'rage_band', 'frenzyband', 'third_eye', 'wallet', 'greendream', 'berserker', 'powerscarf', 'speed_belt', 'black_rock', 'blue_rock', 'silverrock', 'white_rock', 'gold_rock', 'hero_medal', 'musclering', 'flea_vest', 'magic_seal', 'power_seal', 'valor_crest', 'dragon_tear', 'sun_shades', 'prismspecs', 'tonic', 'mid_tonic', 'full_tonic', 'ether', 'mid_ether', 'full_ether', 'elixir', 'hyperether', 'megaelixir', 'heal', 'revive', 'shelter', 'power_meal', 'lapis', 'barrier', 'shield', 'power_tab', 'magic_tab', 'speed_tab', 'petal', 'fang', 'horn', 'feather', 'seed', 'bike_key', 'pendant', 'gate_key', 'prismshard', 'c_trigger', 'tools', 'jerky', 'dreamstone', 'race_log', 'moon_stone', 'sun_stone', 'ruby_knife', 'yakra_key', 'clone', 'tomas_pop', 'petals_2', 'fangs_2', 'horns_2', 'feathers_2', 'jetsoftime', 'pendant_charge', 'rainbow_shell'}
    default = []


class GoodLootSpots7(OptionList):
    """Spots for pool 7 which will be given a random good reward (ignored by vanilla)"""
    display_name = "Good Loot Spots 7"
    valid_keys = {'mt_woe_1st_screen', 'mt_woe_2nd_screen_1', 'mt_woe_2nd_screen_2', 'mt_woe_2nd_screen_3', 'mt_woe_2nd_screen_4', 'mt_woe_2nd_screen_5', 'mt_woe_3rd_screen_1', 'mt_woe_3rd_screen_2', 'mt_woe_3rd_screen_3', 'mt_woe_3rd_screen_4', 'mt_woe_3rd_screen_5', 'mt_woe_final_1', 'mt_woe_final_2', 'mt_woe_key', 'fiona_key', 'arris_dome_rats', 'arris_dome_food_store', 'arris_dome_doan_key', 'arris_dome_food_locker_key', 'sun_palace_key', 'sewers_1', 'sewers_2', 'sewers_3', 'lab_16_1', 'lab_16_2', 'lab_16_3', 'lab_16_4', 'lab_32_1', 'prison_tower_1000', 'geno_dome_1f_1', 'geno_dome_1f_2', 'geno_dome_1f_3', 'geno_dome_1f_4', 'geno_dome_room_1', 'geno_dome_room_2', 'geno_dome_proto4_1', 'geno_dome_proto4_2', 'geno_dome_2f_1', 'geno_dome_2f_2', 'geno_dome_2f_3', 'geno_dome_2f_4', 'geno_dome_boss_1', 'geno_dome_boss_2', 'factory_left_aux_console', 'factory_left_security_right', 'factory_left_security_left', 'factory_right_data_core_1', 'factory_right_data_core_2', 'factory_right_floor_top', 'factory_right_floor_left', 'factory_right_floor_bottom', 'factory_right_floor_secret', 'factory_right_crane_lower', 'factory_right_crane_upper', 'factory_right_info_archive', 'giants_claw_traps', 'giants_claw_caves_1', 'giants_claw_caves_2', 'giants_claw_caves_3', 'giants_claw_caves_4', 'giants_claw_caves_5', 'giants_claw_rock', 'giants_claw_key', 'northern_ruins_antechamber_left_600', 'northern_ruins_antechamber_sealed_600', 'northern_ruins_antechamber_left_1000', 'northern_ruins_antechamber_sealed_1000', 'northern_ruins_back_left_sealed_600', 'northern_ruins_back_right_sealed_600', 'northern_ruins_back_left_sealed_1000', 'northern_ruins_back_right_sealed_1000', 'northern_ruins_basement_600', 'northern_ruins_basement_1000', 'guardia_basement_1', 'guardia_basement_2', 'guardia_basement_3', 'guardia_treasury_1', 'guardia_treasury_2', 'guardia_treasury_3', 'kings_trial_key', 'ozzies_fort_guillotines_1', 'ozzies_fort_guillotines_2', 'ozzies_fort_guillotines_3', 'ozzies_fort_guillotines_4', 'ozzies_fort_final_1', 'ozzies_fort_final_2', 'truce_mayor_1f', 'truce_mayor_2f', 'forest_ruins', 'porre_mayor_2f', 'truce_canyon_1', 'truce_canyon_2', 'fionas_house_1', 'fionas_house_2', 'cursed_woods_1', 'cursed_woods_2', 'frogs_burrow_right', 'zenan_bridge_chef', 'zenan_bridge_chef_tab', 'zenan_bridge_captain', 'snail_stop_key', 'lazy_carpenter', 'heckran_cave_sidetrack', 'heckran_cave_entrance', 'heckran_cave_1', 'heckran_cave_2', 'taban_gift_vest', 'kings_room_1000', 'queens_room_1000', 'kings_room_600', 'queens_room_600', 'royal_kitchen', 'queens_tower_600', 'kings_tower_600', 'kings_tower_1000', 'queens_tower_1000', 'guardia_court_tower', 'manoria_cathedral_1', 'manoria_cathedral_2', 'manoria_cathedral_3', 'manoria_interior_1', 'manoria_interior_2', 'manoria_interior_3', 'manoria_interior_4', 'manoria_shrine_sideroom_1', 'manoria_shrine_sideroom_2', 'manoria_bromide_1', 'manoria_bromide_2', 'manoria_bromide_3', 'manoria_shrine_magus_1', 'manoria_shrine_magus_2', 'yakras_room', 'denadoro_mts_screen2_1', 'denadoro_mts_screen2_2', 'denadoro_mts_screen2_3', 'denadoro_mts_final_1', 'denadoro_mts_final_2', 'denadoro_mts_final_3', 'denadoro_mts_waterfall_top_1', 'denadoro_mts_waterfall_top_2', 'denadoro_mts_waterfall_top_3', 'denadoro_mts_waterfall_top_4', 'denadoro_mts_waterfall_top_5', 'denadoro_mts_entrance_1', 'denadoro_mts_entrance_2', 'denadoro_mts_screen3_1', 'denadoro_mts_screen3_2', 'denadoro_mts_screen3_3', 'denadoro_mts_screen3_4', 'denadoro_mts_ambush', 'denadoro_mts_save_pt', 'denadoro_mts_key', 'bangor_dome_seal_1', 'bangor_dome_seal_2', 'bangor_dome_seal_3', 'trann_dome_seal_1', 'trann_dome_seal_2', 'arris_dome_seal_1', 'arris_dome_seal_2', 'arris_dome_seal_3', 'arris_dome_seal_4', 'truce_inn_sealed_600', 'porre_elder_sealed_1', 'porre_elder_sealed_2', 'guardia_castle_sealed_600', 'guardia_forest_sealed_600', 'truce_inn_sealed_1000', 'porre_mayor_sealed_1', 'porre_mayor_sealed_2', 'guardia_forest_sealed_1000', 'guardia_castle_sealed_1000', 'heckran_sealed_1', 'heckran_sealed_2', 'pyramid_left', 'pyramid_right', 'magic_cave_sealed', 'mystic_mt_stream', 'forest_maze_1', 'forest_maze_2', 'forest_maze_3', 'forest_maze_4', 'forest_maze_5', 'forest_maze_6', 'forest_maze_7', 'forest_maze_8', 'forest_maze_9', 'reptite_lair_reptites_1', 'reptite_lair_reptites_2', 'reptite_lair_key', 'dactyl_nest_1', 'dactyl_nest_2', 'dactyl_nest_3', 'melchior_rainbow_shell', 'melchior_sunstone_rainbow', 'melchior_sunstone_specs', 'frogs_burrow_left', 'guardia_jail_fritz_storage', 'guardia_jail_cell', 'guardia_jail_omnicrone_1', 'guardia_jail_omnicrone_2', 'guardia_jail_omnicrone_3', 'guardia_jail_hole_1', 'guardia_jail_hole_2', 'guardia_jail_outer_wall', 'guardia_jail_omnicrone_4', 'guardia_jail_fritz', 'magus_castle_right_hall', 'sunken_desert_b1_nw', 'sunken_desert_b1_ne', 'sunken_desert_b1_se', 'sunken_desert_b1_sw', 'sunken_desert_b2_nw', 'sunken_desert_b2_n', 'sunken_desert_b2_w', 'sunken_desert_b2_sw', 'sunken_desert_b2_se', 'sunken_desert_b2_e', 'sunken_desert_b2_center', 'magus_castle_guillotine_1', 'magus_castle_guillotine_2', 'magus_castle_slash_room_1', 'magus_castle_slash_room_2', 'magus_castle_statue_hall', 'magus_castle_four_kids', 'magus_castle_ozzie_1', 'magus_castle_ozzie_2', 'magus_castle_enemy_elevator', 'reptite_lair_secret_b2_ne_right', 'lab_32_race_log', 'factory_ruins_generator', 'death_peak_south_face_krakker', 'death_peak_south_face_spawn_save', 'death_peak_south_face_summit', 'death_peak_field', 'death_peak_krakker_parade', 'death_peak_caves_left', 'death_peak_caves_center', 'death_peak_caves_right', 'reptite_lair_secret_b1_sw', 'reptite_lair_secret_b1_ne', 'reptite_lair_secret_b1_se', 'reptite_lair_secret_b2_se_right', 'reptite_lair_secret_b2_ne_or_se_left', 'reptite_lair_secret_b2_sw', 'tyrano_lair_throne_1', 'tyrano_lair_throne_2', 'tyrano_lair_trapdoor', 'tyrano_lair_kino_cell', 'tyrano_lair_maze_1', 'tyrano_lair_maze_2', 'tyrano_lair_maze_3', 'tyrano_lair_maze_4', 'black_omen_aux_command_mid', 'black_omen_aux_command_ne', 'black_omen_grand_hall', 'black_omen_nu_hall_nw', 'black_omen_nu_hall_w', 'black_omen_nu_hall_sw', 'black_omen_nu_hall_ne', 'black_omen_nu_hall_e', 'black_omen_nu_hall_se', 'black_omen_royal_path', 'black_omen_ruminator_parade', 'black_omen_eyeball_hall', 'black_omen_tubster_fly', 'black_omen_martello', 'black_omen_alien_sw', 'black_omen_alien_ne', 'black_omen_alien_nw', 'black_omen_terra_w', 'black_omen_terra_rock', 'black_omen_terra_ne', 'ocean_palace_main_s', 'ocean_palace_main_n', 'ocean_palace_e_room', 'ocean_palace_w_room', 'ocean_palace_switch_nw', 'ocean_palace_switch_sw', 'ocean_palace_switch_ne', 'ocean_palace_switch_secret', 'ocean_palace_final', 'magus_castle_left_hall', 'magus_castle_unskippables', 'magus_castle_pit_e', 'magus_castle_pit_ne', 'magus_castle_pit_nw', 'magus_castle_pit_w', 'taban_gift_suit', 'taban_gift_helm', 'trading_post_petal_fang_base', 'trading_post_petal_fang_upgrade', 'trading_post_petal_horn_base', 'trading_post_petal_horn_upgrade', 'trading_post_petal_feather_base', 'trading_post_petal_feather_upgrade', 'trading_post_fang_horn_base', 'trading_post_fang_horn_upgrade', 'trading_post_fang_feather_base', 'trading_post_fang_feather_upgrade', 'trading_post_horn_feather_base', 'trading_post_horn_feather_upgrade', 'trading_post_special', 'jerky_gift', 'denadoro_rock', 'kajar_rock', 'laruba_rock', 'bekkler_key', 'cyrus_grave_key', 'sun_keep_2300', 'lucca_wondershot', 'taban_sunshades', 'fair_pendant', 'tata_reward', 'toma_reward', 'melchior_forge_masa', 'eot_gaspar_reward', 'hunting_range_nu_reward', 'zeal_mammon_machine', 'magus_castle_slash_sword_floor', 'guardia_prison_lunch_bag', 'cronos_mom', 'truce_mayor_2f_old_man', 'ioka_sweetwater_tonic', 'dorino_inn_powermeal', 'yakra_key_chest', 'courtroom_yakra_key', 'johnny_race_power_tab', 'guardia_forest_power_tab_600', 'guardia_forest_power_tab_1000', 'manoria_confinement_power_tab', 'dorino_bromide_magic_tab', 'porre_market_600_power_tab', 'denadoro_mts_speed_tab', 'tomas_grave_speed_tab', 'giants_claw_caverns_power_tab', 'giants_claw_entrance_power_tab', 'giants_claw_traps_power_tab', 'sun_keep_600_power_tab', 'medina_elder_speed_tab', 'medina_elder_magic_tab', 'magus_castle_flea_magic_tab', 'magus_castle_dungeons_magic_tab', 'trann_dome_sealed_magic_tab', 'arris_dome_sealed_power_tab', 'keepers_dome_magic_tab', 'death_peak_power_tab', 'blackbird_ducts_magic_tab', 'geno_dome_atropos_magic_tab', 'geno_dome_corridor_power_tab', 'geno_dome_labs_magic_tab', 'geno_dome_labs_speed_tab', 'enhasa_nu_battle_magic_tab', 'enhasa_nu_battle_speed_tab', 'kajar_speed_tab', 'kajar_nu_scratch_magic_tab', 'last_village_nu_shop_magic_tab', 'sunken_desert_power_tab', 'mountains_re_nice_magic_tab', 'beast_nest_power_tab', 'mt_woe_magic_tab', 'ocean_palace_elevator_magic_tab', 'ozzies_fort_guillotines_tab', 'proto_dome_portal_tab', 'northern_ruins_heros_grave_magic_tab', 'northern_ruins_landing_power_tab'}
    default = []


class GoodLootRate7(Range):
    """Percent chance to fill a good loot spot with good loot for pool 7"""
    display_name = "Good Loot Rate 7"
    range_start = 0
    range_end = 100
    default = 75


class GoodLoot8(OptionList):
    """Loot that is considered to be good for pool 8 (ignored by vanilla)"""
    display_name = "Good Loot 8"
    valid_keys = {'wood_sword', 'iron_blade', 'steelsaber', 'lode_sword', 'red_katana', 'flint_edge', 'dark_saber', 'aeon_blade', 'demon_edge', 'alloyblade', 'star_sword', 'vedicblade', 'kali_blade', 'shiva_edge', 'bolt_sword', 'slasher', 'bronze_bow', 'iron_bow', 'lode_bow', 'robin_bow', 'sage_bow', 'dream_bow', 'cometarrow', 'sonicarrow', 'valkerye', 'siren', 'air_gun', 'dart_gun', 'auto_gun', 'picomagnum', 'plasma_gun', 'ruby_gun', 'dream_gun', 'megablast', 'shock_wave', 'wondershot', 'graedus', 'tin_arm', 'hammer_arm', 'miragehand', 'stone_arm', 'doomfinger', 'magma_hand', 'megatonarm', 'big_hand', 'kaiser_arm', 'giga_arm', 'terra_arm', 'crisis_arm', 'bronzeedge', 'iron_sword', 'masamune_1', 'flashblade', 'pearl_edge', 'rune_blade', 'bravesword', 'masamune_2', 'demon_hit', 'fist', 'fist_2', 'fist_3', 'iron_fist', 'bronzefist', 'pacifist', 'darkscythe', 'hurricane', 'starscythe', 'doomsickle', 'mop', 'bent_sword', 'bent_hilt', 'swallow', 'slasher_2', 'rainbow', 'hide_tunic', 'karate_gi', 'bronzemail', 'maidensuit', 'iron_suit', 'titan_vest', 'gold_suit', 'ruby_vest', 'dark_mail', 'mist_robe', 'meso_mail', 'lumin_robe', 'flash_mail', 'lode_vest', 'aeon_suit', 'zodiaccape', 'nova_armor', 'prismdress', 'moon_armor', 'ruby_armor', 'ravenarmor', 'gloom_cape', 'white_mail', 'black_mail', 'blue_mail', 'red_mail', 'white_vest', 'black_vest', 'blue_vest', 'red_vest', 'taban_vest', 'taban_suit', 'hide_cap', 'bronzehelm', 'iron_helm', 'beret', 'gold_helm', 'rock_helm', 'ceratopper', 'glow_helm', 'lode_helm', 'aeon_helm', 'prism_helm', 'doom_helm', 'dark_helm', 'gloom_helm', 'safe_helm', 'taban_helm', 'sight_cap', 'memory_cap', 'time_hat', 'vigil_hat', 'ozziepants', 'haste_helm', 'rbow_helm', 'mermaidcap', 'bandana', 'ribbon', 'powerglove', 'defender', 'magicscarf', 'amulet', 'dash_ring', 'hit_ring', 'power_ring', 'magic_ring', 'wall_ring', 'silvererng', 'gold_erng', 'silverstud', 'gold_stud', 'sightscope', 'charm_top', 'rage_band', 'frenzyband', 'third_eye', 'wallet', 'greendream', 'berserker', 'powerscarf', 'speed_belt', 'black_rock', 'blue_rock', 'silverrock', 'white_rock', 'gold_rock', 'hero_medal', 'musclering', 'flea_vest', 'magic_seal', 'power_seal', 'valor_crest', 'dragon_tear', 'sun_shades', 'prismspecs', 'tonic', 'mid_tonic', 'full_tonic', 'ether', 'mid_ether', 'full_ether', 'elixir', 'hyperether', 'megaelixir', 'heal', 'revive', 'shelter', 'power_meal', 'lapis', 'barrier', 'shield', 'power_tab', 'magic_tab', 'speed_tab', 'petal', 'fang', 'horn', 'feather', 'seed', 'bike_key', 'pendant', 'gate_key', 'prismshard', 'c_trigger', 'tools', 'jerky', 'dreamstone', 'race_log', 'moon_stone', 'sun_stone', 'ruby_knife', 'yakra_key', 'clone', 'tomas_pop', 'petals_2', 'fangs_2', 'horns_2', 'feathers_2', 'jetsoftime', 'pendant_charge', 'rainbow_shell'}
    default = []


class GoodLootSpots8(OptionList):
    """Spots for pool 8 which will be given a random good reward (ignored by vanilla)"""
    display_name = "Good Loot Spots 8"
    valid_keys = {'mt_woe_1st_screen', 'mt_woe_2nd_screen_1', 'mt_woe_2nd_screen_2', 'mt_woe_2nd_screen_3', 'mt_woe_2nd_screen_4', 'mt_woe_2nd_screen_5', 'mt_woe_3rd_screen_1', 'mt_woe_3rd_screen_2', 'mt_woe_3rd_screen_3', 'mt_woe_3rd_screen_4', 'mt_woe_3rd_screen_5', 'mt_woe_final_1', 'mt_woe_final_2', 'mt_woe_key', 'fiona_key', 'arris_dome_rats', 'arris_dome_food_store', 'arris_dome_doan_key', 'arris_dome_food_locker_key', 'sun_palace_key', 'sewers_1', 'sewers_2', 'sewers_3', 'lab_16_1', 'lab_16_2', 'lab_16_3', 'lab_16_4', 'lab_32_1', 'prison_tower_1000', 'geno_dome_1f_1', 'geno_dome_1f_2', 'geno_dome_1f_3', 'geno_dome_1f_4', 'geno_dome_room_1', 'geno_dome_room_2', 'geno_dome_proto4_1', 'geno_dome_proto4_2', 'geno_dome_2f_1', 'geno_dome_2f_2', 'geno_dome_2f_3', 'geno_dome_2f_4', 'geno_dome_boss_1', 'geno_dome_boss_2', 'factory_left_aux_console', 'factory_left_security_right', 'factory_left_security_left', 'factory_right_data_core_1', 'factory_right_data_core_2', 'factory_right_floor_top', 'factory_right_floor_left', 'factory_right_floor_bottom', 'factory_right_floor_secret', 'factory_right_crane_lower', 'factory_right_crane_upper', 'factory_right_info_archive', 'giants_claw_traps', 'giants_claw_caves_1', 'giants_claw_caves_2', 'giants_claw_caves_3', 'giants_claw_caves_4', 'giants_claw_caves_5', 'giants_claw_rock', 'giants_claw_key', 'northern_ruins_antechamber_left_600', 'northern_ruins_antechamber_sealed_600', 'northern_ruins_antechamber_left_1000', 'northern_ruins_antechamber_sealed_1000', 'northern_ruins_back_left_sealed_600', 'northern_ruins_back_right_sealed_600', 'northern_ruins_back_left_sealed_1000', 'northern_ruins_back_right_sealed_1000', 'northern_ruins_basement_600', 'northern_ruins_basement_1000', 'guardia_basement_1', 'guardia_basement_2', 'guardia_basement_3', 'guardia_treasury_1', 'guardia_treasury_2', 'guardia_treasury_3', 'kings_trial_key', 'ozzies_fort_guillotines_1', 'ozzies_fort_guillotines_2', 'ozzies_fort_guillotines_3', 'ozzies_fort_guillotines_4', 'ozzies_fort_final_1', 'ozzies_fort_final_2', 'truce_mayor_1f', 'truce_mayor_2f', 'forest_ruins', 'porre_mayor_2f', 'truce_canyon_1', 'truce_canyon_2', 'fionas_house_1', 'fionas_house_2', 'cursed_woods_1', 'cursed_woods_2', 'frogs_burrow_right', 'zenan_bridge_chef', 'zenan_bridge_chef_tab', 'zenan_bridge_captain', 'snail_stop_key', 'lazy_carpenter', 'heckran_cave_sidetrack', 'heckran_cave_entrance', 'heckran_cave_1', 'heckran_cave_2', 'taban_gift_vest', 'kings_room_1000', 'queens_room_1000', 'kings_room_600', 'queens_room_600', 'royal_kitchen', 'queens_tower_600', 'kings_tower_600', 'kings_tower_1000', 'queens_tower_1000', 'guardia_court_tower', 'manoria_cathedral_1', 'manoria_cathedral_2', 'manoria_cathedral_3', 'manoria_interior_1', 'manoria_interior_2', 'manoria_interior_3', 'manoria_interior_4', 'manoria_shrine_sideroom_1', 'manoria_shrine_sideroom_2', 'manoria_bromide_1', 'manoria_bromide_2', 'manoria_bromide_3', 'manoria_shrine_magus_1', 'manoria_shrine_magus_2', 'yakras_room', 'denadoro_mts_screen2_1', 'denadoro_mts_screen2_2', 'denadoro_mts_screen2_3', 'denadoro_mts_final_1', 'denadoro_mts_final_2', 'denadoro_mts_final_3', 'denadoro_mts_waterfall_top_1', 'denadoro_mts_waterfall_top_2', 'denadoro_mts_waterfall_top_3', 'denadoro_mts_waterfall_top_4', 'denadoro_mts_waterfall_top_5', 'denadoro_mts_entrance_1', 'denadoro_mts_entrance_2', 'denadoro_mts_screen3_1', 'denadoro_mts_screen3_2', 'denadoro_mts_screen3_3', 'denadoro_mts_screen3_4', 'denadoro_mts_ambush', 'denadoro_mts_save_pt', 'denadoro_mts_key', 'bangor_dome_seal_1', 'bangor_dome_seal_2', 'bangor_dome_seal_3', 'trann_dome_seal_1', 'trann_dome_seal_2', 'arris_dome_seal_1', 'arris_dome_seal_2', 'arris_dome_seal_3', 'arris_dome_seal_4', 'truce_inn_sealed_600', 'porre_elder_sealed_1', 'porre_elder_sealed_2', 'guardia_castle_sealed_600', 'guardia_forest_sealed_600', 'truce_inn_sealed_1000', 'porre_mayor_sealed_1', 'porre_mayor_sealed_2', 'guardia_forest_sealed_1000', 'guardia_castle_sealed_1000', 'heckran_sealed_1', 'heckran_sealed_2', 'pyramid_left', 'pyramid_right', 'magic_cave_sealed', 'mystic_mt_stream', 'forest_maze_1', 'forest_maze_2', 'forest_maze_3', 'forest_maze_4', 'forest_maze_5', 'forest_maze_6', 'forest_maze_7', 'forest_maze_8', 'forest_maze_9', 'reptite_lair_reptites_1', 'reptite_lair_reptites_2', 'reptite_lair_key', 'dactyl_nest_1', 'dactyl_nest_2', 'dactyl_nest_3', 'melchior_rainbow_shell', 'melchior_sunstone_rainbow', 'melchior_sunstone_specs', 'frogs_burrow_left', 'guardia_jail_fritz_storage', 'guardia_jail_cell', 'guardia_jail_omnicrone_1', 'guardia_jail_omnicrone_2', 'guardia_jail_omnicrone_3', 'guardia_jail_hole_1', 'guardia_jail_hole_2', 'guardia_jail_outer_wall', 'guardia_jail_omnicrone_4', 'guardia_jail_fritz', 'magus_castle_right_hall', 'sunken_desert_b1_nw', 'sunken_desert_b1_ne', 'sunken_desert_b1_se', 'sunken_desert_b1_sw', 'sunken_desert_b2_nw', 'sunken_desert_b2_n', 'sunken_desert_b2_w', 'sunken_desert_b2_sw', 'sunken_desert_b2_se', 'sunken_desert_b2_e', 'sunken_desert_b2_center', 'magus_castle_guillotine_1', 'magus_castle_guillotine_2', 'magus_castle_slash_room_1', 'magus_castle_slash_room_2', 'magus_castle_statue_hall', 'magus_castle_four_kids', 'magus_castle_ozzie_1', 'magus_castle_ozzie_2', 'magus_castle_enemy_elevator', 'reptite_lair_secret_b2_ne_right', 'lab_32_race_log', 'factory_ruins_generator', 'death_peak_south_face_krakker', 'death_peak_south_face_spawn_save', 'death_peak_south_face_summit', 'death_peak_field', 'death_peak_krakker_parade', 'death_peak_caves_left', 'death_peak_caves_center', 'death_peak_caves_right', 'reptite_lair_secret_b1_sw', 'reptite_lair_secret_b1_ne', 'reptite_lair_secret_b1_se', 'reptite_lair_secret_b2_se_right', 'reptite_lair_secret_b2_ne_or_se_left', 'reptite_lair_secret_b2_sw', 'tyrano_lair_throne_1', 'tyrano_lair_throne_2', 'tyrano_lair_trapdoor', 'tyrano_lair_kino_cell', 'tyrano_lair_maze_1', 'tyrano_lair_maze_2', 'tyrano_lair_maze_3', 'tyrano_lair_maze_4', 'black_omen_aux_command_mid', 'black_omen_aux_command_ne', 'black_omen_grand_hall', 'black_omen_nu_hall_nw', 'black_omen_nu_hall_w', 'black_omen_nu_hall_sw', 'black_omen_nu_hall_ne', 'black_omen_nu_hall_e', 'black_omen_nu_hall_se', 'black_omen_royal_path', 'black_omen_ruminator_parade', 'black_omen_eyeball_hall', 'black_omen_tubster_fly', 'black_omen_martello', 'black_omen_alien_sw', 'black_omen_alien_ne', 'black_omen_alien_nw', 'black_omen_terra_w', 'black_omen_terra_rock', 'black_omen_terra_ne', 'ocean_palace_main_s', 'ocean_palace_main_n', 'ocean_palace_e_room', 'ocean_palace_w_room', 'ocean_palace_switch_nw', 'ocean_palace_switch_sw', 'ocean_palace_switch_ne', 'ocean_palace_switch_secret', 'ocean_palace_final', 'magus_castle_left_hall', 'magus_castle_unskippables', 'magus_castle_pit_e', 'magus_castle_pit_ne', 'magus_castle_pit_nw', 'magus_castle_pit_w', 'taban_gift_suit', 'taban_gift_helm', 'trading_post_petal_fang_base', 'trading_post_petal_fang_upgrade', 'trading_post_petal_horn_base', 'trading_post_petal_horn_upgrade', 'trading_post_petal_feather_base', 'trading_post_petal_feather_upgrade', 'trading_post_fang_horn_base', 'trading_post_fang_horn_upgrade', 'trading_post_fang_feather_base', 'trading_post_fang_feather_upgrade', 'trading_post_horn_feather_base', 'trading_post_horn_feather_upgrade', 'trading_post_special', 'jerky_gift', 'denadoro_rock', 'kajar_rock', 'laruba_rock', 'bekkler_key', 'cyrus_grave_key', 'sun_keep_2300', 'lucca_wondershot', 'taban_sunshades', 'fair_pendant', 'tata_reward', 'toma_reward', 'melchior_forge_masa', 'eot_gaspar_reward', 'hunting_range_nu_reward', 'zeal_mammon_machine', 'magus_castle_slash_sword_floor', 'guardia_prison_lunch_bag', 'cronos_mom', 'truce_mayor_2f_old_man', 'ioka_sweetwater_tonic', 'dorino_inn_powermeal', 'yakra_key_chest', 'courtroom_yakra_key', 'johnny_race_power_tab', 'guardia_forest_power_tab_600', 'guardia_forest_power_tab_1000', 'manoria_confinement_power_tab', 'dorino_bromide_magic_tab', 'porre_market_600_power_tab', 'denadoro_mts_speed_tab', 'tomas_grave_speed_tab', 'giants_claw_caverns_power_tab', 'giants_claw_entrance_power_tab', 'giants_claw_traps_power_tab', 'sun_keep_600_power_tab', 'medina_elder_speed_tab', 'medina_elder_magic_tab', 'magus_castle_flea_magic_tab', 'magus_castle_dungeons_magic_tab', 'trann_dome_sealed_magic_tab', 'arris_dome_sealed_power_tab', 'keepers_dome_magic_tab', 'death_peak_power_tab', 'blackbird_ducts_magic_tab', 'geno_dome_atropos_magic_tab', 'geno_dome_corridor_power_tab', 'geno_dome_labs_magic_tab', 'geno_dome_labs_speed_tab', 'enhasa_nu_battle_magic_tab', 'enhasa_nu_battle_speed_tab', 'kajar_speed_tab', 'kajar_nu_scratch_magic_tab', 'last_village_nu_shop_magic_tab', 'sunken_desert_power_tab', 'mountains_re_nice_magic_tab', 'beast_nest_power_tab', 'mt_woe_magic_tab', 'ocean_palace_elevator_magic_tab', 'ozzies_fort_guillotines_tab', 'proto_dome_portal_tab', 'northern_ruins_heros_grave_magic_tab', 'northern_ruins_landing_power_tab'}
    default = []


class GoodLootRate8(Range):
    """Percent chance to fill a good loot spot with good loot for pool 8"""
    display_name = "Good Loot Rate 8"
    range_start = 0
    range_end = 100
    default = 75


class SightscopeAll(Toggle):
    """Enable sightscope usage on all enemies."""
    display_name = "Sightscope All"


class ForcedSightscope(Toggle):
    """Sightscope effect will be present without the item equipped."""
    display_name = "Forced Sightscope"


class ShuffleEnemies(Toggle):
    """Normal enemy types are shuffled (respects enemy size)"""
    display_name = "Shuffle Enemies"


class NormalizeEnemies(Toggle):
    """Modify enemy stats to balanced overly easy/difficult enemies"""
    display_name = "Normalize Enemies"


class DefaultFastLocMovement(Toggle):
    """Default location (dungeon, etc) movement is fast and run button slows"""
    display_name = "Default Fast Loc Movement"


class DefaultFastOwMovement(Toggle):
    """Default overworld movement is fast and run button slows"""
    display_name = "Default Fast Ow Movement"


class DefaultFastEpochMovement(Toggle):
    """Default epoch movement is fast and run button slows"""
    display_name = "Default Fast Epoch Movement"


class BattleSpeed(Range):
    """Default battle speed"""
    display_name = "Battle Speed"
    range_start = 1
    range_end = 8
    default = 5


class MessageSpeed(Range):
    """Default message speed"""
    display_name = "Message Speed"
    range_start = 1
    range_end = 8
    default = 5


class BattleMemoryCursor(Toggle):
    """By default turn battle memory cursor on"""
    display_name = "Battle Memory Cursor"


class MenuMemoryCursor(Toggle):
    """By default turn menu memory cursor on"""
    display_name = "Menu Memory Cursor"


class WindowBackground(Range):
    """Default window background"""
    display_name = "Window Background"
    range_start = 1
    range_end = 8
    default = 1


class UseLSelectWarp(Toggle):
    """Use L+Select instead of Start+Select for house warp"""
    display_name = "Use L Select Warp"


class UseMsu1(Toggle):
    """Apply an MSU-1 patch to the rom."""
    display_name = "Use Msu1"


class CronoPalette(FreeText):
    """Hex format palette for Crono"""
    display_name = "Crono Palette"
    default = ""


class MarlePalette(FreeText):
    """Hex format palette for Marle"""
    display_name = "Marle Palette"
    default = ""


class LuccaPalette(FreeText):
    """Hex format palette for Lucca"""
    display_name = "Lucca Palette"
    default = ""


class RoboPalette(FreeText):
    """Hex format palette for Robo"""
    display_name = "Robo Palette"
    default = ""


class FrogPalette(FreeText):
    """Hex format palette for Frog"""
    display_name = "Frog Palette"
    default = ""


class AylaPalette(FreeText):
    """Hex format palette for Ayla"""
    display_name = "Ayla Palette"
    default = ""


class MagusPalette(FreeText):
    """Hex format palette for Magus"""
    display_name = "Magus Palette"
    default = ""


class RemoveFlashes(Toggle):
    """Remove flashes from many animations"""
    display_name = "Remove Flashes"


class AltLightning2(Choice):
    """Alternate sound effect for lightning 2"""
    display_name = "Alt Lightning2"

    option_no_change = 0
    option_mute = 1
    option_nizbel_release = 2
    default = 0


class DsItemPool(OptionList):
    """DS Items which may appear"""
    display_name = "Ds Item Pool"
    valid_keys = {'dreamseeker', 'venus_bow', 'turboshot', 'spellslinger', 'dragon_arm', 'apocalypse_arm', 'dinoblade', 'judgement_scythe', 'dreamreaper', 'reptite_dress', 'dragon_armor', 'regal_plate', 'regal_gown', 'shadowplume_robe', 'elemental_aegis', 'saurian_leathers', 'dragonhead', 'reptite_tiara', 'masters_crown', 'angels_tiara', 'valor_crest', 'dragons_tear', 'champions_badge'}
    default = ['dreamseeker', 'venus_bow', 'turboshot', 'spellslinger', 'dragon_arm', 'apocalypse_arm', 'dinoblade', 'judgement_scythe', 'dreamreaper', 'reptite_dress', 'dragon_armor', 'regal_plate', 'regal_gown', 'shadowplume_robe', 'elemental_aegis', 'saurian_leathers', 'dragonhead', 'reptite_tiara', 'masters_crown', 'angels_tiara', 'valor_crest', 'dragons_tear', 'champions_badge']


class DsReplacementChance(Range):
    """Percent chance (e.g. 10 for 10 percent) to replace an item with a ds counterpart"""
    display_name = "Ds Replacement Chance"
    range_start = 0
    range_end = 100
    default = 50


class BronzeFistPolicy(Choice):
    """How to modify BronzeFist pre-shuffle"""
    display_name = "Bronze Fist Policy"

    option_vanilla = 0
    option_remove = 1
    option_4x_crit = 2
    option_random_other = 3
    default = 0


class WeaponRandoPool(OptionList):
    """Weapons whose effects will be shuffled"""
    display_name = "Weapon Rando Pool"
    valid_keys = {'wood_sword', 'iron_blade', 'steelsaber', 'lode_sword', 'red_katana', 'flint_edge', 'dark_saber', 'aeon_blade', 'demon_edge', 'alloyblade', 'star_sword', 'vedicblade', 'kali_blade', 'shiva_edge', 'bolt_sword', 'slasher', 'bronze_bow', 'iron_bow', 'lode_bow', 'robin_bow', 'sage_bow', 'dream_bow', 'cometarrow', 'sonicarrow', 'valkerye', 'siren', 'air_gun', 'dart_gun', 'auto_gun', 'picomagnum', 'plasma_gun', 'ruby_gun', 'dream_gun', 'megablast', 'shock_wave', 'wondershot', 'graedus', 'tin_arm', 'hammer_arm', 'miragehand', 'stone_arm', 'doomfinger', 'magma_hand', 'megatonarm', 'big_hand', 'kaiser_arm', 'giga_arm', 'terra_arm', 'crisis_arm', 'bronzeedge', 'iron_sword', 'masamune_1', 'flashblade', 'pearl_edge', 'rune_blade', 'bravesword', 'masamune_2', 'demon_hit', 'fist', 'fist_2', 'fist_3', 'iron_fist', 'bronzefist', 'darkscythe', 'hurricane', 'starscythe', 'doomsickle', 'mop', 'swallow', 'slasher_2', 'rainbow'}
    default = []


class WeaponRandoEffectScheme(Choice):
    """How to randomize weapon effects"""
    display_name = "Weapon Rando Effect Scheme"

    option_no_change = 0
    option_shuffle = 1
    option_shuffle_linked = 2
    option_rdi_random = 3
    default = 2


class WeaponRandoStatBoostScheme(Choice):
    """How to randomize weapon stat boosts"""
    display_name = "Weapon Rando Stat Boost Scheme"

    option_no_change = 0
    option_shuffle = 1
    option_shuffle_linked = 2
    option_rdi_random = 3
    default = 2


class ForcedWeaponEffects(OptionList):
    """Effects guaranteed to exist in the weapon rando pool"""
    display_name = "Forced Weapon Effects"
    valid_keys = {'no_change', 'none', 'wonder', 'doom', 'crisis', 'stop_60', 'slow_60', 'chaos_80', 'stop_80_machines', '4x_crit', '9999_crit', '777_dmg', 'crisis_mp', 'valiant', 'mp_crit', 'mp_crit4x', 'hp_leech_5', 'hp_leech_10', 'mp_leech_2', 'mp_leech_5'}
    default = []


class ForcedWeaponStatBoosts(OptionList):
    """Stat boosts guaranteed to exist in the weapon rando pool"""
    display_name = "Forced Weapon Stat Boosts"
    valid_keys = {'no_change', 'none', 'speed_1', 'hit_2', 'power_2', 'stamina_2', 'magic_2', 'mdef_5', 'speed_3', 'hit_10', 'power_6', 'magic_6', 'mdef_10', 'power_4', 'speed_2', 'mdef_20', 'stamina_6', 'magic_4', 'mdef_12', 'magic_mdef_5', 'power_stamina_10', 'mdef_stamina_10', 'mdef_9', 'magic_10', 'power_10', 'speed_power_3', 'power_5', 'magic_5'}
    default = []


class RandomWeaponEffectSpec(FreeText):
    """Distribution for choosing random effects after the forced ones"""
    display_name = "Random Weapon Effect Spec"
    default = ""


class RandomWeaponStatBoostSpec(FreeText):
    """Distribution for choosing random stat boosts after the forced ones"""
    display_name = "Random Weapon Stat Boost Spec"
    default = ""


class WeaponRandoPool2(OptionList):
    """Weapons whose effects will be shuffled"""
    display_name = "Weapon Rando Pool 2"
    valid_keys = {'wood_sword', 'iron_blade', 'steelsaber', 'lode_sword', 'red_katana', 'flint_edge', 'dark_saber', 'aeon_blade', 'demon_edge', 'alloyblade', 'star_sword', 'vedicblade', 'kali_blade', 'shiva_edge', 'bolt_sword', 'slasher', 'bronze_bow', 'iron_bow', 'lode_bow', 'robin_bow', 'sage_bow', 'dream_bow', 'cometarrow', 'sonicarrow', 'valkerye', 'siren', 'air_gun', 'dart_gun', 'auto_gun', 'picomagnum', 'plasma_gun', 'ruby_gun', 'dream_gun', 'megablast', 'shock_wave', 'wondershot', 'graedus', 'tin_arm', 'hammer_arm', 'miragehand', 'stone_arm', 'doomfinger', 'magma_hand', 'megatonarm', 'big_hand', 'kaiser_arm', 'giga_arm', 'terra_arm', 'crisis_arm', 'bronzeedge', 'iron_sword', 'masamune_1', 'flashblade', 'pearl_edge', 'rune_blade', 'bravesword', 'masamune_2', 'demon_hit', 'fist', 'fist_2', 'fist_3', 'iron_fist', 'bronzefist', 'darkscythe', 'hurricane', 'starscythe', 'doomsickle', 'mop', 'swallow', 'slasher_2', 'rainbow'}
    default = []


class WeaponRandoEffectScheme2(Choice):
    """How to randomize weapon effects"""
    display_name = "Weapon Rando Effect Scheme 2"

    option_no_change = 0
    option_shuffle = 1
    option_shuffle_linked = 2
    option_rdi_random = 3
    default = 2


class WeaponRandoStatBoostScheme2(Choice):
    """How to randomize weapon stat boosts"""
    display_name = "Weapon Rando Stat Boost Scheme 2"

    option_no_change = 0
    option_shuffle = 1
    option_shuffle_linked = 2
    option_rdi_random = 3
    default = 2


class ForcedWeaponEffects2(OptionList):
    """Effects guaranteed to exist in the weapon rando pool"""
    display_name = "Forced Weapon Effects 2"
    valid_keys = {'no_change', 'none', 'wonder', 'doom', 'crisis', 'stop_60', 'slow_60', 'chaos_80', 'stop_80_machines', '4x_crit', '9999_crit', '777_dmg', 'crisis_mp', 'valiant', 'mp_crit', 'mp_crit4x', 'hp_leech_5', 'hp_leech_10', 'mp_leech_2', 'mp_leech_5'}
    default = []


class ForcedWeaponStatBoosts2(OptionList):
    """Stat boosts guaranteed to exist in the weapon rando pool"""
    display_name = "Forced Weapon Stat Boosts 2"
    valid_keys = {'no_change', 'none', 'speed_1', 'hit_2', 'power_2', 'stamina_2', 'magic_2', 'mdef_5', 'speed_3', 'hit_10', 'power_6', 'magic_6', 'mdef_10', 'power_4', 'speed_2', 'mdef_20', 'stamina_6', 'magic_4', 'mdef_12', 'magic_mdef_5', 'power_stamina_10', 'mdef_stamina_10', 'mdef_9', 'magic_10', 'power_10', 'speed_power_3', 'power_5', 'magic_5'}
    default = []


class RandomWeaponEffectSpec2(FreeText):
    """Distribution for choosing random effects after the forced ones"""
    display_name = "Random Weapon Effect Spec 2"
    default = ""


class RandomWeaponStatBoostSpec2(FreeText):
    """Distribution for choosing random stat boosts after the forced ones"""
    display_name = "Random Weapon Stat Boost Spec 2"
    default = ""


class WeaponRandoPool3(OptionList):
    """Weapons whose effects will be shuffled"""
    display_name = "Weapon Rando Pool 3"
    valid_keys = {'wood_sword', 'iron_blade', 'steelsaber', 'lode_sword', 'red_katana', 'flint_edge', 'dark_saber', 'aeon_blade', 'demon_edge', 'alloyblade', 'star_sword', 'vedicblade', 'kali_blade', 'shiva_edge', 'bolt_sword', 'slasher', 'bronze_bow', 'iron_bow', 'lode_bow', 'robin_bow', 'sage_bow', 'dream_bow', 'cometarrow', 'sonicarrow', 'valkerye', 'siren', 'air_gun', 'dart_gun', 'auto_gun', 'picomagnum', 'plasma_gun', 'ruby_gun', 'dream_gun', 'megablast', 'shock_wave', 'wondershot', 'graedus', 'tin_arm', 'hammer_arm', 'miragehand', 'stone_arm', 'doomfinger', 'magma_hand', 'megatonarm', 'big_hand', 'kaiser_arm', 'giga_arm', 'terra_arm', 'crisis_arm', 'bronzeedge', 'iron_sword', 'masamune_1', 'flashblade', 'pearl_edge', 'rune_blade', 'bravesword', 'masamune_2', 'demon_hit', 'fist', 'fist_2', 'fist_3', 'iron_fist', 'bronzefist', 'darkscythe', 'hurricane', 'starscythe', 'doomsickle', 'mop', 'swallow', 'slasher_2', 'rainbow'}
    default = []


class WeaponRandoEffectScheme3(Choice):
    """How to randomize weapon effects"""
    display_name = "Weapon Rando Effect Scheme 3"

    option_no_change = 0
    option_shuffle = 1
    option_shuffle_linked = 2
    option_rdi_random = 3
    default = 2


class WeaponRandoStatBoostScheme3(Choice):
    """How to randomize weapon stat boosts"""
    display_name = "Weapon Rando Stat Boost Scheme 3"

    option_no_change = 0
    option_shuffle = 1
    option_shuffle_linked = 2
    option_rdi_random = 3
    default = 2


class ForcedWeaponEffects3(OptionList):
    """Effects guaranteed to exist in the weapon rando pool"""
    display_name = "Forced Weapon Effects 3"
    valid_keys = {'no_change', 'none', 'wonder', 'doom', 'crisis', 'stop_60', 'slow_60', 'chaos_80', 'stop_80_machines', '4x_crit', '9999_crit', '777_dmg', 'crisis_mp', 'valiant', 'mp_crit', 'mp_crit4x', 'hp_leech_5', 'hp_leech_10', 'mp_leech_2', 'mp_leech_5'}
    default = []


class ForcedWeaponStatBoosts3(OptionList):
    """Stat boosts guaranteed to exist in the weapon rando pool"""
    display_name = "Forced Weapon Stat Boosts 3"
    valid_keys = {'no_change', 'none', 'speed_1', 'hit_2', 'power_2', 'stamina_2', 'magic_2', 'mdef_5', 'speed_3', 'hit_10', 'power_6', 'magic_6', 'mdef_10', 'power_4', 'speed_2', 'mdef_20', 'stamina_6', 'magic_4', 'mdef_12', 'magic_mdef_5', 'power_stamina_10', 'mdef_stamina_10', 'mdef_9', 'magic_10', 'power_10', 'speed_power_3', 'power_5', 'magic_5'}
    default = []


class RandomWeaponEffectSpec3(FreeText):
    """Distribution for choosing random effects after the forced ones"""
    display_name = "Random Weapon Effect Spec 3"
    default = ""


class RandomWeaponStatBoostSpec3(FreeText):
    """Distribution for choosing random stat boosts after the forced ones"""
    display_name = "Random Weapon Stat Boost Spec 3"
    default = ""


class UsePhysMarle(Toggle):
    """+Hit, Physical arrow tech"""
    display_name = "Use Phys Marle"


class UseHasteAll(Toggle):
    """AoE Haste, 15 MP cost"""
    display_name = "Use Haste All"


class UsePhysLucca(Toggle):
    """+Hit. Physical Flame Toss + Bombs"""
    display_name = "Use Phys Lucca"


class UseProtectAll(Toggle):
    """AoE Protect, 2x MP cost"""
    display_name = "Use Protect All"


class UseReraise(Toggle):
    """Life2 gives greendream effect"""
    display_name = "Use Reraise"


class UseMagusDualTechs(Toggle):
    """Magus can perform dual techs with fire/ice/lit2"""
    display_name = "Use Magus Dual Techs"


class UseDaltonizedMagus(Toggle):
    """Magus shadow techs are replaced with Dalton versions"""
    display_name = "Use Daltonized Magus"


class TechRandoScheme(Choice):
    """Scheme to randomize single techs"""
    display_name = "Tech Rando Scheme"

    option_vanilla = 0
    option_shuffle_element = 1
    option_random_element = 2
    option_chaos_element = 3
    default = 0


class MdefGrowthScaleFactor(Range):
    """Scale all magic defense gains by this factor"""
    display_name = "Mdef Growth Scale Factor"
    range_start = 50
    range_end = 150
    default = 100


class MdefCap(Range):
    """The maximum possible magic defense (stats + equip)"""
    display_name = "Mdef Cap"
    range_start = 1
    range_end = 99
    default = 99


class MdefLevelupCap(Range):
    """The maximum possible magic defense gained through leveling"""
    display_name = "Mdef Levelup Cap"
    range_start = 1
    range_end = 99
    default = 99


class DaltonLevel(Range):
    """The internal level of Dalton [Experimental]"""
    display_name = "Dalton Level"
    range_start = 0
    range_end = 99
    default = 26


class DaltonPlusLevel(Range):
    """The internal level of Dalton Plus [Experimental]"""
    display_name = "Dalton Plus Level"
    range_start = 0
    range_end = 99
    default = 20


class ElderSpawnLevel(Range):
    """The internal level of Elder Spawn [Experimental]"""
    display_name = "Elder Spawn Level"
    range_start = 0
    range_end = 99
    default = 46


class FleaLevel(Range):
    """The internal level of Flea [Experimental]"""
    display_name = "Flea Level"
    range_start = 0
    range_end = 99
    default = 19


class GigaMutantLevel(Range):
    """The internal level of Giga Mutant [Experimental]"""
    display_name = "Giga Mutant Level"
    range_start = 0
    range_end = 99
    default = 47


class GolemLevel(Range):
    """The internal level of Golem [Experimental]"""
    display_name = "Golem Level"
    range_start = 0
    range_end = 99
    default = 27


class GolemBossLevel(Range):
    """The internal level of Golem Boss [Experimental]"""
    display_name = "Golem Boss Level"
    range_start = 0
    range_end = 99
    default = 34


class HeckranLevel(Range):
    """The internal level of Heckran [Experimental]"""
    display_name = "Heckran Level"
    range_start = 0
    range_end = 99
    default = 12


class LavosSpawnLevel(Range):
    """The internal level of Lavos Spawn [Experimental]"""
    display_name = "Lavos Spawn Level"
    range_start = 0
    range_end = 99
    default = 32


class MammonMachineLevel(Range):
    """The internal level of Mammon M [Experimental]"""
    display_name = "Mammon Machine Level"
    range_start = 0
    range_end = 99
    default = 44


class MagusNcLevel(Range):
    """The internal level of Magus (North Cape) [Experimental]"""
    display_name = "Magus Nc Level"
    range_start = 0
    range_end = 99
    default = 30


class MasaMuneLevel(Range):
    """The internal level of Masa Mune [Experimental]"""
    display_name = "Masa Mune Level"
    range_start = 0
    range_end = 99
    default = 15


class MegaMutantLevel(Range):
    """The internal level of Mega Mutant [Experimental]"""
    display_name = "Mega Mutant Level"
    range_start = 0
    range_end = 99
    default = 46


class MudImpLevel(Range):
    """The internal level of Mud Imp [Experimental]"""
    display_name = "Mud Imp Level"
    range_start = 0
    range_end = 99
    default = 29


class NizbelLevel(Range):
    """The internal level of Nizbel [Experimental]"""
    display_name = "Nizbel Level"
    range_start = 0
    range_end = 99
    default = 17


class Nizbel2Level(Range):
    """The internal level of Nizbel II [Experimental]"""
    display_name = "Nizbel 2 Level"
    range_start = 0
    range_end = 99
    default = 23


class RetiniteLevel(Range):
    """The internal level of Retinite [Experimental]"""
    display_name = "Retinite Level"
    range_start = 0
    range_end = 99
    default = 28


class RSeriesLevel(Range):
    """The internal level of R Series [Experimental]"""
    display_name = "R Series Level"
    range_start = 0
    range_end = 99
    default = 5


class RustTyranoLevel(Range):
    """The internal level of Rust Tyrano [Experimental]"""
    display_name = "Rust Tyrano Level"
    range_start = 0
    range_end = 99
    default = 35


class SlashLevel(Range):
    """The internal level of Slash Sword [Experimental]"""
    display_name = "Slash Level"
    range_start = 0
    range_end = 99
    default = 20


class SonOfSunLevel(Range):
    """The internal level of Son Of Sun [Experimental]"""
    display_name = "Son Of Sun Level"
    range_start = 0
    range_end = 99
    default = 43


class TerraMutantLevel(Range):
    """The internal level of Terra Mutant [Experimental]"""
    display_name = "Terra Mutant Level"
    range_start = 0
    range_end = 99
    default = 48


class YakraLevel(Range):
    """The internal level of Yakra [Experimental]"""
    display_name = "Yakra Level"
    range_start = 0
    range_end = 99
    default = 4


class YakraXiiiLevel(Range):
    """The internal level of Yakra XIII [Experimental]"""
    display_name = "Yakra Xiii Level"
    range_start = 0
    range_end = 99
    default = 39


class ZomborLevel(Range):
    """The internal level of Zombor [Experimental]"""
    display_name = "Zombor Level"
    range_start = 0
    range_end = 99
    default = 9


class DragonTankLevel(Range):
    """The internal level of Dragon Tank [Experimental]"""
    display_name = "Dragon Tank Level"
    range_start = 0
    range_end = 99
    default = 5


class GigaGaiaLevel(Range):
    """The internal level of Giga Gaia [Experimental]"""
    display_name = "Giga Gaia Level"
    range_start = 0
    range_end = 99
    default = 30


class GuardianLevel(Range):
    """The internal level of Guardian [Experimental]"""
    display_name = "Guardian Level"
    range_start = 0
    range_end = 99
    default = 6


class MagusLevel(Range):
    """The internal level of Magus [Experimental]"""
    display_name = "Magus Level"
    range_start = 0
    range_end = 99
    default = 20


class BlackTyranoLevel(Range):
    """The internal level of Black Tyrano [Experimental]"""
    display_name = "Black Tyrano Level"
    range_start = 0
    range_end = 99
    default = 20


class OzzieTrioLevel(Range):
    """The internal level of Ozzie Trio [Experimental]"""
    display_name = "Ozzie Trio Level"
    range_start = 0
    range_end = 99
    default = 33


class AtroposLevel(Range):
    """The internal level of Atropos Xr [Experimental]"""
    display_name = "Atropos Level"
    range_start = 0
    range_end = 99
    default = 33


class FleaPlusLevel(Range):
    """The internal level of Flea Plus [Experimental]"""
    display_name = "Flea Plus Level"
    range_start = 0
    range_end = 99
    default = 27


class SuperSlashLevel(Range):
    """The internal level of Super Slash [Experimental]"""
    display_name = "Super Slash Level"
    range_start = 0
    range_end = 99
    default = 27


class KrawlieLevel(Range):
    """The internal level of Krawlie [Experimental]"""
    display_name = "Krawlie Level"
    range_start = 0
    range_end = 99
    default = 6


class GatoLevel(Range):
    """The internal level of Gato [Experimental]"""
    display_name = "Gato Level"
    range_start = 0
    range_end = 99
    default = 1


class Zeal2Level(Range):
    """The internal level of Zeal 2 [Experimental]"""
    display_name = "Zeal2 Level"
    range_start = 0
    range_end = 99
    default = 50


class EquipableRandoScheme(Choice):
    """Method for choosing who can equip what"""
    display_name = "Equipable Rando Scheme"

    option_vanilla = 0
    option_random_type = 1
    option_random_all = 2
    default = 0


class CronoLoseEquipNormalPercent(Range):
    """Chance for crono to lose use of normal type gear (random_type scheme)"""
    display_name = "Crono Lose Equip Normal Percent"
    range_start = 0
    range_end = 100
    default = 0


class MarleLoseEquipNormalPercent(Range):
    """Chance for marle to lose use of normal type gear (random_type scheme)"""
    display_name = "Marle Lose Equip Normal Percent"
    range_start = 0
    range_end = 100
    default = 0


class LuccaLoseEquipNormalPercent(Range):
    """Chance for lucca to lose use of normal type gear (random_type scheme)"""
    display_name = "Lucca Lose Equip Normal Percent"
    range_start = 0
    range_end = 100
    default = 0


class RoboLoseEquipNormalPercent(Range):
    """Chance for robo to lose use of normal type gear (random_type scheme)"""
    display_name = "Robo Lose Equip Normal Percent"
    range_start = 0
    range_end = 100
    default = 0


class FrogLoseEquipNormalPercent(Range):
    """Chance for frog to lose use of normal type gear (random_type scheme)"""
    display_name = "Frog Lose Equip Normal Percent"
    range_start = 0
    range_end = 100
    default = 0


class AylaLoseEquipNormalPercent(Range):
    """Chance for ayla to lose use of normal type gear (random_type scheme)"""
    display_name = "Ayla Lose Equip Normal Percent"
    range_start = 0
    range_end = 100
    default = 0


class MagusLoseEquipNormalPercent(Range):
    """Chance for magus to lose use of normal type gear (random_type scheme)"""
    display_name = "Magus Lose Equip Normal Percent"
    range_start = 0
    range_end = 100
    default = 0


class CronoGainEquipDressPercent(Range):
    """Chance for crono to gain use of dress type gear (random_type scheme)"""
    display_name = "Crono Gain Equip Dress Percent"
    range_start = 0
    range_end = 100
    default = 0


class CronoLoseEquipDressPercent(Range):
    """Chance for crono to lose use of dress type gear (random_type scheme)"""
    display_name = "Crono Lose Equip Dress Percent"
    range_start = 0
    range_end = 100
    default = 0


class MarleGainEquipDressPercent(Range):
    """Chance for marle to gain use of dress type gear (random_type scheme)"""
    display_name = "Marle Gain Equip Dress Percent"
    range_start = 0
    range_end = 100
    default = 0


class MarleLoseEquipDressPercent(Range):
    """Chance for marle to lose use of dress type gear (random_type scheme)"""
    display_name = "Marle Lose Equip Dress Percent"
    range_start = 0
    range_end = 100
    default = 0


class LuccaGainEquipDressPercent(Range):
    """Chance for lucca to gain use of dress type gear (random_type scheme)"""
    display_name = "Lucca Gain Equip Dress Percent"
    range_start = 0
    range_end = 100
    default = 0


class LuccaLoseEquipDressPercent(Range):
    """Chance for lucca to lose use of dress type gear (random_type scheme)"""
    display_name = "Lucca Lose Equip Dress Percent"
    range_start = 0
    range_end = 100
    default = 0


class RoboGainEquipDressPercent(Range):
    """Chance for robo to gain use of dress type gear (random_type scheme)"""
    display_name = "Robo Gain Equip Dress Percent"
    range_start = 0
    range_end = 100
    default = 0


class RoboLoseEquipDressPercent(Range):
    """Chance for robo to lose use of dress type gear (random_type scheme)"""
    display_name = "Robo Lose Equip Dress Percent"
    range_start = 0
    range_end = 100
    default = 0


class FrogGainEquipDressPercent(Range):
    """Chance for frog to gain use of dress type gear (random_type scheme)"""
    display_name = "Frog Gain Equip Dress Percent"
    range_start = 0
    range_end = 100
    default = 0


class FrogLoseEquipDressPercent(Range):
    """Chance for frog to lose use of dress type gear (random_type scheme)"""
    display_name = "Frog Lose Equip Dress Percent"
    range_start = 0
    range_end = 100
    default = 0


class AylaGainEquipDressPercent(Range):
    """Chance for ayla to gain use of dress type gear (random_type scheme)"""
    display_name = "Ayla Gain Equip Dress Percent"
    range_start = 0
    range_end = 100
    default = 0


class AylaLoseEquipDressPercent(Range):
    """Chance for ayla to lose use of dress type gear (random_type scheme)"""
    display_name = "Ayla Lose Equip Dress Percent"
    range_start = 0
    range_end = 100
    default = 0


class MagusGainEquipDressPercent(Range):
    """Chance for magus to gain use of dress type gear (random_type scheme)"""
    display_name = "Magus Gain Equip Dress Percent"
    range_start = 0
    range_end = 100
    default = 0


class MagusLoseEquipDressPercent(Range):
    """Chance for magus to lose use of dress type gear (random_type scheme)"""
    display_name = "Magus Lose Equip Dress Percent"
    range_start = 0
    range_end = 100
    default = 0


class CronoGainEquipHeavyArmorPercent(Range):
    """Chance for crono to gain use of heavy_armor type gear (random_type scheme)"""
    display_name = "Crono Gain Equip Heavy Armor Percent"
    range_start = 0
    range_end = 100
    default = 0


class CronoLoseEquipHeavyArmorPercent(Range):
    """Chance for crono to lose use of heavy_armor type gear (random_type scheme)"""
    display_name = "Crono Lose Equip Heavy Armor Percent"
    range_start = 0
    range_end = 100
    default = 0


class MarleGainEquipHeavyArmorPercent(Range):
    """Chance for marle to gain use of heavy_armor type gear (random_type scheme)"""
    display_name = "Marle Gain Equip Heavy Armor Percent"
    range_start = 0
    range_end = 100
    default = 0


class MarleLoseEquipHeavyArmorPercent(Range):
    """Chance for marle to lose use of heavy_armor type gear (random_type scheme)"""
    display_name = "Marle Lose Equip Heavy Armor Percent"
    range_start = 0
    range_end = 100
    default = 0


class LuccaGainEquipHeavyArmorPercent(Range):
    """Chance for lucca to gain use of heavy_armor type gear (random_type scheme)"""
    display_name = "Lucca Gain Equip Heavy Armor Percent"
    range_start = 0
    range_end = 100
    default = 0


class LuccaLoseEquipHeavyArmorPercent(Range):
    """Chance for lucca to lose use of heavy_armor type gear (random_type scheme)"""
    display_name = "Lucca Lose Equip Heavy Armor Percent"
    range_start = 0
    range_end = 100
    default = 0


class RoboGainEquipHeavyArmorPercent(Range):
    """Chance for robo to gain use of heavy_armor type gear (random_type scheme)"""
    display_name = "Robo Gain Equip Heavy Armor Percent"
    range_start = 0
    range_end = 100
    default = 0


class RoboLoseEquipHeavyArmorPercent(Range):
    """Chance for robo to lose use of heavy_armor type gear (random_type scheme)"""
    display_name = "Robo Lose Equip Heavy Armor Percent"
    range_start = 0
    range_end = 100
    default = 0


class FrogGainEquipHeavyArmorPercent(Range):
    """Chance for frog to gain use of heavy_armor type gear (random_type scheme)"""
    display_name = "Frog Gain Equip Heavy Armor Percent"
    range_start = 0
    range_end = 100
    default = 0


class FrogLoseEquipHeavyArmorPercent(Range):
    """Chance for frog to lose use of heavy_armor type gear (random_type scheme)"""
    display_name = "Frog Lose Equip Heavy Armor Percent"
    range_start = 0
    range_end = 100
    default = 0


class AylaGainEquipHeavyArmorPercent(Range):
    """Chance for ayla to gain use of heavy_armor type gear (random_type scheme)"""
    display_name = "Ayla Gain Equip Heavy Armor Percent"
    range_start = 0
    range_end = 100
    default = 0


class AylaLoseEquipHeavyArmorPercent(Range):
    """Chance for ayla to lose use of heavy_armor type gear (random_type scheme)"""
    display_name = "Ayla Lose Equip Heavy Armor Percent"
    range_start = 0
    range_end = 100
    default = 0


class MagusGainEquipHeavyArmorPercent(Range):
    """Chance for magus to gain use of heavy_armor type gear (random_type scheme)"""
    display_name = "Magus Gain Equip Heavy Armor Percent"
    range_start = 0
    range_end = 100
    default = 0


class MagusLoseEquipHeavyArmorPercent(Range):
    """Chance for magus to lose use of heavy_armor type gear (random_type scheme)"""
    display_name = "Magus Lose Equip Heavy Armor Percent"
    range_start = 0
    range_end = 100
    default = 0


class CronoGainEquipPersonalPercent(Range):
    """Chance for crono to gain use of personal type gear (random_type scheme)"""
    display_name = "Crono Gain Equip Personal Percent"
    range_start = 0
    range_end = 100
    default = 0


class CronoLoseEquipPersonalPercent(Range):
    """Chance for crono to lose use of personal type gear (random_type scheme)"""
    display_name = "Crono Lose Equip Personal Percent"
    range_start = 0
    range_end = 100
    default = 0


class MarleGainEquipPersonalPercent(Range):
    """Chance for marle to gain use of personal type gear (random_type scheme)"""
    display_name = "Marle Gain Equip Personal Percent"
    range_start = 0
    range_end = 100
    default = 0


class MarleLoseEquipPersonalPercent(Range):
    """Chance for marle to lose use of personal type gear (random_type scheme)"""
    display_name = "Marle Lose Equip Personal Percent"
    range_start = 0
    range_end = 100
    default = 0


class LuccaGainEquipPersonalPercent(Range):
    """Chance for lucca to gain use of personal type gear (random_type scheme)"""
    display_name = "Lucca Gain Equip Personal Percent"
    range_start = 0
    range_end = 100
    default = 0


class LuccaLoseEquipPersonalPercent(Range):
    """Chance for lucca to lose use of personal type gear (random_type scheme)"""
    display_name = "Lucca Lose Equip Personal Percent"
    range_start = 0
    range_end = 100
    default = 0


class RoboGainEquipPersonalPercent(Range):
    """Chance for robo to gain use of personal type gear (random_type scheme)"""
    display_name = "Robo Gain Equip Personal Percent"
    range_start = 0
    range_end = 100
    default = 0


class RoboLoseEquipPersonalPercent(Range):
    """Chance for robo to lose use of personal type gear (random_type scheme)"""
    display_name = "Robo Lose Equip Personal Percent"
    range_start = 0
    range_end = 100
    default = 0


class FrogGainEquipPersonalPercent(Range):
    """Chance for frog to gain use of personal type gear (random_type scheme)"""
    display_name = "Frog Gain Equip Personal Percent"
    range_start = 0
    range_end = 100
    default = 0


class FrogLoseEquipPersonalPercent(Range):
    """Chance for frog to lose use of personal type gear (random_type scheme)"""
    display_name = "Frog Lose Equip Personal Percent"
    range_start = 0
    range_end = 100
    default = 0


class AylaGainEquipPersonalPercent(Range):
    """Chance for ayla to gain use of personal type gear (random_type scheme)"""
    display_name = "Ayla Gain Equip Personal Percent"
    range_start = 0
    range_end = 100
    default = 0


class AylaLoseEquipPersonalPercent(Range):
    """Chance for ayla to lose use of personal type gear (random_type scheme)"""
    display_name = "Ayla Lose Equip Personal Percent"
    range_start = 0
    range_end = 100
    default = 0


class MagusGainEquipPersonalPercent(Range):
    """Chance for magus to gain use of personal type gear (random_type scheme)"""
    display_name = "Magus Gain Equip Personal Percent"
    range_start = 0
    range_end = 100
    default = 0


class MagusLoseEquipPersonalPercent(Range):
    """Chance for magus to lose use of personal type gear (random_type scheme)"""
    display_name = "Magus Lose Equip Personal Percent"
    range_start = 0
    range_end = 100
    default = 0


class CronoCanEquipPercent(Range):
    """Chance for crono to be able to equip an armor (random_all scheme)"""
    display_name = "Crono Can Equip Percent"
    range_start = 0
    range_end = 100
    default = 0


class MarleCanEquipPercent(Range):
    """Chance for marle to be able to equip an armor (random_all scheme)"""
    display_name = "Marle Can Equip Percent"
    range_start = 0
    range_end = 100
    default = 0


class LuccaCanEquipPercent(Range):
    """Chance for lucca to be able to equip an armor (random_all scheme)"""
    display_name = "Lucca Can Equip Percent"
    range_start = 0
    range_end = 100
    default = 0


class RoboCanEquipPercent(Range):
    """Chance for robo to be able to equip an armor (random_all scheme)"""
    display_name = "Robo Can Equip Percent"
    range_start = 0
    range_end = 100
    default = 0


class FrogCanEquipPercent(Range):
    """Chance for frog to be able to equip an armor (random_all scheme)"""
    display_name = "Frog Can Equip Percent"
    range_start = 0
    range_end = 100
    default = 0


class AylaCanEquipPercent(Range):
    """Chance for ayla to be able to equip an armor (random_all scheme)"""
    display_name = "Ayla Can Equip Percent"
    range_start = 0
    range_end = 100
    default = 0


class MagusCanEquipPercent(Range):
    """Chance for magus to be able to equip an armor (random_all scheme)"""
    display_name = "Magus Can Equip Percent"
    range_start = 0
    range_end = 100
    default = 0


@dataclass
class CTRDIOptions(PerGameCommonOptions):
    xp_scale: XpScale
    tp_scale: TpScale
    split_tp: SplitTp
    fix_tp_doubling: FixTpDoubling
    xp_penalty_level: XpPenaltyLevel
    xp_penalty_percent: XpPenaltyPercent
    level_cap: LevelCap
    boss_xp_factor: BossXpFactor
    midboss_reward_factor: MidbossRewardFactor
    normalize_boss_xp: NormalizeBossXp
    drop_enemy_pool: DropEnemyPool
    drop_reward_pool: DropRewardPool
    drop_rate: DropRate
    custom_drop_enemy_pool: CustomDropEnemyPool
    custom_drop_reward_pool: CustomDropRewardPool
    drop_enemy_pool_2: DropEnemyPool2
    drop_reward_pool_2: DropRewardPool2
    drop_rate_2: DropRate2
    custom_drop_enemy_pool_2: CustomDropEnemyPool2
    custom_drop_reward_pool_2: CustomDropRewardPool2
    drop_enemy_pool_3: DropEnemyPool3
    drop_reward_pool_3: DropRewardPool3
    drop_rate_3: DropRate3
    custom_drop_enemy_pool_3: CustomDropEnemyPool3
    custom_drop_reward_pool_3: CustomDropRewardPool3
    drop_enemy_pool_4: DropEnemyPool4
    drop_reward_pool_4: DropRewardPool4
    drop_rate_4: DropRate4
    custom_drop_enemy_pool_4: CustomDropEnemyPool4
    custom_drop_reward_pool_4: CustomDropRewardPool4
    mark_dropping_enemies: MarkDroppingEnemies
    charm_enemy_pool: CharmEnemyPool
    charm_reward_pool: CharmRewardPool
    charm_rate: CharmRate
    custom_charm_enemy_pool: CustomCharmEnemyPool
    custom_charm_reward_pool: CustomCharmRewardPool
    charm_enemy_pool_2: CharmEnemyPool2
    charm_reward_pool_2: CharmRewardPool2
    charm_rate_2: CharmRate2
    custom_charm_enemy_pool_2: CustomCharmEnemyPool2
    custom_charm_reward_pool_2: CustomCharmRewardPool2
    charm_enemy_pool_3: CharmEnemyPool3
    charm_reward_pool_3: CharmRewardPool3
    charm_rate_3: CharmRate3
    custom_charm_enemy_pool_3: CustomCharmEnemyPool3
    custom_charm_reward_pool_3: CustomCharmRewardPool3
    charm_enemy_pool_4: CharmEnemyPool4
    charm_reward_pool_4: CharmRewardPool4
    charm_rate_4: CharmRate4
    custom_charm_enemy_pool_4: CustomCharmEnemyPool4
    custom_charm_reward_pool_4: CustomCharmRewardPool4
    mark_charmable_enemies: MarkCharmableEnemies
    tech_order: TechOrder
    tech_damage: TechDamage
    tech_damage_random_factor_min: TechDamageRandomFactorMin
    tech_damage_random_factor_max: TechDamageRandomFactorMax
    preserve_magic: PreserveMagic
    black_hole_factor: BlackHoleFactor
    black_hole_min: BlackHoleMin
    show_full_tech_list: ShowFullTechList
    balance_tech_mps: BalanceTechMps
    custom_damage_mps: CustomDamageMps
    normalize_techs: NormalizeTechs
    dynamic_scaling_scheme: DynamicScalingScheme
    levels_per_boss: LevelsPerBoss
    levels_per_quest: LevelsPerQuest
    levels_per_key_item: LevelsPerKeyItem
    levels_per_objective: LevelsPerObjective
    levels_per_character: LevelsPerCharacter
    max_scaling_level: MaxScalingLevel
    dynamic_scale_lavos: DynamicScaleLavos
    dynamic_scale_lavos_gauntlet: DynamicScaleLavosGauntlet
    defense_safety_min_level: DefenseSafetyMinLevel
    defense_safety_max_level: DefenseSafetyMaxLevel
    obstacle_safety_level: ObstacleSafetyLevel
    normal_enemy_hp_scale: NormalEnemyHpScale
    static_boss_hp_scale: StaticBossHpScale
    static_hp_scale_lavos: StaticHpScaleLavos
    element_safety_level: ElementSafetyLevel
    millennial_fair_mod: MillennialFairMod
    guardia_forest_1000_mod: GuardiaForest1000Mod
    guardia_forest_600_mod: GuardiaForest600Mod
    crono_trial_mod: CronoTrialMod
    heckran_cave_mod: HeckranCaveMod
    truce_canyon_mod: TruceCanyonMod
    manoria_cathedral_mod: ManoriaCathedralMod
    denadoro_mountains_mod: DenadoroMountainsMod
    cursed_woods_mod: CursedWoodsMod
    lab_16_mod: Lab16Mod
    lab_32_mod: Lab32Mod
    sewers_mod: SewersMod
    death_peak_mod: DeathPeakMod
    arris_dome_mod: ArrisDomeMod
    proto_dome_mod: ProtoDomeMod
    factory_ruins_mod: FactoryRuinsMod
    mystic_mountains_mod: MysticMountainsMod
    hunting_range_mod: HuntingRangeMod
    dactyl_nest_mod: DactylNestMod
    shell_trial_mod: ShellTrialMod
    zenan_bridge_mod: ZenanBridgeMod
    northern_ruins_mod: NorthernRuinsMod
    giants_claw_mod: GiantsClawMod
    ozzies_fort_mod: OzziesFortMod
    magus_castle_mod: MagusCastleMod
    magic_cave_mod: MagicCaveMod
    sunken_desert_mod: SunkenDesertMod
    sun_palace_mod: SunPalaceMod
    geno_dome_mod: GenoDomeMod
    forest_maze_mod: ForestMazeMod
    reptite_lair_mod: ReptiteLairMod
    tyrano_lair_mod: TyranoLairMod
    black_omen_mod: BlackOmenMod
    north_cape_mod: NorthCapeMod
    epoch_battle_mod: EpochBattleMod
    blackbird_mod: BlackbirdMod
    enhasa_mod: EnhasaMod
    ocean_palace_mod: OceanPalaceMod
    mt_woe_mod: MtWoeMod
    additional_key_items: AdditionalKeyItems
    forced_spots: ForcedSpots
    loose_key_items: LooseKeyItems
    incentive_spots: IncentiveSpots
    incentive_factor: IncentiveFactor
    excluded_spots: ExcludedSpots
    decay_factor: DecayFactor
    starter_rewards: StarterRewards
    out_of_logic_starter_rewards: OutOfLogicStarterRewards
    hard_lavos_end_boss: HardLavosEndBoss
    boats_of_time: BoatsOfTime
    jets_of_time: JetsOfTime
    min_flight_depth: MinFlightDepth
    lock_gates: LockGates
    disable_element_locks: DisableElementLocks
    block_zenan_600: BlockZenan600
    block_zenan_1000: BlockZenan1000
    boss_randomization_type: BossRandomizationType
    midboss_randomization_type: MidbossRandomizationType
    vanilla_boss_spots: VanillaBossSpots
    boss_pool: BossPool
    midboss_pool: MidbossPool
    shop_inventory_randomization: ShopInventoryRandomization
    shop_capacity_randomization: ShopCapacityRandomization
    not_buyable_items: NotBuyableItems
    not_sellable_items: NotSellableItems
    item_base_prices: ItemBasePrices
    item_price_randomization: ItemPriceRandomization
    item_price_min_multiplier: ItemPriceMinMultiplier
    item_price_max_multiplier: ItemPriceMaxMultiplier
    guaranteed_shop_items: GuaranteedShopItems
    custom_shop_item_spec: CustomShopItemSpec
    show_all_chars_in_shop: ShowAllCharsInShop
    num_algetty_portal_objectives: NumAlgettyPortalObjectives
    num_omen_objectives: NumOmenObjectives
    num_bucket_objectives: NumBucketObjectives
    num_gauntlet_objectives: NumGauntletObjectives
    num_timegauge_objectives: NumTimegaugeObjectives
    no_omen_gauntlet: NoOmenGauntlet
    objective_1: Objective1
    objective_2: Objective2
    objective_3: Objective3
    objective_4: Objective4
    objective_5: Objective5
    objective_6: Objective6
    objective_7: Objective7
    objective_8: Objective8
    shuffle_entrances: ShuffleEntrances
    preserve_spots: PreserveSpots
    rest_vanilla: RestVanilla
    vanilla_spots: VanillaSpots
    shuffle_gates: ShuffleGates
    separate_gate_eras: SeparateGateEras
    lair_ruins_default_spot: LairRuinsDefaultSpot
    preserve_spots_1: PreserveSpots1
    preserve_spots_2: PreserveSpots2
    preserve_spots_3: PreserveSpots3
    preserve_spots_4: PreserveSpots4
    starter_min_level: StarterMinLevel
    starter_min_techlevel: StarterMinTechlevel
    fair_min_level: FairMinLevel
    fair_min_techlevel: FairMinTechlevel
    cathedral_min_level: CathedralMinLevel
    cathedral_min_techlevel: CathedralMinTechlevel
    castle_min_level: CastleMinLevel
    castle_min_techlevel: CastleMinTechlevel
    trial_min_level: TrialMinLevel
    trial_min_techlevel: TrialMinTechlevel
    proto_min_level: ProtoMinLevel
    proto_min_techlevel: ProtoMinTechlevel
    north_cape_min_level: NorthCapeMinLevel
    north_cape_min_techlevel: NorthCapeMinTechlevel
    burrow_min_level: BurrowMinLevel
    burrow_min_techlevel: BurrowMinTechlevel
    dactyl_min_level: DactylMinLevel
    dactyl_min_techlevel: DactylMinTechlevel
    death_peak_min_level: DeathPeakMinLevel
    death_peak_min_techlevel: DeathPeakMinTechlevel
    yakra_box_min_level: YakraBoxMinLevel
    yakra_box_min_techlevel: YakraBoxMinTechlevel
    minimum_recruits: MinimumRecruits
    scale_level_to_leader: ScaleLevelToLeader
    scale_techlevel_to_leader: ScaleTechlevelToLeader
    scale_gear: ScaleGear
    loot_pool: LootPool
    custom_loot_pool: CustomLootPool
    loot_assignment_scheme: LootAssignmentScheme
    good_loot: GoodLoot
    good_loot_spots: GoodLootSpots
    good_loot_rate: GoodLootRate
    post_assign_shuffle_rate: PostAssignShuffleRate
    trading_post_base_cost: TradingPostBaseCost
    trading_post_upgrade_cost: TradingPostUpgradeCost
    trading_post_special_cost: TradingPostSpecialCost
    johnny_key_threshold: JohnnyKeyThreshold
    johnny_low_threshold: JohnnyLowThreshold
    johnny_low_item: JohnnyLowItem
    johnny_low_quantity: JohnnyLowQuantity
    johnny_mid_threshold: JohnnyMidThreshold
    johnny_mid_item: JohnnyMidItem
    johnny_mid_quantity: JohnnyMidQuantity
    johnny_high_threshold: JohnnyHighThreshold
    johnny_high_item: JohnnyHighItem
    johnny_high_quantity: JohnnyHighQuantity
    use_tech_level_treasures: UseTechLevelTreasures
    extra_tech_levels_per_char: ExtraTechLevelsPerChar
    tech_level_forced_spots: TechLevelForcedSpots
    guaranteed_loot: GuaranteedLoot
    guaranteed_loot_exact: GuaranteedLootExact
    good_loot_2: GoodLoot2
    good_loot_spots_2: GoodLootSpots2
    good_loot_rate_2: GoodLootRate2
    good_loot_3: GoodLoot3
    good_loot_spots_3: GoodLootSpots3
    good_loot_rate_3: GoodLootRate3
    good_loot_4: GoodLoot4
    good_loot_spots_4: GoodLootSpots4
    good_loot_rate_4: GoodLootRate4
    good_loot_5: GoodLoot5
    good_loot_spots_5: GoodLootSpots5
    good_loot_rate_5: GoodLootRate5
    good_loot_6: GoodLoot6
    good_loot_spots_6: GoodLootSpots6
    good_loot_rate_6: GoodLootRate6
    good_loot_7: GoodLoot7
    good_loot_spots_7: GoodLootSpots7
    good_loot_rate_7: GoodLootRate7
    good_loot_8: GoodLoot8
    good_loot_spots_8: GoodLootSpots8
    good_loot_rate_8: GoodLootRate8
    sightscope_all: SightscopeAll
    forced_sightscope: ForcedSightscope
    shuffle_enemies: ShuffleEnemies
    normalize_enemies: NormalizeEnemies
    default_fast_loc_movement: DefaultFastLocMovement
    default_fast_ow_movement: DefaultFastOwMovement
    default_fast_epoch_movement: DefaultFastEpochMovement
    battle_speed: BattleSpeed
    message_speed: MessageSpeed
    battle_memory_cursor: BattleMemoryCursor
    menu_memory_cursor: MenuMemoryCursor
    window_background: WindowBackground
    use_l_select_warp: UseLSelectWarp
    use_msu1: UseMsu1
    crono_palette: CronoPalette
    marle_palette: MarlePalette
    lucca_palette: LuccaPalette
    robo_palette: RoboPalette
    frog_palette: FrogPalette
    ayla_palette: AylaPalette
    magus_palette: MagusPalette
    remove_flashes: RemoveFlashes
    alt_lightning2: AltLightning2
    ds_item_pool: DsItemPool
    ds_replacement_chance: DsReplacementChance
    bronze_fist_policy: BronzeFistPolicy
    weapon_rando_pool: WeaponRandoPool
    weapon_rando_effect_scheme: WeaponRandoEffectScheme
    weapon_rando_stat_boost_scheme: WeaponRandoStatBoostScheme
    forced_weapon_effects: ForcedWeaponEffects
    forced_weapon_stat_boosts: ForcedWeaponStatBoosts
    random_weapon_effect_spec: RandomWeaponEffectSpec
    random_weapon_stat_boost_spec: RandomWeaponStatBoostSpec
    weapon_rando_pool_2: WeaponRandoPool2
    weapon_rando_effect_scheme_2: WeaponRandoEffectScheme2
    weapon_rando_stat_boost_scheme_2: WeaponRandoStatBoostScheme2
    forced_weapon_effects_2: ForcedWeaponEffects2
    forced_weapon_stat_boosts_2: ForcedWeaponStatBoosts2
    random_weapon_effect_spec_2: RandomWeaponEffectSpec2
    random_weapon_stat_boost_spec_2: RandomWeaponStatBoostSpec2
    weapon_rando_pool_3: WeaponRandoPool3
    weapon_rando_effect_scheme_3: WeaponRandoEffectScheme3
    weapon_rando_stat_boost_scheme_3: WeaponRandoStatBoostScheme3
    forced_weapon_effects_3: ForcedWeaponEffects3
    forced_weapon_stat_boosts_3: ForcedWeaponStatBoosts3
    random_weapon_effect_spec_3: RandomWeaponEffectSpec3
    random_weapon_stat_boost_spec_3: RandomWeaponStatBoostSpec3
    use_phys_marle: UsePhysMarle
    use_haste_all: UseHasteAll
    use_phys_lucca: UsePhysLucca
    use_protect_all: UseProtectAll
    use_reraise: UseReraise
    use_magus_dual_techs: UseMagusDualTechs
    use_daltonized_magus: UseDaltonizedMagus
    tech_rando_scheme: TechRandoScheme
    mdef_growth_scale_factor: MdefGrowthScaleFactor
    mdef_cap: MdefCap
    mdef_levelup_cap: MdefLevelupCap
    dalton_level: DaltonLevel
    dalton_plus_level: DaltonPlusLevel
    elder_spawn_level: ElderSpawnLevel
    flea_level: FleaLevel
    giga_mutant_level: GigaMutantLevel
    golem_level: GolemLevel
    golem_boss_level: GolemBossLevel
    heckran_level: HeckranLevel
    lavos_spawn_level: LavosSpawnLevel
    mammon_machine_level: MammonMachineLevel
    magus_nc_level: MagusNcLevel
    masa_mune_level: MasaMuneLevel
    mega_mutant_level: MegaMutantLevel
    mud_imp_level: MudImpLevel
    nizbel_level: NizbelLevel
    nizbel_2_level: Nizbel2Level
    retinite_level: RetiniteLevel
    r_series_level: RSeriesLevel
    rust_tyrano_level: RustTyranoLevel
    slash_level: SlashLevel
    son_of_sun_level: SonOfSunLevel
    terra_mutant_level: TerraMutantLevel
    yakra_level: YakraLevel
    yakra_xiii_level: YakraXiiiLevel
    zombor_level: ZomborLevel
    dragon_tank_level: DragonTankLevel
    giga_gaia_level: GigaGaiaLevel
    guardian_level: GuardianLevel
    magus_level: MagusLevel
    black_tyrano_level: BlackTyranoLevel
    ozzie_trio_level: OzzieTrioLevel
    atropos_level: AtroposLevel
    flea_plus_level: FleaPlusLevel
    super_slash_level: SuperSlashLevel
    krawlie_level: KrawlieLevel
    gato_level: GatoLevel
    zeal2_level: Zeal2Level
    equipable_rando_scheme: EquipableRandoScheme
    crono_lose_equip_normal_percent: CronoLoseEquipNormalPercent
    marle_lose_equip_normal_percent: MarleLoseEquipNormalPercent
    lucca_lose_equip_normal_percent: LuccaLoseEquipNormalPercent
    robo_lose_equip_normal_percent: RoboLoseEquipNormalPercent
    frog_lose_equip_normal_percent: FrogLoseEquipNormalPercent
    ayla_lose_equip_normal_percent: AylaLoseEquipNormalPercent
    magus_lose_equip_normal_percent: MagusLoseEquipNormalPercent
    crono_gain_equip_dress_percent: CronoGainEquipDressPercent
    crono_lose_equip_dress_percent: CronoLoseEquipDressPercent
    marle_gain_equip_dress_percent: MarleGainEquipDressPercent
    marle_lose_equip_dress_percent: MarleLoseEquipDressPercent
    lucca_gain_equip_dress_percent: LuccaGainEquipDressPercent
    lucca_lose_equip_dress_percent: LuccaLoseEquipDressPercent
    robo_gain_equip_dress_percent: RoboGainEquipDressPercent
    robo_lose_equip_dress_percent: RoboLoseEquipDressPercent
    frog_gain_equip_dress_percent: FrogGainEquipDressPercent
    frog_lose_equip_dress_percent: FrogLoseEquipDressPercent
    ayla_gain_equip_dress_percent: AylaGainEquipDressPercent
    ayla_lose_equip_dress_percent: AylaLoseEquipDressPercent
    magus_gain_equip_dress_percent: MagusGainEquipDressPercent
    magus_lose_equip_dress_percent: MagusLoseEquipDressPercent
    crono_gain_equip_heavy_armor_percent: CronoGainEquipHeavyArmorPercent
    crono_lose_equip_heavy_armor_percent: CronoLoseEquipHeavyArmorPercent
    marle_gain_equip_heavy_armor_percent: MarleGainEquipHeavyArmorPercent
    marle_lose_equip_heavy_armor_percent: MarleLoseEquipHeavyArmorPercent
    lucca_gain_equip_heavy_armor_percent: LuccaGainEquipHeavyArmorPercent
    lucca_lose_equip_heavy_armor_percent: LuccaLoseEquipHeavyArmorPercent
    robo_gain_equip_heavy_armor_percent: RoboGainEquipHeavyArmorPercent
    robo_lose_equip_heavy_armor_percent: RoboLoseEquipHeavyArmorPercent
    frog_gain_equip_heavy_armor_percent: FrogGainEquipHeavyArmorPercent
    frog_lose_equip_heavy_armor_percent: FrogLoseEquipHeavyArmorPercent
    ayla_gain_equip_heavy_armor_percent: AylaGainEquipHeavyArmorPercent
    ayla_lose_equip_heavy_armor_percent: AylaLoseEquipHeavyArmorPercent
    magus_gain_equip_heavy_armor_percent: MagusGainEquipHeavyArmorPercent
    magus_lose_equip_heavy_armor_percent: MagusLoseEquipHeavyArmorPercent
    crono_gain_equip_personal_percent: CronoGainEquipPersonalPercent
    crono_lose_equip_personal_percent: CronoLoseEquipPersonalPercent
    marle_gain_equip_personal_percent: MarleGainEquipPersonalPercent
    marle_lose_equip_personal_percent: MarleLoseEquipPersonalPercent
    lucca_gain_equip_personal_percent: LuccaGainEquipPersonalPercent
    lucca_lose_equip_personal_percent: LuccaLoseEquipPersonalPercent
    robo_gain_equip_personal_percent: RoboGainEquipPersonalPercent
    robo_lose_equip_personal_percent: RoboLoseEquipPersonalPercent
    frog_gain_equip_personal_percent: FrogGainEquipPersonalPercent
    frog_lose_equip_personal_percent: FrogLoseEquipPersonalPercent
    ayla_gain_equip_personal_percent: AylaGainEquipPersonalPercent
    ayla_lose_equip_personal_percent: AylaLoseEquipPersonalPercent
    magus_gain_equip_personal_percent: MagusGainEquipPersonalPercent
    magus_lose_equip_personal_percent: MagusLoseEquipPersonalPercent
    crono_can_equip_percent: CronoCanEquipPercent
    marle_can_equip_percent: MarleCanEquipPercent
    lucca_can_equip_percent: LuccaCanEquipPercent
    robo_can_equip_percent: RoboCanEquipPercent
    frog_can_equip_percent: FrogCanEquipPercent
    ayla_can_equip_percent: AylaCanEquipPercent
    magus_can_equip_percent: MagusCanEquipPercent


option_groups: list[OptionGroup] = [

    OptionGroup(
        "Battle Rewards",
        [
            XpScale,
            TpScale,
            SplitTp,
            FixTpDoubling,
            XpPenaltyLevel,
            XpPenaltyPercent,
            LevelCap,
            BossXpFactor,
            MidbossRewardFactor,
            NormalizeBossXp,
            DropEnemyPool,
            DropRewardPool,
            DropRate,
            CustomDropEnemyPool,
            CustomDropRewardPool,
            DropEnemyPool2,
            DropRewardPool2,
            DropRate2,
            CustomDropEnemyPool2,
            CustomDropRewardPool2,
            DropEnemyPool3,
            DropRewardPool3,
            DropRate3,
            CustomDropEnemyPool3,
            CustomDropRewardPool3,
            DropEnemyPool4,
            DropRewardPool4,
            DropRate4,
            CustomDropEnemyPool4,
            CustomDropRewardPool4,
            MarkDroppingEnemies,
            CharmEnemyPool,
            CharmRewardPool,
            CharmRate,
            CustomCharmEnemyPool,
            CustomCharmRewardPool,
            CharmEnemyPool2,
            CharmRewardPool2,
            CharmRate2,
            CustomCharmEnemyPool2,
            CustomCharmRewardPool2,
            CharmEnemyPool3,
            CharmRewardPool3,
            CharmRate3,
            CustomCharmEnemyPool3,
            CustomCharmRewardPool3,
            CharmEnemyPool4,
            CharmRewardPool4,
            CharmRate4,
            CustomCharmEnemyPool4,
            CustomCharmRewardPool4,
            MarkCharmableEnemies,

        ]
    ),

    OptionGroup(
        "Tech Options",
        [
            TechOrder,
            TechDamage,
            TechDamageRandomFactorMin,
            TechDamageRandomFactorMax,
            PreserveMagic,
            BlackHoleFactor,
            BlackHoleMin,
            ShowFullTechList,
            BalanceTechMps,
            CustomDamageMps,
            NormalizeTechs,

        ]
    ),

    OptionGroup(
        "Scaling Options",
        [
            DynamicScalingScheme,
            LevelsPerBoss,
            LevelsPerQuest,
            LevelsPerKeyItem,
            LevelsPerObjective,
            LevelsPerCharacter,
            MaxScalingLevel,
            DynamicScaleLavos,
            DynamicScaleLavosGauntlet,
            DefenseSafetyMinLevel,
            DefenseSafetyMaxLevel,
            ObstacleSafetyLevel,
            NormalEnemyHpScale,
            StaticBossHpScale,
            StaticHpScaleLavos,
            ElementSafetyLevel,
            MillennialFairMod,
            GuardiaForest1000Mod,
            GuardiaForest600Mod,
            CronoTrialMod,
            HeckranCaveMod,
            TruceCanyonMod,
            ManoriaCathedralMod,
            DenadoroMountainsMod,
            CursedWoodsMod,
            Lab16Mod,
            Lab32Mod,
            SewersMod,
            DeathPeakMod,
            ArrisDomeMod,
            ProtoDomeMod,
            FactoryRuinsMod,
            MysticMountainsMod,
            HuntingRangeMod,
            DactylNestMod,
            ShellTrialMod,
            ZenanBridgeMod,
            NorthernRuinsMod,
            GiantsClawMod,
            OzziesFortMod,
            MagusCastleMod,
            MagicCaveMod,
            SunkenDesertMod,
            SunPalaceMod,
            GenoDomeMod,
            ForestMazeMod,
            ReptiteLairMod,
            TyranoLairMod,
            BlackOmenMod,
            NorthCapeMod,
            EpochBattleMod,
            BlackbirdMod,
            EnhasaMod,
            OceanPalaceMod,
            MtWoeMod,

        ]
    ),

    OptionGroup(
        "Logic Options",
        [
            AdditionalKeyItems,
            ForcedSpots,
            LooseKeyItems,
            IncentiveSpots,
            IncentiveFactor,
            ExcludedSpots,
            DecayFactor,
            StarterRewards,
            OutOfLogicStarterRewards,
            HardLavosEndBoss,
            BoatsOfTime,
            JetsOfTime,
            MinFlightDepth,
            LockGates,
            DisableElementLocks,
            BlockZenan600,
            BlockZenan1000,

        ]
    ),

    OptionGroup(
        "Boss Rando Options",
        [
            BossRandomizationType,
            MidbossRandomizationType,
            VanillaBossSpots,
            BossPool,
            MidbossPool,

        ]
    ),

    OptionGroup(
        "Shop Options",
        [
            ShopInventoryRandomization,
            ShopCapacityRandomization,
            NotBuyableItems,
            NotSellableItems,
            ItemBasePrices,
            ItemPriceRandomization,
            ItemPriceMinMultiplier,
            ItemPriceMaxMultiplier,
            GuaranteedShopItems,
            CustomShopItemSpec,
            ShowAllCharsInShop,

        ]
    ),

    OptionGroup(
        "Objective Options",
        [
            NumAlgettyPortalObjectives,
            NumOmenObjectives,
            NumBucketObjectives,
            NumGauntletObjectives,
            NumTimegaugeObjectives,
            NoOmenGauntlet,
            Objective1,
            Objective2,
            Objective3,
            Objective4,
            Objective5,
            Objective6,
            Objective7,
            Objective8,

        ]
    ),

    OptionGroup(
        "Entrance Options",
        [
            ShuffleEntrances,
            PreserveSpots,
            RestVanilla,
            VanillaSpots,
            ShuffleGates,
            SeparateGateEras,
            LairRuinsDefaultSpot,
            PreserveSpots1,
            PreserveSpots2,
            PreserveSpots3,
            PreserveSpots4,

        ]
    ),

    OptionGroup(
        "Recruit Options",
        [
            StarterMinLevel,
            StarterMinTechlevel,
            FairMinLevel,
            FairMinTechlevel,
            CathedralMinLevel,
            CathedralMinTechlevel,
            CastleMinLevel,
            CastleMinTechlevel,
            TrialMinLevel,
            TrialMinTechlevel,
            ProtoMinLevel,
            ProtoMinTechlevel,
            NorthCapeMinLevel,
            NorthCapeMinTechlevel,
            BurrowMinLevel,
            BurrowMinTechlevel,
            DactylMinLevel,
            DactylMinTechlevel,
            DeathPeakMinLevel,
            DeathPeakMinTechlevel,
            YakraBoxMinLevel,
            YakraBoxMinTechlevel,
            MinimumRecruits,
            ScaleLevelToLeader,
            ScaleTechlevelToLeader,
            ScaleGear,

        ]
    ),

    OptionGroup(
        "Treasure Options",
        [
            LootPool,
            CustomLootPool,
            LootAssignmentScheme,
            GoodLoot,
            GoodLootSpots,
            GoodLootRate,
            PostAssignShuffleRate,
            TradingPostBaseCost,
            TradingPostUpgradeCost,
            TradingPostSpecialCost,
            JohnnyKeyThreshold,
            JohnnyLowThreshold,
            JohnnyLowItem,
            JohnnyLowQuantity,
            JohnnyMidThreshold,
            JohnnyMidItem,
            JohnnyMidQuantity,
            JohnnyHighThreshold,
            JohnnyHighItem,
            JohnnyHighQuantity,
            UseTechLevelTreasures,
            ExtraTechLevelsPerChar,
            TechLevelForcedSpots,
            GuaranteedLoot,
            GuaranteedLootExact,
            GoodLoot2,
            GoodLootSpots2,
            GoodLootRate2,
            GoodLoot3,
            GoodLootSpots3,
            GoodLootRate3,
            GoodLoot4,
            GoodLootSpots4,
            GoodLootRate4,
            GoodLoot5,
            GoodLootSpots5,
            GoodLootRate5,
            GoodLoot6,
            GoodLootSpots6,
            GoodLootRate6,
            GoodLoot7,
            GoodLootSpots7,
            GoodLootRate7,
            GoodLoot8,
            GoodLootSpots8,
            GoodLootRate8,

        ]
    ),

    OptionGroup(
        "Enemy Options",
        [
            SightscopeAll,
            ForcedSightscope,
            ShuffleEnemies,
            NormalizeEnemies,

        ]
    ),

    OptionGroup(
        "Post Rando Options",
        [
            DefaultFastLocMovement,
            DefaultFastOwMovement,
            DefaultFastEpochMovement,
            BattleSpeed,
            MessageSpeed,
            BattleMemoryCursor,
            MenuMemoryCursor,
            WindowBackground,
            UseLSelectWarp,
            UseMsu1,
            CronoPalette,
            MarlePalette,
            LuccaPalette,
            RoboPalette,
            FrogPalette,
            AylaPalette,
            MagusPalette,
            RemoveFlashes,
            AltLightning2,

        ]
    ),

    OptionGroup(
        "Gear Rando Options",
        [
            DsItemPool,
            DsReplacementChance,
            BronzeFistPolicy,
            WeaponRandoPool,
            WeaponRandoEffectScheme,
            WeaponRandoStatBoostScheme,
            ForcedWeaponEffects,
            ForcedWeaponStatBoosts,
            RandomWeaponEffectSpec,
            RandomWeaponStatBoostSpec,
            WeaponRandoPool2,
            WeaponRandoEffectScheme2,
            WeaponRandoStatBoostScheme2,
            ForcedWeaponEffects2,
            ForcedWeaponStatBoosts2,
            RandomWeaponEffectSpec2,
            RandomWeaponStatBoostSpec2,
            WeaponRandoPool3,
            WeaponRandoEffectScheme3,
            WeaponRandoStatBoostScheme3,
            ForcedWeaponEffects3,
            ForcedWeaponStatBoosts3,
            RandomWeaponEffectSpec3,
            RandomWeaponStatBoostSpec3,

        ]
    ),

    OptionGroup(
        "Character Options",
        [
            UsePhysMarle,
            UseHasteAll,
            UsePhysLucca,
            UseProtectAll,
            UseReraise,
            UseMagusDualTechs,
            UseDaltonizedMagus,
            TechRandoScheme,
            MdefGrowthScaleFactor,
            MdefCap,
            MdefLevelupCap,

        ]
    ),

    OptionGroup(
        "Boss Scaling Options",
        [
            DaltonLevel,
            DaltonPlusLevel,
            ElderSpawnLevel,
            FleaLevel,
            GigaMutantLevel,
            GolemLevel,
            GolemBossLevel,
            HeckranLevel,
            LavosSpawnLevel,
            MammonMachineLevel,
            MagusNcLevel,
            MasaMuneLevel,
            MegaMutantLevel,
            MudImpLevel,
            NizbelLevel,
            Nizbel2Level,
            RetiniteLevel,
            RSeriesLevel,
            RustTyranoLevel,
            SlashLevel,
            SonOfSunLevel,
            TerraMutantLevel,
            YakraLevel,
            YakraXiiiLevel,
            ZomborLevel,
            DragonTankLevel,
            GigaGaiaLevel,
            GuardianLevel,
            MagusLevel,
            BlackTyranoLevel,
            OzzieTrioLevel,
            AtroposLevel,
            FleaPlusLevel,
            SuperSlashLevel,
            KrawlieLevel,
            GatoLevel,
            Zeal2Level,

        ]
    ),

    OptionGroup(
        "Equipable Options",
        [
            EquipableRandoScheme,
            CronoLoseEquipNormalPercent,
            MarleLoseEquipNormalPercent,
            LuccaLoseEquipNormalPercent,
            RoboLoseEquipNormalPercent,
            FrogLoseEquipNormalPercent,
            AylaLoseEquipNormalPercent,
            MagusLoseEquipNormalPercent,
            CronoGainEquipDressPercent,
            CronoLoseEquipDressPercent,
            MarleGainEquipDressPercent,
            MarleLoseEquipDressPercent,
            LuccaGainEquipDressPercent,
            LuccaLoseEquipDressPercent,
            RoboGainEquipDressPercent,
            RoboLoseEquipDressPercent,
            FrogGainEquipDressPercent,
            FrogLoseEquipDressPercent,
            AylaGainEquipDressPercent,
            AylaLoseEquipDressPercent,
            MagusGainEquipDressPercent,
            MagusLoseEquipDressPercent,
            CronoGainEquipHeavyArmorPercent,
            CronoLoseEquipHeavyArmorPercent,
            MarleGainEquipHeavyArmorPercent,
            MarleLoseEquipHeavyArmorPercent,
            LuccaGainEquipHeavyArmorPercent,
            LuccaLoseEquipHeavyArmorPercent,
            RoboGainEquipHeavyArmorPercent,
            RoboLoseEquipHeavyArmorPercent,
            FrogGainEquipHeavyArmorPercent,
            FrogLoseEquipHeavyArmorPercent,
            AylaGainEquipHeavyArmorPercent,
            AylaLoseEquipHeavyArmorPercent,
            MagusGainEquipHeavyArmorPercent,
            MagusLoseEquipHeavyArmorPercent,
            CronoGainEquipPersonalPercent,
            CronoLoseEquipPersonalPercent,
            MarleGainEquipPersonalPercent,
            MarleLoseEquipPersonalPercent,
            LuccaGainEquipPersonalPercent,
            LuccaLoseEquipPersonalPercent,
            RoboGainEquipPersonalPercent,
            RoboLoseEquipPersonalPercent,
            FrogGainEquipPersonalPercent,
            FrogLoseEquipPersonalPercent,
            AylaGainEquipPersonalPercent,
            AylaLoseEquipPersonalPercent,
            MagusGainEquipPersonalPercent,
            MagusLoseEquipPersonalPercent,
            CronoCanEquipPercent,
            MarleCanEquipPercent,
            LuccaCanEquipPercent,
            RoboCanEquipPercent,
            FrogCanEquipPercent,
            AylaCanEquipPercent,
            MagusCanEquipPercent,

        ]
    )
]
