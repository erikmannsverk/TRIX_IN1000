a = 2

def endreA():
    a = 5

endreA()
print(a)

###

a = 2

def endreA():
    a = 5

b = endreA()
print(a)

###

a = 2

def endreA():
    return 5

a = endreA()
print(a)

###

a = 2

def endreA(b):
    b = 5
    return b

endreA(a)
print(a)

###

a = 2

def endreA(b):
    b = 5
    return b

a = endreA(a)
print(a)

###

a = 2

def endreA(b):
    b = 5
    return b

a = endreA(a)
print(b)
