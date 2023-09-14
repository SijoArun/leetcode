import numpy as np
import pandas as pd

data = [[0, 95, 100, 105], [1, 70, None, 80]]
products = pd.DataFrame(data, columns=['product_id', 'store1', 'store2', 'store3']).astype({'product_id':'int64', 'store1':'int64', 'store2':'int64', 'store3':'int64'})
def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(
        products, id_vars='product_id', var_name='store', value_name='price'
    ).dropna()


print(rearrange_products_table(products))



rearrange_products_table(products)
