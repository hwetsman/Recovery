def Update_Savings(dict1):
    savings = dict1['savings']
    income_dict = dict1['income']
    income = income_dict['meetings']+income_dict['sponsees']+income_dict['service']
    costs_dict = dict1['costs']
    cost = costs_dict['resentments']+costs_dict['distractions']
    total = savings-cost+income
    dict1['savings'] = max(total, 0)
    return dict1


def Add_Cost(inventory, factor, quantity):
    value = inventory['costs'][factor]
    value = value+quantity
    inventory['costs'][factor] = max(value, 0)
    return inventory


def Reset_Cost(inventory, factor):
    inventory['costs'][factor] = 0
    return inventory


def Add_Income(inventory, factor, quantity):
    value = inventory['costs'][factor]
    value = value+quantity
    inventory['income'][factor] = max(value, 0)
    return inventory


def Reset_Income(inventory, factor):
    inventory['income'][factor] = 0
    return inventory


inventory = {'income': {'meetings': 4, 'sponsees': 2, 'service': 0},
             'costs': {'resentments': 1, 'distractions': 1},
             'savings': 0}
# print('Starting Inventory')
# print(inventory)
# print()
#
# print('Update Savings')
# inventory = Update_Savings(inventory)
# print(inventory)
# print()
#
# print('Add Resentments')
# inventory = Add_Cost(inventory, 'resentments', 2)
# print(inventory)
# print()
# print('Update Savings Again')
# inventory = Update_Savings(inventory)
# print(inventory)
# print()
#
# print('Decrease Distractions')
# inventory = Add_Cost(inventory, 'distractions', -2)
# print(inventory)
# print()
# print('Update Savings Again')
# inventory = Update_Savings(inventory)
# print(inventory)
# print()
#
# print('Reset resentments')
# inventory = Reset_Cost(inventory, 'resentments')
# print('Reset Resentments')
# print(inventory)
# print()
# print('Update Savings Again')
# inventory = Update_Savings(inventory)
# print(inventory)
# print()
# print()
