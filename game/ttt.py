import pygame
from copy import copy,deepcopy

def checkRowWinner(table):
    for x in table:
        if sum(x)==3:
            return 3
        elif sum(x)==-3:
            return -3
    return 0

def checkColumnWinner(table):
    if table[0][0]+table[1][0]+table[2][0]==3 or table[0][1]+table[1][1]+table[2][1]==3 or table[0][2]+table[1][2]+table[2][2]==3:
        return 3
    elif table[0][0]+table[1][0]+table[2][0]==-3 or table[0][1]+table[1][1]+table[2][1]==-3 or table[0][2]+table[1][2]+table[2][2]==-3:
        return -3
    return 0

def checkCrossWinner(table):
    sum=0
    for i in range(3):
        sum+=table[i][i]
    if sum==3 or sum==-3:
        return sum
    sum=0
    for i in range(3):
        sum+=table[i][2-i]
    if sum==3 or sum==-3:
        return sum
    return 0

def checkTerminalState(table):
    #3->player1 winner, -3->player2 winner, 0->draw
    rowWinner = checkRowWinner(table)
    if rowWinner:
        return rowWinner
    columnWinner = checkColumnWinner(table)
    if columnWinner:
        return columnWinner
    crossWinner = checkCrossWinner(table)
    if crossWinner:
        return crossWinner
    checkZero=0
    for x in range(3):
        for y in range(3):
            if table[x][y]==0:
                checkZero+=1
    if not checkZero:
        return 0
    return -10


def AI(table,player):
    currentState = checkTerminalState(table)
    if currentState==3:
        return 1
    elif currentState==-3:
        return -1
    elif currentState==0:
        return 0
    if player == -1:
        ans=1000000000
        for a in range(3):
            for b in range(3):
                if table[a][b]==0:
                    table[a][b]=player
                    ans=min(ans,AI(table,-1*player))
                    table[a][b]=0
        return ans
    else:
        ans=-1000000000
        for a in range(3):  
            for b in range(3):
                if table[a][b]==0:
                    table[a][b]=player
                    ans=max(ans,AI(table,-1*player))
                    table[a][b]=0
        return ans
        

def main():
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    pygame.display.set_caption("AI Tic-Tac-Toe")
    screen.fill((200,200,200))

    def drawGrid():
        grid = (100,100,100)
        for x  in range(3):
            pygame.draw.line(screen,grid, (0,x*200),(600,x*200),3)
            pygame.draw.line(screen,grid, (x*200,0),(x*200,600),3)

    click = False
    running =True
    table = []
    player = 1

    for i in range(3):
        row = [0]*3
        table.append(row)

    def updateState():
        white = (0,0,0)
        black = (255,255,255)
        x_cell = 0
        for x in table:
            y_cell = 0
            for y in x:
                if y==1:
                    pygame.draw.line(screen,white,(y_cell*200+30,x_cell*200+30),(y_cell*200+170,x_cell*200+170),6)
                    pygame.draw.line(screen,white,(y_cell*200+30,x_cell*200+170),(y_cell*200+170,x_cell*200+30),6)
                elif y==-1:
                    pygame.draw.circle(screen,black,(y_cell*200+100,x_cell*200+100),75,6)
                y_cell+=1
            x_cell+=1
        

    while running:
        drawGrid()
        updateState()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            if player == -1:
                #(x,y) = AI(table)
                checkTable = deepcopy(table)
                ans=100000
                AI(checkTable,-1)
                x_temp=int(-1)
                y_temp=int(-1)
                for x in range(3):
                    for y in range(3):
                        if table[x][y]==0:
                            table[x][y]=-1
                            temp=AI(table,1)
                            table[x][y]=0
                            print(x,y,"-",temp)
                            if(ans>temp):
                                ans=temp
                                x_temp,y_temp=x,y
                table[x_temp][y_temp]=-1
                player*=-1
                print("=========XXXXXXX=========")
            if event.type == pygame.MOUSEBUTTONDOWN and click==False and player==1:
                click=True
            if event.type == pygame.MOUSEBUTTONUP and click==True and player==1:
                click=False
                coordinates = pygame.mouse.get_pos()
                x_cell = coordinates[1] // 200
                y_cell = coordinates[0] // 200
                if table[x_cell][y_cell] == 0:
                    table[x_cell][y_cell] = player
                    player *= -1
        pygame.display.update()
    pygame.quit()

if __name__=="__main__":
    main()