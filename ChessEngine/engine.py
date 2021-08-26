'''
This part is the engine of the chess game
'''
class gameState():
    def __init__(self):
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bP","bP","bP","bP","bP","bP","bP","bP"],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["wP","wP","wP","wP","wP","wP","wP","wP"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]
        self.moves=[]
        self.whiteTurn = True
        self.whiteKingLocation = (7,4)
        self.blackKingLocation = (0,4)
        self.check = False
        self.checkingpieces = [] #list of pieces that are checking

    def moveAction(self,move):
        self.board[move.startR][move.startC]="  "
        self.board[move.endR][move.endC]=move.movedpiece
        self.whiteTurn = not self.whiteTurn
        self.moves.append(move)
        if move.movedpiece == "wK":
            self.whiteKingLocation = (move.endR,move.endC)
        if move.movedpiece == "bK":
            self.whiteKingLocation = (move.endR,move.endC)
    '''
    CTRL + Z to undo a move
    '''
    def undo(self):
        if len(self.moves)>0:
            move = self.moves.pop()
            self.board[move.startR][move.startC]=move.movedpiece
            self.board[move.endR][move.endC]=move.capturedpiece
            self.whiteTurn = not self.whiteTurn
            if move.movedpiece == "wK":
                self.whiteKingLocation = (move.startR,move.startC)
            if move.movedpiece == "bK":
                self.whiteKingLocation = (move.startR,move.startC)
    '''
    In progress
    '''
    # def checkingCheck(self):
    #     '''
    #     CHECK FOR KNIGHT MOVES STILL
    #     '''
    #     if self.whiteTurn:
    #         knightmoves = [(self.whiteKingLocation[0]-2,self.whiteKingLocation[1]-1),(self.whiteKingLocation[0]-2,self.whiteKingLocation[1]+1),(self.whiteKingLocation[0]-1,self.whiteKingLocation[1]+2),(self.whiteKingLocation[0]+1,self.whiteKingLocation[1]+2),(self.whiteKingLocation[0]+2,self.whiteKingLocation[1]+1),(self.whiteKingLocation[0]+2,self.whiteKingLocation[1]-1),(self.whiteKingLocation[0]+1,self.whiteKingLocation[1]-2),(self.whiteKingLocation[0]-1,self.whiteKingLocation[1]-2)]
    #         for n in knightmoves:
    #             if self.board[n[0]][n[1]]=="bN":
    #                 self.check=True
    #                 self.checkingpieces.append(("bN",8,n))
    #         for direction in range(8):#left clockwise
    #             if direction==0:
    #                 for s in range(1,8):
    #                     if self.whiteKingLocation[1]-s>=0:
    #                         if self.board[self.whiteKingLocation[0]][self.whiteKingLocation[1]-s][0]=="w":
    #                             break
    #                         elif self.board[self.whiteKingLocation[0]][self.whiteKingLocation[1]-s]=="bR" or self.board[self.whiteKingLocation[0]][self.whiteKingLocation[1]-s]=="bQ":
    #                             position = (self.whiteKingLocation[0],self.whiteKingLocation[1]-s)
    #                             self.check=True
    #                             self.checkingpieces.append((self.board[self.whiteKingLocation[0]][self.whiteKingLocation[1]-s],direction,position))
    #                             break
    #                         elif self.board[self.whiteKingLocation[0]][self.whiteKingLocation[1]-s][0]=="b":
    #                             break
    #             if direction==1:
    #                 if self.whiteKingLocation[1]-1>=0 and self.whiteKingLocation[0]-1>=0:
    #                     if self.board[self.whiteKingLocation[0]-1][self.whiteKingLocation[1]-1][0]=="bP":
    #                         position = (self.whiteKingLocation[0]-1,self.whiteKingLocation[1]-1)
    #                         self.check=True
    #                         self.checkingpieces.append(("bP",direction,position))
    #                         continue

    #                 for s in range(1,8):
    #                     if self.whiteKingLocation[1]-s>=0 and self.whiteKingLocation[0]-s>=0:
    #                         if self.board[self.whiteKingLocation[0]-s][self.whiteKingLocation[1]-s][0]=="w":
    #                             break
    #                         elif self.board[self.whiteKingLocation[0]-s][self.whiteKingLocation[1]-s]=="bB" or self.board[self.whiteKingLocation[0]-s][self.whiteKingLocation[1]-s]=="bQ":
    #                             position = (self.whiteKingLocation[0]-s,self.whiteKingLocation[1]-s)
    #                             self.check=True
    #                             self.checkingpieces.append((self.board[self.whiteKingLocation[0]][self.whiteKingLocation[1]-s],direction,position))
    #                             break
    #                         elif self.board[self.whiteKingLocation[0]-s][self.whiteKingLocation[1]-s][0]=="b":
    #                             break
    #             if direction==2:
    #                 for s in range(1,8):
    #                     if self.whiteKingLocation[0]-s>=0:
    #                         if self.board[self.whiteKingLocation[0]-s][self.whiteKingLocation[1]][0]=="w":
    #                             break
    #                         elif self.board[self.whiteKingLocation[0]-s][self.whiteKingLocation[1]]=="bR" or self.board[self.whiteKingLocation[0]-s][self.whiteKingLocation[1]]=="bQ":
    #                             self.check=True
    #                             self.checkingpieces.append((self.board[self.whiteKingLocation[0]-s][self.whiteKingLocation[1]],direction))
    #                             break
    #                         elif self.board[self.whiteKingLocation[0]-s][self.whiteKingLocation[1]][0]=="b":
    #                             break
    #             if direction==3:
    #                 if self.whiteKingLocation[0]-1>=0 and self.whiteKingLocation[1]+1<=7:
    #                     if self.board[self.whiteKingLocation[0]-1][self.whiteKingLocation[1]+1][0]=="bP":
    #                         self.check=True
    #                         self.checkingpieces.append(("bP",direction))
    #                         continue
    #                 for s in range(1,8):
    #                     if self.whiteKingLocation[0]-s>=0 and self.whiteKingLocation[1]+s<=7:
    #                         if self.board[self.whiteKingLocation[0]-s][self.whiteKingLocation[1]+s][0]=="w":
    #                             break
    #                         elif self.board[self.whiteKingLocation[0]-s,self.whiteKingLocation[1]+s]=="bB" or self.board[self.whiteKingLocation[0]-s][self.whiteKingLocation[1]+s]=="bQ":
    #                             self.check=True
    #                             self.checkingpieces.append(self.board[self.whiteKingLocation[0]-s][self.whiteKingLocation[1]+s])
    #                             break
    #                         elif self.board[self.whiteKingLocation[0]-s][self.whiteKingLocation[1]+s][0]=="b":
    #                             break
    #             if direction==4:
    #                 for s in range(1,8):
    #                     if self.whiteKingLocation[1]+s<=7:
    #                         if self.board[self.whiteKingLocation[0]][self.whiteKingLocation[1]+s][0]=="w":
    #                             break
    #                         elif self.board[self.whiteKingLocation[0]][self.whiteKingLocation[1]+s]=="bR" or self.board[self.whiteKingLocation[0]][self.whiteKingLocation[1]+s]=="bQ":
    #                             self.check=True
    #                             self.checkingpieces.append(self.board[self.whiteKingLocation[0]][self.whiteKingLocation[1]+s])
    #                             break
    #                         elif self.board[self.whiteKingLocation[0]][self.whiteKingLocation[1]+s][0]=="b":
    #                             break
    #             if direction==5:
    #                 for s in range(1,8):
    #                     if self.whiteKingLocation[0]+s<=7 and self.whiteKingLocation[1]+s<=7:
    #                         if self.board[self.whiteKingLocation[0]+s][self.whiteKingLocation[1]+s][0]=="w":
    #                             break
    #                         elif self.board[self.whiteKingLocation[0]+s][self.whiteKingLocation[1]+s][0]=="bB" or self.board[self.whiteKingLocation[0]+s][self.whiteKingLocation[1]+s][0]=="bQ":
    #                             self.check=True
    #                             self.checkingpieces.append(self.board[self.whiteKingLocation[0]+s][self.whiteKingLocation[1]+s])
    #                             break
    #                         elif self.board[self.whiteKingLocation[0]+s][self.whiteKingLocation[1]+s][0]=="b":
    #                             break
    #             if direction==6:
    #                 for s in range(1,8):
    #                     if self.whiteKingLocation[0]+s<=7:
    #                         if self.board[self.whiteKingLocation[0]+s][self.whiteKingLocation[1]][0]=="w":
    #                             break
    #                         elif self.board[self.whiteKingLocation[0]+s][self.whiteKingLocation[1]]=="bR" or self.board[self.whiteKingLocation[0]+s][self.whiteKingLocation[1]]=="bQ":
    #                             self.check=True
    #                             self.checkingpieces.append(self.board[self.whiteKingLocation[0]+s][self.whiteKingLocation[1]])
    #                             break
    #                         elif self.board[self.whiteKingLocation[0]+s][self.whiteKingLocation[1]][0]=="b":
    #                             break
    #             if direction==7:
    #                 for s in range(1,8):
    #                     if self.whiteKingLocation[0]+s<=7 and self.whiteKingLocation[1]-s>=0:
    #                         if self.board[self.whiteKingLocation[0]+s][self.whiteKingLocation[1]-s][0]=="w":
    #                             break
    #                         elif self.board[self.whiteKingLocation[0]+s][self.whiteKingLocation[1]-s][0]=="bB" or self.board[self.whiteKingLocation[0]+s][self.whiteKingLocation[1]-s][0]=="bQ":
    #                             self.check=True
    #                             self.checkingpieces.append(self.board[self.whiteKingLocation[0]+s][self.whiteKingLocation[1]-s])
    #                             break
    #                         elif self.board[self.whiteKingLocation[0]+s][self.whiteKingLocation[1]-s][0]=="b":
    #                             break
    #     else:
    #         for direction in range(8):#left clockwise
    #             if direction==0:
    #                 for s in range(1,8):
    #                     if self.whiteKingLocation[1]-s>=0:
    #                         if self.board[self.whiteKingLocation[0]][self.whiteKingLocation[1]-s][0]=="b":
    #                             break
    #                         elif self.board[self.whiteKingLocation[0]][self.whiteKingLocation[1]-s]=="wR" or self.board[self.whiteKingLocation[0]][self.whiteKingLocation[1]-s]=="wQ":
    #                             self.check=True
    #                             self.checkingpieces.append(self.board[self.whiteKingLocation[0]][self.whiteKingLocation[1]-s])
    #                             break
    #                         elif self.board[self.whiteKingLocation[0]][self.whiteKingLocation[1]-s][0]=="w":
    #                             break
    #             if direction==1:
    #                 for s in range(1,8):
    #                     if self.whiteKingLocation[1]-s>=0 and self.whiteKingLocation[0]-s>=0:
    #                         if self.board[self.whiteKingLocation[0]-s][self.whiteKingLocation[1]-s][0]=="b":
    #                             break
    #                         elif self.board[self.whiteKingLocation[0]-s][self.whiteKingLocation[1]-s]=="wB" or self.board[self.whiteKingLocation[0]-s][self.whiteKingLocation[1]-s]=="wQ":
    #                             self.check=True
    #                             self.checkingpieces.append(self.board[self.whiteKingLocation[0]][self.whiteKingLocation[1]-s])
    #                             break
    #                         elif self.board[self.whiteKingLocation[0]-s][self.whiteKingLocation[1]-s][0]=="w":
    #                             break
    #             if direction==2:
    #                 for s in range(1,8):
    #                     if self.whiteKingLocation[0]-s>=0:
    #                         if self.board[self.whiteKingLocation[0]-s][self.whiteKingLocation[1]][0]=="b":
    #                             break
    #                         elif self.board[self.whiteKingLocation[0]-s][self.whiteKingLocation[1]]=="wR" or self.board[self.whiteKingLocation[0]-s][self.whiteKingLocation[1]]=="wQ":
    #                             self.check=True
    #                             self.checkingpieces.append(self.board[self.whiteKingLocation[0]-s][self.whiteKingLocation[1]])
    #                             break
    #                         elif self.board[self.whiteKingLocation[0]-s][self.whiteKingLocation[1]][0]=="w":
    #                             break
    #             if direction==3:
    #                 for s in range(1,8):
    #                     if self.blackKingLocation[0]-s>=0 and self.blackKingLocation[1]+s<=7:
    #                         if self.board[self.blackKingLocation[0]-s][self.blackKingLocation[1]+s][0]=="b":
    #                             break
    #                         elif self.board[self.blackKingLocation[0]-s][self.blackKingLocation[1]+s]=="wB" or self.board[self.blackKingLocation[0]-s][self.blackKingLocation[1]+s]=="wQ":
    #                             self.check=True
    #                             self.checkingpieces.append(self.board[self.blackKingLocation[0]-s][self.self.blackKingLocation[1]+s])
    #                             break
    #                         elif self.board[self.blackKingLocation[0]-s][self.blackKingLocation[1]+s][0]=="w":
    #                             break
    #             if direction==4:
    #                 for s in range(1,8):
    #                     if self.blackKingLocation[1]+s<=7:
    #                         if self.board[self.blackKingLocation[0]][self.blackKingLocation[1]+s][0]=="b":
    #                             break
    #                         elif self.board[self.blackKingLocation[0]][self.blackKingLocation[1]+s]=="wR" or self.board[self.blackKingLocation[0]][self.blackKingLocation[1]+s]=="wQ":
    #                             self.check=True
    #                             self.checkingpieces.append(self.board[self.blackKingLocation[0]][self.blackKingLocation[1]+s])
    #                             break
    #                         elif self.board[self.blackKingLocation[0]][self.blackKingLocation[1]+s][0]=="w":
    #                             break
    #             if direction==5:
    #                 if self.blackKingLocation[0]+1<=7 and self.blackKingLocation[1]+1<=7:
    #                     if self.board[self.blackKingLocation[0]+1][self.blackKingLocation[1]+1][0]=="wP":
    #                         self.check=True
    #                         self.checkingpieces.append("wP")
    #                         continue
    #                 for s in range(1,8):
    #                     if self.blackKingLocation[0]+s<=7 and self.blackKingLocation[1]+s<=7:
    #                         if self.board[self.blackKingLocation[0]+s][self.blackKingLocation[1]+s][0]=="b":
    #                             break
    #                         elif self.board[self.blackKingLocation[0]+s][self.blackKingLocation[1]+s][0]=="wB" or self.board[self.blackKingLocation[0]+s][self.blackKingLocation[1]+s][0]=="wQ":
    #                             self.check=True
    #                             self.checkingpieces.append(self.board[self.blackKingLocation[0]+s][self.blackKingLocation[1]+s])
    #                             break
    #                         elif self.board[self.blackKingLocation[0]+s][self.blackKingLocation[1]+s][0]=="w":
    #                             break
    #             if direction==6:
    #                 for s in range(1,8):
    #                     if self.blackKingLocation[0]+s<=7:
    #                         if self.board[self.blackKingLocation[0]+s][self.blackKingLocation[1]][0]=="b":
    #                             break
    #                         elif self.board[self.blackKingLocation[0]+s][self.blackKingLocation[1]]=="wR" or self.board[self.blackKingLocation[0]+s][self.blackKingLocation[1]]=="wQ":
    #                             self.check=True
    #                             self.checkingpieces.append(self.board[self.blackKingLocation[0]+s][self.blackKingLocation[1]])
    #                             break
    #                         elif self.board[self.blackKingLocation[0]+s][self.blackKingLocation[1]][0]=="w":
    #                             break
    #             if direction==7:
    #                 if self.blackKingLocation[0]+1<=7 and self.blackKingLocation[1]-1>=0:
    #                     if self.board[self.blackKingLocation[0]+1][self.blackKingLocation[1]+1][0]=="wP":
    #                         self.check=True
    #                         self.checkingpieces.append("wP")
    #                         continue
    #                 for s in range(1,8):
    #                     if self.blackKingLocation[0]+s<=7 and self.blackKingLocation[1]-s>=0:
    #                         if self.board[self.blackKingLocation[0]+s][self.blackKingLocation[1]-s][0]=="b":
    #                             break
    #                         elif self.board[self.blackKingLocation[0]+s][self.blackKingLocation[1]-s][0]=="wB" or self.board[self.blackKingLocation[0]+s][self.blackKingLocation[1]-s][0]=="wQ":
    #                             self.check=True
    #                             self.checkingpieces.append(self.board[self.blackKingLocation[0]+s][self.blackKingLocation[1]-s])
    #                             break
    #                         elif self.board[self.blackKingLocation[0]+s][self.blackKingLocation[1]-s][0]=="w":
    #                             break

                    


    def getPossibleMoves(self):
        possiblemoves = []
        if self.whiteTurn==True:
            for row in range(8):
                for column in range(8):
                    if self.board[row][column]=="  ":
                        continue
                    if self.board[row][column]=="wP":
                        self.getPawnMoves(row,column,possiblemoves)
                    if self.board[row][column]=="wR":
                        self.getRookMoves(row,column,possiblemoves)
                    if self.board[row][column]=="wN":
                        self.getKnightMoves(row,column,possiblemoves)
                    if self.board[row][column]=="wB":
                        self.getBishopMoves(row,column,possiblemoves)
                    if self.board[row][column]=="wQ":
                        self.getQueenMoves(row,column,possiblemoves)
                    if self.board[row][column]=="wK":
                        self.getKingMoves(row,column,possiblemoves)
        else:
            for row in range(8):
                for column in range(8):
                    if self.board[row][column]=="  ":
                        continue
                    if self.board[row][column]=="bP":
                        self.getPawnMoves(row,column,possiblemoves)
                    if self.board[row][column]=="bR":
                        self.getRookMoves(row,column,possiblemoves)
                    if self.board[row][column]=="bN":
                        self.getKnightMoves(row,column,possiblemoves)
                    if self.board[row][column]=="bB":
                        self.getBishopMoves(row,column,possiblemoves)
                    if self.board[row][column]=="bQ":
                        self.getQueenMoves(row,column,possiblemoves)
                    if self.board[row][column]=="bK":
                        self.getKingMoves(row,column,possiblemoves)

        return possiblemoves

    def getPawnMoves(self,row,column,possiblemoves):
        if self.whiteTurn:
            if row>0:
                if self.board[row-1][column]=="  ":
                        possiblemoves.append(Move((row,column),(row-1,column),self.board))
                if column<=6:
                    if self.board[row-1][column+1]!="  ":
                        if self.board[row-1][column+1][0]=="b":
                            possiblemoves.append(Move((row,column),(row-1,column+1),self.board))
                if column>=1:
                    if self.board[row-1][column-1]!="  ":
                        if self.board[row-1][column-1][0]=="b":
                            possiblemoves.append(Move((row,column),(row-1,column-1),self.board))
                if row == 6 :
                    if self.board[row-2][column]=="  ":
                        possiblemoves.append(Move((row,column),(row-2,column),self.board))
        else:
            if row<7:
                if self.board[row+1][column]=="  ":
                        possiblemoves.append(Move((row,column),(row+1,column),self.board))
                if column<=6:
                    if self.board[row+1][column+1]!="  ":
                        if self.board[row+1][column+1][0]=="w":
                            possiblemoves.append(Move((row,column),(row+1,column+1),self.board))
                if column>=1:
                    if self.board[row+1][column-1]!="  ":
                        if self.board[row+1][column-1][0]=="w":
                            possiblemoves.append(Move((row,column),(row+1,column-1),self.board))
                if row == 1 :
                    if self.board[row+2][column]=="  ":
                        possiblemoves.append(Move((row,column),(row+2,column),self.board))
            
    def getRookMoves(self,row,column,possiblemoves):
        if self.whiteTurn:
            for direction in range(4):#left up right down
                print("direction",direction)
                for square in range(1,8):
                    # print("square",square)
                    if direction==0:
                        if column-square>=0:
                            if self.board[row][column-square][0]!="w":
                                if self.board[row][column-square][0]=="b":
                                    possiblemoves.append(Move((row,column),(row,column-square),self.board))
                                    break
                                else:
                                    possiblemoves.append(Move((row,column),(row,column-square),self.board))
                                
                    if direction==1:
                        if row-square>=0:
                            if self.board[row-square][column][0]!="w":
                                if self.board[row-square][column][0]=="b":
                                    possiblemoves.append(Move((row,column),(row-square,column),self.board))
                                    break
                                else:
                                    possiblemoves.append(Move((row,column),(row-square,column),self.board))
                            else:
                                break
                    if direction==2:
                        if column+square<=7:
                            if self.board[row][column+square][0]!="w":
                                if self.board[row][column+square][0]=="b":
                                    possiblemoves.append(Move((row,column),(row,column+square),self.board)) 
                                    break
                                else:
                                     possiblemoves.append(Move((row,column),(row,column+square),self.board))
                            else:
                                break          
                    if direction==3:
                        if row+square<=7:
                            if self.board[row+square][column][0]!="w":
                                if self.board[row+square][column][0]=="b":
                                    possiblemoves.append(Move((row,column),(row+square,column),self.board))
                                    break
                                else:
                                    possiblemoves.append(Move((row,column),(row+square,column),self.board))
                            else:
                                break
        else:
            for direction in range(4):#left up right down
                for square in range(1,8):
                    if direction==0:
                        if column-square>=0:
                            if self.board[row][column-square][0]!="b":
                                if self.board[row][column-square][0]=="w":
                                    possiblemoves.append(Move((row,column),(row,column-square),self.board))
                                    break
                                else:
                                    possiblemoves.append(Move((row,column),(row,column-square),self.board))
                                
                    if direction==1:
                        if row-square>=0:
                            if self.board[row-square][column][0]!="b":
                                if self.board[row-square][column][0]=="w":
                                    possiblemoves.append(Move((row,column),(row-square,column),self.board))
                                    break
                                else:
                                    possiblemoves.append(Move((row,column),(row-square,column),self.board))
                            else:
                                break
                    if direction==2:
                        if column+square<=7:
                            if self.board[row][column+square][0]!="b":
                                if self.board[row][column+square][0]=="w":
                                    possiblemoves.append(Move((row,column),(row,column+square),self.board)) 
                                    break
                                else:
                                     possiblemoves.append(Move((row,column),(row,column+square),self.board))
                            else:
                                break          
                    if direction==3:
                        if row+square<=7:
                            if self.board[row+square][column][0]!="b":
                                if self.board[row+square][column][0]=="w":
                                    possiblemoves.append(Move((row,column),(row+square,column),self.board))
                                    break
                                else:
                                    possiblemoves.append(Move((row,column),(row+square,column),self.board))
                            else:
                                break

    def getKnightMoves(self,row,column,possiblemoves):
        #top left going clockwise
        endmoves = [(row-2,column-1),(row-2,column+1),(row-1,column+2),(row+1,column+2),(row+2,column+1),(row+2,column-1),(row+1,column-2),(row-1,column-2)]
        
        if self.whiteTurn:
            for m in endmoves:
                if m[0]>=0 and m[0]<=7 and m[1]>=0 and m[1]<=7:
                    if self.board[m[0]][m[1]][0]!="w":
                        possiblemoves.append(Move((row,column),m,self.board))
        else:
            for m in endmoves:
                if m[0]>=0 and m[0]<=7 and m[1]>=0 and m[1]<=7:
                    if self.board[m[0]][m[1]][0]!="b":
                        possiblemoves.append(Move((row,column),m,self.board))
    
    def getBishopMoves(self,row,column,possiblemoves):
        if self.whiteTurn:
            for direction in range(4):#topleft and clockwise
                for square in range(1,8):
                    if direction==0:
                        if row-square>=0 and column-square>=0:
                            if self.board[row-square][column-square][0]!="w":
                                if self.board[row-square][column-square][0]=="b":
                                    possiblemoves.append(Move((row,column),(row-square,column-square),self.board))
                                    break
                                else:
                                    possiblemoves.append(Move((row,column),(row-square,column-square),self.board))
                            else:
                                break
                    if direction==1:
                        if row-square>=0 and column+square<=7:
                            if self.board[row-square][column+square][0]!="w":
                                if self.board[row-square][column+square][0]=="b":
                                    possiblemoves.append(Move((row,column),(row-square,column+square),self.board))
                                    break
                                else:
                                    possiblemoves.append(Move((row,column),(row-square,column+square),self.board))
                            else:
                                break
                    if direction==2:
                        if row+square<=7 and column+square<=7:
                            if self.board[row+square][column+square][0]!="w":
                                if self.board[row+square][column+square][0]=="b":
                                    possiblemoves.append(Move((row,column),(row+square,column+square),self.board))
                                    break
                                else:
                                    possiblemoves.append(Move((row,column),(row+square,column+square),self.board))
                            else:
                                break
                    if direction==3:
                        if row+square<=7 and column-square>=0:
                            if self.board[row+square][column-square][0]!="w":
                                if self.board[row+square][column-square][0]=="b":
                                    possiblemoves.append(Move((row,column),(row+square,column-square),self.board))
                                    break
                                else:
                                    possiblemoves.append(Move((row,column),(row+square,column-square),self.board))
                            else:
                                break
        else:
            for direction in range(4):#topleft and clockwise
                for square in range(1,8):
                    if direction==0:
                        if row-square>=0 and column-square>=0:
                            if self.board[row-square][column-square][0]!="b":
                                if self.board[row-square][column-square][0]=="w":
                                    possiblemoves.append(Move((row,column),(row-square,column-square),self.board))
                                    break
                                else:
                                    possiblemoves.append(Move((row,column),(row-square,column-square),self.board))
                            else:
                                break
                    if direction==1:
                        if row-square>=0 and column+square<=7:
                            if self.board[row-square][column+square][0]!="b":
                                if self.board[row-square][column+square][0]=="w":
                                    possiblemoves.append(Move((row,column),(row-square,column+square),self.board))
                                    break
                                else:
                                    possiblemoves.append(Move((row,column),(row-square,column+square),self.board))
                            else:
                                break
                    if direction==2:
                        if row+square<=7 and column+square<=7:
                            if self.board[row+square][column+square][0]!="b":
                                if self.board[row+square][column+square][0]=="w":
                                    possiblemoves.append(Move((row,column),(row+square,column+square),self.board))
                                    break
                                else:
                                    possiblemoves.append(Move((row,column),(row+square,column+square),self.board))
                            else:
                                break
                    if direction==3:
                        if row+square<=7 and column-square>=0:
                            if self.board[row+square][column-square][0]!="b":
                                if self.board[row+square][column-square][0]=="w":
                                    possiblemoves.append(Move((row,column),(row+square,column-square),self.board))
                                    break
                                else:
                                    possiblemoves.append(Move((row,column),(row+square,column-square),self.board))
                            else:
                                break
    
    def getQueenMoves(self,row,column,possiblemoves):
        self.getBishopMoves(row,column,possiblemoves)
        self.getRookMoves(row,column,possiblemoves)
    
    def getKingMoves(self,row,column,possiblemoves):
        #start from left go clockwise
        endmoves = [(row,column-1),(row-1,column-1),(row-1,column),(row-1,column+1),(row,column+1),(row+1,column+1),(row+1,column),(row+1,column-1)]

        if self.whiteTurn:
            for m in endmoves:
                if m[0]>=0 and m[0]<=7 and m[1]>=0 and m[1]<=7:
                    if self.board[m[0]][m[1]][0]!="w":
                        possiblemoves.append(Move((row,column),m,self.board))
        else:
            for m in endmoves:
                if m[0]>=0 and m[0]<=7 and m[1]>=0 and m[1]<=7:
                    if self.board[m[0]][m[1]][0]!="b":
                        possiblemoves.append(Move((row,column),m,self.board))

class Move():
    def __init__(self,start,end,board):
        self.movedpiece = board[start[0]][start[1]]
        self.capturedpiece = board[end[0]][end[1]]
        self.startR = start[0]
        self.startC = start[1]
        self.endR = end[0]
        self.endC = end[1]
    
    def __eq__(self, o):
        if isinstance(o,Move):
            if self.startR==o.startR and self.startC==o.startC and self.endR==o.endR and self.endC==o.endC:
                return True
            return False

    def getNotation(self):
        return self.getChessPosition(self.startR,self.startC)+self.getChessPosition(self.endR,self.endC)
    def getChessPosition(self,row,column):
        dictRowtoRank = {0:"8",1:"7",2:"6",3:"5",4:"4",5:"3",6:"2",7:"1"}
        dictColumntoFile = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h"}
        return dictColumntoFile[column]+dictRowtoRank[row]