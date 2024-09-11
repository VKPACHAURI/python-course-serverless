def fun(task):
    print("the function is execting",task)

def doItMyWay(task):
    print('quickly performing', task)


def taskExecutor(mylist,callme):
    for x in mylist:
        print('performing task setup and going to invoke')
        callme(x)
        print('performing the post activities and going to wrap the task')
        print('-------------------------------')
#the function which is passed as parameter to another function-called callback function
taskExecutor(["Building","Compiling","Packing","Deploying"],fun)        