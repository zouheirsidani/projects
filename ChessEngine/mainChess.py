'''
The main part.
So how the game functions
'''
import pygame as p
import engine

p.init()
width = height = 400
squareSize = int(width/8)
images={}
fps = 15

def imageLoad():
    images["wP"]=p.transform.scale(p.image.load("images/wP.png"),(squareSize,squareSize))
    images["bP"]=p.transform.scale(p.image.load("images/bP.png"),(squareSize,squareSize))
    images["wK"]=p.transform.scale(p.image.load("images/wK.png"),(squareSize,squareSize))
    images["bK"]=p.transform.scale(p.image.load("images/bK.png"),(squareSize,squareSize))
    images["wQ"]=p.transform.scale(p.image.load("images/wQ.png"),(squareSize,squareSize))
    images["bQ"]=p.transform.scale(p.image.load("images/bQ.png"),(squareSize,squareSize))
    images["wN"]=p.transform.scale(p.image.load("images/wN.png"),(squareSize,squareSize))
    images["wB"]=p.transform.scale(p.image.load("images/wB.png"),(squareSize,squareSize))
    images["wR"]=p.transform.scale(p.image.load("images/wR.png"),(squareSize,squareSize))
    images["bN"]=p.transform.scale(p.image.load("images/bN.png"),(squareSize,squareSize))
    images["bB"]=p.transform.scale(p.image.load("images/bB.png"),(squareSize,squareSize))
    images["bR"]=p.transform.scale(p.image.load("images/bR.png"),(squareSize,squareSize))

def run():

    screen = p.display.set_mode((height,width))
    screen.fill(p.Color("white"))
    gamestate = engine.gameState()
    clock = p.time.Clock()
    imageLoad()
    possiblemoves = gamestate.getPossibleMoves()
    selected = ()
    clicks = []
    condition=True
    while condition:
        for event in p.event.get():
            if event.type == p.QUIT:
                condition = False
            elif event.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                if selected == (location[1]//squareSize,location[0]//squareSize):
                    selected = ()
                    clicks = []
                else:
                    selected = (location[1]//squareSize,location[0]//squareSize)
                    clicks.append(selected)
                if len(clicks)==2:
                    move = engine.Move(clicks[0],clicks[1],gamestate.board)
                    print(move.getNotation())
                    if move in possiblemoves:
                        gamestate.moveAction(move)
                        possiblemoves = gamestate.getPossibleMoves()
                        selected = ()
                        clicks = []
                    else:
                        clicks = [selected]
                    
                    
            elif event.type == p.KEYDOWN:
                if event.key == p.K_z and p.key.get_mods()& p.KMOD_CTRL:
                    gamestate.undo()
                    possiblemoves = gamestate.getPossibleMoves()
        representGame(screen,gamestate)
        clock.tick(fps)
        p.display.flip()

def representGame(screen,gamestate):
    representBoard(screen,gamestate.board)

def representBoard(screen,board):
    for row in range(8):
        i=0
        if row%2==1: 
            #start with dark
            i=1
        for column in range(8):
            if i==0:
                p.draw.rect(screen,p.Color("#e4bda2"),p.Rect(column*squareSize,row*squareSize,squareSize,squareSize))
                i=1
            else:
                p.draw.rect(screen,p.Color("#a55f2f"),p.Rect(column*squareSize,row*squareSize,squareSize,squareSize))
                i=0
            if board[row][column]!="  ":
                screen.blit(images[board[row][column]],p.Rect(column*squareSize,row*squareSize,squareSize,squareSize))


# if __name__=="__run__":
#     run()
run()