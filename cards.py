import pandas as pd
import numpy as np

file = 'cards.csv'

df = pd.read_csv(file)
# print(df)

deck = ['bad_day', 'bad_day', 'bad_day', 'bad_day', 'bad_day', 'bad_day',
        'bad_day', 'bad_day', 'fired', 'fired', 'fired', 'divorce', 'divorce',
        'birthday', 'birthday', 'birthday', 'less_than_10', 'less_than_10',
        'less_than_10', 'first_step', 'first_step', 'first_step', 'bigshot',
        'bigshot', 'bigshot', 'old_lover', 'old_lover', 'old_lover', 'opioid',
        'opioid', 'opioid', 'trigger', 'trigger', 'trigger', 'trigger',
        'trigger', 'trigger', 'trigger', 'trigger', 'bonus', 'bonus', 'bonus',
        'fight', 'fight', 'fight', 'fight']


def Pick_A_Card():
    card = np.random.choice(deck)
    return card


card = Pick_A_Card()
print(card)
