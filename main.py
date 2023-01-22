import pygame
import sys
from pygame.locals import *


class game:
    state = ["Ahmed VS Yassine , Ahmed Won !"]

    def __init__(self):
        self.grid = [[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]]

    def affiche(self):
        for i in range(6):
            for j in range(7):
                print("|{}".format(self.grid[i][j]), end="")
            print("|")

    def validMove(self, x):
        return ((0 <= x <= 6) and self.grid[0][x] == 0)

    def select(self, x, mark):
        if (self.validMove(x)):
            cp = 0
            for i in range(6):
                if ((self.grid[i][x] != 0)):
                    self.grid[i-1][x] = mark
                    break
                else:
                    cp += 1
            if (cp == 6):
                self.grid[i][x] = mark
        else:
            print("Ce n'est pas valide !")
            s = int(input("Try Again !"))
            self.select(s, mark)


class player:
    def __init__(self, game: game, name=''):
        self.name = name
        self.win = False
        self.game = game
        self.draw = False
        self.color = (0, 0, 0)

    def checkLigne(self, mark, game: game):
        for i in range(0, 6):
            j = 0
            while (j != 4):
                if (game.grid[i][j] == game.grid[i][j+1] == game.grid[i][j+2] == game.grid[i][j+3] == mark):
                    return True
                else:
                    j += 1
        return False

    def checkCol(self, mark, game: game):
        for j in range(0, 7):
            i = 0
            while (i != 3):
                if (game.grid[i][j] == game.grid[i+1][j] == game.grid[i+2][j] == game.grid[i+3][j] == mark):
                    return True
                else:
                    i += 1
        return False

    def checkDiag1(self, mark, game: game):
        for j in range(0, 4):
            i = 0
            while (i != 3):
                if (game.grid[i][j] == game.grid[i+1][j+1] == game.grid[i+2][j+2] == game.grid[i+3][j+3] == mark):
                    return True
                else:
                    i += 1
        return False

    def checkDiag2(self, mark, game: game):
        for j in [6, 5, 4, 3]:
            i = 0
            while (i != 3):
                if (game.grid[i][j] == game.grid[i+1][j-1] == game.grid[i+2][j-2] == game.grid[i+3][j-3] == mark):

                    return True
                else:
                    i += 1
        return False

    def checkWin(self, mark, g):
        if (self.checkLigne(mark, g) or self.checkCol(mark, g) or self.checkDiag1(mark, g) or self.checkDiag2(mark, g)):
            self.win = True
            print("{} you won !!!".format(self.name))

    def checkDraw(self, g):
        res = True
        for i in range(0, 6):
            for j in range(0, 7):
                if (g.grid[i][j] != 0):
                    res = res and True
                else:
                    res = res and False
        if (res):
            print("its a draw !!")
        self.draw == res


