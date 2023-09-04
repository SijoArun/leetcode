import pandas as pd

data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
data = [[1, 3], [2, 1]]
orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers_with_orders = set(orders['customerId'])
    customers_without_orders = customers[~customers['id'].isin(customers_with_orders)]['name']
    result = pd.DataFrame({'Customers': customers_without_orders})
    return result

print(find_customers(customers,orders))