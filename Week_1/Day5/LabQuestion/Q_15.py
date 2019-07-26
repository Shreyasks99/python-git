class Name:
    def __init__(self,accno,name,balance):

        self.accno = accno
        self.name = name
        self.balance = balance

    def get_accno(self):
	    return self.accno

    def set_accno(self, accno):
	    self.accno = accno

    def get_name(self):
        return self.name
        
    def set_name(self, name):
        self.name = name

    def get_balance(self):
        return self.balance
        
    def set_balance(self, balance):
        self.balance = balance


    