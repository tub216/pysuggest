#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import suggest

def test_suggest():
    trans = 3
    
    groups = suggest.intArray(3)
    photos = suggest.intArray(3)
    
    photos[0] = 0
    groups[0] = 0
        
    photos[1] = 1
    groups[1] = 1
        
    photos[2] = 1
    groups[2] = 0
        
    nphotos = 2
    ngroups = 2    
        
    print 'trans',trans
    print 'ngroups',ngroups
    print 'nphotos',nphotos    
    
    print 'initing'
    
    rhandle = suggest.SUGGEST_Init(nphotos,ngroups,trans,photos,groups,2,1,0.4)

    print 'inited'
    
    results = suggest.intArray(1)
    pgroups = suggest.intArray(1)
    pgroups[0] = 0
    
    print suggest.SUGGEST_TopN(rhandle, 1, pgroups, 1, results)    

    suggest.SUGGEST_Clean(rhandle)

    print 'done'    

if __name__== '__main__' :
    test_suggest() 
