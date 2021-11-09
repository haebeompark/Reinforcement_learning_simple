import numpy as np
from record.log.error import ErrorManagement as E
from enum import Enum

class Field():
    field = ""
    scale = 8
    def __init__(self,scale):
        #scale은 짝수
        #scale is even number
        self.scale = scale
        Field.createFieldWithScale(scale)
        try:
            self.field = Field.createFieldWithScale(scale)
        except:
            E.err("field:__init__:ERR-parameter invalid")

    def convertToNode(self):
        return Field.FieldToNode(self.field)

    def setFieldWithNode(self,arr):
        self.Field = NodeToField(arr)

    def display(self):
        field = self.field
        onDisplay = np.zeros((self.scale,self.scale),str)
        c=0
        for col in field:
            r=0
            for att in col:
                onDisplay[c][r] = Field.convertShapeForDisplay(att)
                r+=1
            c+=1
        for col in onDisplay:
            column = ''
            for att in col:
                column += att
            print(column)

    @staticmethod
    def convertShapeForDisplay(att):
        # 보여주기 위해 변환
        if att == color.black.value:
            return 'O'
        elif att == color.white.value:
            return 'X'
        else:
            return '_'

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
            E.err("field:nodeToField:ERR-type miss match")
        return result

    @staticmethod
    def FieldToNode(cls,field):
        result = 0
        try:
            result = field.reshape(64)
        except:
            E.err("field:FieldToNode:ERR-type miss match")
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
            E.err("othello:nodeToField:ERR-type miss match")
        return result
    
    def FieldToNode(self,field):
        result = 0
        if (field.dtype == self.field.dtype):
            result = field.reshape(64)
        else:
            E.err("othello:FieldToNode:ERR-type miss match")
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
    #othello를 제어
    p1 = ""
    p2 = ""
    field = ""
    turn = ""
    noWay = False

    def __init__(self):
        self.field = Field(8)
        self.p1 = othello(self.field,first = "me").Link(self)
        self.p2 = othello(self.field,first = "you").Link(self,self.p1)
        self.p1.Link(self,self.p2)
        self.turn = self.p1
        self.field.display()

    def oneStep(self):
        #누가 둘 차례인지 감지한다
        # = self.turn
        #감지한 플레이어에게 현재 필드상황을 알려주며 돌을 놓는 함수를 실행
        #플레이어가 놓은 곳을 감지한다
        here = self.turn.Next(self.field)
        if here == -1:
            #놓을 공간이 없으면
            if self.noWay == True:
                #턴넘김 연속발생
                self.endGame()
            self.noWay = True
            #만약 플레이어가 돌을 놓을 수 없다면 다음 플레이어에게 순서를 넘긴다. 이때 턴넘김 변수를 수정하여
            #두 플레이어가 연속으로 턴을 넘길 경우 그대로 게임이 종료되도록 한다
        else:
            #필드를 수정한다
            self.noWay = False
            self.modifyField(here,self.turn)

        self.turn = self.turn.opponent

        

