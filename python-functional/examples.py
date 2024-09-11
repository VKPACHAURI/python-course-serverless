a=[111,222,323,432,543,654,765,876]

def checktype(a):
    if a%2==0:
        return "EVEN"
    else:
        return "ODD"
# map function take the arguemnst as function and iterable
result=map(checktype,a)  
print(result) 
print(list(result))