import pandas as pd

data = [['2020-05-30', 'Headphone'], ['2020-06-01', 'Pencil'], ['2020-06-02', 'Mask'], ['2020-05-30', 'Basketball'], ['2020-06-01', 'Bible'], ['2020-06-02', 'Mask'], ['2020-05-30', 'T-Shirt']]
activities = pd.DataFrame(data, columns=['sell_date', 'product']).astype({'sell_date':'datetime64[ns]', 'product':'object'})
def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities=activities.drop_duplicates().reset_index()
    return activities.groupby(
        'sell_date'
    )['product'].agg([
        ('num_sold', 'nunique'),
        ('products', lambda x: ','.join(sorted(x.unique())))
    ]).reset_index()


print(categorize_products(activities))