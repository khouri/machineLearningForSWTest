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


def analisa_csv(path_csv):
    
    print("=====================================================")
    print("=====================================================")
    print("=====================================================")
    
    branchcsv = pd.read_csv(path_csv, sep = ';')
    
    #remove o index
    branchcsv = branchcsv.drop(['Unnamed: 0'],axis = 1)
    
    print("Número de classes criadas teste: {}".format(branchcsv.shape[0]))
    print("Número de atributos das classes criadas teste: {}".format(branchcsv.shape[1]))
    print("Total de casos de teste criados para todas as classes: {}".format(branchcsv.number_of_tests.sum()))
    print("Média de testes criados por classe: {}".format( round(branchcsv.number_of_tests.sum()/branchcsv.shape[0], 2) ))
    print("Tamanho médio(num statements) dos casos de testes criados: {}".format( round(branchcsv.length_of_testes.mean(), 2) ))
    print("Número de classes cujos testes geraram warning: {}".format( round(branchcsv.warnings.count(), 2) ))
    print("Número de classes cujos testes geraram exceptions: {}".format( round(branchcsv.exceptions.count(), 2) ))
    print("Número de classes cujos testes tiveram problemas de permissão: {}".format( round(branchcsv.permissions.count(), 2) ))
    
    print("=======================================================================")
