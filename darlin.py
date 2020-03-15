import pygame as pg,sys
import time
from pygame.locals import  *

# variables locales
"""
    ici on definit les variables globales tels que le gagnant,la taille de la fenetre,etc
    @author : darlin :)
"""
XO = 'x'
winner = None
width = 400
height =400
draw = False
white= (255,255,255)
line_color = (10,10,10)

# plan de jeu
BOARD=[[None] * 3, [None] * 3, [None] * 3]


#initialiser les valeurs de pygame

pg.init()
fps=30
CLOCK=pg.time.Clock()
screen = pg.display.set_mode((width,height+100),0,32)
pg.display.set_caption("TIC TAC TOE DE DARLIN")

#Traiter les images

opening =pg.image.load('tic tac opening.png')
o_img = pg.image.load('O.png')
x_img = pg.image.load('X.png')

#donner une bonne taille

opening = pg.transform.scale(opening,(width,height+100))
x_img = pg.transform.scale(x_img,(80,80))
o_img = pg.transform.scale(o_img,(80,80))

#definition des fonctions de jeu

def game_opening():
    screen.blit(opening,(0,0))
    pg.display.update()
    time.sleep(1)
    screen.fill(white)

    #Dessiner la ligne verticale
    pg.draw.line(screen , line_color ,(width/3,0) , (width/3 , height) , 7)
    pg.draw.line(screen , line_color , (width/3*2,0),(width/3*2,height) , 7)
    #Dessiner la ligne horizontale
    pg.draw.line(screen, line_color , (0,height/3),(width,height/3),7)
    pg.draw.line(screen , line_color , (0 , height/3*2),(width,height/3*2))
    draw_status()

def draw_status():
    global draw
    if winner is None:
        message ="tour de"+ XO.upper()
    else:
        message = XO.upper()+ "a gagner"
    font = pg.font.Font(None,30)
    text = font.render(message,1,white)


    screen.fill((0,0,0),(0,400,500,100))
    text_rect = text.get_rect(center=(width/2,500-50))
    screen.blit(text,text_rect)
    pg.display.update()

def check_win():
    global BOARD,winner,draw
    #verifier les gagnants de maniere verticale
    for row in range(0,3):
        if BOARD[row][0] == BOARD[row][1] == BOARD[row][2] and BOARD[row][0] != None:
            winner = BOARD[row][0]
            pg.draw.line(screen,(0,255,34),(0,(row+1)*height/3 - height/6), (width,(row+1)*height/3 - height/4),4)
            break


    #verifier les gagnants de maniere horizontale
    for col in range(0,3):
        if BOARD[0][col] == BOARD[1][col] == BOARD[2][col] and BOARD[0][col] != None:
            winner = BOARD[0][col]
            pg.draw.line(screen,(0,255,34) , ((col + 1)* width/3 - width/6, 0),\
                          ((col + 1)* width/3 - width/6, height), 4)
            break

    #verifier les gangants avec les diagonales
    if (BOARD[0][0] == BOARD[1][1] == BOARD[2][2]) and (BOARD[0][0] is not None):
        # game won diagonally left to right
        winner = BOARD[0][0]
        pg.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)
    if (BOARD[0][2] == BOARD[1][1] == BOARD[2][0]) and (BOARD[0][2] is not None):
        # game won diagonally right to left
        winner = BOARD[0][2]
        pg.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)
    if (all([all(row) for row in BOARD]) and winner is None):
        draw = True
    draw_status()


def draw_XO(row,col):
    global BOARD,XO
    if row == 1:
        posx = 30
    elif row == 2:
        posx = width/3 +30
    elif row == 3:
        posx = width/3*2 + 30
    if col == 1:
        posy = 30
    elif col == 2:
        posy = height/3 + 30
    elif col == 3:
        posy = height/3*2 + 30
    BOARD[row - 1][col - 1] = XO
    if XO == "x":
        screen.blit(x_img,(posy,posx))
        XO = 'o'
    else:
        screen.blit(o_img,(posy,posx))
        XO = 'x'

    pg.display.update()
def userClick():
    #prend les coodonnees de x et de y
    x,y = pg.mouse.get_pos()
    #prend les colonnes des clicks (1-3)
    if(x<width/3):
        col = 1
    elif (x<width/3*2):
        col = 2
    elif(x<width):
        col = 3
    else:
        col = None
    #prend les lignes des click (1-3)
    if(y<height/3):
        row = 1
    elif (y<height/3*2):
        row = 2
    elif(y<height):
        row = 3
    else:
        row = None
    print(row,col)
    if(row and col and BOARD[row-1][col-1] is None):
        global XO
        #dessine x et o sur l'ecran
        draw_XO(row,col)
        check_win()


def reset_game():
    global BOARD, winner,XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_opening()
    winner=None
    BOARD = [[None] * 3, [None] * 3, [None] * 3]

game_opening()
# run the game loop forever
while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type is MOUSEBUTTONDOWN:
            # the user clicked; place an X or O
            userClick()
            if(winner or draw):
                reset_game()
        pg.display.update()
        CLOCK.tick(fps)


