from inventory import Add_Cost, Reset_Cost, Update_Savings, inventory, Add_Income, Reset_Income
from random import randint
from game_map import spaces
import pandas as pd

# inventory = {'income': {'meetings': 4, 'sponsees': 2, 'service': 0},
#              'costs': {'resentments': 1, 'distractions': 1},
#              'savings': 0}

print()
print(inventory)
inventory = Add_Cost(inventory, 'resentments', 2)
print(inventory)
print()
for i in range(10):
    print(randint(1, 6))
