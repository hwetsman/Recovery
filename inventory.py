

def Update_Savings(dict1):
    savings = dict1['savings']
    income_dict = dict1['income']
    income = income_dict['meetings']+income_dict['sponsees']+income_dict['service']
    costs_dict = dict1['costs']
    cost = costs_dict['resentments']+costs_dict['distractions']
    total = savings-cost+income
    dict1['savings'] = total
    return dict1


# def Add_Resentment(inventory):


inventory = {'income': {'meetings': 1, 'sponsees': 2, 'service': 0},
             'costs': {'resentments': 0, 'distractions': 1},
             'savings': 0}

inventory = Update_Savings(inventory)
print(inventory)
print()
inventory = Update_Savings(inventory)
print(inventory)
print()
print()
