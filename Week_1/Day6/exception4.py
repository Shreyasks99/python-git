class MaxLimitError(Exception):
    def __init__(self,message):
        self.message = message
    
    def __str__(self):
        return f"{ self.__class__.__name__} : {self.message}"

c = 0
def login(username,password):
    global c
    if username =="abc" and password == "bcd":
        print("Login is succesfful")
    else:
        print("Bad credentisls")
    c +=1
    if c > 2:
        raise MaxLimitError("You have entered manimum number of tries")

login("ABC","BCD")
login("ASD","NBV")
login("SDF","IST")
login("a","c")