#    print(branchcsv[branchcsv.test_suit_mutation_score.isna()])
#    print(branchcsv[branchcsv.test_suit_mutation_score.notnull()].test_suit_mutation_score)
    
    notNatest_suit_mutation_score = branchcsv[branchcsv.test_suit_mutation_score.notnull()].copy(deep = True)
    Natest_suit_mutation_score = branchcsv[branchcsv.test_suit_mutation_score.isna()].copy(deep = True)
    notNatest_suit_mutation_score['test_suit_mutation_score_noPercent'] = notNatest_suit_mutation_score.test_suit_mutation_score.str.replace('%','')
    
    notNatest_suit_mutation_score.test_suit_mutation_score_noPercent = notNatest_suit_mutation_score.test_suit_mutation_score_noPercent.astype(int)
    print("max mutation score: {}".format(notNatest_suit_mutation_score.test_suit_mutation_score_noPercent.max()))
    print("min mutation score: {}".format(notNatest_suit_mutation_score.test_suit_mutation_score_noPercent.min()))
    print("mean mutation score: {}".format(round(notNatest_suit_mutation_score.test_suit_mutation_score_noPercent.mean(),2)))
    print("number of NaN: {}".format(Natest_suit_mutation_score.test_suit_mutation_score.isna().sum()))
    
    print("=======================================================================")
    
    notNatime_spent_to_execute_tests = branchcsv[branchcsv.time_spent_to_execute_tests.notnull()].copy(deep = True)
    Natime_spent_to_execute_tests = branchcsv[branchcsv.time_spent_to_execute_tests.isna()].copy(deep = True)
    notNatime_spent_to_execute_tests['time_spent_to_execute_tests_no_unity'] = notNatime_spent_to_execute_tests['time_spent_to_execute_tests'].str.replace('ms','')
    notNatime_spent_to_execute_tests.time_spent_to_execute_tests_no_unity = notNatime_spent_to_execute_tests.time_spent_to_execute_tests_no_unity.astype(int)
    
    print("max time_spent_to_execute_tests: {} (seg)".format(notNatime_spent_to_execute_tests.time_spent_to_execute_tests_no_unity.max()/1000))
    print("min time_spent_to_execute_tests: {} (seg)".format(notNatime_spent_to_execute_tests.time_spent_to_execute_tests_no_unity.min()/1000))
    print("mean time_spent_to_execute_tests: {} (seg)".format(round(notNatime_spent_to_execute_tests.time_spent_to_execute_tests_no_unity.mean()/1000),2))
    print("number of NaN: {}".format(Natime_spent_to_execute_tests.time_spent_to_execute_tests.isna().sum()))
        
    #Limpeza
    print("=====================================================")
    notNatest_suit_coverage = branchcsv[branchcsv.test_suit_coverage.notnull()].copy(deep = True)
    Natest_suit_coverage = branchcsv[branchcsv.test_suit_coverage.isna()].copy(deep = True)
    notNatest_suit_coverage['test_suit_coverage_no_unity'] = notNatest_suit_coverage['test_suit_coverage'].str.replace('%','')
    notNatest_suit_coverage.test_suit_coverage_no_unity = notNatest_suit_coverage.test_suit_coverage_no_unity.astype(int)
    
    print("max test_suit_coverage: {} (%)".format(notNatest_suit_coverage.test_suit_coverage_no_unity.max()))
    print("min test_suit_coverage: {} (%)".format(notNatest_suit_coverage.test_suit_coverage_no_unity.min()))
    print("mean test_suit_coverage: {} (%)".format(round(notNatest_suit_coverage.test_suit_coverage_no_unity.mean(),2)))
    print("number of NaN: {}".format(Natest_suit_coverage.test_suit_coverage.isna().sum()))
    print("=====================================================")
    
    #Limpeza
    notNacoverage_of_criterion = branchcsv[branchcsv.coverage_of_criterion.notnull()].copy(deep = True)
    Nacoverage_of_criterion = branchcsv[branchcsv.coverage_of_criterion.isna()].copy(deep = True)

    notNacoverage_of_criterion['coverage_of_criterion_no_unity'] = notNacoverage_of_criterion['coverage_of_criterion'].str.replace('%','')
    notNacoverage_of_criterion['coverage_of_criterion_no_unity'] = notNacoverage_of_criterion['coverage_of_criterion_no_unity'].str.replace(' \(no goals\)','')
    notNacoverage_of_criterion.coverage_of_criterion_no_unity = notNacoverage_of_criterion.coverage_of_criterion_no_unity.astype(int)
    
    
    print("max coverage_of_criterion_no_unity: {} (%)".format(notNacoverage_of_criterion.coverage_of_criterion_no_unity.max()))
    print("min coverage_of_criterion_no_unity: {} (%)".format(notNacoverage_of_criterion.coverage_of_criterion_no_unity.min()))
    print("mean coverage_of_criterion_no_unity: {} (%)".format(round(notNacoverage_of_criterion.coverage_of_criterion_no_unity.mean(),2)))
    print("number of NaN: {}".format(Nacoverage_of_criterion.coverage_of_criterion.isna().sum()))
    
    print("=====================================================")
    
    #
    print("GA - métricas:")
    notNasearch_finished_after = branchcsv[branchcsv.search_finished_after.notnull()].copy(deep = True)
    Nasearch_finished_after = branchcsv[branchcsv.search_finished_after.isna()].copy(deep = True)
    
    notNasearch_finished_after['search_finished_after_no_unity'] = notNasearch_finished_after['search_finished_after'].str.replace('s','')
    notNasearch_finished_after.search_finished_after_no_unity = notNasearch_finished_after.search_finished_after_no_unity.astype(int)

    print("=====================================================")
    print("max search_finished_after_no_unity: {} (s)".format(notNasearch_finished_after.search_finished_after_no_unity.max()))
    print("min search_finished_after_no_unity: {} (s)".format(notNasearch_finished_after.search_finished_after_no_unity.min()))
    print("mean search_finished_after_no_unity: {} (s)".format(round(notNasearch_finished_after.search_finished_after_no_unity.mean(),2)))
    print("number of NaN: {}".format(Nasearch_finished_after.search_finished_after.isna().sum()))
    
    print("=====================================================")
    notNanum_generations = branchcsv[branchcsv.num_generations.notnull()].copy(deep = True)
    Nanum_generations = branchcsv[branchcsv.num_generations.isna()].copy(deep = True)


    print("max num_generations: {}".format(notNanum_generations.num_generations.max()))
    print("min num_generations: {}".format(notNanum_generations.num_generations.min()))
    print("mean num_generations: {}".format(round(notNanum_generations.num_generations.mean(),2)))
    print("number of NaN: {}".format(Nanum_generations.num_generations.isna().sum()))
    
    print("=====================================================")
    notNanum_statements = branchcsv[branchcsv.num_statements.notnull()].copy(deep = True)
    Nanum_statements = branchcsv[branchcsv.num_statements.isna()].copy(deep = True)
    
    print("max num_statements: {}".format(notNanum_statements.num_statements.max()))
    print("min num_statements: {}".format(notNanum_statements.num_statements.min()))
    print("mean num_statements: {}".format(round(notNanum_statements.num_statements.mean(),2)))
    print("number of NaN: {}".format(Nanum_statements.num_statements.isna().sum()))
    
    print("=====================================================")
    notNabest_ind_fitness = branchcsv[branchcsv.best_ind_fitness.notnull()].copy(deep = True)
    Nabest_ind_fitness = branchcsv[branchcsv.best_ind_fitness.isna()].copy(deep = True)
    
    print("max best_ind_fitness: {}".format(round(notNabest_ind_fitness.best_ind_fitness.max(),2)))
    print("min best_ind_fitness: {}".format(notNabest_ind_fitness.best_ind_fitness.min()))
    print("mean best_ind_fitness: {}".format(round(notNabest_ind_fitness.best_ind_fitness.mean(),2)))
    print("number of NaN: {}".format(Nabest_ind_fitness.best_ind_fitness.isna().sum()))
    
    print("=====================================================")
    print("=====================================================")
    print("=====================================================")
    print("Tempo Geral")
    
    #Tempo total rodando testes: converter para horas
    print("sum time_spent_to_execute_tests: {} (horas)".format(round( notNatime_spent_to_execute_tests.time_spent_to_execute_tests_no_unity.sum()/(1000*60*60),2 ) ) ) 
    
    #Tempo total de pesquisa do GA:
    print("sum search_finished_after_no_unity: {} (horas)".format(round( notNasearch_finished_after.search_finished_after_no_unity.sum()/(60*60),2)))

    print("=====================================================")
    print("=====================================================")
    print("=====================================================")

pass

branchcsv = 'parseado_branch.csv'
weakcsv = 'parseado_weakmutation.csv'
strongcsv = 'parseado_strongmutation_no_error.csv'

analisa_csv(branchcsv)

