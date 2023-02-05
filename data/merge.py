#       ▄▀█ █▀▄▀█ █▀█ █▀█ █▀▀
#      	█▀█ █░▀░█ █▄█ █▀▄ ██▄

#         © Copyright 2022

#       https://t.me/amorescam

#     🔒 Licensed under the GNU GPLv3
#     🧟‍♂️ Not for open source

import pandas as pd
import csv

df1 = pd.read_csv('data-scientist.csv')
df2 = pd.read_csv('software-engineer.csv')
df3 = pd.read_csv('computer-systems.csv')

frames = [df1, df2, df3]
result = pd.concat(frames)
result.drop_duplicates()
result.drop(result.columns[0], axis=1)

result.to_csv('out.csv', index=False, quoting=csv.QUOTE_ALL)
