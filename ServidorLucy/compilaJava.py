#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 11:02:44 2019

@author: adilsonlopeskhouri
"""

import os.path, subprocess
from subprocess import STDOUT, PIPE

def compile_java (java_file):
    subprocess.check_call(['/usr/bin/javac', java_file])

def execute_java (java_file):
    cmd=['java', java_file]
    proc=subprocess.Popen(cmd, stdout = PIPE, stderr = STDOUT)
    inputi = subprocess.Popen(cmd, stdin = PIPE)
    print(proc.stdout.read())


def compila2(java_file):
    cmd = """/usr/bin/javac """ + java_file
    print(cmd)
    proc = subprocess.Popen(cmd, shell=True)


#/Users/adilsonlopeskhouri/Desktop/machine/machineLearningForSWTest/ServidorLucy/
compila2("DirsoTesteXXXX.java")
#execute_java("FmtRewrap")



#pesquisa por testes find Users/ -name "*FmtRewrap*" 

