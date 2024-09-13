
from mydecortors import resourceHandler



@resourceHandler
def process(filename):
    print('playing with resource here that si ',filename)
    print('manipulating and writing the resources')

@resourceHandler
def dbactivity(db):
    print('working with db resources',db)
    print('playing with db data')    

process('file name e.txt')
dbactivity('mysql database')    