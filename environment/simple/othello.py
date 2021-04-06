import numpy as np
from enum import Enum

class field():
    field = ""
    def __init__(self,scale):
        field = np.zeros((scale,scale))
        left = scale/2 - 1
        right = scale/2
        black = color.black
        white = color.white

        field[left,left] = black
        field[left,right] = white
        field[right,left] = white
        field[right,right] = black
        self.field = field

    @classmethod
    def NodeToField(cls,arr):
        result = 0
        if (arr.dtype == field.dtype):
            result = arr.reshape(8,8)
        else:
            print("field:nodeToField:ERR-type miss match")
        return result
    @classmethod
    def FieldToNode(cls,field):
        result = 0
        if (field.dtype == self.field.dtype):
            result = field.reshape(64)
        else:
            print("field:FieldToNode:ERR-type miss match")
        return result

class color(Enum):
    black = 1
    white = -1
    empty = 0
class othello:
    field = np.zeros((8,8))
    passCount = 0
    dealer = ""
    myColor = color.empty
    opponent = ""
    def __init__(self,field,first = "me"):
        self.field = field
        if first == "me":
            myColor = color.black.value
        else:
            myColor = color.white.value

    def Link(self, dealer,opponent = ""):
        self.dealer = dealer
        self.opponent = opponent
        return self

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

    def NextTurn(self,laySpot):
        #laySpot : 0~63 의 정수
        dealer = self.dealer
        dealer.ModifyField(laySpot)
        dealer.NextTurn()
        #턴이 끝나서 넘김
        # -1인경우 둘곳이 없단 이야기
        return laySpot

    def Lay(self,zeroIndex):
        result = 0
        if len(zeroIndex) < 1:
            result = -1
        else:
            #TODO result = NN.cycle(zeroIndex,self.Field)
            pass
        self.NextTurn(result)

    def Seek(self):
        node = self.FieldToNode(self.field)
        zeroIndex = np.where(node == 0)
        if (len(zeroIndex)==0):
            print("pass")
            passCount += 1
        else:
            print(zeroIndex)


class dealer():
    p1 = ""
    p2 = ""
    field = ""

    functionDict = {}
    #딜러는 오셀로 게임과 동시에 생성되며 게임 그 자체이기도 하면서 게임 관리자이다. 스스로 종료 가능하다
    def CreateField(self):
         field = np.zeros((8,8))
         white = color.white.value
         black = color.black.value
         field[3][3] = black
         field[3][4] = white
         field[4][3] = white
         field[4][4] = black
         return field

    def __init__(self):
        self.field = self.CreateField()
        self.p1 = othello(self.field,first = "me").Link(self)
        self.p2 = othello(self.field,first = "you").Link(self,self.p1)
        self.p1.Link(self,self.p2)
        print(self.field)

