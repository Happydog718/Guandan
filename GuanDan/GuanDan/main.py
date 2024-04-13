import random
import copy
card = random.sample(range(0, 104), 54)
cardtrans = {'A': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
cardlist = ['A', 'A', 'A', 'A', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '6', '6',
            '6', '6','7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '10', '10', '10', '10', 'J', 'J', 'J', 'J',
            'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K', 'A', 'A', 'A', 'A', '2', '2', '2', '2', '3', '3', '3', '3',
            '4', '4', '4', '4', '5', '5', '5', '5', '6', '6', '6', '6','7', '7', '7', '7', '8', '8', '8', '8',
            '9', '9', '9', '9', '10', '10', '10', '10', 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K']
cardtype = ("single", "double", "string", "triple", "triple-double", "double-triple", "bomb", "three-two")
aicard=[]


class yourcard:
    ycard=[]
    ycardjustout=[]
    def __init__(self):
        for i in card[0:27]:
            self.ycard.append(cardlist[i])
    def sortcard(self, onecard = ycard):
        pd = True
        while pd:
            pd = False
            for i in range(len(onecard) - 1):
                if cardtrans[onecard[i]] > cardtrans[onecard[i + 1]]:
                    pd = True
                    onecard[i], onecard[i + 1] = onecard[i + 1], onecard[i]
    def showcard(self):
        for i in self.ycard:
            print(i, end=',')
        print('\n')
    def bombpd(self, yout):
        numbers = yout
        for i in range(len(numbers) - 1):
            if numbers[i]!=numbers[i+1]:
                return False
        return True
    def stringpd(self, yout):
        numbers = yout
        for i in range(len(numbers)-1):
            if (cardtrans[numbers[i]]+1) != cardtrans[numbers[i+1]]:
                return False
        return True
    def cardout(self, aitype="", aipoint=0):
        if len(self.ycard)==0:
            return "youwin", 0
        ctype = ""
        cpoint = 0
        pd=True
        pd1=False
        while pd:
            for i in self.ycardjustout:
                self.ycard.append(i)
            self.sortcard()
            self.showcard()
            yout = input("请输入你要出的牌，以空格间隔(如果不出牌，请输入E)：")
            yout=yout.split()
            self.sortcard(yout)
            if yout[0]=='E':
                self.ycardjustout=[]
                print("过")
                return "", 0
            if yout[0]!='E':
                for i in yout:
                    if i in self.ycard:
                        self.ycard.remove(i)
                        self.ycardjustout.append(i)
                    else:
                        for i in self.ycardjustout:
                            self.ycard.append(i)
                        self.ycardjustout = []
                        print("手牌中没有选的牌")
                        pd1=True
                        break
            if pd1:
                continue
            self.ycardjustout=[]
            if True:
                print("你出的牌是:", yout)
                for i in yout:
                    self.ycardjustout.append(i)
                lenout = len(yout)
                if lenout == 1:
                    ctype = "single"
                    cpoint = cardtrans[yout[0]]
                    pd=False
                elif lenout == 2:
                    if yout[0] == yout[1]:
                        ctype = "double"
                        cpoint = cardtrans[yout[0]]
                        pd=False
                    else:
                        print("没有这样的组合")
                        continue
                elif lenout == 3:
                    if yout[0]==yout[1] and yout[1]==yout[2]:
                        ctype = "triple"
                        cpoint=cardtrans[yout[0]]
                        pd=False
                    else:
                        print("没有这样的组合")
                        continue
                elif lenout == 4:
                    if self.bombpd(yout):
                        ctype = "bomb"
                        cpoint=cardtrans[yout[0]]
                        pd=False
                    else:
                        print("没有这样的组合")
                        continue
                elif lenout == 5:
                    if self.bombpd(yout):
                        ctype = "bomb"
                        cpoint=cardtrans[yout[0]]
                        pd=False
                    elif yout[0]==yout[1] and yout[1]==yout[2] and yout[4]==yout[3]:
                        ctype= "three-two"
                        cpoint=cardtrans[yout[0]]
                        pd=False
                    elif yout[0] == yout[1] and yout[2] == yout[3] and yout[3] == yout[4]:
                        ctype = "three-two"
                        cpoint = cardtrans[yout[4]]
                        pd=False
                    elif self.stringpd(yout):
                        ctype = "string"
                        cpoint=cardtrans[yout[-1]]
                        pd=False
                    else:
                        print("没有这样的组合")
                        continue
                elif lenout == 6:
                    if self.bombpd(yout):
                        ctype = "bomb"
                        cpoint=cardtrans[yout[0]]
                        pd=False
                    elif self.stringpd(yout):
                        ctype = "string"
                        cpoint=cardtrans[yout[-1]]
                        pd=False
                    elif yout[0]==yout[1] and yout[2]==yout[3] and yout[4]==yout[5]:
                        ctype= "triple-double"
                        cpoint=cardtrans[yout[-1]]
                        pd=False
                    elif yout[0]==yout[1] and yout[1]==yout[2] and yout[3]==yout[4] and yout[4]==yout[5]:
                        ctype = "double-triple"
                        cpoint=cardtrans[yout[-1]]
                        pd=False
                    else:
                        print("出牌不合法")
                        continue
                elif self.bombpd(yout):
                    ctype = "bomb"
                    cpoint=cardtrans[yout[0]]
                    pd=False
                elif self.stringpd(yout):
                    ctype = "string"
                    cpoint=cardtrans[yout[-1]]
                    pd=False
                else:
                    print("没有这样的组合")
                    continue
            if aitype=="" or (ctype=="bomb"and aitype!="bomb"):
                return ctype, cpoint
            else:
                if ctype==aitype and cpoint>aipoint:
                    self.ycardjustout=[]
                    return ctype, cpoint
                else:
                    for i in self.ycardjustout:
                        self.ycard.append(i)
                        print("出的牌组合不对或比对方小")
                    self.sortcard()
                    self.ycardjustout=[]
                    pd1=True
            if pd1:
                continue
#    def cardin(self, aitype="", aipoint=0):
#        while True:
#            ytype, ypoint = self.cardout()
#            if ytype==aitype and ypoint>aipoint:
#                self.ycardjustout=[]
#                return ytype, ypoint
#            else:
#                for i in self.ycardjustout:
#                    self.ycard.append(i)
#                    print("出牌不合法")
#                self.sortcard()
#                self.ycardjustout=[]


class Aicard:
    aicard=[]
    def __init__(self):
        for i in card[27:54]:
            self.aicard.append(cardlist[i])
    def sortcard(self, onecard = aicard):
        pd = True
        while pd:
            pd = False
            for i in range(len(onecard) - 1):
                if cardtrans[onecard[i]] > cardtrans[onecard[i + 1]]:
                    pd = True
                    onecard[i], onecard[i + 1] = onecard[i + 1], onecard[i]
    def showcard(self):
        for i in self.aicard:
            print(i, end=',')
        print('\n')
    def bombpd(self, yout):
        numbers = yout
        for i in range(len(numbers) - 1):
            if numbers[i]!=numbers[i+1]:
                return False
        return True
    def stringpd(self, yout):
        numbers = yout
        for i in range(len(numbers)-1):
            if (cardtrans[numbers[i]]+1) != cardtrans[numbers[i+1]]:
                return False
        return True
    def cardpd(self, card):
        self.sortcard(card)
        ctype=""
        cpoint=0
        lenout=len(card)
        if lenout==0:
            return False
        if lenout == 1:
            ctype = "single"
            cpoint = cardtrans[card[0]]
        elif lenout == 2:
            if card[0] == card[1]:
                ctype = "double"
                cpoint = cardtrans[card[0]]
            else:
                return False
        elif lenout == 3:
            if card[0] == card[1] and card[1] == card[2]:
                ctype = "triple"
                cpoint = cardtrans[card[0]]
            else:
                return False
        elif lenout == 4:
            if self.bombpd(card):
                ctype = "bomb"
                cpoint = cardtrans[card[0]]
            else:
                return False
        elif lenout == 5:
            if self.bombpd(card):
                ctype = "bomb"
                cpoint = cardtrans[card[0]]
            elif card[0] == card[1] and card[1] == card[2] and card[4] == card[3]:
                ctype = "three-two"
                cpoint = cardtrans[card[0]]
            elif card[0] == card[1] and card[2] == card[3] and card[3] == card[4]:
                ctype = "three-two"
                cpoint = cardtrans[card[4]]
            elif self.stringpd(card):
                ctype = "string"
                cpoint = cardtrans[card[-1]]
            else:
                return False
        elif lenout == 6:
            if self.bombpd(card):
                ctype = "bomb"
                cpoint = cardtrans[card[0]]
            elif self.stringpd(card):
                ctype = "string"
                cpoint = cardtrans[card[-1]]
            elif card[0] == card[1] and card[2] == card[3] and card[4] == card[5]:
                ctype = "triple-double"
                cpoint = cardtrans[card[-1]]
            elif card[0] == card[1] and card[1] == card[2] and card[3] == card[4] and card[4] == card[5]:
                ctype = "double-triple"
                cpoint = cardtrans[card[-1]]
            else:
                return False
        elif self.bombpd(card):
            ctype = "bomb"
            cpoint = cardtrans[card[0]]
        elif self.stringpd(card):
            ctype = "string"
            cpoint = cardtrans[card[-1]]
        else:
            return False
        return ctype, cpoint
    def searchcard(self, ctype="", cpoint=0):
        if len(self.aicard)==0:
            return "aiwin", 0
        result=[[]]
        result1=[[]]
        cardcanout=[]
        for i in self.aicard:
            for j in result:
                x=j
                x.append(i)
                if len(x)<5 or (len(x)>=5 and self.cardpd(x)!=False):
                    result1.append(x)
            result=copy.deepcopy(result1)
        result.pop(0)
        for i in result:
            if self.cardpd(i)!=False:
                cardcanout.append(i)
        lencanout=len(cardcanout)
        aitype=""
        aipoint=0
        if ctype=="" or (aitype=="bomb" and ctype!="bomb"):
            numout=random.sample(range(lencanout), 1)
            print("AI出牌为", cardcanout[numout[0]])
            for i in cardcanout[numout[0]]:
                self.aicard.pop(self.aicard.index(i))
            aitype, aipoint=self.cardpd(cardcanout[numout[0]])
            return aitype, aipoint
        else:
            cardcanout1=[]
            for i in cardcanout:
                aitype, aipoint=self.cardpd(i)
                if aitype==ctype and aipoint>cpoint:
                    cardcanout1.append(i)
            cardcanout=copy.deepcopy(cardcanout1)
            if len(cardcanout)!=0:
                #numout = random.sample(range(0,len(cardcanout)), 1)
                print("AI出牌为", cardcanout[0])
                for i in cardcanout[0]:
                    self.aicard.pop(self.aicard.index(i))
                aitype, aipoint = self.cardpd(cardcanout[0])
                return aitype, aipoint
            else:
                print("AI无牌可出")
                return "", 0


you = yourcard()
ai = Aicard()
ctype=""
cpoint=0
aitype=""
aipoint=0
while aitype!="aiwin" and ctype!="youwin":
    you.sortcard()
    ctype, cpoint = you.cardout(aitype, aipoint)
    ai.sortcard()
    aitype, aipoint = ai.searchcard(ctype, cpoint)
if aitype=="aiwin":
    print("aiwin")
else:
    print("youwin")