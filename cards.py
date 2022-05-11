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


def Parse_Card(df, card):
    output = {}
    print()
    print(card)
    if card == 'first_step':
        output['text'] = "Keep this card in case you need it but it is the next person's turn"
        return output
    else:
        temp = df[df.card_name == card]
        temp.reset_index(inplace=True, drop=True)
        print(temp)
        if temp.shape[0] == 1:
            output['text'] = "This is a no choice card"
            temp = temp.loc[:, (temp != 0).any(axis=0)]
            temp = temp.loc[:, (temp != 'None').any(axis=0)]
            temp = temp.drop('choice', axis=1)
            for col in temp.columns:
                output[col] = temp.loc[0, col]
            return output
        else:
            output['text'] = "We all have choices"
            return output


card = Pick_A_Card()
outcome = Parse_Card(df, card)
print(outcome)
print()
print()
