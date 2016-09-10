#!usr/bin/env python

COLOURS = (1,2,3,4,5,6,7,8)
TAM = 4
ILEGAL_ARGUMENT = "ilegal argument"

class Secuence(): 
    COLOURS = (1,2,3,4,5,6,7,8)
    TAM = 4
    ILEGAL_ARGUMENT = "ilegal argument"

    def __init__(self,codigo = []):
        for a in codigo:
            if a in COLOURS:
                continue
            else:
                raise ValueError(ILEGAL_ARGUMENT)
        self.codigo = codigo

    def add(self,color):
        if color in COLOURS and len(self.codigo) <= TAM: 
            self.codigo.append(color)
        else:
            raise ValueError(ILEGAL_ARGUMENT)
            
    def delete(self):
        if len(self.codigo) > 0:
            self.codigo.pop()
            return True
        else:
            return False
            
    
