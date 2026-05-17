import pygame
import sys
import subprocess  # 用於執行其他 Python 檔案


def show_selected_character(character_name, character_image, script_path):
    """顯示玩家選擇的角色畫面，並提供返回主畫面的選項"""
    pygame.init()
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    width, height = 800, 500
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("角色選擇結果")
    font = pygame.font.SysFont('microsoftjhenghei', 36)

    # 主畫面
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # 按下 Enter 跳轉到對應腳本
                    pygame.quit()
                    try:
                        subprocess.run(["python", script_path], check=True)  # 執行對應腳本
                    except subprocess.CalledProcessError as e:
                        print(f"執行腳本失敗: {e}")
                    sys.exit()
                elif event.key == pygame.K_BACKSPACE:  # 按下 Backspace 返回主畫面
                    return  # 返回主畫面

        # 畫面渲染
        screen.fill(BLACK)
        title_text = font.render(f"你選擇了: {character_name}", True, WHITE)
        screen.blit(title_text, (width // 2 - title_text.get_width() // 2, 50))
        character_image = pygame.transform.scale(character_image, (300, 300))  # 放大角色圖片
        screen.blit(character_image, (width // 2 - character_image.get_width() // 2, 150))

        # 提示按鍵
        help_text = font.render("按 Enter 繼續 | 按 Backspace 返回主畫面", True, WHITE)
        screen.blit(help_text, (width // 2 - help_text.get_width() // 2, 450))

        pygame.display.update()


def main():
    # 初始化pygame
    pygame.init()
    # 設定視窗標題
    pygame.display.set_caption("角色選單")
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    # 視窗寬高設定
    width, height = 800, 500
    screen = pygame.display.set_mode((width, height))
    font = pygame.font.SysFont('microsoftjhenghei', 36)
    clock = pygame.time.Clock()

    # 載入角色圖片
    ch1_image = pygame.image.load("inside/test_pic/ch1.png")
    ch2_image = pygame.image.load("inside/test_pic/ch2.png")
    ch1_image = pygame.transform.scale(ch1_image, (100, 200))  # 調整圖片大小
    ch2_image = pygame.transform.scale(ch2_image, (100, 200))

    # 角色選項
    characters = ["角色1", "角色2"]
    images = [ch1_image, ch2_image]
    scripts = ["ch1_rule.py", "ch2_rule.py"]  # 確保路徑正確
    selected = 0

    # 主遊戲迴圈
    while True:
        # 處理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # 左鍵選擇上一個角色
                    selected = (selected - 1) % len(characters)
                elif event.key == pygame.K_RIGHT:  # 右鍵選擇下一個角色
                    selected = (selected + 1) % len(characters)
                elif event.key == pygame.K_RETURN:  # 按下 Enter 確認選擇
                    # 顯示選擇結果畫面並跳轉到對應腳本
                    show_selected_character(characters[selected], images[selected], scripts[selected])
                elif event.key == pygame.K_BACKSPACE:  # 按下 Backspace 返回主畫面
                    pygame.quit()
                    subprocess.run(["python", "main.py"], check=True)  # 執行 main.py
                    sys.exit()

        # === 畫面渲染 ===
        screen.fill(BLACK)
        title_text = font.render("選擇你的角色", True, WHITE)
        screen.blit(title_text, (width // 2 - title_text.get_width() // 2, 50))
        font1 = pygame.font.SysFont('microsoftjhenghei', 24)
        help_text = font1.render("方向鍵左、右選擇選單，Enter選擇 | Backspace返回主畫面", True, WHITE)
        screen.blit(help_text, (10, height - 30))

        # 顯示角色圖片和名稱
        if selected == 0:
            screen.blit(ch1_image, (200, 200))
            ch1_text = font.render(characters[0], True, WHITE)
            screen.blit(ch1_text, (200 + ch1_image.get_width() // 2 - ch1_text.get_width() // 2, 360))
        else:
            screen.blit(ch2_image, (450, 200))
            ch2_text = font.render(characters[1], True, WHITE)
            screen.blit(ch2_text, (450 + ch2_image.get_width() // 2 - ch2_text.get_width() // 2, 360))

        # 高亮選中的角色
        if selected == 0:
            pygame.draw.rect(screen, WHITE, (140, 190, 270, 270), 3)  # 高亮角色1
        else:
            pygame.draw.rect(screen, WHITE, (390, 190, 270, 270), 3)  # 高亮角色2

        # 更新畫面
        pygame.display.update()
        clock.tick(60)


# 執行程式
if __name__ == "__main__":
    main()