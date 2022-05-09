import os


file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sep = os.path.sep

player_path = file_path + sep + "assets" + sep + "sprites" + sep + "player" + sep
mr_bean_path = file_path + sep + "assets" + sep + "sprites" + sep + "mr_bean" + sep
enemies_path = file_path + sep + "assets" + sep + "sprites" + sep + "enemies" + sep
map_path = file_path + sep + "assets" + sep + "tilemaps" + sep

MR_BEAN_SPRITES = [f"{mr_bean_path}MrBeanCelebrating.png",
                   f"{mr_bean_path}MrBeanOnOneFoot.png",
                   f"{mr_bean_path}MrBeanWaiting.png"]

IDLE_DOWN_SPRITES = [
    f"{player_path}idle_anim{sep}tile000.png",
    f"{player_path}idle_anim{sep}tile001.png",
    f"{player_path}idle_anim{sep}tile002.png",
    f"{player_path}idle_anim{sep}tile003.png",
    f"{player_path}idle_anim{sep}tile004.png",
]

IDLE_UP_SPRITES = [
    f"{player_path}idle_up_anim{sep}tile000.png",
    f"{player_path}idle_up_anim{sep}tile001.png",
    f"{player_path}idle_up_anim{sep}tile002.png",
    f"{player_path}idle_up_anim{sep}tile003.png",
    f"{player_path}idle_up_anim{sep}tile004.png",
]

IDLE_SIDE_SPRITES = [
    f"{player_path}idle_side_anim{sep}tile000.png",
    f"{player_path}idle_side_anim{sep}tile001.png",
    f"{player_path}idle_side_anim{sep}tile002.png",
    f"{player_path}idle_side_anim{sep}tile003.png",
    f"{player_path}idle_side_anim{sep}tile004.png",
]

WALK_DOWN_SPRITES = [
    f"{player_path}walk_down_anim{sep}tile000.png",
    f"{player_path}walk_down_anim{sep}tile001.png",
    f"{player_path}walk_down_anim{sep}tile002.png",
    f"{player_path}walk_down_anim{sep}tile003.png",
    f"{player_path}walk_down_anim{sep}tile004.png",
    f"{player_path}walk_down_anim{sep}tile005.png",
]

WALK_UP_SPRITES = [
    f"{player_path}walk_up_anim{sep}tile000.png",
    f"{player_path}walk_up_anim{sep}tile001.png",
    f"{player_path}walk_up_anim{sep}tile002.png",
    f"{player_path}walk_up_anim{sep}tile003.png",
    f"{player_path}walk_up_anim{sep}tile004.png",
    f"{player_path}walk_up_anim{sep}tile005.png",
]

SIDE_WALK_SPRITES = [
    f"{player_path}side_walk_anim{sep}tile000.png",
    f"{player_path}side_walk_anim{sep}tile001.png",
    f"{player_path}side_walk_anim{sep}tile002.png",
    f"{player_path}side_walk_anim{sep}tile003.png",
    f"{player_path}side_walk_anim{sep}tile004.png",
    f"{player_path}side_walk_anim{sep}tile005.png",
]

ATTACK_DOWN_SPRITES = [
    f"{player_path}attack_down_anim{sep}tile000.png",
    f"{player_path}attack_down_anim{sep}tile001.png",
    f"{player_path}attack_down_anim{sep}tile002.png",
]

ATTACK_UP_SPRITES = [
    f"{player_path}attack_up_anim{sep}tile000.png",
    f"{player_path}attack_up_anim{sep}tile001.png",
    f"{player_path}attack_up_anim{sep}tile002.png",
]

ATTACK_SIDE_SPRITES = [
    f"{player_path}attack_side_anim{sep}tile000.png",
    f"{player_path}attack_side_anim{sep}tile001.png",
    f"{player_path}attack_side_anim{sep}tile002.png",
]

PICK_UP_SPRITES = [
    f"{player_path}pick_up_anim{sep}tile000.png",
    f"{player_path}pick_up_anim{sep}tile001.png",
    f"{player_path}pick_up_anim{sep}tile002.png",
    f"{player_path}pick_up_anim{sep}tile003.png",
    f"{player_path}pick_up_anim{sep}tile004.png",
]

MAP_PATH = [map_path + "map_1.tmj",
            map_path + "map_2.tmj",
            map_path + "map_3.tmj",
            map_path + "map_4.tmj"]
