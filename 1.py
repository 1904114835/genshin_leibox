import random
class lei_box():
    def __init__(self,num:int,state:int,rule:[],leibox):
        if len(rule)!=num:
            print("规则错误")
            return False
        if len(leibox)==0:
            self._lei_box=[random.randint(0,state-1) for i in range(num)]
        else:
            self._lei_box=[i for i in leibox]
        self.num=num
        self.state=state
        self.rule_list=rule
    def get(self):
        return self._lei_box
    def change_one(self,pos):
        if pos>=self.num:
            print("下标溢出")
            return False
        self._lei_box[pos]=(self._lei_box[pos]+1)%self.state
    def change_back_one(self,pos):
        if pos>=self.num:
            print("下标溢出")
            return False
        self._lei_box[pos]=(self._lei_box[pos]-1)%self.state
    def show(self):
        print("box:",self._lei_box)
    def change_rule(self,pos):
        temp_rule=self.rule_list[pos]
        for i in temp_rule:
            self.change_one(i)
    def change_rule_back(self,pos):
        temp_rule=self.rule_list[pos]
        for i in temp_rule:
            self.change_back_one(i)
    def check(self):
        if len(set(self._lei_box))==1:
            return True
        else:
            return False
    def change_oplist(self,op):
        for i in range(len(op)):
            if op[i] == 1:                
                self.change_rule(i%self.num)
    def change_oplist_back(self,op):
        for i in range(len(op)):
            if op[i] == 1:                
                self.change_rule_back(i%self.num)
                
def rand(box):
    box.show()
    while not box.check():
        t=random.randint(0,len(box.get())-1)
        print(t)
        box.change_rule(t)
    box.show()
    
def trace(box,op,n=0):
    #显然每个机关不应该被转动大于等于sate次，因为这样相当于没转动
    #那么最长的序列，应该是(state-1)*num次
    #print(op)
    if n >= box.num*(box.state-1):
        return
    box.change_oplist(op)
    if box.check():
        #box.show()
        global finalop
        if sum(op)<sum(finalop):
            finalop=[i for i in op]
        #print("op:",op)
        return 
    box.change_oplist_back(op)
    trace(box,op,n+1)
    top=[op[i] for i in range(len(op))]
    top[n]=1
    trace(box,top,n+1)
    return

def readbox():
    print("计数从0开始")
    num=int(input("输入雷方块个数，一个整数，以回车结尾"))
    state=int(input("输入雷方块状态数，一个整数，以回车结尾"))
    arr = input("输入雷方块状态，一组整数，以空格隔开，以回车结尾") 
    leibox = [int(n) for n in arr.split()]
    rule=[]
    for i in range(num):
        arr = input("输入打击第%d个雷方块的变化规则，一组整数，以空格隔开，以回车结尾".format(i)) 
        intarr = [int(n) for n in arr.split()]       
        rule.append(intarr)
#    print(num,state,rule,leibox)
    return num,state,rule,leibox
#num=4
#state=3
#rule=[[0,1],[1,3],[2,0],[3,1,2]]
#leibox=[0,1,0,1]

if __name__=="__main__":
    num,state,rule,leibox=readbox()
    
    box=lei_box(num,state,rule,leibox)
    finalop=[1 for i in range(int(box.num*(box.state-1)))]
    
    trace(box,[0 for i in range(int(box.num*(box.state-1)))])
    #print(finalop)
    op_can_read=[]
    for i in range(len(finalop)):
        if finalop[i]==1:
            op_can_read.append(i%box.num)
    print(op_can_read)