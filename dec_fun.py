#decorated fun==> Design pattern
#DRY==>don't repeat same section of code

def dec_fun(fn):
    def inner_fn(n1,n2):
        if n2>n1:
            (n1,n2)=(n2,n1)                            #swap
        return fn(n1,n2)
    return inner_fn

@dec_fun
def sub(n1,n2):
    return n1-n2
@dec_fun
def div(n1,n2):
    return  n1/n2
print (sub(10,20))
print(sub(20,10))
print(div(10,20))
print(div(20,10))