class GameUI:
    p1Name = ''
    p2Name = ''

    def __init__(self):
        self.CHIP_SIZE = 80
        self.OFFSET = 60
        self.CHIP_OFFSET = 20
        self.BOARD_HEIGHT = 600
        self.CHIP_RADIUS = int(self.CHIP_SIZE / 2)

        pygame.init()
        pygame.font.init()
        pygame.display.set_caption('Connect 4 with Python')
        self.mainClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 700))
        # self._board_img = pygame.image.load("./img/board.png")
        # self._board_img_numbers = pygame.image.load("./img/board_numbers.png")
        self.fontTitre = pygame.font.SysFont('Calibri', 50)
        self.font = pygame.font.SysFont('Calibri', 26)

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    click = False

    def getNames(self):
        screen = pygame.display.set_mode((700, 600))
        screen.fill((0, 190, 255))
        pygame.display.set_caption('Names')
        user_ip1 = ''
        user_ip2 = ''
        font = pygame.font.SysFont('Calibri', 26)
        text_box1 = pygame.Rect(350, 190, 200, 50)
        text_box2 = pygame.Rect(350, 250, 200, 50)
        button_1 = pygame.Rect(450, 400, 150, 50)
        active1 = False
        active2 = False
        color1 = pygame.Color('purple')
        color2 = pygame.Color('purple')
        clock = pygame.time.Clock()
        click = False
        while True:

            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if events.type == pygame.MOUSEBUTTONDOWN:
                    if events.button == 1:
                        click = True
                        if button_1.collidepoint((events.pos)):
                            if click:
                                self.board(user_ip1, user_ip2)
                        else:
                            if text_box1.collidepoint(events.pos):
                                active1 = True
                            else:
                                active1 = False
                            if text_box2.collidepoint(events.pos):
                                active2 = True
                            else:
                                active2 = False

                if events.type == pygame.KEYDOWN:
                    if active1:
                        if events.key == pygame.K_BACKSPACE:
                            user_ip1 = user_ip1[:-1]
                        else:
                            user_ip1 += events.unicode
                    if active2:
                        if events.key == pygame.K_BACKSPACE:
                            user_ip2 = user_ip2[:-1]
                        else:
                            user_ip2 += events.unicode

            if active1:
                color1 = pygame.Color('red')
            else:
                color1 = pygame.Color('purple')
            if active2:
                color2 = pygame.Color('red')
            else:
                color2 = pygame.Color('purple')

            self.draw_text('Enter Your name :', font,
                           (0, 0, 0), self.screen, 50, 130)
            self.draw_text('Player 1', font,
                           (0, 0, 0), self.screen, 80, 200)
            self.draw_text('Player 2', font,
                           (0, 0, 0), self.screen, 80, 260)

            pygame.draw.rect(self.screen, color1, text_box1, 4)
            pygame.draw.rect(self.screen, color2, text_box2, 4)
            pygame.draw.rect(self.screen, (255, 0, 0), button_1)
            self.draw_text('NEXT', font,
                           (255, 255, 255), self.screen, 497, 413)

            surf1 = font.render(user_ip1, True, 'black')
            surf2 = font.render(user_ip2, True, 'black')

            self.screen.blit(surf1, (text_box1.x + 5, text_box1.y + 5))
            self.screen.blit(surf2, (text_box2.x + 5, text_box2.y + 5))

            pygame.display.update()
            clock.tick(50)

    def winner(self, name1, c, lis):
        while True:
            text_box1 = pygame.Rect(100, 200, 500, 300)
            if (c == 'win'):
                st = name1+" is the winner"
            if (c == 'draw'):
                st = "its a draw !"

            button_1 = pygame.Rect(400, 400, 150, 50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == MOUSEBUTTONDOWN:
                    if 550 > pygame.mouse.get_pos()[0] > 400 and 450 > pygame.mouse.get_pos()[1] > 400:
                        self.main_menu(lis)

            pygame.draw.rect(self.screen, (255, 255, 255), text_box1, 0, 20)
            self.draw_text(st, self.fontTitre, (0, 0, 255),
                           self.screen, 210, 280)

            pygame.draw.rect(self.screen, (255, 0, 0), button_1)
            self.draw_text('NEXT', self.font,
                           (255, 255, 255), self.screen, 447, 413)

            pygame.display.update()

    def board(self, n1, n2):

        running = True
        g = game()
        p1 = player(GameUI.p1Name, g)
        p2 = player(GameUI.p2Name, g)

        while running:
            self._screen = pygame.display.set_mode((700, 800))
            self.screen.fill((0, 0, 0))
            RED = (255, 0, 0)
            YELLOW = (255, 255, 0)
            GREEN = (0, 100, 0)
            button_1 = pygame.Rect(25, 620, 50, 50)
            button_2 = pygame.Rect(125, 620, 50, 50)
            button_3 = pygame.Rect(225, 620, 50, 50)
            button_4 = pygame.Rect(325, 620, 50, 50)
            button_5 = pygame.Rect(425, 620, 50, 50)
            button_6 = pygame.Rect(525, 620, 50, 50)
            button_7 = pygame.Rect(625, 620, 50, 50)
            pygame.draw.rect(self.screen, (0, 150, 0), button_1)
            pygame.draw.rect(self.screen, (0, 150, 0), button_2)
            pygame.draw.rect(self.screen, (0, 150, 0), button_3)
            pygame.draw.rect(self.screen, (0, 150, 0), button_4)
            pygame.draw.rect(self.screen, (0, 150, 0), button_5)
            pygame.draw.rect(self.screen, (0, 150, 0), button_6)
            pygame.draw.rect(self.screen, (0, 150, 0), button_7)

            c = 0

            while (((p1.win == False) and (p2.win == False)) and (p1.draw == False)):

                for row in range(6):
                    for col in range(7):
                        pygame.draw.rect(self.screen, GREEN,
                                         (col * 100, row * 100, 100, 100), 2)
                        if g.grid[row][col] == 1:
                            pygame.draw.circle(
                                self.screen, RED, (col * 100 + 50, row * 100 + 50), 40)
                        elif g.grid[row][col] == 2:
                            pygame.draw.circle(
                                self.screen, YELLOW, (col * 100 + 50, row * 100 + 50), 40)

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == MOUSEBUTTONDOWN:
                        print(c)
                        pygame.draw.rect(self.screen, (0, 0, 0),
                                         (0, 670, 700, 700))
                        self.draw_text('{0}\'s Turn'.format(n2), self.fontTitre, (255, 255, 255),
                                       self.screen, 200, 700)
                        if (c % 2 == 0):

                            if 75 > pygame.mouse.get_pos()[0] > 25 and 670 > pygame.mouse.get_pos()[1] > 620:
                                g.select(0, 1)
                                g.affiche()
                                print('kmlt')
                                p1.checkDraw(g)
                                p1.checkWin(1, g)
                                if (p1.win == True):
                                    g.state.append("{} VS {} , {} Won !".format(
                                        n1, n2, n1))
                                    self.winner(n1, 'win', g.state)
                                    break
                                if (p1.draw == True):
                                    g.state.append(
                                        "{} VS {} , It's A Draw".format(n1, n2))
                                    self.winner(n1, 'draw', g.state)
                                    break
                                c += 1
                                break
                            if 175 > pygame.mouse.get_pos()[0] > 125 and 670 > pygame.mouse.get_pos()[1] > 620:
                                g.select(1, 1)
                                g.affiche()
                                p1.checkDraw(g)
                                p1.checkWin(1, g)
                                if (p1.win == True):
                                    g.state.append("{} VS {} , {} Won !".format(
                                        n1, n2, n1))
                                    self.winner(n1, 'win', g.state)
                                    break
                                if (p1.draw == True):
                                    g.state.append(
                                        "{} VS {} , It's A Draw".format(n1, n2))
                                    self.winner(n1, 'draw', g.state)
                                    break
                                c += 1
                                break
                            if 275 > pygame.mouse.get_pos()[0] > 225 and 670 > pygame.mouse.get_pos()[1] > 620:
                                g.select(2, 1)
                                g.affiche()
                                p1.checkDraw(g)
                                p1.checkWin(1, g)
                                if (p1.win == True):
                                    g.state.append("{} VS {} , {} Won !".format(
                                        n1, n2, n1))
                                    self.winner(n1, 'win', g.state)
                                    break
                                if (p1.draw == True):
                                    g.state.append(
                                        "{} VS {} , It's A Draw".format(n1, n2))
                                    self.winner(n1, 'draw', g.state)
                                    break
                                c += 1
                                break
                            if 375 > pygame.mouse.get_pos()[0] > 325 and 670 > pygame.mouse.get_pos()[1] > 620:
                                g.select(3, 1)
                                g.affiche()
                                p1.checkDraw(g)
                                p1.checkWin(1, g)
                                if (p1.win == True):
                                    g.state.append("{} VS {} , {} Won !".format(
                                        n1, n2, n1))
                                    self.winner(n1, 'win', g.state)
                                    break
                                if (p1.draw == True):
                                    g.state.append(
                                        "{} VS {} , It's A Draw".format(n1, n2))
                                    self.winner(n1, 'draw', g.state)
                                    break
                                c += 1
                                break
                            if 475 > pygame.mouse.get_pos()[0] > 425 and 670 > pygame.mouse.get_pos()[1] > 620:
                                g.select(4, 1)
                                g.affiche()
                                p1.checkDraw(g)
                                p1.checkWin(1, g)
                                if (p1.win == True):
                                    g.state.append("{} VS {} , {} Won !".format(
                                        n1, n2, n1))
                                    self.winner(n1, 'win', g.state)
                                    break
                                if (p1.draw == True):
                                    g.state.append(
                                        "{} VS {} , It's A Draw".format(n1, n2))
                                    self.winner(n1, 'draw', g.state)
                                    break
                                c += 1
                                break
                            if 575 > pygame.mouse.get_pos()[0] > 525 and 670 > pygame.mouse.get_pos()[1] > 620:
                                g.select(5, 1)
                                g.affiche()
                                p1.checkDraw(g)
                                p1.checkWin(1, g)
                                if (p1.win == True):
                                    g.state.append("{} VS {} , {} Won !".format(
                                        n1, n2, n1))
                                    self.winner(n1, 'win', g.state)
                                    break
                                if (p1.draw == True):
                                    g.state.append(
                                        "{} VS {} , It's A Draw".format(n1, n2))
                                    self.winner(n1, 'draw', g.state)
                                    break
                                c += 1
                                break
                            if 675 > pygame.mouse.get_pos()[0] > 625 and 670 > pygame.mouse.get_pos()[1] > 620:
                                g.select(6, 1)
                                g.affiche()
                                p1.checkDraw(g)
                                p1.checkWin(1, g)
                                if (p1.win == True):
                                    g.state.append("{} VS {} , {} Won !".format(
                                        n1, n2, n1))
                                    self.winner(n1, 'win', g.state)
                                    break
                                if (p1.draw == True):
                                    g.state.append(
                                        "{} VS {} , It's A Draw".format(n1, n2))
                                    self.winner(n1, 'draw', g.state)
                                    break
                                c += 1
                                break
                            self.draw_text('{0}\'s Turn'.format(n2), self.fontTitre, (255, 255, 255),
                                           self.screen, 200, 700)

                        else:
                            pygame.draw.rect(self.screen, (0, 0, 0),
                                             (0, 670, 700, 700))
                            self.draw_text('{0}\'s Turn'.format(n1), self.fontTitre, (255, 255, 255),
                                           self.screen, 200, 700)

                            if 75 > pygame.mouse.get_pos()[0] > 25 and 670 > pygame.mouse.get_pos()[1] > 620:
                                g.select(0, 2)
                                g.affiche()
                                p2.checkDraw(g)
                                p2.checkWin(2, g)
                                if (p2.win == True):
                                    g.state.append("{} VS {} , {} Won !".format(
                                        n2, n1, n2))
                                    self.winner(n2, 'win', g.state)
                                    break
                                if (p2.draw == True):
                                    g.state.append(
                                        "{} VS {} , It's A Draw".format(n1, n2))
                                    self.winner(n1, 'draw', g.state)
                                    break
                                c += 1
                                break
                            if 175 > pygame.mouse.get_pos()[0] > 125 and 670 > pygame.mouse.get_pos()[1] > 620:
                                g.select(1, 2)
                                g.affiche()
                                p2.checkDraw(g)
                                p2.checkWin(2, g)
                                if (p2.win == True):
                                    g.state.append("{} VS {} , {} Won !".format(
                                        n2, n1, n2))
                                    self.winner(n2, 'win', g.state)
                                    break
                                if (p2.draw == True):
                                    g.state.append(
                                        "{} VS {} , It's A Draw".format(n1, n2))
                                    self.winner(n1, 'draw', g.state)
                                    break
                                c += 1
                                break
                            if 275 > pygame.mouse.get_pos()[0] > 225 and 670 > pygame.mouse.get_pos()[1] > 620:
                                g.select(2, 2)
                                g.affiche()
                                p2.checkDraw(g)
                                p2.checkWin(2, g)
                                if (p2.win == True):
                                    g.state.append("{} VS {} , {} Won !".format(
                                        n2, n1, n2))
                                    self.winner(n2, 'win', g.state)
                                    break
                                if (p2.draw == True):
                                    g.state.append(
                                        "{} VS {} , It's A Draw".format(n1, n2))
                                    self.winner(n1, 'draw', g.state)
                                    break
                                c += 1
                                break
                            if 375 > pygame.mouse.get_pos()[0] > 325 and 670 > pygame.mouse.get_pos()[1] > 620:
                                g.select(3, 2)
                                g.affiche()
                                p2.checkDraw(g)
                                p2.checkWin(2, g)
                                if (p2.win == True):
                                    g.state.append("{} VS {} , {} Won !".format(
                                        n2, n1, n2))
                                    self.winner(n2, 'win', g.state)
                                    break
                                if (p2.draw == True):
                                    g.state.append(
                                        "{} VS {} , It's A Draw".format(n1, n2))
                                    self.winner(n1, 'draw', g.state)
                                    break
                                c += 1
                                break
                            if 475 > pygame.mouse.get_pos()[0] > 425 and 670 > pygame.mouse.get_pos()[1] > 620:
                                g.select(4, 2)
                                g.affiche()
                                p2.checkDraw(g)
                                p2.checkWin(2, g)
                                if (p2.win == True):
                                    g.state.append("{} VS {} , {} Won !".format(
                                        n2, n1, n2))
                                    self.winner(n2, 'win', g.state)
                                    break
                                if (p2.draw == True):
                                    g.state.append(
                                        "{} VS {} , It's A Draw".format(n1, n2))
                                    self.winner(n1, 'draw', g.state)
                                    break
                                c += 1
                                break
                            if 575 > pygame.mouse.get_pos()[0] > 525 and 670 > pygame.mouse.get_pos()[1] > 620:
                                g.select(5, 2)
                                g.affiche()
                                p2.checkDraw(g)
                                p2.checkWin(2, g)
                                if (p2.win == True):
                                    g.state.append("{} VS {} , {} Won !".format(
                                        n2, n1, n2))
                                    self.winner(n2, 'win', g.state)
                                    break
                                if (p2.draw == True):
                                    g.state.append(
                                        "{} VS {} , It's A Draw".format(n1, n2))
                                    self.winner(n1, 'draw', g.state)
                                c += 1
                                break
                            if 675 > pygame.mouse.get_pos()[0] > 625 and 670 > pygame.mouse.get_pos()[1] > 620:
                                g.select(6, 2)
                                g.affiche()
                                p2.checkDraw(g)
                                p2.checkWin(2, g)
                                if (p2.win == True):
                                    g.state.append("{} VS {} , {} Won !".format(
                                        n2, n1, n2))
                                    self.winner(n2, 'win', g.state)
                                    break
                                if (p2.draw == True):
                                    g.state.append(
                                        "{} VS {} , It's A Draw".format(n1, n2))
                                    self.winner(n1, 'draw', g.state)
                                    break
                                c += 1
                                break

                pygame.display.update()

    def history(self, lis):
        while True:
            self._screen = pygame.display.set_mode((800, 700))
            self.screen.fill((0, 190, 255))
            button_1 = pygame.Rect(400, 400, 150, 50)

            x = 0
            for a in lis:
                self.draw_text(a, self.font, (0, 0, 0), self.screen, 0, x)
                x += 30

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == MOUSEBUTTONDOWN:
                    if 550 > pygame.mouse.get_pos()[0] > 400 and 450 > pygame.mouse.get_pos()[1] > 400:
                        self.main_menu(lis)

            pygame.draw.rect(self.screen, (255, 0, 0), button_1)
            self.draw_text('BACK', self.font,
                           (255, 255, 255), self.screen, 447, 413)
            pygame.display.update()

    def main_menu(self, L):

        while True:
            self._screen = pygame.display.set_mode((800, 700))
            self.screen.fill((0, 190, 255))
            self.draw_text('Connect Four', self.fontTitre,
                           (0, 0, 0), self.screen, 280, 180)
            self.draw_text('Made by Ahmed Gharbi', self.font,
                           (0, 0, 0), self.screen, 280, 650)

            mx, my = pygame.mouse.get_pos()

            # creating buttons
            button_1 = pygame.Rect(310, 290, 200, 50)
            button_2 = pygame.Rect(310, 370, 200, 50)
            button_3 = pygame.Rect(310, 450, 200, 50)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if button_1.collidepoint((mx, my)):
                            self.getNames()
                        if button_2.collidepoint((mx, my)):
                            self.history(L)
                        if button_3.collidepoint((mx, my)):
                            pygame.quit()
                            sys.exit()

            # defining functions when a certain button is pressed

            pygame.draw.rect(self.screen, (255, 0, 0), button_1)
            pygame.draw.rect(self.screen, (255, 0, 0), button_2)
            pygame.draw.rect(self.screen, (255, 0, 0), button_3)

            # writing text on top of button
            self.draw_text('PLAY', self.font,
                           (255, 255, 255), self.screen, 385, 305)
            self.draw_text('HISTORY', self.font,
                           (255, 255, 255), self.screen, 365, 385)
            self.draw_text('EXIT', self.font,
                           (255, 255, 255), self.screen, 385, 465)

            pygame.display.update()
            self.mainClock.tick(60)


def sortie():
    pygame.quit()
    sys.exit()


# define screens
# Update the screen
# define screen functions
# main

ui = GameUI()
ui.main_menu(["Ahmed VS Yassine , Ahmed Won !"])
