import pygame
import sys
import os
import subprocess
import random

def main(selected_character):
    # 初始化pygame
    pygame.init()
    # 設定視窗標題
    pygame.display.set_caption("Fighting Game")
    # 顏色
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    # 視窗寬高設定
    width, height = 640, 500
    screen = pygame.display.set_mode((width, height))

    # 檢查圖片是否存在
    def check_img(path):
        if not os.path.exists(path):
            print(f"圖片不存在: {path}")
            sys.exit()
        return pygame.image.load(path)
    
    if selected_character == "角色2":
        ch2 = {
            "x" : 100,
            "y" : 300,
            "width" : 100,
            "height" : 150,
            "facing" : 1, # 1: 右, -1: 左
            "last_facing": 1,
            "life" : 500,
            "energy": 0,
            "speed": 7,
            "is_jumping": False,
            "vertical_speed": 0,
            "attack_type": None,
            "is_in_hard_stun": False,  # 是否處於硬直狀態
            "is_hurt": False,  # 是否處於受傷狀態
            "hurt_start_time": 0,  # 初始化受傷開始時間
            "hurt_duration": 0,    # 初始化受傷持續時間
            "block_energy": 100,  # 防禦條初始值
            "is_blocking": False,  # 是否正在防禦
            "attack_start_time": 0,
            "last_damage_time": 0,
            "hard_stun_duration": 0,
            "jump_speed": 15,
            "gravity": 0.5,
            "max_jump_height": 200,
            "image": check_img("inside/test_pic/ch2.png"),
            "img_hurt": check_img("inside/test_pic/ch2_hurted.png"),
            "attack_images": {
                "light": check_img("inside/test_pic/ch2_light.png"),
                "medium": check_img("inside/test_pic/ch2_mid.png"),
                "heavy": check_img("inside/test_pic/ch2_heavy.png"),
            },
            "hitbox_img_ch2": check_img("inside/test_pic/ch2_hitbox.png"),
            "hitbox_rect":pygame.Rect(100,300,60,150),  # 獲取 hitbox 的矩形範圍
            "is_broken": False,  # 是否處於破防狀態
            "break_start_time": 0,  # 破防開始時間
            "img_break": check_img("inside/test_pic\ch2_break.png"),  # 破防圖片
            "special_active": False,
            "special2_active": False,
            #倒地
            "is_knockdown": False,
            "knockdown_start_time": 0,
            "knockdown_duration": 1000,  # 倒地動畫持續1秒
            "knockdown_angle": 0,
            # 特殊技1
            "special_ch2_img": check_img("inside/test_pic\ch2_cycle.png"),
            "spe_x": 0,
            "spe_y": 0,
            "spe_speed": 1,
            "spe_active": False,
            # 特殊技2
            "special2_ch2_img": check_img("inside/test_pic\ch2_shi.png"),
            "spe2_x": 0,
            "spe2_y": 0,
            "spe2_speed": 1,
            "spe2_active": False,
            "special2_active_ch2": False,  # 添加特殊技狀態
        }
        ch1 = {
            "x" : 400,
            "y" : 300,
            "width" : 100,
            "height" : 150,
            "facing" : -1, # 1: 右, -1: 左
            "last_facing": -1,
            "life" : 600,
            "speed": 4,
            "energy": 0,
            "is_jumping": False,
            "vertical_speed": 0,
            "attack_type": None,
            "is_in_hard_stun": False,  # 是否處於硬直狀態
            "is_hurt": False,  # 是否處於受傷狀態
            "hurt_start_time": 0,  # 初始化受傷開始時間
            "hurt_duration": 0,    # 初始化受傷持續時間
            "block_energy": 100,  # 防禦條初始值
            "is_blocking": False,  # 是否正在防禦
            "attack_start_time": 0,
            "last_damage_time": 0,
            "hard_stun_duration": 0,
            "jump_speed": 15,
            "gravity": 0.5,
            "max_jump_height": 200,
            "image": check_img("inside/test_pic/ch1.png"),
            "img_hurt": check_img("inside/test_pic/ch1_hurted.png"),
            "attack_images": {
                "light": check_img("inside/test_pic/ch1_light.png"),
                "medium": check_img("inside/test_pic/ch1_mid.png"),
                "heavy": check_img("inside/test_pic/ch1_heavy.png"),
            },
            "hitbox_img_ch1": check_img("inside/test_pic/ch1_hitbox.png"),
            "hitbox_rect":pygame.Rect(420,300,60,150),  # 獲取 hitbox 的矩形範圍
            "is_broken": False,  # 是否處於破防狀態
            "break_start_time": 0,  # 破防開始時間
            "img_break": check_img("inside/test_pic\ch1_break.png"),  # 破防圖片
            "special_active": False,
            "special2_active": False,
            #倒地
            "is_knockdown": False,
            "knockdown_start_time": 0,
            "knockdown_duration": 1000,  # 倒地動畫持續1秒
            "knockdown_angle": 0,
            # 特殊技1
            "special_image_pose": check_img("inside/test_pic/ch1_hadouken.png"),
            "special_image": check_img("inside/test_pic\hadouken.png"),
            "special_speed": 10,
            "special_active": False,  # 是否正在施放特殊技
            "special_x": 0,           # 特殊技的 x 座標
            "special_y": 0,           # 特殊技的 y 座標
            "special_direction": 1,   # 特殊技方向
            # 特殊技2
            "special2_img_pose": check_img("inside/test_pic/ch1_shoryuken.png"),
            "special2_active": False,  # 是否正在施放特殊技
            "special2_x": 0,           # 特殊技的 x 座標
            "special2_y": 0,           # 特殊技的 y 座標
            "special2_direction": 1,   # 特殊技方向
        }
        player = ch2
        opponent = ch1
        player_keys = {"left": pygame.K_a, "right": pygame.K_d, "up": pygame.K_w, "defense": pygame.K_s, "light": pygame.K_j, "medium": pygame.K_k, "heavy": pygame.K_l}
        opponent_keys = {"left": pygame.K_LEFT, "right": pygame.K_RIGHT, "up": pygame.K_UP, "defense": pygame.K_DOWN, "light": pygame.K_KP1, "medium": pygame.K_KP2, "heavy": pygame.K_KP3}
    else:
        print(f"未知角色: {selected_character}")
        sys.exit()
    # 調整角色圖片大小
    def scale_character_images(character):
        # 調整普通圖片大小，保持比例
        original_width, original_height = character["image"].get_size()
        scale_factor = character["height"] / original_height
        new_width = int(original_width * scale_factor)
        character["image"] = pygame.transform.scale(character["image"], (new_width, character["height"]))
        if character["facing"] == -1:  # 如果角色面向左，翻轉普通圖片
            character["image"] = pygame.transform.flip(character["image"], True, False)
        character["img_break"] = pygame.transform.scale(character["img_break"], (new_width, character["height"]))
        if character["facing"] == -1:  # 如果角色面向左，翻轉破防圖片
            character["img_break"] = pygame.transform.flip(character["img_break"], True, False)

        # 使用相同的比例調整受傷圖片大小
        character["img_hurt"] = pygame.transform.scale(character["img_hurt"], (new_width, character["height"]))
        if character["facing"] == -1:  # 如果角色面向左，翻轉受傷圖片
            character["img_hurt"] = pygame.transform.flip(character["img_hurt"], True, False)

        # 使用相同的比例調整攻擊圖片大小
        for attack_type in character["attack_images"]:
            character["attack_images"][attack_type] = pygame.transform.scale(
                character["attack_images"][attack_type], (new_width, character["height"])
            )
            if character["facing"] == -1:  # 如果角色面向左，翻轉攻擊圖片
                character["attack_images"][attack_type] = pygame.transform.flip(
                    character["attack_images"][attack_type], True, False
                )

    scale_character_images(ch1)
    scale_character_images(ch2)
    # 設置倒地狀態
    def set_knockdown_state(character):
        character["is_knockdown"] = True
        character["knockdown_start_time"] = pygame.time.get_ticks()
        character["knockdown_angle"] = 0

    def scale_special_move_ch1_img(character):
        # 調整特殊技1圖片大小
        if "special_image_pose" in character and "special_image" in character:
            try:
                # 調整特殊技準備動作圖片
                original_pose_width, original_pose_height = character["special_image_pose"].get_size()
                pose_scale = character["height"] / original_pose_height
                new_pose_width = int(original_pose_width * pose_scale)
                character["special_image_pose"] = pygame.transform.scale(
                    character["special_image_pose"], 
                    (new_pose_width, character["height"])
                )
                if character["facing"] == 1:  # 修改這裡：當面向右時翻轉圖片
                    character["special_image_pose"] = pygame.transform.flip(character["special_image_pose"], True, False)

                # 調整特殊技發射圖片
                original_special_width, original_special_height = character["special_image"].get_size()
                special_scale = 0.3  # 可以調整這個值來改變特殊技圖片的大小
                new_special_width = int(original_special_width * special_scale)
                new_special_height = int(original_special_height * special_scale)
                character["special_image"] = pygame.transform.scale(
                    character["special_image"], 
                    (new_special_width, new_special_height)
                )
            except Exception as e:
                print(f"特殊技1圖片處理錯誤: {e}")

        # 調整特殊技2圖片大小
        if "special2_img_pose" in character:
            try:
                # 調整特殊技2準備動作圖片
                original_pose_width, original_pose_height = character["special2_img_pose"].get_size()
                pose_scale = character["height"] / original_pose_height
                new_pose_width = int(original_pose_width * pose_scale)
                character["special2_img_pose"] = pygame.transform.scale(
                    character["special2_img_pose"], 
                    (new_pose_width, character["height"])
                )
                if character["facing"] == 1:  # 修改這裡：當面向右時翻轉圖片
                    character["special2_img_pose"] = pygame.transform.flip(character["special2_img_pose"], True, False)
                else:
                    character["special2_img_pose"] = character["special2_img_pose"]
            except Exception as e:
                print(f"特殊技2圖片處理錯誤: {e}")
                print(f"圖片路徑: {character.get('special2_img_pose', '未找到')}")

    scale_special_move_ch1_img(ch1)

    # 調整ch2的特殊技圖片大小
    def scale_special_move_ch2_img(character):
        if "special_ch2_img" in character:
            try:
                # 調整特殊技2準備動作圖片
                original_pose_width, original_pose_height = character["special_ch2_img"].get_size()
                pose_scale = character["height"] / original_pose_height
                new_pose_width = int(original_pose_width * pose_scale)
                character["special_ch2_img"] = pygame.transform.scale(
                    character["special_ch2_img"], 
                    (new_pose_width, character["height"])
                )
                if character["facing"] == -1:
                    character["special_ch2_img"] = pygame.transform.flip(character["special_ch2_img"], True, False)
            except Exception as e:
                print(f"特殊技2圖片處理錯誤: {e}")
                print(f"圖片路徑: {character.get('special_ch2_img', '未找到')}")
        if "special2_ch2_img" in character:
            try:
                # 調整特殊技2準備動作圖片
                original_pose_width, original_pose_height = character["special2_ch2_img"].get_size()
                pose_scale = character["height"] / original_pose_height
                new_pose_width = int(original_pose_width * pose_scale)
                character["special2_ch2_img"] = pygame.transform.scale(
                    character["special2_ch2_img"], 
                    (new_pose_width, character["height"])
                )
                if character["facing"] == -1:
                    image = pygame.transform.flip(image, True, False)
                screen.blit(image, (character["x"], character["y"]))
            except Exception as e:
                print(f"特殊技2圖片處理錯誤: {e}")
                print(f"圖片路徑: {character.get('special2_ch2_img', '未找到')}")
    
    scale_special_move_ch2_img(ch2)

    # 繪製生命值條
    def draw_health_bar_ch1(screen, character, x, y, max_width, height, color):
        max_life = 600
        health_ratio = character["life"] / max_life
        current_width = int(max_width * health_ratio)
        # 低於30%時變色
        if health_ratio < 0.3:
            bar_color = BLUE  # 低血量變綠色（如要紅色請改成 RED）
        else:
            bar_color = color
        pygame.draw.rect(screen, (100, 100, 100), (x, y, max_width, height))
        pygame.draw.rect(screen, bar_color, (x, y, current_width, height))
    
    def draw_health_bar_ch2(screen, character, x, y, max_width, height, color):
        max_life = 500
        health_ratio = character["life"] / max_life
        current_width = int(max_width * health_ratio)
        if health_ratio < 0.3:
            bar_color = BLUE  
        else:
            bar_color = color
        pygame.draw.rect(screen, (100, 100, 100), (x, y, max_width, height))
        pygame.draw.rect(screen, bar_color, (x, y, current_width, height))

    # 繪製能量條
    def draw_energy_bar(screen, character, x, y, max_width, height, color):
    # 計算能量條的寬度
        energy_ratio = character["energy"] / 100  # 假設最大能量值為 50
        current_width = int(max_width * energy_ratio)
        # 繪製背景條（灰色）
        pygame.draw.rect(screen, (100, 100, 100), (x, y, max_width, height))
        # 繪製當前能量條
        pygame.draw.rect(screen, color, (x, y, current_width, height))

    # 處理角色移動
    def handle_movement(keys, character,opponent,keys_map):
        if character["is_broken"]:  # 如果角色處於破防狀態，禁止移動
            return
        if character["is_in_hard_stun"]:
            if character["is_jumping"]:
                character["y"] += character["vertical_speed"]
                character["vertical_speed"] += character["gravity"]
                if character["y"] >= 300:
                    character["y"] = 300
                    character["is_jumping"] = False
                    character["vertical_speed"] = 0
            return
        original_x = character["x"]  # 保存原始位置，用於碰撞檢測
        original_y = character["y"]  # 保存原始位置，用於碰撞檢測
    
        if keys[keys_map["left"]]:
            character["x"] -= character["speed"]
        if keys[keys_map["right"]]:
            character["x"] += character["speed"]
        if not character["is_jumping"] and keys[keys_map["up"]]:
            character["is_jumping"] = True
            character["vertical_speed"] = -character["jump_speed"]
        

        if character["is_jumping"]:
            character["y"] += character["vertical_speed"]
            character["vertical_speed"] += character["gravity"]
            if character["y"] >= 300:
                character["y"] = 300
                character["is_jumping"] = False
                character["vertical_speed"] = 0
        # 更新 hitbox_rect 的位置
        character["hitbox_rect"].center = (character["x"] + character["width"] // 2, character["y"] + character["height"] // 2)

        # 檢查是否與對手的 hitbox_rect 發生水平碰撞
        if character["hitbox_rect"].colliderect(opponent["hitbox_rect"]):
            character["x"] = original_x  # 如果水平碰撞，恢復到原始位置
            character["hitbox_rect"].center = (character["x"] + character["width"] // 2, character["y"] + character["height"] // 2)

        # 檢查是否與對手的 hitbox_rect 發生垂直碰撞
        if character["hitbox_rect"].colliderect(opponent["hitbox_rect"]):
            if character["y"] < opponent["y"]:  # 如果角色在對手上方
                character["y"] = opponent["y"] - character["height"]  # 將角色移到對手上方
                # 根據對手的相對位置滑動
                if character["x"] < opponent["x"]:  # 如果角色在對手的左側
                    character["x"] -= character["speed"]  # 向左滑動
                elif character["x"] > opponent["x"]:  # 如果角色在對手的右側
                    character["x"] += character["speed"]  # 向右滑動
            

            # 更新 hitbox_rect 的位置
            character["hitbox_rect"].center = (character["x"] + character["width"] // 2, character["y"] + character["height"] // 2)

    # 處理角色面向方向
    def update_character_image(player, opponent):
        # 如果角色處於硬直狀態，禁止更新面向方向
        if not player["is_in_hard_stun"]:
            if player["x"] > opponent["x"]:
                player["facing"] = -1
            else:
                player["facing"] = 1

        if not opponent["is_in_hard_stun"]:
            if opponent["x"] > player["x"]:
                opponent["facing"] = -1
            else:
                opponent["facing"] = 1
        # 更新 player 的圖片方向
        if player["facing"] != player["last_facing"]:  # 如果面向方向改變
            player["image"] = pygame.transform.flip(player["image"], True, False)
            player["img_hurt"] = pygame.transform.flip(player["img_hurt"], True, False)  # 翻轉受傷圖片
            player["img_break"] = pygame.transform.flip(player["img_break"], True, False)  # 翻轉破防圖片
            for attack_type in player["attack_images"]:  # 翻轉攻擊圖片
                player["attack_images"][attack_type] = pygame.transform.flip(
                    player["attack_images"][attack_type], True, False
                )
            player["last_facing"] = player["facing"]  # 更新最後的面向方向

        # 更新 opponent 的圖片方向
        if opponent["facing"] != opponent["last_facing"]:  # 如果面向方向改變
            opponent["image"] = pygame.transform.flip(opponent["image"], True, False)
            opponent["img_hurt"] = pygame.transform.flip(opponent["img_hurt"], True, False)  # 翻轉受傷圖片
            opponent["img_break"] = pygame.transform.flip(opponent["img_break"], True, False)  # 翻轉破防圖片
            for attack_type in opponent["attack_images"]:  # 翻轉攻擊圖片
                opponent["attack_images"][attack_type] = pygame.transform.flip(
                    opponent["attack_images"][attack_type], True, False
                )
            opponent["last_facing"] = opponent["facing"]  # 更新最後的面向方向

    # 處理攻擊
    def handle_attack(event, character, attack_keys):
        if character["is_broken"]:  # 如果角色處於破防狀態，禁止攻擊
            return
        current_time = pygame.time.get_ticks()
        if event.type == pygame.KEYDOWN:
            # 檢查是否正在使用特殊技
            if character.get("special_active", False):
                return
            if event.key == attack_keys["light"]:
                character["attack_type"] = "light"
                character["attack_start_time"] = current_time
                character["hard_stun_duration"] = 300  # 輕攻擊硬直時間
                character["is_in_hard_stun"] = True  # 進入硬直狀態
            elif event.key == attack_keys["medium"]:
                character["attack_type"] = "medium"
                character["attack_start_time"] = current_time
                character["hard_stun_duration"] = 500  # 中攻擊硬直時間
                character["is_in_hard_stun"] = True  # 進入硬直狀態
            elif event.key == attack_keys["heavy"]:
                character["attack_type"] = "heavy"
                character["attack_start_time"] = current_time
                character["hard_stun_duration"] = 700  # 重攻擊硬直時間
                character["is_in_hard_stun"] = True  # 進入硬直狀態
 
    # 根據攻擊類型顯示對應的攻擊圖片
    def draw_character_ch1(screen, character):
        if character.get("is_knockdown", False):
            elapsed = pygame.time.get_ticks() - character["knockdown_start_time"]
            duration = character.get("knockdown_duration", 1000)
            angle = 360 * min(elapsed / duration, 1)  # 旋轉一圈
            character["knockdown_angle"] = angle
            rotated_img = pygame.transform.rotate(character["image"], angle)
            rect = rotated_img.get_rect(center=(character["x"] + character["width"] // 2, character["y"] + character["height"] // 2 + 30))
            screen.blit(rotated_img, rect.topleft)
        elif character.get("special2_active", False):  # 優先檢查是否在使用升龍拳
            try:
                if character["facing"] == 1:  # 面向右
                    screen.blit(character["special2_img_pose"], (character["x"], character["y"]))
                else:  # 面向左
                    flipped_pose = pygame.transform.flip(character["special2_img_pose"], True, False)
                    screen.blit(flipped_pose, (character["x"], character["y"]))
            except Exception as e:
                print(f"升龍拳圖片顯示錯誤: {e}")
        elif character.get("special_active", False):  # 然後檢查是否在使用波動拳
            try:
                if character["facing"] == 1:  # 面向右
                    screen.blit(character["special_image_pose"], (character["x"], character["y"]))
                else:  # 面向左
                    flipped_pose = pygame.transform.flip(character["special_image_pose"], True, False)
                    screen.blit(flipped_pose, (character["x"], character["y"]))
            except Exception as e:
                print(f"波動拳圖片顯示錯誤: {e}")
        elif character["is_broken"]:  # 如果角色處於破防狀態
            screen.blit(character["img_break"], (character["x"], character["y"]))
        elif character.get("is_hurt", False):  # 如果角色處於受傷狀態
            screen.blit(character["img_hurt"], (character["x"], character["y"]))
        elif character["attack_type"] is not None:  # 如果角色正在普通攻擊
            attack_image = character["attack_images"].get(character["attack_type"])
            if attack_image:
                screen.blit(attack_image, (character["x"], character["y"]))
            else:
                print(f"攻擊圖片未找到: {character['attack_type']}")
        else:  # 顯示普通圖片
            screen.blit(character["image"], (character["x"], character["y"]))
    
    def draw_character_ch2(screen, character):
        if character.get("is_knockdown", False):
            elapsed = pygame.time.get_ticks() - character["knockdown_start_time"]
            duration = character.get("knockdown_duration", 1000)
            angle = 360 * min(elapsed / duration, 1)  # 旋轉一圈
            character["knockdown_angle"] = angle
            rotated_img = pygame.transform.rotate(character["image"], angle)
            rect = rotated_img.get_rect(center=(character["x"] + character["width"] // 2, character["y"] + character["height"] // 2 + 30))
            screen.blit(rotated_img, rect.topleft)
        elif character.get("special2_active_ch2", False):  # 優先檢查是否在使用升龍拳
            try:
                if character["facing"] == 1:  # 面向右
                    screen.blit(character["special2_img_pose"], (character["x"], character["y"]))
                else:  # 面向左
                    flipped_pose = pygame.transform.flip(character["special2_img_pose"], True, False)
                    screen.blit(flipped_pose, (character["x"], character["y"]))
            except Exception as e:
                print(f"升龍拳圖片顯示錯誤: {e}")
        elif character.get("special_active", False):  # 然後檢查是否在使用波動拳
            try:
                if character["facing"] == 1:  # 面向右
                    screen.blit(character["special_image_pose"], (character["x"], character["y"]))
                else:  # 面向左
                    flipped_pose = pygame.transform.flip(character["special_image_pose"], True, False)
                    screen.blit(flipped_pose, (character["x"], character["y"]))
            except Exception as e:
                print(f"波動拳圖片顯示錯誤: {e}")
        elif character["is_broken"]:  # 如果角色處於破防狀態
            screen.blit(character["img_break"], (character["x"], character["y"]))
        elif character.get("is_hurt", False):  # 如果角色處於受傷狀態
            screen.blit(character["img_hurt"], (character["x"], character["y"]))
        elif character["attack_type"] is not None:  # 如果角色正在普通攻擊
            attack_image = character["attack_images"].get(character["attack_type"])
            if attack_image:
                screen.blit(attack_image, (character["x"], character["y"]))
            else:
                print(f"攻擊圖片未找到: {character['attack_type']}")
        else:  # 顯示普通圖片
            screen.blit(character["image"], (character["x"], character["y"]))
    

    # 根據攻擊類型設置碰撞箱寬度和傷害
    def handle_attack_collision(attacker, defender):
        if attacker["attack_type"] is not None:
            # 設置默認值，防止未賦值的情況
            attack_width = 0
            damage = 0
            damage_interval = 1000  # 默認值，防止未賦值
            hurt_duration = 0
            energy_gain = 0
            knockback_distance = 0  # 擊退距離
            block_cost = 10  # 防禦時扣除的防禦條值
            block_gain_energy = 0  # 防禦後能量增加

            # 根據攻擊類型設置參數
            if attacker["attack_type"] == "light":
                attack_width = 25
                damage = 10
                damage_interval = 500
                hurt_duration = 200
                energy_gain = 5
                knockback_distance = 10  # 輕攻擊擊退距離
                block_cost = 5  # 輕攻擊防禦消耗
                block_gain_energy = 5  # 輕攻擊防禦後能量增加
            elif attacker["attack_type"] == "medium":
                attack_width = 30
                damage = 20
                damage_interval = 700
                hurt_duration = 400
                energy_gain = 10
                knockback_distance = 15  # 中攻擊擊退距離
                block_cost = 10  # 中攻擊防禦消耗
                block_gain_energy = 5  # 中攻擊防禦後能量增加
            elif attacker["attack_type"] == "heavy":
                attack_width = 35
                damage = 30
                damage_interval = 900
                hurt_duration = 650
                energy_gain = 20
                knockback_distance = 20  # 重攻擊擊退距離
                block_cost = 15  # 重攻擊防禦消耗
                block_gain_energy = 10  # 重攻擊防禦後能量增加


            # 根據面向方向設置攻擊的碰撞箱
            if attacker["facing"] == 1:  # 面向右
                attack_rect = pygame.Rect(
                    attacker["hitbox_rect"].right,  # 從角色右側開始
                    attacker["hitbox_rect"].top,
                    attack_width,
                    attacker["hitbox_rect"].height
                )
            elif attacker["facing"] == -1:  # 面向左
                attack_rect = pygame.Rect(
                    attacker["hitbox_rect"].left - attack_width,  # 從角色左側開始
                    attacker["hitbox_rect"].top,
                    attack_width,
                    attacker["hitbox_rect"].height
                )

            # 檢查是否碰撞
            if attack_rect.colliderect(defender["hitbox_rect"]):
                current_time = pygame.time.get_ticks()
                

                if current_time - attacker["last_damage_time"] > damage_interval:
                    if defender["is_blocking"]:
                        defender["block_energy"] -= block_cost
                        defender["block_energy"] = max(0, defender["block_energy"])
                        if defender["block_energy"] <= 0 and not defender["is_broken"]:
                            defender["is_broken"] = True
                            defender["break_start_time"] = current_time
                        if not attacker.get("damage_done", False):
                            attacker["energy"] = min(attacker["energy"] + block_gain_energy, 100)
                            attacker["damage_done"] = True
                            defender["energy"] = min(defender["energy"] + block_gain_energy, 100)
                            attacker["last_damage_time"] = current_time  # 加這行，防禦時也重設攻擊冷卻
                    else:
                        defender["life"] -= damage
                        defender["life"] = max(0, defender["life"])
                        defender["is_hurt"] = True
                        defender["hurt_start_time"] = current_time
                        defender["hurt_duration"] = hurt_duration
                        defender["last_damage_time"] = current_time
                        attacker["energy"] = min(attacker["energy"] + energy_gain, 100)
                        attacker["last_damage_time"] = current_time  # 攻擊成功也重設攻擊冷卻
                    
                    # 擊退防守方
                    if attacker["facing"] == 1:  # 攻擊者面向右
                        defender["x"] += knockback_distance
                        attacker["x"] -= knockback_distance
                    elif attacker["facing"] == -1:  # 攻擊者面向左
                        defender["x"] -= knockback_distance
                        attacker["x"] += knockback_distance

                        # 防止防守方超出邊界
                    defender["x"] = max(0, min(defender["x"], 640 - defender["width"]))  # 假設遊戲寬度為 640

    # 繪製防禦條
    def draw_block_bar(screen, character, x, y, max_width, height, color):
        # 計算防禦條的寬度
        block_ratio = character["block_energy"] / 100  # 假設最大防禦值為 100
        current_width = int(max_width * block_ratio)
        # 繪製背景條（灰色）
        pygame.draw.rect(screen, (100, 100, 100), (x, y, max_width, height))
        # 繪製當前防禦條
        pygame.draw.rect(screen, color, (x, y, current_width, height))

    # ch1的特殊技
    def draw_special_move(screen, character):
        if character.get("special_active", False):
            current_time = pygame.time.get_ticks()
            # 如果還在準備動作時間內
            if current_time - character["attack_start_time"] < character["hard_stun_duration"]:
                # 顯示準備動作（使用圖片）
                try:
                    # 根據面向方向決定準備動作的位置
                    if character["facing"] == 1:  # 面向右
                        screen.blit(character["special_image_pose"], (character["x"], character["y"]))
                    else:  # 面向左
                        # 翻轉圖片並調整位置
                        flipped_pose = pygame.transform.flip(character["special_image_pose"], True, False)
                        screen.blit(flipped_pose, (character["x"], character["y"]))
                except Exception as e:
                    print(f"準備動作圖片顯示錯誤: {e}")
            else:
                # 準備動作結束後發射特殊技（使用多個藍色方形形成波紋效果）
                # 每隔一定距離繪製一個方形
                for i in range(3):  # 同時顯示3個波紋
                    offset = i * 10  # 波紋之間的間距
                    if character["special_direction"] == 1:  # 向右
                        pygame.draw.rect(screen, (0, 0, 255), 
                            (character["special_x"] - offset, character["special_y"], 20, 20))
                    else:  # 向左
                        pygame.draw.rect(screen, (0, 0, 255), 
                            (character["special_x"] + offset, character["special_y"], 20, 20))

    def handle_special_move(ch1, ch2, keys, key_maps, screen, width):
        # 檢查能量是否足夠且未在特殊技狀態
        if ch1["energy"] >= 20 and not ch1.get("special_active", False):
            # 根據面向方向決定按鍵組合
            is_right_facing = ch1["facing"] == 1
            correct_keys = (keys[key_maps["light"]] and keys[key_maps["defense"]] and (keys[key_maps["left"]] if is_right_facing else keys[key_maps["right"]]))

            if correct_keys:
                # 設置特殊技初始位置
                ch1["special_x"] = ch1["x"] + (ch1["width"] // 2 if is_right_facing else -ch1["width"] // 2)
                ch1["special_y"] = ch1["y"] + ch1["height"] // 2
                
                # 設置特殊技狀態
                ch1["special_active"] = True
                ch1["attack_type"] = None
                ch1["special_direction"] = ch1["facing"]
                ch1["energy"] -= 20
                ch1["is_in_hard_stun"] = True
                ch1["attack_start_time"] = pygame.time.get_ticks()
                ch1["hard_stun_duration"] = 500

        # 特殊技移動與碰撞檢測
        if ch1["special_active"]:
            current_time = pygame.time.get_ticks()
            # 如果已經過了準備動作時間
            if current_time - ch1["attack_start_time"] >= ch1["hard_stun_duration"]:
                # 移動特殊技
                speed = 5
                ch1["special_x"] += speed * ch1["special_direction"]
                
                # 判斷碰撞（檢查所有波紋）
                for i in range(3):
                    offset = i * 10
                    if ch1["special_direction"] == 1:  # 向右
                        special_rect = pygame.Rect(ch1["special_x"] - offset, ch1["special_y"], 20, 20)
                    else:  # 向左
                        special_rect = pygame.Rect(ch1["special_x"] + offset, ch1["special_y"], 20, 20)
                    
                    if special_rect.colliderect(ch2["hitbox_rect"]):
                        if ch2["is_blocking"]:  # 如果對手在防禦
                            ch2["block_energy"] -= 30
                            ch2["block_energy"] = max(0, ch2["block_energy"])
                            if ch2["block_energy"] <= 0 and not ch2["is_broken"]:
                                ch2["is_broken"] = True
                                ch2["break_start_time"] = pygame.time.get_ticks()
                        else:  # 如果對手沒有防禦
                            ch2["life"] -= 25
                            ch2["is_hurt"] = True
                            ch2["hurt_start_time"] = pygame.time.get_ticks()
                            ch2["hurt_duration"] = 600
                        ch1["special_active"] = False
                        ch1["is_in_hard_stun"] = False
                        break  # 只要有一個波紋命中就結束特殊技
                
                # 超出畫面消失
                if ch1["special_x"] < 0 or ch1["special_x"] > width:
                    ch1["special_active"] = False
                    ch1["is_in_hard_stun"] = False
    # ch1的特殊技2
    def draw_special2_move(screen, character):
        if character.get("special2_active", False):
            try:
                if character["facing"] == -1:  # 面向右
                    flipped_pose = pygame.transform.flip(character["special2_img_pose"], True, False)
                    screen.blit(flipped_pose, (character["x"], character["y"]))
                    
                else:  # 面向左
                    screen.blit(character["special2_img_pose"], (character["x"], character["y"]))
            except Exception as e:
                print(f"升龍拳圖片顯示錯誤: {e}")

    def handle_special2_move(ch1, ch2, keys, key_maps, screen, width):
        if "special2_img_pose" not in ch1:
            return
            
        if ch1["energy"] >= 30 and not ch1.get("special2_active", False):
            is_right_facing = ch1["facing"] == 1
            correct_keys = (keys[key_maps["medium"]] and keys[key_maps["defense"]] and (keys[key_maps["right"]] if is_right_facing else keys[key_maps["left"]]))

            if correct_keys:
                # 重新載入並設置特殊技2圖片
                ch1["special2_img_pose"] = pygame.image.load("inside/test_pic/ch1_shoryuken.png")
                original_pose_width, original_pose_height = ch1["special2_img_pose"].get_size()
                pose_scale = ch1["height"] / original_pose_height
                new_pose_width = int(original_pose_width * pose_scale)
                ch1["special2_img_pose"] = pygame.transform.scale(
                    ch1["special2_img_pose"], 
                    (new_pose_width, ch1["height"])
                )
 
                ch1["special2_active"] = True
                ch1["attack_type"] = None
                ch1["energy"] -= 20
                ch1["is_in_hard_stun"] = True
                ch1["attack_start_time"] = pygame.time.get_ticks()
                ch1["hard_stun_duration"] = 500
                
                ch1["is_jumping"] = True
                ch1["vertical_speed"] = -ch1["jump_speed"] * 1
                
                ch1["special2_x"] = ch1["x"] + (ch1["width"] // 2 if is_right_facing else -ch1["width"] // 2)
                ch1["special2_y"] = ch1["y"]
                
                # 創建更大的hitbox
                if is_right_facing:
                    special_hitbox = pygame.Rect(
                        ch1["hitbox_rect"].right - 40,  # 調整起始位置
                        ch1["hitbox_rect"].top - 40,  # 增加上方判定範圍
                        ch1["hitbox_rect"].width + 40,  # 增加判定寬度
                        ch1["hitbox_rect"].height + 40  # 增加判定高度
                    )
                else:
                    special_hitbox = pygame.Rect(
                        ch1["hitbox_rect"].left - 40,  # 調整起始位置
                        ch1["hitbox_rect"].top - 40,  # 增加上方判定範圍
                        ch1["hitbox_rect"].width + 40,  # 增加判定寬度
                        ch1["hitbox_rect"].height + 40  # 增加判定高度
                    )
                
                # 檢查碰撞
                if special_hitbox.colliderect(ch2["hitbox_rect"]):
                    if ch2["is_blocking"]:
                        ch2["block_energy"] -= 40
                        ch2["block_energy"] = max(0, ch2["block_energy"])
                        if ch2["block_energy"] <= 0 and not ch2["is_broken"]:
                            ch2["is_broken"] = True
                            ch2["break_start_time"] = pygame.time.get_ticks()
                    else:
                        ch2["life"] -= 35
                        ch2["is_hurt"] = True
                        ch2["hurt_start_time"] = pygame.time.get_ticks()
                        ch2["hurt_duration"] = 800
                        # 添加擊飛效果
                        ch2["is_jumping"] = True
                        ch2["vertical_speed"] = -ch2["jump_speed"] * 1.25  # 增加擊飛高度
                        # 水平擊退
                        knockback_distance = 75  # 增加擊退距離
                        # 修改擊退方向判斷邏輯
                        if ch1["x"] < ch2["x"]:  # 如果 ch1 在 ch2 左邊
                            ch2["x"] += knockback_distance
                        else:  # 如果 ch1 在 ch2 右邊
                            ch2["x"] -= knockback_distance
                        # 確保不會超出畫面邊界
                        ch2["x"] = max(0, min(ch2["x"], width - ch2["width"]))
                        # 設置擊飛狀態
                        ch2["is_in_hard_stun"] = True
                        ch2["attack_start_time"] = pygame.time.get_ticks()
                        ch2["hard_stun_duration"] = 800
                        # === 新增：啟用倒地動畫 ===
                        set_knockdown_state(ch2)

        # 檢查升龍拳落地
        if ch1["special2_active"] and not ch1["is_jumping"]:
            ch1["special2_active"] = False
            ch1["is_in_hard_stun"] = False
            ch1["attack_type"] = None
            # 重置圖片
            original_pose_width, original_pose_height = ch1["special2_img_pose"].get_size()
            pose_scale = ch1["height"] / original_pose_height
            new_pose_width = int(original_pose_width * pose_scale)
            ch1["special2_img_pose"] = pygame.transform.scale(
                ch1["special2_img_pose"], 
                (new_pose_width, ch1["height"])
            )
            # 根據當前面向方向決定是否翻轉圖片
            if ch1["facing"] == 1:  # 面向右時翻轉圖片
                ch1["special2_img_pose"] = pygame.transform.flip(ch1["special2_img_pose"], True, False)

    # ch2的特殊技
    def draw_special_move_ch2(screen, character):
        if character.get("special_active", False):
            try:
                current_time = pygame.time.get_ticks()
                # 每100毫秒翻轉一次
                should_flip = (current_time // 100) % 2 == 0
                
                # 獲取原始圖片
                image = character["special_ch2_img"]
                
                # 根據時間決定是否翻轉
                if should_flip:
                    image = pygame.transform.flip(image, True, False)
                
                # 根據角色面向方向決定是否額外翻轉
                if character["facing"] == -1:
                    image = pygame.transform.flip(image, True, False)
                
                # 繪製圖片
                screen.blit(image, (character["x"], character["y"]))
                
            except Exception as e:
                print(f"特殊技圖片顯示錯誤: {e}")
                print(f"圖片路徑: {character.get('special_ch2_img', '未找到')}")

    def handle_special_move_ch2(ch2, ch1, keys, key_maps, screen, width):
        if ch2["energy"] >= 20 and not ch2.get("special_active", False):
            is_right_facing = ch2["facing"] == 1
            correct_keys = (keys[key_maps["light"]] and keys[key_maps["defense"]] and (keys[key_maps["left"]] if is_right_facing else keys[key_maps["right"]]))
            
            if correct_keys:
                ch2["special_active"] = True
                ch2["attack_type"] = None
                ch2["energy"] -= 20
                ch2["is_in_hard_stun"] = True
                ch2["attack_start_time"] = pygame.time.get_ticks()
                ch2["hard_stun_duration"] = 500
                ch2["damage_dealt"] = False  # 添加傷害標記

                # 保存原始 hitbox 位置
                ch2["original_hitbox"] = ch2["hitbox_rect"].copy()
                # 暫時移除 hitbox
                ch2["hitbox_rect"] = pygame.Rect(0, 0, 0, 0)

                # 保存原始位置
                ch2["original_x"] = ch2["x"]
                ch1["original_x"] = ch1["x"]

                ch2["special_x"] = ch2["x"] + (ch2["width"] // 2 if is_right_facing else -ch2["width"] // 2)
                ch2["special_y"] = ch2["y"]

        # 處理位置交換
        if ch2["special_active"]:
            current_time = pygame.time.get_ticks()
            move_speed = 5  # 移動速度

            # 計算目標位置（對手的位置）
            target_x = ch1["original_x"]
            
            # 計算移動進度（0到1之間的值）
            progress = min(1.0, abs(ch2["x"] - target_x) / abs(ch2["original_x"] - target_x))
            
            # 移動 ch2 到目標位置
            if ch2["x"] < target_x:
                ch2["x"] = min(ch2["x"] + move_speed, target_x)
            elif ch2["x"] > target_x:
                ch2["x"] = max(ch2["x"] - move_speed, target_x)

            # 移動 ch1 到 ch2 的原始位置
            if ch1["x"] < ch2["original_x"]:
                ch1["x"] = min(ch1["x"] + move_speed, ch2["original_x"])
            elif ch1["x"] > ch2["original_x"]:
                ch1["x"] = max(ch1["x"] - move_speed, ch2["original_x"])

            # 根據移動進度調整面向
            if progress < 0.5:  # 前半段
                # 讓兩個角色互相面對
                ch2["facing"] = 1 if ch2["x"] < ch1["x"] else -1
                ch1["facing"] = -1 if ch2["x"] < ch1["x"] else 1
            else:  # 後半段
                # 讓兩個角色面向各自的最終位置
                ch2["facing"] = 1 if ch2["original_x"] < ch1["original_x"] else -1
                ch1["facing"] = -1 if ch2["original_x"] < ch1["original_x"] else 1

            # 檢查是否在交換過程中且尚未造成傷害
            if (abs(ch2["x"] - target_x) > move_speed or abs(ch1["x"] - ch2["original_x"]) > move_speed) and not ch2.get("damage_dealt", False):
                # 創建一個攻擊判定區域
                attack_rect = pygame.Rect(
                    ch2["x"],
                    ch2["y"],
                    ch2["width"],
                    ch2["height"]
                )
                # 如果攻擊判定區域碰到對手
                if attack_rect.colliderect(ch1["hitbox_rect"]):
                    if ch1["is_blocking"]:  # 如果對手在防禦
                        ch1["block_energy"] -= 10
                        ch1["block_energy"] = max(0, ch1["block_energy"])
                        if ch1["block_energy"] <= 0 and not ch1["is_broken"]:
                            ch1["is_broken"] = True
                            ch1["break_start_time"] = pygame.time.get_ticks()
                    else:  # 如果對手沒有防禦
                        ch1["life"] -= 20  # 造成傷害
                        ch1["life"] = max(0, ch1["life"])
                        ch1["is_hurt"] = True
                        ch1["hurt_start_time"] = current_time
                        ch1["hurt_duration"] = 300
                    # 增加能量
                    ch2["energy"] = min(ch2["energy"] + 10, 100)
                    ch2["damage_dealt"] = True  # 標記已造成傷害

            # 檢查是否完成位置交換
            if (abs(ch2["x"] - target_x) < move_speed and 
                abs(ch1["x"] - ch2["original_x"]) < move_speed):
                ch2["special_active"] = False
                ch2["is_in_hard_stun"] = False
                # 恢復原始 hitbox
                if "original_hitbox" in ch2:
                    ch2["hitbox_rect"] = ch2["original_hitbox"]
                    del ch2["original_hitbox"]
                # 清理臨時變量
                if "original_x" in ch2:
                    del ch2["original_x"]
                if "original_x" in ch1:
                    del ch1["original_x"]
                if "damage_dealt" in ch2:
                    del ch2["damage_dealt"]  # 清理傷害標記

     #ch2的特殊技2
    
    # ch2的特殊技2
    def draw_special2_move_ch2(screen, character):
        if character.get("special2_active_ch2", False):
            # 獲取原始圖片
            original_img = character["special2_ch2_img"]
            
            # 根據面向方向決定是否翻轉
            if character["facing"] == -1:  # 面向右時，需要翻轉圖片
                img = pygame.transform.flip(original_img, True, False) 
            else:  # 面向左時，使用原始圖片
                img = original_img

            move_speed = 5
            if character["facing"] == 1:
                character["spe2_x"] += move_speed
            elif character["facing"] == -1:
                character["spe2_x"] -= move_speed
            
            # 繪製殘影
            for i in range(5):  # 繪製5個殘影
                alpha = 255 - (i * 50)  # 逐漸降低透明度
                if alpha < 0:
                    alpha = 0
                # 創建殘影圖片
                shadow = pygame.Surface(img.get_size(), pygame.SRCALPHA)
                shadow.fill((255, 255, 255, alpha))
                shadow_image = img.copy()
                shadow_image.blit(shadow, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                
                # 計算殘影位置
                offset = i * 10
                if character["facing"] == 1:  # 向右
                    shadow_x = character["spe2_x"] - offset
                else:  # 向左
                    shadow_x = character["spe2_x"] + offset
                
                # 繪製殘影
                screen.blit(shadow_image, (shadow_x, character["spe2_y"]))
            
            # 繪製主體
            screen.blit(img, (character["spe2_x"], character["spe2_y"]))
            
            # 檢查是否超出畫面
            if character["spe2_x"] < -100 or character["spe2_x"] > width + 100:
                character["special2_active_ch2"] = False

    def handle_special2_move_ch2(ch2, ch1, keys, key_maps, screen, width):             
        # 檢查能量和血量條件
        if ch2["energy"] >= 70 and ch2["life"] <= 500*0.3 and not ch2.get("special2_active", False):
            # 檢查按鍵組合：中攻擊 + 右 + 左
            correct_keys = (keys[key_maps["medium"]] and keys[key_maps["defense"]] and keys[key_maps["right"]] and (keys[key_maps["left"]]))
            
            if correct_keys:
                ch2["special2_active_ch2"] = True
                ch2["attack_type"] = None
                ch2["energy"] -= 70  # 消耗70點能量
                ch2["is_in_hard_stun"] = True
                ch2["attack_start_time"] = pygame.time.get_ticks()
                ch2["hard_stun_duration"] = 500
                
                # 設置初始位置
                ch2["spe2_x"] = ch2["x"]
                ch2["spe2_y"] = ch2["y"]
                ch2["damage_dealt"] = False  # 添加傷害標記
                ch2["special2_direction"] = ch2["facing"]  # 使用ch2當前的面向方向
                print("open")  # 添加調試信息

        # 處理特殊技移動和碰撞
        if ch2["special2_active_ch2"]:
            move_speed = 5  # 移動速度
            
            # 根據ch2的面向方向移動
            if ch2["facing"] == 1:  # 向右
                ch2["spe2_x"] += move_speed
            else:  # 向左
                ch2["spe2_x"] -= move_speed
            
            # 創建攻擊判定區域
            attack_rect = pygame.Rect(
                ch2["spe2_x"],
                ch2["spe2_y"],
                ch2["width"],
                ch2["height"]
            )
            
            # 檢查碰撞
            if attack_rect.colliderect(ch1["hitbox_rect"]) and not ch2.get("damage_dealt", False):
                # 設置動畫狀態
                ch2["show_special2_animation"] = True
                ch2["animation_start_time"] = pygame.time.get_ticks()
                
                # 無視防禦，直接扣除60%血量
                damage = int(600 * 0.6)  
                ch1["life"] -= damage
                ch1["life"] = max(0, ch1["life"])
                ch1["is_hurt"] = True
                ch1["hurt_start_time"] = pygame.time.get_ticks()
                ch1["hurt_duration"] = 800

                
                # 添加擊退效果
                knockback_distance = 100
                if ch2["facing"] == 1:  # 如果ch2面向右
                    ch1["x"] += knockback_distance
                else:  # 如果ch2面向左
                    ch1["x"] -= knockback_distance
                
                # 確保不會超出畫面邊界
                ch1["x"] = max(0, min(ch1["x"], width - ch1["width"]))
                
                # 設置擊飛狀態
                ch1["is_in_hard_stun"] = True
                ch1["attack_start_time"] = pygame.time.get_ticks()
                ch1["hard_stun_duration"] = 800
                
                # 添加擊飛效果
                ch1["is_jumping"] = True
                ch1["vertical_speed"] = -ch1["jump_speed"] * 1.5
                
                ch2["damage_dealt"] = True
                ch2["special2_active_ch2"] = False
                ch2["is_in_hard_stun"] = False
                
    def draw_special2_animation(screen, character, width, height):
        if character.get("show_special2_animation", False):
            current_time = pygame.time.get_ticks()
            if current_time - character["animation_start_time"] < 1500:  # 1.5秒動畫
                # 創建全黑背景
                black_surface = pygame.Surface((width, height))
                black_surface.fill((0, 0, 0))
                screen.blit(black_surface, (0, 0))
                
                try:
                    # 載入所有ch2_shi_img資料夾中的圖片
                    images = []
                    image_dir = os.path.join(os.path.dirname(__file__), "inside", "test_pic", "ch2_shi_img")
                    
                    # 檢查目錄是否存在
                    if not os.path.exists(image_dir):
                        print(f"錯誤：目錄 {image_dir} 不存在")
                        return
                        
                    # 列出目錄中的所有文件
                    files = os.listdir(image_dir)
                    
                    # 載入所有PNG圖片
                    for filename in files:
                        if filename.endswith('.png'):
                            img_path = os.path.join(image_dir, filename)
                            try:
                                img = pygame.image.load(img_path)
                                img = pygame.transform.scale(img, (200, 200))
                                images.append(img)
                            except Exception as e:
                                print(f"載入圖片 {filename} 時出錯: {e}")
                    
                    if images:
                        # 每50毫秒切換一張圖片
                        frame_duration = 50  # 每幀50毫秒
                        current_frame = (current_time - character["animation_start_time"]) // frame_duration
                        current_frame = current_frame % len(images)  # 循環播放
                        
                        # 獲取當前幀的圖片
                        current_image = images[current_frame]
                        
                        # 使用當前時間作為隨機種子，確保每幀位置都不同
                        random.seed(current_time + current_frame)
                        
                        # 計算隨機位置（確保圖片不會超出螢幕）
                        max_x = width - current_image.get_width()
                        max_y = height - current_image.get_height()
                        image_x = random.randint(10, max_x)
                        image_y = random.randint(10, max_y)
                        
                        # 繪製圖片
                        screen.blit(current_image, (image_x, image_y))
                        pygame.display.flip()  # 強制更新顯示
                    else:
                        print("警告：沒有找到任何圖片")
                except Exception as e:
                    print(f"特殊技2動畫顯示錯誤: {e}")
                    import traceback
                    traceback.print_exc()
            else:
                # 動畫結束
                character["show_special2_animation"] = False

    # 顯示勝利畫面
    def show_winner_screen(winner):
        pygame.init()
        screen = pygame.display.set_mode((640, 500))
        pygame.display.set_caption("Winner Screen")
        font = pygame.font.SysFont('microsoftjhenghei', 74)
        small_font = pygame.font.SysFont('microsoftjhenghei', 36)

        # 背景顏色
        screen.fill((0, 0, 0))

        # 顯示勝利者
        winner_text = font.render(f"{winner} Wins!", True, (255, 255, 255))
        text_rect = winner_text.get_rect(center=(320, 200))
        screen.blit(winner_text, text_rect)

        # 顯示選項
        restart_text = small_font.render("Press R to Restart", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=(320, 300))
        screen.blit(restart_text, restart_rect)

        quit_text = small_font.render("Press Q to Quit", True, (255, 255, 255))
        quit_rect = quit_text.get_rect(center=(320, 350))
        screen.blit(quit_text, quit_rect)

        pygame.display.flip()
        # 等待玩家選擇
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # 按下 R 鍵重新開始
                        pygame.quit()
                        subprocess.run(["python", "main.py"])  # 執行 main.py
                        sys.exit()
                        
                    elif event.key == pygame.K_q:  # 按下 Q 鍵退出遊戲
                        pygame.quit()
                        sys.exit()

    # 背景
    img_bg = pygame.image.load("inside/test_pic/backpic.png")
    bg_x = 0

    # 建立時鐘物件，用於控制遊戲更新頻率
    clock = pygame.time.Clock()

    # 倒數計時器
    countdown_time = 99  # 倒數時間（秒）

     # === 主遊戲迴圈 ===
    while True:
        if player.get("show_special2_animation", False):
            draw_special2_animation(screen, player, width, height)
            pygame.display.update()
            clock.tick(120)
            # 動畫結束後立即判斷勝負
            if not player.get("show_special2_animation", False):
                if player["life"] <= 0:
                    show_winner_screen("Player 2")
                    pygame.quit()
                    sys.exit()
                if opponent["life"] <= 0:
                    show_winner_screen("Player 1")
                    pygame.quit()
                    sys.exit()
            continue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 檢查角色生命值
            if player["life"] <= 0:
                show_winner_screen("Player 2")  # 顯示玩家 2 勝利畫面
                pygame.quit()
                sys.exit()

            if opponent["life"] <= 0:
                show_winner_screen("Player 1")  # 顯示玩家 1 勝利畫面
                pygame.quit()
                sys.exit()
               # 計算剩餘時間
            current_time = pygame.time.get_ticks()
            remaining_time = max(0, countdown_time - current_time // 1000)  # 計算剩餘時間，防止小於 0

            # 如果時間結束，判定勝負
            if remaining_time == 0:
                if player["life"] > opponent["life"]:
                    show_winner_screen("Player 1")  # 顯示玩家 1 勝利畫面
                elif opponent["life"] > player["life"]:
                    show_winner_screen("Player 2")  # 顯示玩家 2 勝利畫面
                else:
                    show_winner_screen("Draw")  # 平局
                pygame.quit()
                sys.exit()
            current_time = pygame.time.get_ticks()

            if player["is_broken"]:
                if current_time - player["break_start_time"] > 2000:  # 破防持續 2 秒
                    player["is_broken"] = False  # 恢復狀態
                    player["block_energy"] = 50  # 恢復部分防禦條
            if opponent["is_broken"]:
                if current_time - opponent["break_start_time"] > 2000:  # 破防持續 2 秒
                    opponent["is_broken"] = False  # 恢復狀態
                    opponent["block_energy"] = 50  # 恢復部分防禦條
            # 防禦條自動回復（破防時不回復）
            block_recover_speed = 1  # 每幀回復量，可自行調整
            if not player["is_broken"] and player["block_energy"] < 100:
                player["block_energy"] = min(100, player["block_energy"] + block_recover_speed)
            if not opponent["is_broken"] and opponent["block_energy"] < 100:
                opponent["block_energy"] = min(100, opponent["block_energy"] + block_recover_speed)
            
            # 處理倒地狀態
            if player["is_knockdown"]:
                if pygame.time.get_ticks() - player["knockdown_start_time"] > player["knockdown_duration"]:
                    player["is_knockdown"] = False
                    player["y"] = 300  # 站起來
                    player["knockdown_angle"] = 0
            if opponent["is_knockdown"]:
                if pygame.time.get_ticks() - opponent["knockdown_start_time"] > opponent["knockdown_duration"]:
                    opponent["is_knockdown"] = False
                    opponent["y"] = 300  # 站起來
                    opponent["knockdown_angle"] = 0

            # 處理攻擊碰撞
            handle_attack(event, player, player_keys)
            handle_attack(event, opponent, opponent_keys)

            # 更新角色面向方向
            if player["x"] > opponent["x"]:
                player["facing"] = -1
                opponent["facing"] = 1
                
            else:
                player["facing"] = 1
                opponent["facing"] = -1
                

            update_character_image(player, opponent)

            # 更新角色圖片
            current_time = pygame.time.get_ticks()
            if player["attack_type"] is not None and current_time - player["attack_start_time"] > player["hard_stun_duration"]:
                player["attack_type"] = None
                player["damage_done"] = False  # 重置傷害標記

            if opponent["attack_type"] is not None and current_time - opponent["attack_start_time"] > opponent["hard_stun_duration"]:
                opponent["attack_type"] = None
                opponent["damage_done"] = False  # 重置傷害標記
                
            # 檢查 ch1 的硬直恢復
            if player["is_hurt"] and current_time - player["hurt_start_time"] > player["hurt_duration"]:
                player["is_hurt"] = False  # 結束受傷狀態

            # 檢查 ch2 的硬直恢復
            if opponent["is_hurt"] and current_time - opponent["hurt_start_time"] > opponent["hurt_duration"]:
                opponent["is_hurt"] = False  # 結束受傷狀態

            # 檢查 ch1 的硬直恢復
            if player["is_in_hard_stun"] and current_time - player["attack_start_time"] > player["hard_stun_duration"]:
                player["is_in_hard_stun"] = False  # 結束硬直狀態

            # 檢查 ch2 的硬直恢復
            if opponent["is_in_hard_stun"] and current_time - opponent["attack_start_time"] > opponent["hard_stun_duration"]:
                opponent["is_in_hard_stun"] = False  # 結束硬直狀態

        

        current_time = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()
        handle_movement(keys, player,opponent,player_keys)
        handle_movement(keys, opponent,player, opponent_keys)
        # 同步更新 hitbox_rect 的位置
        if player["facing"] == 1:
            player["hitbox_rect"].topleft = (player["x"]+5, player["y"])
            opponent["hitbox_rect"].topleft = (opponent["x"]+25, opponent["y"])
        elif player["facing"] == -1:
            player["hitbox_rect"].topleft = (player["x"]+25, player["y"])
            opponent["hitbox_rect"].topleft = (opponent["x"]+20, opponent["y"])

                  # 處理防禦按鍵
        if keys[player_keys["defense"]]:
            player["is_blocking"] = True
        else:
            player["is_blocking"] = False

        if keys[opponent_keys["defense"]]:
            opponent["is_blocking"] = True
        else:
            opponent["is_blocking"] = False

        # 處理特殊技

        handle_special_move_ch2(player, opponent, keys, player_keys, screen, width)
        handle_special2_move_ch2(player, opponent, keys, player_keys, screen, width)

        handle_special_move(opponent, player, keys, opponent_keys, screen, width)
        handle_special2_move(opponent, player, keys, opponent_keys, screen, width)
        

        # 檢查升龍拳落地
        if player["special2_active"] and not player["is_jumping"]:
            player["special2_active"] = False
            player["is_in_hard_stun"] = False
            player["attack_type"] = None

        # 處理攻擊碰撞
        handle_attack_collision(player, opponent)
        handle_attack_collision(opponent, player)

        if player.get("show_special2_animation", False):
            draw_special2_animation(screen, player, width, height)
            pygame.display.update()
            clock.tick(60)
            continue  # 跳過本幀其他繪圖

        # 清空畫面
        screen.fill(BLACK)

        # 繪製背景
        screen.blit(img_bg, (bg_x, 0))

        # 繪製生命值條
        draw_health_bar_ch2(screen, player, 50, 20, 200, 20, GREEN)  # 玩家生命值條
        draw_health_bar_ch1(screen, opponent, 390, 20, 200, 20, GREEN)  # 對手生命值條

        # 繪製能量條
        draw_energy_bar(screen, player, 50, height - 40, 200, 20, BLUE)  # 玩家能量條
        draw_energy_bar(screen, opponent, 390, height - 40, 200, 20, BLUE)  # 對手能量條

        # 繪製防禦條
        draw_block_bar(screen, player, 50, 50, 200, 10, RED)  # 玩家 1 防禦條
        draw_block_bar(screen, opponent, 390, 50, 200, 10, RED)  # 玩家 2 防禦條

            
        # 繪製倒數時間
        font = pygame.font.SysFont('microsoftjhenghei', 36)
        timer_text = font.render(f"{remaining_time}", True, WHITE)
        timer_rect = timer_text.get_rect(center=(width // 2, 30))  # 顯示在生命條中間
        screen.blit(timer_text, timer_rect)

        

        # 特殊技繪製
        draw_special_move_ch2(screen, player)
        draw_special2_move_ch2(screen, player)

        draw_special_move(screen, opponent)
        draw_special2_move(screen, opponent)

        # 繪製角色
        draw_character_ch2(screen, player)
        draw_character_ch1(screen, opponent)

        draw_special2_animation(screen, player, width, height)
        
        

        # 用圖片顯示 hitbox
        screen.blit(player["hitbox_img_ch2"], player["hitbox_rect"].topleft)    # 玩家 1 的 hitbox 圖片
        screen.blit(opponent["hitbox_img_ch1"], opponent["hitbox_rect"].topleft)  # 玩家 2 的 hitbox 圖片

        

        # 邊界限制
        if player["x"] < 0:
            player["x"] = 0
        elif player["x"] > width - player["width"]:
            player["x"] = width - player["width"]
        if opponent["x"] < 0:
            opponent["x"] = 0
        elif opponent["x"] > width - opponent["width"]:
            opponent["x"] = width - opponent["width"]
        
        pygame.display.update()
        clock.tick(120)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        selected_character = sys.argv[1]
    else:
        selected_character = "角色2"  # 預設角色
    main(selected_character)