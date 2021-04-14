def div(x,y):
    print(x/y)

def smart_div(fun):
    def inner(x,y):
        if x<y:
            x,y=y,x
            return fun(x,y)

    return inner

div=smart_div(div)
div(2,4)
import calc