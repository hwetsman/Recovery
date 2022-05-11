import pandas as pd
import numpy

file = 'cards.csv'

df = pd.read_csv(file)
print(df)

cards = list(set(df.card_name.tolist()))
print(cards)
deck = ['bad_day', 'bad_day', 'bad_day', 'bad_day', 'bad_day', 'bad_day', 'bad_day', 'bad_day',
        'fired', 'fired', 'fired',
        'divorce', 'divorce',
        'birthday', 'birthday', 'birthday',
        'less_than_10', 'less_than_10', 'less_than_10',
        'first_step', 'first_step', 'first_step',
        'bigshot', 'bigshot', 'bigshot',
        'old_lover', 'old_lover', 'old_lover',
        'trigger', 'trigger', 'trigger', 'trigger', 'trigger', 'trigger', 'trigger', 'trigger',
        'opioid', 'opioid', 'opioid',
        'bonus', 'bonus', 'bonus',
        'fired', 'fired', 'fired', 'fired']
