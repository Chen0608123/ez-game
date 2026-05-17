import pygame
import sys
import subprocess  # 用於執行其他 Python 檔案


def main():
    # 定義顏色
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    # 定義視窗大小
    WIDTH = 800
    HEIGHT = 600

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("格鬥遊戲")

    font = pygame.font.SysFont('microsoftjhenghei', 74)
    title_text = font.render("格鬥遊戲", True, (255, 255, 255))
    start_text = font.render("開始遊戲", True, (255, 255, 255))
    rule_text = font.render("如何遊玩", True, (255, 255, 255))
    quit_text = font.render("退出遊戲", True, (255, 255, 255))

    selected = 0
    options = [start_text, rule_text, quit_text]

    while True:
        screen.fill((BLACK))
        screen.blit(title_text, (250, 100))
        font1 = pygame.font.SysFont('microsoftjhenghei', 24)
        help_text = font1.render("上、下選擇選單，enter選擇", True, WHITE)
        screen.blit(help_text, (10, HEIGHT - 30))
        for i, option in enumerate(options):
            color = (255, 255, 255) if i == selected else (100, 100, 100)
            text = font.render("開始遊戲" if i == 0 else "如何遊玩" if i == 1 else "退出遊戲", True, color)
            screen.blit(text, (300, 250 + i * 100))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if selected == 0:  # 開始遊戲
                        pygame.quit()  # 關閉當前的 Pygame 視窗
                        subprocess.run(["python", "choose.py"])  # 執行 choose.py
                        sys.exit()
                    elif selected == 1:  # 如何遊玩
                        pygame.quit()  # 關閉當前的 Pygame 視窗
                        subprocess.run(["python", "interface.py"])  # 執行 rules.py
                        sys.exit()
                    elif selected == 2:  # 退出遊戲
                        pygame.quit()
                        sys.exit()


if __name__ == "__main__":
    main()