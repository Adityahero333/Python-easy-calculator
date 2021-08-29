def sum(a,b):
        c = a +b
        return c
    
def sub(x,y):
    c = a - b
    return c

def invsub(y,x):
    c = b - a
    return c

def div(s,t):
    c = a/b
    d = a%b
    print("On dividing",a," by ",b ," quotient is", c)
    print("On dividing",a," by ",b ,"remainder is", d)
    
def invdiv(s,t):
    c = b/a
    d = b%a
    print("On dividing",b," by ",a ," quotient is", c)
    print("On dividing",b," by ",a ,"remainder is", d)

def mul(c,v):
    c = a * b
    return c



recalc = 0
while recalc < 1:
    a = int(input("Enter first number >> "))
    b = int(input("Enter second number >> "))
    print(" ")
    print("d = divide")
    print("m = multiply")
    print("a = addition")
    print("s = substraction")
    print("type 'all' to do all operations")
    whatToDo = input("What operation to do (d / m / a / s / all) ")
    print(" ")
 
    
    if whatToDo == "d":
        print(div(a,b))    
    
    elif whatToDo == "m":
        print(mul(a,b))
        
    elif whatToDo == "a":
        print(sum(a,b))
        
    elif whatToDo == "s":
        print(sub(a,b))
    
    elif whatToDo == "all":
        print("sum is" , sum(a,b))
        print("product is" , mul(a,b))
        print(div(a,b))
        print(invdiv(a,b))
        print("On subtracting",a ," from ",b, "the result is" ,sub(a,b))
        print("On subtracting",b ," from ",a, "the result is" ,invsub(b,a))
    
    again = input("Calculate again> (y/n) > ")
    if again == "n":
        recalc = 1
        break