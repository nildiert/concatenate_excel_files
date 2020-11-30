#!/usr/bin/env python

import pandas as pd

with open('data.txt') as reader:
    data = reader.read()
    names = data.split('\n')[2:-1]
    df = pd.DataFrame()
    for file in names:
        if file.endswith('.xlsx'):
            file = 'data/' + file
            df_excel = pd.read_excel(file)
            df = df.append(pd.read_excel(file), ignore_index=True)

df.to_excel('combined_file.xlsx')