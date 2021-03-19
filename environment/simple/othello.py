import numpy as np
class othello:
    field = np.zeros((8,8))
    passCount = 0
    linked = ""
    def __init__(self,first = "me"):
        if first == "me":
            initiate = 1
        else:
            initiate = -1
        self.field[3][3] = initiate
        self.field[4][3] = -1 * initiate
        self.field[3][4] = -1 * initiate
        self.field[4][4] = initiate
        print(self.field[3][3])
        print(self.field)

    def Link(self, dealer):
        #서로를 참조하는 형태가아닌 딜러가 이어주는 형태로 진행
        #딜러는 두 플레이어의 정보를 가지고 있으며 othello클래스의 method들을 실행하게 된다
        #main은 딜러에게 플레이어 둘을 넣어주는 것이 끝
        self.linked = dealer

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
        #턴이 끝나서 넘김
        # -1인경우 둘곳이 없단 이야기
        return laySpot

    def lay(self,zeroIndex):
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
    #딜러는 오셀로 게임과 동시에 생성되며 게임 그 자체이기도 하면서 게임 관리자이다. 스스로 종료 가능하다
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def __init__(self):
        self.p1 = othello(first = "me")
        self.p2 = othello(first = "you")

     