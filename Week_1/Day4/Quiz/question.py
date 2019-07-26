class Question:
    def __init__(self,qdata,op_1,op_2,op_3,op_4,canswer):
        self.qdata = qdata
        self.op_1 = op_1
        self.op_2 = op_2
        self.op_3 = op_3
        self.op_4 = op_4
        self.c_answer = canswer

    def __str__(self):
        return f"{self.qdata} \nA.{self.op_1} \nB.{self.op_2} \nC.{self.op_3} \nD.{self.op_4}"