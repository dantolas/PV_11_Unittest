import cmath

def addNumbers(a ,b):
    if(not isinstance(a,(float,int,complex)) or not isinstance(b,(float,int,complex))):
        raise Exception("Only numbers can be added.")

    return a+b