import random

class Jeu:

    __vide, __bonbon, __snake = ' ', 'b', 's'
    __bonbon_t = []

    def __init__(self,rows,columns):
        self.__rows = rows
        self.__columns = columns
        self.__plateau_l = [[self.__vide]*self.__columns]
        self.__snake_l = [[int(self.__columns/2),int(self.__rows/2)]]
        for k in range(self.__rows-1):
            self.__plateau_l.append([self.__vide]*self.__columns)
        self.__plateau_l[self.__snake_l[0][0]][self.__snake_l[0][1]] = self.__snake
        self.__bonbon_t = self.__setRandBonbon()

    def getRows(self):
        return self.__rows

    def getColumns(self):
        return self.__columns

    def getPlateau(self):
        return self.__plateau_l

    def snakeMove(self,dir):
        __lenght = len(self.__snake_l)-1
        __rows_ = self.__snake_l[__lenght][0]
        __columns_ = self.__snake_l[__lenght][1]
        if dir == "up":
            if(self.__snake_l[__lenght][0] > 0):
                self.__snake_l.append([(__rows_ - 1),__columns_])
            else:
                raise 
        elif dir == "down":
            if(self.__snake_l[__lenght][0] < self.__rows):
                self.__snake_l.append([(__rows_ + 1),__columns_])
            else:
                raise 
        elif dir == "left":
            if(self.__snake_l[__lenght][1] > 0):
                self.__snake_l.append([__rows_,(__columns_ - 1)])
            else:
                raise 
        elif dir == "right":
            if(self.__snake_l[__lenght][1] < self.__columns):
                self.__snake_l.append([__rows_,(__columns_ + 1)])
            else:
                raise 
        else:
            return 
        for k in range(1,__lenght):
            if self.__snake_l[k][0] == __rows_ and self.__snake_l[k][1] == __columns_:
                raise
            else:
                continue
        if self.__snake_l[__lenght] == self.__bonbon_t:
            self.__bonbon_t = self.__setRandBonbon()
        else:
            self.__plateau_l[self.__snake_l[0][0]][self.__snake_l[0][1]] = self.__vide
            self.__snake_l.pop(0)
        self.__updatePlateau()


    def __updateSnakeOnPlateau(self):
        for k in self.__snake_l:
            self.__plateau_l[k[0]][k[1]] = self.__snake

    def __updatePlateau(self):
        self.__updateSnakeOnPlateau()
        self.__plateau_l[self.__bonbon_t[0]][self.__bonbon_t[1]] = self.__bonbon


    def __setRandBonbon(self):
        return [(random.randint(1,self.__rows-1)),(random.randint(1,self.__columns-1))]

    def isOnBonbon(self,rows,columns):
        if((self.__snake_l[len(self.__snake_l)-1][0] == rows) and (self.__snake_l[len(self.__snake_l)-1][1] == columns)):
            return True
        else:
            return False