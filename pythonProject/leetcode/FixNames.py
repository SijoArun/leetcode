import pandas as pd

data = [[2, 'aLice'], [1, 'bOB']]
users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name']=users['name'].map(lambda row: str(row).capitalize())
    users= users.sort_values(by='user_id',ascending=True)
    return users



print(fix_names(users))