import math
import random
import numpy as np

class Grid:
    """Class Grid make the grid in form of matrix (nested list) and merge the 
    elements in the list"""
    
    def __init__(self):
        """Creating and Initializes the nested list variable grid_row"""
        self.grid_row = []
        
    def random_two(self):
        """Generate 2 at random position in the self.grid_row (matrix)"""
        #random position for inserting 2
        index = random.randint(0,5)  
        row_index1 = random.randint(0,5)
        row_index2 = random.randint(0,5)
        
        for i in range(6): 
            # Append an empty sublist inside the list 
            self.grid_row.append([]) 
            # Append 2 at random position inside the sublist through comparison 
            for j in range(6):
                if i == index:
                    if ((j == row_index1) or (j == row_index2)):
                        self.grid_row[i].append(2)
                    else:
                        self.grid_row[i].append(" ")
                else:
                    self.grid_row[i].append(" ")
                    
    def print_grid(self):
        """Print the grid - matrix """
        for i in range(0,6):
            print('[%s]' % ' , '.join(map(str,self.grid_row[i])))


    def merge(self):
        """Merge the elements of the list (tiles) depending on factors like 
        direction, number and next element"""
        
        print("""Enter keys for direction:
Right: r    Left: l   Up: u    Down: d    Discontinue: Any other key""")
        # Taking the input direction from 
        for z in range(0,100):
                key = input("key: ")
                
                if key == "u":
                    for q in range(6):
                        for i in range(5,-1,-1):
                            for j in range(0,6):
                                for n in range(1,11):
                                    if self.grid_row[i][j]==math.pow(2, n):
                                        if i==0:
                                            continue
                                        #Swap the elements if empty (" ")
                                        elif self.grid_row[i-1][j] == " ":
                                            temp = self.grid_row[i][j]
                                            self.grid_row[i][j] = self.grid_row[i-1][j]
                                            self.grid_row[i-1][j] = temp
                                        #inserting 2 at i-1 and " " (empty) at i th   
                                        elif self.grid_row[i-1][j] == math.pow(2, n):
                                            if self.grid_row[i-1][j] == self.grid_row[i][j]:
                                                self.grid_row[i][j] = " "
                                                self.grid_row[i-1][j] = int(math.pow(2,n+1))
                                                
                                            else:
                                                self.grid_row[i-1][j] = self.grid_row[i-1][j]
                                                self.grid_row[i][j] = self.grid_row[i][j]
                                        else:
                                            continue
                                    else:
                                        continue

                elif key == "r":
                    for i in range(0,6):
                        for j in range(0,6):
                            for n in range(1,10):
                                if self.grid_row[i][j]==math.pow(2, n):
                                    if j==5:
                                        continue
                                    elif self.grid_row[i][j+1] == " ":
                                        temp = self.grid_row[i][j]
                                        self.grid_row[i][j] = self.grid_row[i][j+1]
                                        self.grid_row[i][j+1] = temp
                                    elif self.grid_row[i][j+1] == math.pow(2, n): 
                                        if self.grid_row[i][j] == self.grid_row[i][j+1]:
                                            self.grid_row[i][j+1] = int(math.pow(2,n+1))
                                            self.grid_row[i][j] = " "
                                        else:
                                            self.grid_row[i][j] = self.grid_row[i][j]
                                            self.grid_row[i][j+1] = self.grid_row[i][j+1]
                                    else:
                                        continue
                                else:
                                    continue
                                
                elif key == "l":
                    for i in range(0,6):
                        for j in range(5,-1,-1):
                            for n in range(1,11):
                                if self.grid_row[i][j]==math.pow(2, n):
                                    if j==0:
                                        continue
                                    elif self.grid_row[i][j-1] == " ":
                                        temp = self.grid_row[i][j]
                                        self.grid_row[i][j] = self.grid_row[i][j-1]
                                        self.grid_row[i][j-1] = temp
                                    elif self.grid_row[i][j-1] == math.pow(2, n): 
                                        if self.grid_row[i][j] == self.grid_row[i][j-1]:
                                            self.grid_row[i][j-1] = int(math.pow(2,n+1))
                                            self.grid_row[i][j] = " "
                                        else:
                                            self.grid_row[i][j] = self.grid_row[i][j]
                                            self.grid_row[i][j-1] = self.grid_row[i][j-1]
                                    else:
                                        continue
                                else:
                                    continue
                             
                            
                elif key == "d":
                    for i in range(0,6):
                        for j in range(0,6):
                            for n in range(1,10):
                                if self.grid_row[i][j]==math.pow(2, n):
                                    if i==5:
                                        continue
                                    elif self.grid_row[i+1][j] == " ":
                                        temp = self.grid_row[i][j]
                                        self.grid_row[i][j] = self.grid_row[i+1][j]
                                        self.grid_row[i+1][j] = temp
                                    elif self.grid_row[i+1][j] == math.pow(2, n):
                                        if self.grid_row[i+1][j] == self.grid_row[i][j]:
                                            self.grid_row[i+1][j] = int(math.pow(2,n+1))
                                            self.grid_row[i][j] = " "
                                        else:
                                            self.grid_row[i+1][j] = self.grid_row[i+1][j]
                                            self.grid_row[i][j] = self.grid_row[i][j]
                                    else:
                                        continue
                                else:
                                    continue
                                    
                else:
                    print("Game is discontinued")
                    break
                
                # Generate 2 at random position after merging of the elements
                g_index = random.randint(0,5)
                r_index = random.randint(0,5)
       
                for i in range(0,6):
                    for j in range(0,6):
                        if self.grid_row[g_index][r_index]==" ":
                            self.grid_row[g_index][r_index]=np.random.choice([2,4],p=[0.9,0.1])
                           
               #print the matrix(list) with merged elements and a new element
                for i in range(0,6):
                            print('[%s]' % ' , '.join(map(str,self.grid_row[i]))) 
 
# calling the class methods using instance variables
G1 = Grid()
G1.random_two()
G1.print_grid()
G1.merge()             
            
                
                
                