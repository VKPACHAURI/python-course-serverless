def resourceHandler(fun):
    def logicController(*args,**kwargs):
        print("checking the resource and its authenticate")
        print("going to the actual function to run")
        fun(*args,**kwargs)
        print("Deallocating the memory allooted for the process")
        print("###################process terminated##############")
    return logicController    