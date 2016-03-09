
myfile = open( "c:\work\WINCMD.INI", "r" )

#print( type( myfile ) );
#print( id( myfile ) );


# Line include new line at the end
for line in  myfile :
    print( "linija %s", line )