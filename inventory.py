

def Update_Savings(inventory):
    income_dict = inventory['income']
    income = income_dict['meetings']+income_dict['sponsees']+income_dict['service']
    costs_dict = inventory['costs']
    cost = costs_dict['resentments']+costs_dict['distractions']
    savings = inventory['savings']-cost+income
    print(savings)
    return savings


inventory = {'income': {'meetings': 1, 'sponsees': 2, 'service': 0},
             'costs': {'resentments': 0, 'distractions': 1},
             'savings': 0}

inventory['savings'] = Update_Savings(inventory)
print(inventory)
inventory['savings'] = Update_Savings(inventory)
print(inventory)
