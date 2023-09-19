import pandas as pd

data = [[101, 'John', 'A', 102], [102, 'Dan', 'A', 101], [103, 'James', 'A', 101], [104, 'Amy', 'A', 101], [105, 'Anne', 'A', 101], [106, 'Ron', 'B', 101]]
employee = pd.DataFrame(data, columns=['id', 'name', 'department', 'managerId']).astype({'id':'Int64', 'name':'object', 'department':'object', 'managerId':'Int64'})
def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    manager_id_count=employee.groupby(['managerId'])['id'].count().reset_index()
    manager_id_count = manager_id_count[manager_id_count['id'] >= 5]
    result_df = employee[employee['id'].isin(manager_id_count['managerId'])]
    return result_df[['name']]

print(find_managers(employee))