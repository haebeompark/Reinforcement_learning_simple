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
        try:
            self.field = Field.createFieldWithScale(scale)
            # numpy타입의 2차원배열 생성됨 (scale by scale)
        except:
            E.err("field:__init__:ERR-parameter invalid")

    def convertToNode(self):
        return Field.FieldToNode(self.field)

    def setFieldWithNode(self,arr):
        self.Field = Field.NodeToField(arr)

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
            raise #scale이 odd인경우 에러 발생시키기
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
    
    @staticmethod
    def Reverse(cls, field, here: int, myColor, scale: int):
        # scale이 8일 때
        # here : 0~63
        # x : 0~7
        # y : 0~7
        x = int(here) / int(scale)
        y = int(here) % int(scale)
        # + 증가, 0 부동, - 감소 하는 쪽으로의 방향을 뜻한다.
        # 첫번째 시도 : (x,y)에 대하여 (+,0) 방향
        if x >= 6 :
            # x가 6 또는 7인 경우 탐색할 필요가 없음.
            pass
        else:
            for i in range (x+1, 8):
                # x+2부터 7까지의 자리를 탐색하게 된다. x+1자리에 같은색 돌이 있으면 뒤집을 수 없다.
                if field[i,y] == color.empty.value:
                    # 같은 색의 돌보다 빈자리를 먼저 탐색했다면 절대 뒤집을 수 없다. 여기서 skip
                    break
                elif field[i,y] == myColor:
                    #가장 근접한 돌 발견시 사이에 있는 다른 돌들을 전부 뒤집는다.
                    for k in range(x+1, i):
                        field[k,y] = myColor
                    break
        # 두번째 시도 : (x,y)에 대하여 (-,0) 방향
        if x <= 1 :
            # x가 0또는 1인 경우 탐색할 필요가 없음.
            pass
        else:
            for i_r in range (8-x, 8):
                i = 7-i_r
                # i : x-1 ~ 0 DESC
                if field[i,y] == color.empty.value:
                    break
                elif field[i,y] == myColor:
                    for k in range(i+1, x):
                        field[k,y] = myColor
        # 세번째, 네번째 시도 : x로 적힌것을 y로 변경 (0,+), (0,-)방향
        if y >= 6 :
            # x가 6 또는 7인 경우 탐색할 필요가 없음.
            pass
        else:
            for i in range (y+1, 8):
                if field[x,i] == color.empty.value:
                    break
                elif field[x,i] == myColor:
                    for k in range(x+1, i):
                        field[x,k] = myColor
                    break
        if y <= 1 :
            pass
        else:
            for i_r in range (8-y, 8):
                i = 7-i_r
                # i : x-1 ~ 0 DESC
                if field[x,i] == color.empty.value:
                    break
                elif field[x,i] == myColor:
                    for k in range(i+1, x):
                        field[x,k] = myColor
        # 다섯번째부터는 대각선 방향을 탐색한다.
        # 다섯번째 : (+,+)방향
        if x >=6 or y>=6:
            pass
        else:
            M = max(x,y)
            maxCount = 8-M
            # 둘중 큰값에 의해 탐색의 최대치가 정해진다.
            for i_plus in range(1, maxCount):
                if field[x+i_plus,y+i_plus] == color.empty.value:
                    break
                elif field[x+i_plus,y+i_plus] == myColor:
                    for k_plus in range(1, i_plus):
                        field[x+k_plus, y+k_plus] == myColor
                    break
        
        # 여섯번째 : (-,-)방향
        if x <= 1 or y <= 1:
            pass
        else:
            M = max(7-x,7-y)
            maxCount = 8-M
            # 둘중 큰값에 의해 탐색의 최대치가 정해진다.
            for i_plus in range(1, maxCount):
                if field[x-i_plus,y-i_plus] == color.empty.value:
                    break
                elif field[x-i_plus,y-i_plus] == myColor:
                    for k_plus in range(1, i_plus):
                        field[x-k_plus, y-k_plus] == myColor
                    break
                
        # 일곱 여덟번째는 x,y가 서로 다른 부호를 같게 된다. (+,-) (-,+)
        # 일곱번째 : (+,-)방향
        if x >=6 or y <= 1:
            pass
        else:
            M = max(x,7-y)
            maxCount = 8-M
            # 둘중 큰값에 의해 탐색의 최대치가 정해진다.
            for i_plus in range(1, maxCount):
                if field[x+i_plus,y-i_plus] == color.empty.value:
                    break
                elif field[x+i_plus,y-i_plus] == myColor:
                    for k_plus in range(1, i_plus):
                        field[x+k_plus, y-k_plus] == myColor
                    break
        
        # 여덟번째 : (-,+)방향
        if x <= 1 or y >= 6:
            pass
        else:
            M = max(7-x,y)
            maxCount = 8-M
            # 둘중 큰값에 의해 탐색의 최대치가 정해진다.
            for i_plus in range(1, maxCount):
                if field[x-i_plus,y+i_plus] == color.empty.value:
                    break
                elif field[x-i_plus,y+i_plus] == myColor:
                    for k_plus in range(1, i_plus):
                        field[x-k_plus, y+k_plus] == myColor
                    break
        
        # 이렇게 변경된 field를 반환해준다.
        return field

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
        if (arr.dtype == self.field.dtype):
            # d타입을 field변수와 비교하여 다르면 에러(코드상으로 잘못되었는 경우)
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
            self.passCount += 1
        else:
            print(zeroIndex)


class dealer():
    #othello를 제어
    p1 = ""
    p2 = ""
    field = ""
    turn = ""
    noWay = False
    scale = 8

    def __init__(self):
        self.field = Field(self.scale)
        self.p1 = othello(self.field,first = "me").Link(self)
        self.p2 = othello(self.field,first = "you").Link(self,self.p1)
        # Link() : 자신의 상대편을 명시한다.
        # 이를 통해 dealer와 두 플레이어는 결속된다.
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
        
    def modifyField(self, here: int,turn: othello):
        # 돌이 놓아짐으로서 변경을 반영하게 된다.
        # here : 놓는 위치
        # turn : othello인스턴스
        
        # 1. 상하좌우 및 대각선 방향의 8향을 탐색한다.
        # 2. 각 방향당 아래를 실행(총 8번하게 된다)
        # 3. 선택된 방향쪽에 나와 같은 색이 있는가?
        # 4. YES -> 가장 가까운 색의 돌을 기억한다.
        # 4.1 NO -> pass
        # 5. 4번에서 탐색된 같은색의 돌과 방금 놓은 돌의 사이에 다른색의 돌로 가득 매워져있는가?
        # 6. YES -> 사이의 돌을 전부 나와 같은색으로 변경
        # 6.1 NO -> pass
        # 7 방향을 바꿔서 7번 더 실행
        
        nodeList = Field.NodeToField(self.field)
        if nodeList[here] != color.empty.value:
            E.err("dealer:modifyField:ERR-node is not empty")
        else:
            #self.field[here/self.scale, here%self.scale] = turn.myColor
            Field.Reverse(self.field, here, turn.myColor, self.scale)
        return

