import pygame


class game:
    state = ["Ahmed VS Yassine , Ahmed Won !"]

    def __init__(self):
        self.grid = [[0, 2, 1, 2, 1, 2, 1],
                     [1, 2, 1, 2, 1, 2, 1],
                     [2, 1, 2, 1, 2, 1, 2],
                     [1, 2, 1, 2, 1, 2, 1],
                     [1, 2, 1, 2, 1, 2, 1],
                     [1, 2, 1, 2, 1, 2, 1]]
        # self._screen = pygame.display.set_mode((800, 700))
        # self.CHIP_SIZE = 80
        # self.OFFSET = 60
        # self.CHIP_OFFSET = 20
        # self.BOARD_HEIGHT = 600
        # self.CHIP_RADIUS = int(self.CHIP_SIZE / 2)
        # pygame.init()
        # pygame.font.init()
        # pygame.display.set_caption('Puissance 4')
        # programIcon = pygame.image.load('logo.png')
        # pygame.display.set_icon(programIcon)
        # self._screen.fill((107, 232, 209))
        # self._font = pygame.font.SysFont('Calibri', 26)

    # def drawMain(self):
    #     text = self._font.render(
    #         "Welcome to Puissance 4 !", True, (50, 255, 50))
    #     self._screen.blit(text, (50, 10))
    #     pygame.display.flip()

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


class player:
    def __init__(self, name, game: game):
        self.name = name
        self.win = False
        self.game = game

    def checkLigne(self, mark):
        for i in range(0, 6):
            j = 0
            while (j != 4):
                if (self.game.grid[i][j] == self.game.grid[i][j+1] == self.game.grid[i][j+2] == self.game.grid[i][j+3] == mark):
                    return True
                else:
                    j += 1
        return False

    def checkCol(self, mark):
        for j in range(0, 7):
            i = 0
            while (i != 3):
                if (self.game.grid[i][j] == self.game.grid[i+1][j] == self.game.grid[i+2][j] == self.game.grid[i+3][j] == mark):
                    return True
                else:
                    i += 1
        return False

    def checkDiag1(self, mark):
        for j in range(0, 4):
            i = 0
            while (i != 3):
                if (self.game.grid[i][j] == self.game.grid[i+1][j+1] == self.game.grid[i+2][j+2] == self.game.grid[i+3][j+3] == mark):
                    return True
                else:
                    i += 1
        return False

    def checkDiag2(self, mark):
        for j in [6, 5, 4, 3]:
            i = 0
            while (i != 3):
                if (self.game.grid[i][j] == self.game.grid[i+1][j-1] == self.game.grid[i+2][j-2] == self.game.grid[i+3][j-3] == mark):

                    return True
                else:
                    i += 1
        return False

    def checkWin(self, mark):
        if (self.checkLigne(mark) or self.checkCol(mark) or self.checkDiag1(mark) or self.checkDiag2(mark)):
            self.win = True
            print("{} you won !!!".format(self.name))

    def checkDraw(self):
        res = True
        for i in range(0, 6):
            for j in range(0, 7):
                if (self.game.grid[i][j] != 0):
                    res = res and True
                else:
                    res = res and False
        if (res):
            print("its a draw !!")
        return res


def switch(choix):
    if (choix == 1):
        name1 = input("Name of the first player :")
        name2 = input("Name of the second player :")
        p1 = player(name1, g)
        p2 = player(name2, g)
        while (((p1.win == False) and (p2.win == False)) and (p1.checkDraw() == False)):
            print(p1.checkDraw())
            print("\nTour de {}".format(p1.name))
            g.affiche()
            x = int(input("Donner position : "))
            p1.game.select(x, 1)
            g.affiche()
            print(p1.checkDraw())
            p1.checkWin(1)
            if (p1.win == True):
                g.state.append("{} VS {} , {} Won !".format(
                    p1.name, p2.name, p1.name))
                break
            if (p1.checkDraw() == True):
                g.state.append(
                    "{} VS {} , It's A Draw".format(p1.name, p2.name))
                break
            print("\nTour de {}".format(p2.name))
            g.affiche()
            x = int(input("Donner position : "))
            p2.game.select(x, 2)
            g.affiche()
            p2.checkWin(2)
            if (p2.win == True):
                g.state.append("{} VS {} , {} Won !".format())
        a = input("Want to play again ? y/n")
        if (a == "y"):
            switch(1)
        else:
            switch(0)
    elif (choix == 2):
        print(g.state)
        print("0) Back")
        switch(int(input()))
    elif (choix == 3):
        return 0
    elif (choix == 0):
        print("Welcome to Puissance 4 !")
        print("1) Play")
        print("2) History")
        print("3) Exit")
        z = int(input())
        switch(z)


g = game()
switch(0)
