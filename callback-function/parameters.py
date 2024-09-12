def myfun(*multi,**kwparams):
    print(multi)
    print(type(multi))

myfun(1)
myfun(1,2)
myfun(1,2,3,4)
myfun(1,2,3,4,5,6,7,8,9)   
myfun(name="Radhey") 