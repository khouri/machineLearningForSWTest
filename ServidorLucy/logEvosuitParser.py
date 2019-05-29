#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 19:31:54 2019

@author: adilsonlopeskhouri
"""

import re
import sys
import pandas as pd
import numpy as np


def parse_evosuite_log_file(path):
     
     df_log_evo = pd.DataFrame(columns=('class_name',
                                        'number_of_goals',
                                        'number_of_tests',
                                        'length_of_testes',
                                        'ga_zero_fitness',
                                        'ga_max_time',
                                        'ga_shutdown_test_writer',
                                        'test_suit_mutation_score',
                                        'time_spent_to_execute_tests',
                                        'test_suit_coverage',
                                        'num_coverage_goals',
                                        'criterion',
                                        'coverage_of_criterion',
                                        'search_finished_after',
                                        'num_generations',
                                        'num_statements',   
                                        'best_ind_fitness',
                                        'permissions',
                                        'warnings',
                                        'exceptions'
                                        ))
     class_name = None
     number_of_goals = None
     number_of_tests = None
     length_of_testes = None
     ga_zero_fitness = None
     ga_max_time = None
     ga_shutdown_test_writer = None
     test_suit_mutation_score = None
     time_spent_to_execute_tests = None
     test_suit_coverage = None
     num_coverage_goals = None
     criterion = None
     coverage_of_criterion = None
     search_finished_after = None
     num_generations = None
     num_statements    = None
     best_ind_fitness = None
     permissions = '' 
     warnings = ''
     exceptions = ''
     
     
     marcacaoPermissao = False  
     marcacaoExceptions = False  
     
     with open(path) as fp:  
         
       line = fp.readline()
       cnt = 1
       while line:
           
           #warnings
           if(line.find("WARN") != -1):
               warnings = warnings + line.split("WARN")[1].strip() + "\n //"

           #exceptions
#           if( marcacaoExceptions == True or line.find( "ERROR") != -1 ):
#               marcacaoExceptions = True
#               
#               #Acabou a descricao de erro
#               if( str(line[0]).find('*') == 0 and line.find( "ERROR") == -1 ):
#                   marcacaoExceptions = False
#                   
#               if(str(line[0]).find('*') != 0):
#                   exceptions = exceptions + line + " // "
                   
               
           if( marcacaoPermissao == True or line.find( "Permissions denied during test execution") != -1 ):
               marcacaoPermissao = True
               
               #Acabou a descricao de erro
               if( str(line[0]).find('*') == 0 and line.find( "Permissions denied during test execution") == -1 ):
                   marcacaoPermissao = False
                   
               if(str(line[0]).find('*') != 0):
                   permissions = permissions + line + " // "
           
           if(line.find("Going to generate test cases for class:") != -1):
               l = line.strip().split("class:")[1]
               class_name = l.strip()
           
           if(line.find("Total number of goals") != -1):
               l = line.strip().split("goals:")
               number_of_goals = l[1].split(":")[0].strip()

           if(line.find("tests with total length") != -1):
               l = line.strip().split(" tests with total length ")
               number_of_tests = l[0].replace('* Generated ','').split(":")[0].strip()               
               length_of_testes = l[1].strip()
               
           #GA-Budget
           if(line.find("ZeroFitness") != -1):
               l = line.strip().split(":")
               ga_zero_fitness = l[1].strip()
               
           if(line.find("MaxTime") != -1):
               l = line.strip().split(":")
               ga_max_time = l[1].strip()
           
           if(line.find("ShutdownTestWriter") != -1):
               l = line.strip().split(":")
               ga_shutdown_test_writer = l[1].strip()
           
           if(line.find("Resulting test suite's mutation score") != -1):
               l = line.strip().split("score:")
               test_suit_mutation_score = l[1].strip()

           if(line.find("Time spent executing tests") != -1):
               l = line.strip().split("tests:")
               time_spent_to_execute_tests = l[1].strip()
           
           if(line.find("Resulting test suite's coverage") != -1):
               l = line.strip().split("coverage:")
               test_suit_coverage = l[1].strip()
            
           if(line.find("Number of covered goals") != -1):
               l = line.strip().split("goals:")
               num_coverage_goals = l[1].split(":")[0].strip()
               
           if(line.find("Coverage of criterion") != -1):
               l = line.strip().split("criterion")
               criterion = l[1].split(":")[0].strip()
               coverage_of_criterion = l[1].split(":")[1].strip()
                
           if(line.find("Search finished after") != -1):              
               #Quebra em 3 blocos de informacao
               l = line.strip().split(", ")

               #tempo de busca
               l0tmp = l[0].split(" and ")

               #tempo
               search_finished_after = l0tmp[0].split("after ")[1].strip()

               #geracoes
               num_generations = l0tmp[1].split(" generations")[0].strip()
               
               #statements
               l1tmp = l[1].split(" ")
               num_statements = l1tmp[0].strip()
               
               #individual fitness
               l2tmp = l[2].split(": ")
               best_ind_fitness = l2tmp[1].strip()
               
               
           #Linha de erros de permissão

           if(line.find("Done") != -1):
               #add to dataframe
               df_log_evo = df_log_evo.append({
                                                'class_name':class_name,
                                                'number_of_goals':number_of_goals,
                                                'number_of_tests':number_of_tests,
                                                'length_of_testes':length_of_testes,
                                                'ga_zero_fitness':ga_zero_fitness,
                                                'ga_max_time':ga_max_time,
                                                'ga_shutdown_test_writer':ga_shutdown_test_writer,
                                                'test_suit_mutation_score':test_suit_mutation_score,
                                                'time_spent_to_execute_tests':time_spent_to_execute_tests,
                                                'test_suit_coverage':test_suit_coverage,
                                                'num_coverage_goals':num_coverage_goals,
                                                'criterion':criterion,
                                                'coverage_of_criterion':coverage_of_criterion,
                                                'search_finished_after':search_finished_after,
                                                'num_generations':num_generations,
                                                'num_statements':num_statements,   
                                                'best_ind_fitness':best_ind_fitness,
                                                'permissions':permissions,
                                                'warnings':warnings,
                                                'exceptions':exceptions
                                           }, ignore_index=True)
                
               class_name = None
               number_of_goals = None
               number_of_tests = None
               length_of_testes = None
               ga_zero_fitness = None
               ga_max_time = None
               ga_shutdown_test_writer = None
               test_suit_mutation_score = None
               time_spent_to_execute_tests = None
               test_suit_coverage = None
               num_coverage_goals = None
               criterion = None
               coverage_of_criterion = None
               search_finished_after = None
               num_generations = None
               num_statements    = None
               best_ind_fitness = None
               permissions = ''
               warnings = ''
               exceptions = ''
            
           line = fp.readline()
           cnt += 1
    
     return(df_log_evo)
pass

#
##Branch
#path = "Closure.18b.branch.1.log"
#config_evo_run = parse_evosuite_log_file(path)
#config_evo_run.to_csv('parseado_branch.csv',sep = ';')


#weakmutation
#path = "Closure.18b.weakmutation.2.log"
#config_evo_run = parse_evosuite_log_file(path)
#config_evo_run.to_csv('parseado_weakmutation.csv',sep = ';')


#strongmutation
#path = "Closure.18b.strongmutation.3.log"
#config_evo_run = parse_evosuite_log_file(path)
#config_evo_run.to_csv('parseado_strongmutation_no_error.csv',sep = ';')



