import sys

import numpy as np
import pandas as pd

from config import *

import matplotlib.pyplot as plt
import dataframe_image as dfi


print('Hello King, welcome to the Decision Making tool.')
decision_type = input(start_sentence)

try:
    decision_type = int(decision_type)
except:
    raise Exception(error_string)
trade_factors = []
if decision_type == 1:
    trade_factors = trade_factors_job

factors_names = [dic['name'] for dic in trade_factors]
abs_weights = [dic['weight absolute'] for dic in trade_factors]
rel_weights = [dic['weight relative'] for dic in trade_factors]

print('\nThe trade factors currently selected, with their absolute and relative scores, are:\n')
for fac in trade_factors:
    print("{:<50} {:<25} {:<25}".format('Name: ' + fac['name'], 'Absolute score: ' + str(fac['weight absolute']),
                                  'Relative score: ' + str(fac['weight relative'])))
modify = input('\nDo you want to modify something? If yes, digit Y, otherwise anything else')
if modify == 'Y':
    sys.exit()
print('\nOkay I will ask you a few questions now.')

n_options = input('How many options do you want to evaluate? Digit an integer.')
try:
    n_options= int(n_options)
    print('\nOkay so you have {} options.'.format(n_options))
except:
    raise Exception(error_string)

print('\nNow we will attribute 1 to 10 scores on each trade factor for each option.')

table = []
rows = []
columns = [f[:3] for f in factors_names]
columns = [''.join([word[0] for word in fac.split()]) for fac in factors_names]
columns = ['\n'.join([word for word in fac.split()]) for fac in factors_names]
columns.extend(['Absolute Score', 'Relative Score'])

for i in range(n_options):
    option_name = input('Option {}. How do you want to name it?'.format(i+1))
    rows.append(option_name)
    answer_list = [option_name]
    answer_list2 = []
    for factor in trade_factors:
        score = input('Option {}: Evaluate the {} factor, whose description is: {}'.format(option_name, factor['name'], factor['description']))
        try:
            score = int(score)
        except:
            print('Insert a number from 1 to 10, please. ')
            score = input('Option {}: Evaluate the {}'.format(option_name, factor['name']))
            try:
                score = int(score)
            except:
                raise Exception(error_string)

        answer_list.append(score)
        answer_list2 = answer_list[1:]

    absolute_score = np.round(np.sum([abs_weights[i] * answer_list2[i] for i in range(len(abs_weights))]) / np.sum(abs_weights), decimals=2)
    relative_score = np.round(np.sum([rel_weights[i] * answer_list2[i] for i in range(len(rel_weights))]) / np.sum(rel_weights), decimals=2)

    print(f'\nDone with the option {option_name}!!')

    answer_list.extend([absolute_score, relative_score])

    table.append(answer_list)



fig, ax = plt.subplots(figsize=(15,10))

# Turn off the axis
ax.axis('off')

table_sorted = sorted(table, key=lambda x: x[-1], reverse=True)
rows = [option[0] for option in table_sorted]
table_sorted = [option[1:] for option in table_sorted]

# Add a table
the_table = ax.table(cellText=table_sorted,
                      rowLabels=rows,
                      colLabels=columns,
                      loc='center')
the_table.scale(1, 3) # Increase the size of the cells by 50%

# TODO: ADD A LABEL WITH THE ACRONYMS!!

# # Add a legend below the table
# couples = []
# for i in range(len(columns)):
#     couples.append((columns[i], factors_names[i]))
# legend_text = " | ".join("-".join([acro,full]) for acro, full in couples)
# plt.text(0, 0, legend_text, ha='center', va='bottom', fontsize=3)

# plt.axis('off')

# Set the title and label of the x-axis to empty strings
ax.set_title('')
ax.set_xlabel('')

plt.show()






