#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 20:46:05 2019

@author: adilsonlopeskhouri
"""

import re
import sys
import pandas as pd
import numpy as np


#Conventions for the pd command line
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 100)


weakcsv = 'parseado_weakmutation.csv'
branchcsv = 'parseado_branch.csv'
strongcsv = 'parseado_strongmutation_no_error.csv'


branchcsv = pd.read_csv(branchcsv, sep = ';')

#remove o index
branchcsv = branchcsv.drop(['Unnamed: 0'],axis = 1)

print(branchcsv)
print("=====================================================")
#Overview
print(branchcsv.dtypes)

#aqui faco as conversoes
print("=====================================================")
print("Número de classes criadas teste: {}".format(branchcsv.shape[0]))
print("Número de atributos das classes criadas teste: {}".format(branchcsv.shape[1]))
print("=====================================================")

#aqui analiso o trem
print(branchcsv.head(n = 3))




