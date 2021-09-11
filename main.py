import os
import time
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

grid_x = 4
grid_y = 4

CRED    = '\33[31m'
CYELLOW = '\33[33m'

used_space1 = " /--\ "
used_space3 = "/####\\"
used_space4 = "\####/"
used_space6 = " \--/ "

not_used_space = "        "

Rows = []

LastMove = [0,0]
current_player = 0

class GridItem:
    X = 0
    Y = 0
    slot = 0
    def __init__(self,x,y):
        self.X = x
        self.Y = y
        self.slot = 0

def SetupGame():
    global Rows
    global LastMove
    global current_player
    global grid_x
    global grid_y
    grid_x = int_input("Please Input the lenght on the board (i.e 8): ",0,10)
    grid_y = int_input("Please Input the Hight on the board (i.e 6): ",0,10)
    for Y in range(grid_y):
        Row = []
        for X in range(grid_x):
            Row.append(GridItem(X,Y))
        Rows.append(Row)
    LastMove = [0,0]
    current_player = 0
        


def MakeLine(Line):
    
    Lines = []
    for item in range(6):
        Lines.append("");

    for item in range(len(Line)):
        if Line[item].slot == 0:
            Lines[0] += f"|--------|"
            Lines[1] += f"|{not_used_space}|"
            Lines[2] += f"|{not_used_space}|"
            Lines[3] += f"|{not_used_space}|"
            Lines[4] += f"|{not_used_space}|"
            Lines[5] += f"|--------|"
        else:
            if Line[item].slot == 1:
                color = CRED
            if Line[item].slot == 2:
                color = CYELLOW
            Lines[0] += f"|--------|"
            Lines[1] += f"|{color} {used_space1} \33[0m|"
            Lines[2] += f"|{color} {used_space3} \33[0m|"
            Lines[3] += f"|{color} {used_space4} \33[0m|"
            Lines[4] += f"|{color} {used_space6} \33[0m|"
            Lines[5] += f"|--------|"
    ReturnData = "";
    for item in range(6):
        ReturnData += Lines[item]+"\n"
    return ReturnData




def Draw():
    print("\033[H\033[J", end="")
    print(f"Player {current_player+1} Turn")
    DataToPrint = ""
    for item in range(len(Rows)):
        DataToPrint += MakeLine(Rows[item])
    print(DataToPrint,end="");

def HasWinner(pos):
    X = pos[0]
    Y = pos[1]
    player =  Rows[Y][X].slot
    if player == 0:
        return False
    if X-1 >= 0 and Rows[Y][X-1].slot == player:
        if X-2 >= 0 and Rows[Y][X-2].slot == player:
            if X-3 >= 0 and Rows[Y][X-3].slot == player:
                return True # 1,1,1,X
            if X+1 < grid_x and Rows[Y][X+1].slot == player:
                return True # 1,1,X,1
        else:
            if X+1 < grid_x and Rows[Y][X+1].slot == player:
                if X+2 < grid_x and Rows[Y][X+2].slot == player:
                    return True # 1,X,1,1
    elif X+1 < grid_x and Rows[Y][X+1].slot == player:
        if X+2 < grid_x and Rows[Y][X+2].slot == player:
            if X+3 < grid_x and Rows[Y][X+3].slot == player:
                return True # X,1,1,1




    # if Y-1 >= 0 and Rows[Y-1][X].slot == player:
    #     if Y-2 >= 0 and Rows[Y-2][X].slot == player:
    #         if Y-3 >= 0 and Rows[Y-3][X].slot == player:
    #             return True # 1,1,1,X
    #         if Y+1 < grid_y and Rows[Y+1][X].slot == player:
    #             return True # 1,1,X,1
    #     else:
    #         if Y+1 < grid_y and Rows[Y+1][X].slot == player:
    #             if Y+2 < grid_y and Rows[Y+2][X].slot == player:
    #                 return True # 1,X,1,1
    if Y+1 < grid_y and Rows[Y+1][X].slot == player:
        if Y+2 < grid_y and Rows[Y+2][X].slot == player:
            if Y+3 < grid_y and Rows[Y+3][X].slot == player:
                return True # X,1,1,1 Top-down

    if Y+1 < grid_y and X+1 < grid_x and Rows[Y+1][X+1].slot == player:
        if Y+2 < grid_y and X+2 < grid_x and Rows[Y+2][X+2].slot == player:
            if Y+3 < grid_y and X+3 < grid_x and Rows[Y+3][X+3].slot == player:
                return True # 1,1,1,X
            if Y-1 >= 0 and X-1 >= 0 and Rows[Y-1][X-1].slot == player:
                return True # 1,1,X,1
        else:
            if Y-1 >= 0 and X-1 >= 0 and Rows[Y-1][X-1].slot == player:
                if Y-2 >= 0 and X-2 >= 0 and Rows[Y-2][X-2].slot == player:
                    return True # 1,X,1,1
    elif Y-1 >= 0 and X-1 >= 0 and Rows[Y-1][X-1].slot == player:
        if Y-2 >= 0 and X-2 >= 0 and Rows[Y-2][X-2].slot == player:
            if Y-3 >= 0 and X-3 >= 0 and Rows[Y-3][X-3].slot == player:
                return True # X,1,1,1:



    if Y+1 < grid_y and X-1 >= 0 and Rows[Y+1][X-1].slot == player:
        if Y+2 < grid_y and X-2 >= 0 and Rows[Y+2][X-2].slot == player:
            if Y+3 < grid_y and X-3 >= 0 and Rows[Y+3][X-3].slot == player:
                return True # 1,1,1,X
            if Y-1 >= 0 and X+1 < grid_x and Rows[Y-1][X+1].slot == player:
                return True # 1,1,X,1
        else:
            if Y-1 >= 0 and X+1 < grid_x  and Rows[Y-1][X+1].slot == player:
                if Y-2 >= 0 and X+2 < grid_x  and Rows[Y-2][X+2].slot == player:
                    return True # 1,X,1,1
    elif Y-1 >= 0 and X+1 < grid_x and Rows[Y-1][X+1].slot == player:
        if Y-2 >= 0 and X+2 < grid_x and Rows[Y-2][X+2].slot == player:
            if Y-3 >= 0 and X+3 < grid_x and Rows[Y-3][X+3].slot == player:
                return True # X,1,1,1:

    return False
        


def int_input(text,min,max):
    try:
        num = int(input(text))
        if num >= min and num <= max:
            return num
        else:
            return int_input(text,min,max)
    except:
        return int_input(text,min,max)

def Is_X_full(X):
    return Rows[0][X].slot != 0

def add_to_x(X,player):
    global Rows
    for item in range(grid_y):
        if Rows[item][X].slot == 0:
            Rows[item][X].slot = player+1
            
            if item+1 != grid_y:
                if Rows[item+1][X].slot == 0:
                    Draw()
                    time.sleep(.2)
                    Rows[item][X].slot = 0
                else:
                    break;
    return [X,item]
            
                
def has_moves():
    has_moves = True
    for item in range(grid_x):
        if Rows[0][item].slot == 0:
            return True
    return False 




SetupGame()



while(HasWinner(LastMove) == False and has_moves()):
    Draw()
    X = int_input(f"Number 1-{grid_x}: ",1,grid_x)-1
    if Is_X_full(X) == False:
        LastMove = add_to_x(X,current_player)
        current_player = ((current_player+1) % 2)
    else:
        print("Sorry, No more spaces. Try Again")
        time.sleep(1);


current_player = ((current_player+1) % 2)

Draw()

if HasWinner(LastMove):
    print(f"Winner Player {current_player+1}")
else:
    print("Draw")
