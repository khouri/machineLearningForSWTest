#!/usr/bin/python

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('statistics.csv') # Make sure the path is correct
bp = df.boxplot(column='Size', by='configuration_id')
bp = df.boxplot(column='Length', by='configuration_id')
bp = df.boxplot(column='MutationScore', by='configuration_id')
plt.show()