"""
LEGB
Local,Enclosing,Global,Built-in
"""

# rule for check the scope of the variable  local -> enclosed -> global ->built-in

x = 'global x'   #global

def test():
    x='local x'   #local
    print(x)


test()
print(x)    


#---

# X = 'global X'

def test():
    global X  # this line take global X varibale at  line 19
    X = 'local X' # change global x to 'local X' for line 19
    print(X)     # return local X

test()   # local X
print(X)    # local X 



#--------

def outer():
    x="outer_x"     # local to outer() and enclosed for inner()
    def inner():
        x="inner_x"   # local to inner()
        print(x)
    
    inner()
    print(x) 

outer()       



def outer():
    x="outer_x"     # local to outer() and enclosed for inner()
    def inner():
        nonlocal x   # this line will take enclose varibla x at line 47
        x="inner_x1"   # modif "outer_x" to "inner_x" for enclose local to inner()
        print(x)
    
    inner()
    print(x) 

outer()   