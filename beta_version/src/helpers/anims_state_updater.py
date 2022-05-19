from beta_version.src.load_assets import PICK_UP_SPRITES
from beta_version.src.helpers.game_parameters import *


def update_idle_down_anim(idle_down_status, anim_sprites_len):
    if idle_down_status > (anim_sprites_len - 1) * UPDATES_PER_FRAME:
        idle_down_status = 0
    else:
        idle_down_status += 1

    return idle_down_status


def update_idle_up_anim(idle_up_status, anim_sprites_len):
    if idle_up_status > (anim_sprites_len - 1) * UPDATES_PER_FRAME:
        idle_up_status = 0
    else:
        idle_up_status += 1

    return idle_up_status


def update_idle_side_anim(idle_side_status, anim_sprites_len):
    if idle_side_status > (anim_sprites_len - 1) * UPDATES_PER_FRAME:
        idle_side_status = 0
    else:
        idle_side_status += 1

    return idle_side_status


def update_walk_down_anim(walk_down_status, anim_sprites_len):
    if walk_down_status > (anim_sprites_len - 1) * UPDATES_PER_FRAME:
        walk_down_status = 0
    else:
        walk_down_status += 1

    return walk_down_status


def update_walk_up_anim(walk_up_status, anim_sprites_len):
    if walk_up_status > (anim_sprites_len - 1) * UPDATES_PER_FRAME:
        walk_up_status = 0
    else:
        walk_up_status += 1

    return walk_up_status


def update_side_walk_anim(walk_side_status, anim_sprites_len):
    if walk_side_status > (anim_sprites_len - 1) * UPDATES_PER_FRAME:
        walk_side_status = 0
    else:
        walk_side_status += 1

    return walk_side_status


def update_attack_down_anim(attack_down_status, anim_sprites_len):
    if attack_down_status > (anim_sprites_len - 1) * UPDATES_PER_FRAME:
        attack_down_status = 0
    else:
        attack_down_status += 1

    return attack_down_status


def update_attack_up_anim(attack_up_status, anim_sprites_len):
    if attack_up_status > (anim_sprites_len - 1) * UPDATES_PER_FRAME:
        attack_up_status = 0
    else:
        attack_up_status += 1

    return attack_up_status


def update_attack_side_anim(attack_side_status, anim_sprites_len):
    if attack_side_status > (anim_sprites_len - 1) * UPDATES_PER_FRAME:
        attack_side_status = 0
    else:
        attack_side_status += 1

    return attack_side_status


def update_pick_up_anim(pick_up_status):
    if pick_up_status > (len(PICK_UP_SPRITES) - 1) * UPDATES_PER_FRAME:
        pick_up_status = 0
        picking = WAITING_PICKING
    else:
        pick_up_status += 1
        picking = PICKING

    return pick_up_status, picking
