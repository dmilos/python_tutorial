import os
import hashlib
import string

def char2hex( char ):
    return format(ord(char), '02x')

def print_hex( data ):
    str =''
    for c in data:
        str += char2hex(c)
    return str

def scan_dir( top ):
    
    for root, dir, file in os.walk( top, topdown = False ):
        for name in file:
            #print os.path.join( root, name )
            m = hashlib.md5()
            with open( os.path.join( root, name ) ) as handle:
                m.update( handle.read() )
                
                #print( print_hex( m.digest() ) )
            print '{ \' MD5\' : \'' + print_hex( m.digest() )  + '\', \'name\' : ' + '\'' + os.path.join( root, name ) +'\' }'

scan_dir( 'c:\\temp\ss' )