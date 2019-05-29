#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 19:52:12 2019

@author: adilsonlopeskhouri
"""

import re
import sys

def leArquivo(path, splitPattern):
    
    strg = """java -cp .:"./junit-4.12.jar:evosuite-1.0.6.jar:./outputTeste/Closure/evosuite-branch/1/:hamcrest-core-1.3.jar:./Clojure_18_bug/build/compiler.jar" org.junit.runner.JUnitCore"""
    
    with open(path) as fp:  
       line = fp.readline()
       cnt = 1
       while line:
           l = line.strip().split(splitPattern)[1].replace('/','.').replace('.class','')
           if l.find("_scaffolding") == -1:
               #print(l)               
               strg = strg + " " +l
           line = fp.readline()
           cnt += 1

    print(strg)
pass

arquivo = sys.argv[1]
padrao = sys.argv[2]
leArquivo(arquivo, padrao)


