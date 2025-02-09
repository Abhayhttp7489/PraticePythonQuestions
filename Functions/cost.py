def calculate_total_cost(cart):
    total_cost=0
    for item in cart:
        total_cost+=item['price']*item['quantity']
    return total_cost

#example of cart data

cart=[
    {'name':'apple','price':0.5,'quantity':4},
    {'name':'Banana','price':0.3,'quantity':6},
    {'name':'Orange','price':0.7,'quantity':3}
]

#calling the function
print(calculate_total_cost(cart))