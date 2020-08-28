from tkinter import *
import tkinter as tk
import random,math
import numpy as np


BACKGROUND_COLOR_CELLS = {2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
                         16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
                         128: "#edcf72", 256: "#edcc61", 512: "#edc850",
                         1024: "#edc53f", 2048: "#edc22e",
                         4096: "#eee4da", 8192: "#edc22e", 16384: "#f2b179",
                         32768: "#f59563", 65536: "#f67c5f", }

def merge(mat,key):
    """
    Helper function that merges a single row or column in 2048
    """
    if key == "up":
            # for loop to move all the tiles in one direco
            for q in range(6):    
                for i in range(5,-1,-1):
                    for j in range(0,6):
                        for n in range(1,11):
                            if mat[i][j]==math.pow(2, n):
                                if i==0:
                                    continue
                                #Swap the elements if empty or 0
                                elif mat[i-1][j] == 0:
                                    temp = mat[i][j]
                                    mat[i][j] = mat[i-1][j]
                                    mat[i-1][j] = temp
                                #inserting 2 at i-1 and 0 at i th   
                                elif mat[i-1][j] == math.pow(2, n):
                                    if mat[i-1][j] == mat[i][j]:
                                        mat[i][j] = 0
                                        mat[i-1][j] = int(math.pow(2,n+1))
                                        
                                    else:
                                        mat[i-1][j] = mat[i-1][j]
                                        mat[i][j] = mat[i][j]
                                else:
                                    continue
                            else:
                                continue

    elif key == "right":
        for q in range(6):
            for i in range(0,6):
                for j in range(0,6):
                    for n in range(1,10):
                        if mat[i][j]==math.pow(2, n):
                            if j==5:
                                continue
                            elif mat[i][j+1] == 0:
                                temp = mat[i][j]
                                mat[i][j] = mat[i][j+1]
                                mat[i][j+1] = temp
                            elif mat[i][j+1] == math.pow(2, n): 
                                if mat[i][j] == mat[i][j+1]:
                                    mat[i][j+1] = int(math.pow(2,n+1))
                                    mat[i][j] = 0
                                else:
                                    mat[i][j] = mat[i][j]
                                    mat[i][j+1] = mat[i][j+1]
                            else:
                                continue
                        else:
                            continue
                    
    elif key == "left":
        for q in range(6):
            for i in range(0,6):
                for j in range(5,-1,-1):
                    for n in range(1,11):
                        if mat[i][j]==math.pow(2, n):
                            if j==0:
                                continue
                            elif mat[i][j-1] == 0:
                                temp = mat[i][j]
                                mat[i][j] = mat[i][j-1]
                                mat[i][j-1] = temp
                            elif mat[i][j-1] == math.pow(2, n): 
                                if mat[i][j] == mat[i][j-1]:
                                    mat[i][j-1] = int(math.pow(2,n+1))
                                    mat[i][j] = 0
                                else:
                                    mat[i][j] = mat[i][j]
                                    mat[i][j-1] = mat[i][j-1]
                            else:
                                continue
                        else:
                            continue
                 
                
    elif key == "down":
        for q in range(6):
            for i in range(0,6):
                for j in range(0,6):
                    for n in range(1,10):
                        if mat[i][j]==math.pow(2, n):
                            if i==5:
                                mat[i][j] = mat[i][j]
                            elif mat[i+1][j] == 0:
                                temp = mat[i][j]
                                mat[i][j] = mat[i+1][j]
                                mat[i+1][j] = temp
                            elif mat[i+1][j] == math.pow(2, n):
                                if mat[i+1][j] == mat[i][j]:
                                    mat[i+1][j] = int(math.pow(2,n+1))
                                    mat[i][j] = 0
                                else:
                                    mat[i+1][j] = mat[i+1][j]
                                    mat[i][j] = mat[i][j]
                            else:
                                continue
                        else:
                            continue
                                   
    return mat
class TwentyFortyEight(Frame):
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        Frame.__init__(self)
        self.grid_ht=grid_height
        self.grid_wt=grid_width
        self.grid()
        print("""-----------  2048  ------------
Click on 2048 window to start the game.
Use ARROW KEYS to move the tiles.""")
        self.master.title('2048')
        self.master.bind('<Left>', self.left)
        self.master.bind('<Right>', self.right)
        self.master.bind('<Up>', self.up)
        self.master.bind('<Down>', self.down)
        self.buttonframe = tk.Frame(self)
        self.buttonframe.grid(row=2, column=0, columnspan=4)
        tk.Button(self.buttonframe, text = "New Game",command=self.reset).grid(row=0, column=0)
        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()
        self.mainloop()
        

    def init_grid(self):
        self.background = Frame(self, bg="#92877d",width=self.grid_wt, height=self.grid_ht)
        self.background.grid()
        
        for i in range(6):
            grid_row = []
            for j in range(6):
                self.cell = Frame(self.background, bg="#9e948a",
                             width=400 / 6,
                             height=400 / 6)
                self.cell.grid(row=i, column=j, padx=10,
                          pady=10)
                t = Label(master=self.cell, text="",
                          bg="#9e948a",
                          justify=CENTER, font=("Verdana", 20, "bold"), width=4, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)
        

    def init_matrix(self):
        
        self.matrix = []

        for i in range(6):
            self.matrix.append([0] * 6)

        index = random.randint(0,5)  
        row_index1 = random.randint(0,5)
        row_index2 = random.randint(0,5)
        for i in range(6):
            for j in range(6):
                if i==index:
                    if (j==row_index1) or (j==row_index2):
                        self.matrix[i][j]=2
                    else:
                        self.matrix[i][j]=0
                else:
                    self.matrix[i][j]=0
        

    def update_grid_cells(self):
        
        for i in range(6):
            for j in range(6):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(
                        text="", bg="#9e948a")
                else:
                    self.grid_cells[i][j].configure(text=str(
                        new_number), bg=BACKGROUND_COLOR_CELLS[new_number])

        self.update_idletasks()    
          

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.init_matrix()
        self.update_grid_cells()
        

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        String_grid = ""
        for i in range(len(self.matrix)):
            for j in range (len(self.matrix[0])):
                String_grid += ( str(self.matrix[i][j]) + " ")
            String_grid += '\n'
        return String_grid

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_ht

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_wt

    def left(self, events):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        self.matrix=merge(self.matrix,"left")
        self.update_grid_cells()
        self.new_tile()
        pass
    
    def right(self, events):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        self.matrix=merge(self.matrix,"right")
        self.update_grid_cells()
        self.new_tile()
        pass
    
    def up(self, events):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        self.matrix=merge(self.matrix,"up")
        self.update_grid_cells()
        self.new_tile()
        pass
    
    def down(self, events):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        self.matrix=merge(self.matrix,"down")
        self.update_grid_cells()
        self.new_tile()
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        r_index = random.randint(0,5)
        c_index = random.randint(0,5)
        new_num = np.random.choice([2,4],p=[0.9,0.1])
        for i in range(0,6):
            for j in range(0,6):
                if self.matrix[r_index][c_index]==0:
                    self.matrix[r_index][c_index]=new_num
                    self.set_tile(r_index , c_index, new_num)

        self.update_grid_cells()
        
        pass

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.matrix[row][col] = value
        pass

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.matrix[row][col]


Gameone = TwentyFortyEight(400,400)



    
        
