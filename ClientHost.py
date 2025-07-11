import pygame
from Network import Network  # Use local network
from player import Player

pygame.init()
width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Host Player (Player 0)")

class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("Lexend", 40)
        text = font.render(self.text, True, (255, 255, 255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False

def redrawWindow(win, game, p):
    win.fill((128, 128, 128))

    if not (game.connected()):
        font = pygame.font.SysFont("Lexend", 60)
        text = font.render("Waiting for remote player...", True, (255, 0, 0))
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
        
        # Show IP address for others to connect
        font_small = pygame.font.SysFont("Lexend", 30)
        ip_text = font_small.render("Share this IP: 172.25.27.124", True, (0, 255, 0))
        win.blit(ip_text, (width/2 - ip_text.get_width()/2, height/2 + 50))
    else:
        font = pygame.font.SysFont("Lexend", 60)
        text = font.render("Your move", True, (0, 255, 255))
        win.blit(text, (80, 200))

        text = font.render("Remote Player", True, (0, 255, 255))
        win.blit(text, (390, 200))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        if game.bothWent():
            text1 = font.render(move1, True, (0, 0, 0))
            text2 = font.render(move2, True, (0, 0, 0))
        else:
            if game.p1Went and p == 0:
                text1 = font.render(move1, True, (0, 0, 0))
            elif game.p1Went:
                text1 = font.render("Locked in...", True, (0, 0, 0))
            else:
                text1 = font.render("Waiting...", True, (0, 0, 0))

            if game.p2Went and p == 1:
                text2 = font.render(move2, True, (0, 0, 0))
            elif game.p2Went:
                text2 = font.render("Locked in...", True, (0, 0, 0))
            else:
                text2 = font.render("Waiting...", True, (0, 0, 0))

        if p == 1:
            win.blit(text2, (100, 350))
            win.blit(text1, (400, 350))
        else:
            win.blit(text1, (100, 350))
            win.blit(text2, (400, 350))

        for btn in btns:
            btn.draw(win)

    pygame.display.update()

btns = [Button("Rock", 50, 500, (0, 0, 0)), Button("Scissors", 250, 500, (128, 0, 0)), Button("Paper", 450, 500, (70, 130, 180))]

def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()  # Uses localhost connection
    player = int(n.getP())
    print("You are the host player (Player", player, ")")
    print("Share your IP (172.25.27.124) with the other player!")

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("No game found")
            break

        if game.bothWent():
            redrawWindow(win, game, player)
            pygame.time.delay(500)
            try:
                game = n.send("reset")
            except:
                run = False
                print("No game found")
                break

            font = pygame.font.SysFont("Lexend", 90)
            if (game.winner() == 1 and player == 1) or (game.winner() == 0 and player == 0):
                text = font.render("You win!", True, (255, 0, 0))
            elif game.winner() == -1:
                text = font.render("Tie!", True, (255, 0, 0))
            else:
                text = font.render("You Lose!", True, (255, 0, 0))

            win.blit(text, (width/2 - text.get_width()/2, height/8 - text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos) and game.connected:
                        if player == 0:
                            if not game.p1Went:
                                n.send(btn.text)
                        else:
                            if not game.p2Went:
                                n.send(btn.text)
        redrawWindow(win, game, player)

if __name__ == "__main__":
    main()
