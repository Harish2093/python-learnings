def hello(*args):
    print(args)

#hello(0)

def hellokwargs(**kwargs):
    kwargs['New'] = 'Harish'
    print(kwargs)

inn = {'old':'Ha'}
#hellokwargs(**inn)

def master(normal, *args,**kwargs):
    print(normal)
    print(args)
    print(kwargs)
lis = [0,1]
master('harish',  0,3, 4, *lis, **{'Sir':"Patil"},**{'name':'harish'})