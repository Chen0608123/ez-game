import pygame
import sys
import subprocess  # 用於執行其他 Python 檔案

def main():
    # 定義顏色
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    WIDTH = 800
    HEIGHT = 600
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("角色2介紹")
    font = pygame.font.SysFont('microsoftjhenghei', 24)

    interface_img = pygame.image.load("inside\ch2_rule.png")
    interface_img = pygame.transform.scale(interface_img, (WIDTH, HEIGHT))  # 調整圖片大小


    while True:
        # 處理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:  # 按下 Backspace 返回主畫面
                    pygame.quit()
                    subprocess.run(["python", "main.py"])  # 執行 main.py
                    sys.exit()
                

        # === 畫面渲染 ===
        screen.fill(BLACK)
        screen.blit(interface_img, (0, 0))


        help_text = font.render("按 Backspace 返回主畫面", True, BLACK)
        screen.blit(help_text, (WIDTH // 2 - help_text.get_width() // 2, HEIGHT - 30))

        pygame.display.update()

if __name__ == "__main__":
    main()