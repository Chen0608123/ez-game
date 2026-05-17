import pygame
import sys
import subprocess  # 用於執行其他 Python 檔案

def main():
    # 初始化pygame
    pygame.init()
    # 設定視窗標題
    pygame.display.set_caption("選擇角色")
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    LIGHT_BLUE = (173, 216, 230)
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.SysFont('microsoftjhenghei', 36)
    clock = pygame.time.Clock()

    # 載入角色圖片
    ch1_image = pygame.image.load("inside/test_pic/ch1.png")
    ch2_image = pygame.image.load("inside/test_pic/ch2.png")
    ch1_image = pygame.transform.scale(ch1_image, (100, 150))  # 調整圖片大小
    ch2_image = pygame.transform.scale(ch2_image, (100, 150))

    # 角色選項
    characters = ["角色1", "角色2"]
    images = [ch1_image, ch2_image]
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
                    pygame.quit()
                    # 根據選擇的角色跳轉到不同場景
                    if characters[selected] == "角色1":
                        subprocess.run(["python", "ch1_field.py", characters[selected]])
                    elif characters[selected] == "角色2":
                        subprocess.run(["python", "ch2_field.py", characters[selected]])
                    sys.exit()
                elif event.key == pygame.K_BACKSPACE:  # 按下 Backspace 返回主畫面
                    pygame.quit()
                    subprocess.run(["python", "main.py"])  # 執行 main.py
                    sys.exit()

        # === 畫面渲染 ===
        screen.fill(LIGHT_BLUE)
        title_text = font.render("選擇你的角色", True, WHITE)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))
        font1 = pygame.font.SysFont('microsoftjhenghei', 24)
        help_text = font1.render("方向鍵左、右選擇選單，Enter選擇 | Backspace返回主畫面", True, WHITE)
        screen.blit(help_text, (10, HEIGHT - 30))

        # 顯示角色圖片和名稱
        for i, image in enumerate(images):
            x = 200 + i * 300
            y = 200
            screen.blit(image, (x, y))
            color = WHITE if i == selected else (100, 100, 100)
            char_text = font.render(characters[i], True, color)
            screen.blit(char_text, (x + image.get_width() // 2 - char_text.get_width() // 2, y + 160))

        # 高亮選中的角色
        if selected == 0:
            pygame.draw.rect(screen, WHITE, (190, 190, 170, 170), 3)  # 高亮角色1
        else:
            pygame.draw.rect(screen, WHITE, (490, 190, 170, 170), 3)  # 高亮角色2

        # 更新畫面
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()