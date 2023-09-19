import pandas as pd

data = [[6, 1, 549], [8, 1, 834], [4, 2, 394], [11, 3, 657], [13, 3, 257]]
store = pd.DataFrame(data, columns=['bill_id', 'customer_id', 'amount']).astype({'bill_id':'int64', 'customer_id':'int64', 'amount':'int64'})
def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    data1=store[store['amount']>500].drop_duplicates(subset='customer_id').copy().reset_index()
    result = [[data1['customer_id'].count()]]
    return pd.DataFrame(result,columns=['rich_count']).astype({'rich_count':'object'})

print(count_rich_customers(store))