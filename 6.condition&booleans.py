def function():
    print("hello")


print(
    function()
)  # print(fun_name()) - execute the statement inside it and return the value if no return is there it return None


def greet(name="kp"):
    return f"Hi {name}"


print(greet("kartikey"))


# def function_name(postional_argument,keyword_argument=value):
#   pass


# always put postional_argument before the keyword_argument
# keyword_argument -> argu = value


# -------------- *args(take all postional_argument as tuple) , **kwargs(take keyword_argument as dictionary)


def biodata(*args, **kwargs):
    print(args)  # ('jane','india')
    print(kwargs)  # {'age': 24,'job': 'engineer'}


biodata("jane", "india", age=24, job="engineer")
