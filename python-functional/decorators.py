
from mydecorators import resourceHandler
from mydecorators import takeBackup


@resourceHandler
def process(filename):
    print('playing with resource here that si ',filename)
    print('manipulating and writing the resources')

@resourceHandler
def dbactivity(db):
    print('working with db resources',db)
    print('playing with db data')  


@takeBackup(location="d:\\takeit")
def dbfun(db):
    print("performing a db actvity of db",db)
    print("playing with db data")      

#process('file name e.txt')
#dbactivity('mysql database')    
dbfun("oracle")