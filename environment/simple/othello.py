import numpy as np
from lib.log.error import ErrorManagement as E
from enum import Enum

class Field():
    field = ""
    def __init__(self,scale):
        #scale은 짝수
        #scale is even number
        Field.createFieldWithScale(scale)
        try:
            self.field = Field.createFieldWithScale(scale)
        except:
            print("field:__init__:ERR-parameter invalid")

    def convertToNode(self):
        return Field.FileToNode(self.field)

    def setFieldWithNode(self,arr):
        self.Field = NodeToField(arr)

    @staticmethod
    def createFieldWithScale(scale):
        field =""
        if scale %2 == 0:
            field = np.zeros((scale,scale))
            left = int(scale/2 - 1)
            right = int(scale/2)
            black = color.black.value
            white = color.white.value
            field[left][left] = black
            field[left][right] = white
            field[right][left] = white
            field[right][right] = black
        else:
            raise
        return field

    @staticmethod
    def NodeToField(cls,arr):
        result = 0
        try:
            result = arr.reshape(8,8)
        except:
            print("field:nodeToField:ERR-type miss match")
        return result

    @staticmethod
    def FieldToNode(cls,field):
        result = 0
        try:
            result = field.reshape(64)
        except:
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
    turn = ""

    def __init__(self):
        E.err("hello")
        self.field = Field(8)
        self.p1 = othello(self.field,first = "me").Link(self)
        self.p2 = othello(self.field,first = "you").Link(self,self.p1)
        self.p1.Link(self,self.p2)
        self.turn = self.p1
        print(self.field.field)

    def oneStep(self):
        #누가 둘 차례인지 감지한다
        # = self.turn
        #감지한 플레이어에게 현재 필드상황을 알려주며 돌을 놓는 함수를 실행
        #플레이어가 놓은 곳을 감지한다
        here = self.turn.Lay(self.field)
        #필드를 수정한다
        self.modifyField(here,self.turn)
        self.turn = self.turn.opponent

        #만약 플레이어가 돌을 놓을 수 없다면 다음 플레이어에게 순서를 넘긴다. 이때 턴넘김 변수를 수정하여
        #두 플레이어가 연속으로 턴을 넘길 경우 그대로 게임이 종료되도록 한다

