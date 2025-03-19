x = 50
def fun1():
    global x
    x = 20
fun1()
print(x) # it should print 20