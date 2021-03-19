import numpy as np
class othello:
    field = np.zeros((8,8))
    passCount = 0
    def __init__(self):
        self.field[3][3] = 1
        self.field[4][3] = -1
        self.field[3][4] = -1
        self.field[4][4] = 1
        print(self.field[3][3])
        print(self.field)
    def NodeToField(self,arr):
        result = 0
        if (arr.dtype == field.dtype):
            result = arr.reshape(8,8)
        else:
            print("othello:nodeToField:ERR-type miss match")
        return result
    
    def FieldToNode(self,field):
        result = 0
        if (field.dtype == self.field.dtype):
            result = field.reshape(64)
        else:
            print("othello:FieldToNode:ERR-type miss match")
        return result

    def seek(self):
        node = self.FieldToNode(self.field)
        zeroIndex = np.where(node == 0)
        if (len(zeroIndex)==0):
            print("pass")
            passCount += 1
        else:
            print(zeroIndex)
