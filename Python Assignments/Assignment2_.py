# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 07:35:37 2015

@author: buddingscientist
"""

import urllib2
ur = "http://www.uniprot.org/uniprot/?query=go:morphogen%20activity+AND+organism:9606&format=tab&columns=id,genes,database(PDB),length" 
file_ = urllib2.urlopen(ur)

header =file_.readline()
contents = file_.read()



listy = []

def findShort(contents):
    a = contents.split('\n')
    b = a.pop()
    listx = []
    for item in a:
        c = item.split('\t')
        listx.append(c)
    i = -1
    for item in listx:
        length = item[len(item)-1]
        i+=1    
        dictionary = (length, i)
        listy.append(dictionary)
        listy.sort()
        index = listy[0][1]
        answer = listx[index][0]
    print '(1) The shortest sequence is: ', answer, ', with a length of: ', listy[0][0], ' residues.'

def retrieveID(contents):
    a = contents.split('\n')
    b = a.pop()
    listx = []
    lista = []
    for item in a:
        c = item.split('\t')
        listx.append(c)
    for stuff in listx:
        ID = stuff[0]
        geneName = tuple(stuff[1].split())
        tuple1 = (geneName, ID)
        lista.append(tuple1)
    dicti = dict(lista)
    Dick = []
    for i in dicti.keys():
        for j in i:
            newTup = (j, dicti[i])
            Dick.append(newTup)
            Dick_=dict(Dick)
    query = raw_input('(2) Enter a gene name to see its ID: ')
    if query not in Dick_.keys():
        print 'Not a valid query...' 
    else:
        print 'ID of ', str(query), ' is ', str(Dick_[str(query)])
        
def retrievePDB(contents):
    a = contents.split('\n')
    a.pop()
    listx = []
    list1=[]
    
    for item in a:
        c = item.split('\t')
        listx.append(c)
    
    for stuff in listx:
        ID = stuff[0]
        if ';' in stuff[2]:
            PDB = str(stuff[2].split(';'))
            while '' in PDB:
                PDB=PDB.replace('\'\'','')
                tupletjie = [ID,PDB]
                break
                
        else:
            PDB = 'False'
            tupletjie = [ID,PDB]
            
        list1.append(tupletjie)
    
    query = raw_input('(3) Enter an ID to see its PDB cross reference: ')
    johnson=0    
    while johnson < len(list1):
        if query == list1[johnson][0]:
            print 'PDB cross reference(s) of', query, 'is', list1[johnson][1]
            johnson +=1
        else:
            johnson+=1

def numGenesPerID(contents):
    a = contents.split('\n')
    a.pop()
    listx = []
    list1=[]
    for item in a:
        c = item.split('\t')
        listx.append(c)
    for stuff in listx:
        ID = stuff[0]
        genes = stuff[1]
        splitUp = genes.split()
        list1.append((len(splitUp),ID))
    list1.sort()
    print '(4) The number of genes per ID, in ascending order, is: ',list1  

def printPairsGenesPDBs(contents):
    a = contents.split('\n')
    a.pop()
    listx = []
    lista = []
    listb = []
    for item in a:
        c = item.split('\t')
        listx.append(c)
        
    for stuff in listx:
        genes = stuff[1].split()
        if ';' in stuff[2]:
            PDB = stuff[2].split(';')
            while '' in PDB:
                PDB.pop()
                if '' not in PDB:
                    break
                else: continue
        else:
            PDB = False
            
        lista.append(genes)
        listb.append(PDB)
    print '(5) The following is a list of all gene/PDB cross reference pairs: '
    jesus = 0
    while jesus < len(lista):
        for gene in lista[jesus]:
            try:
                #for P in listb[jesus]:
                    christ=0
                    while christ < len(listb[jesus]):
                        print gene, listb[jesus][christ]
                        christ+=1
            except TypeError:
                print gene, 'False'
        jesus+=1
    
        

findShort(contents)
retrieveID(contents)
retrievePDB(contents)
numGenesPerID(contents)
printPairsGenesPDBs(contents)
